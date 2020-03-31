"""Core CALC_Radio Calculator Package

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be returned by overriding the function:
        def getCalculationList(self):
"""

from collections import OrderedDict
# import math
from enum import Enum
from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pycalcmodel.core.variable import ModelVariableFormat, CreateModelVariableEnum
from pyradioconfig.parts.common.calculators.calc_radio import CALC_Radio


class CALC_Radio_panther(CALC_Radio):
    """
    Init internal variables
    """

    def __init__(self):
        self._major = 1
        self._minor = 0
        self._patch = 0

    def calc_if_frequency_hz_value(self, model):
        """
        calculate smallest IF frequency that analog filter can be centered\n
        at and that works with calculated bandwidth.
        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        bw_analog = model.vars.iffilt_bandwidth_actual.value
        bw_digital = model.vars.bandwidth_actual.value

        # loop over all possible center frequencies the analog filter
        # can be centered around given analog filter bandwidths
        for ratio_reg, ratio in self.iffilt_ratio.items():

            f_if = bw_analog * ratio

            # pick first setting that ensures the lower edge of the band
            # is beyond 107 KHz lower threshold
            if f_if - bw_digital / 2.0 > 107e3:
                break

        model.vars.if_frequency_hz.value = int(f_if)

    def calc_iffilt_ratio_reg(self, model):
        """
        calculate CENTFREQ register setting given desired IF frequency and\n
        analog filter bandwidths already decided. \n
        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        bw_analog = model.vars.iffilt_bandwidth_actual.value
        f_if = float(model.vars.if_frequency_hz.value)

        ratio_target = f_if / bw_analog

        best_error = 99

        # loop over all ratios and find best closest to target ratio
        for ratio_reg, ratio in self.iffilt_ratio.items():

            error = abs(ratio - ratio_target)
            if error < best_error:
                best_error = error
                best_ratio_reg = ratio_reg

        self._reg_write(model.vars.RAC_IFFILTCTRL_CENTFREQ, best_ratio_reg)

    def calc_if_center_analog_hz_actual(self, model):
        """
        given analog filter bandwidths and ration calculated actual IF \n
        center frequency for analog filters.
        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        bw_analog = model.vars.iffilt_bandwidth_actual.value
        ratio = model.vars.iffilt_ratio_actual.value

        model.vars.if_center_analog_hz_actual.value = int(bw_analog * ratio)

    def calc_lpfbwrx(self, model):
        """
        calculate frequency synthesizer's LPF bandwidth for TX and write to register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        # Always set to narrowest bandwidth
        model.vars.pll_bandwidth_rx.value = model.vars.pll_bandwidth_rx.var_enum.BW_250KHz

    def calc_reg_lpfbwtx_lpfbwrx(self, model):
        """
        Write the rx and tx sequencer registers for the SYNTH_LPFCTRL register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        pll_bandwidth_tx = model.vars.pll_bandwidth_tx.value.value
        pll_bandwidth_rx = model.vars.pll_bandwidth_rx.value.value

        self._reg_write(model.vars.RAC_LPFCTRL_LPFBWRX, pll_bandwidth_rx)
        self._reg_write(model.vars.RAC_LPFCTRL_LPFBWTX, pll_bandwidth_tx)

        #
        # We also need to set the miracle mode bit.  Usually this is
        # cleared, but it can be forced to a 1.  So set the global variable to
        # 0, then read it back.  The readback will be a 1 if it was forced to a 1,
        # and otherwise it will get set to 0.
        #
        model.vars.pll_bandwidth_miracle_mode.value = False
        if model.vars.pll_bandwidth_miracle_mode.value == True:
            self._reg_write(model.vars.RAC_LPFCTRL_MIRACLEMODE, 1)
        else:
            self._reg_write(model.vars.RAC_LPFCTRL_MIRACLEMODE, 0)

    def calc_reg_ifadcctrl(self, model):
        """
        gdc:  Set based on request from Euisoo:  https://jira.silabs.com/browse/LABATEPDB-36

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        self._reg_write(model.vars.RAC_IFADCCTRL_VLDOCLKGEN, 3)
        self._reg_write(model.vars.RAC_IFADCCTRL_REGENCLKDELAY, 3)

        self._reg_write(model.vars.RAC_IFADCCTRL_INPUTSCALE, 0)
        self._reg_write(model.vars.RAC_IFADCCTRL_OTA1CURRENT, 2)
        self._reg_write(model.vars.RAC_IFADCCTRL_OTA2CURRENT, 2)
        self._reg_write(model.vars.RAC_IFADCCTRL_OTA3CURRENT, 2)
        self._reg_write(model.vars.RAC_IFADCCTRL_VCM, 2)
        self._reg_write(model.vars.RAC_IFADCCTRL_VLDOSERIES, 3)
        self._reg_write(model.vars.RAC_IFADCCTRL_VLDOSERIESCURR, 3)
        self._reg_write(model.vars.RAC_IFADCCTRL_VLDOSHUNT, 2)
        self._reg_write(model.vars.RAC_IFADCCTRL_INVERTCLK, 1)

    def calc_reg_vcoctrl(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        # Leave at Panther default, 12
        # self._reg_write(model.vars.RAC_VCOCTRL_VCOAMPLITUDE, 10)
        self._reg_write(model.vars.RAC_VCOCTRL_VCODETEN, 1)
        self._reg_write(model.vars.RAC_VCOCTRL_VCODETMODE, 1)
        self._reg_write(model.vars.RAC_VCOCTRL_VCOAREGCURR, 1)
        self._reg_write(model.vars.RAC_VCOCTRL_VCOCREGCURR, 2)
        self._reg_write(model.vars.RAC_VCOCTRL_VCODIVCURR, 15)

    def calc_reg_vcodetamplitude(self, model):

        lodiv = model.vars.lodiv_actual.value

        # https://jira.silabs.com/browse/LABATEPDB-154 set to 10 for subgig
        subgig_band = model.vars.subgig_band.value

        # Leave this at Panther default if left to be calculated
        reg = 4

        self._reg_write(model.vars.RAC_VCOCTRL_VCODETAMPLITUDE, reg)

    def calc_reg_chpctrl_mmdctrl(self, model):

        self._reg_write(model.vars.RAC_CHPCTRL1_BYPREPLDOTX, 0)
        self._reg_write(model.vars.RAC_CHPCTRL1_TRIMREPLDO, 1)
        self._reg_write(model.vars.RAC_MMDCTRL1_BYPREPLDOTX, 0)
        self._reg_write(model.vars.RAC_MMDCTRL1_TRIMREPLDO, 1)
        self._reg_write(model.vars.RAC_SGLNAMIXCTRL1_ENRFPKD, 0)

        etsi = model.vars.etsi_cat1_compatible.value
        if etsi == model.vars.etsi_cat1_compatible.var_enum.Band_169:
            self._reg_write(model.vars.RAC_CHPCTRL1_BYPREPLDORX, 0)
            self._reg_write(model.vars.RAC_MMDCTRL1_BYPREPLDORX, 0)
            self._reg_write(model.vars.RAC_IFPGACTRL1_LBWMODE, 1)
            self._reg_write(model.vars.RAC_SGLNAMIXCTRL1_TRIMNPATHBW, 3)
        else:
            self._reg_write(model.vars.RAC_CHPCTRL1_BYPREPLDORX, 1)
            self._reg_write(model.vars.RAC_MMDCTRL1_BYPREPLDORX, 1)
            self._reg_write(model.vars.RAC_IFPGACTRL1_LBWMODE, 0)
            self._reg_write(model.vars.RAC_SGLNAMIXCTRL1_TRIMNPATHBW, 0)

    def calc_reg_synthctrl(self, model):
        """

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        subgig_band = model.vars.subgig_band.value

        if subgig_band:
            reg = 7
        else:
            reg = 3

        self._reg_write(model.vars.SYNTH_CTRL_DITHERDSMOUTPUT, reg)

        self._reg_write(model.vars.SYNTH_CTRL_DITHERDAC, 3)
        self._reg_write(model.vars.SYNTH_CTRL_DITHERDSMINPUT, 1)
        self._reg_write(model.vars.SYNTH_CTRL_DSMMODE, 0)
        self._reg_write(model.vars.SYNTH_CTRL_LSBFORCE, 0)
        self._reg_write(model.vars.SYNTH_CTRL_LOCKTHRESHOLD, 3)
        self._reg_write(model.vars.SYNTH_CTRL_AUXLOCKTHRESHOLD, 5)
        self._reg_write(model.vars.SYNTH_CTRL_PRSMUX0, 0)
        self._reg_write(model.vars.SYNTH_CTRL_PRSMUX1, 0)


    def calc_lpfbwtx(self, model):
        """
        calculate frequency synthesizer's LPF bandwidth for TX and write to register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        target_bw_khz = model.vars.bandwidth_actual.value / 1000.0

        if target_bw_khz < 750:
            model.vars.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_750KHz
        elif target_bw_khz < 1000:
            model.vars.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_1000KHz
        elif target_bw_khz < 1200:
            model.vars.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_1200KHz
        elif target_bw_khz < 1500:
            model.vars.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_1500KHz
        elif target_bw_khz < 2000:
            model.vars.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_2000KHz
        elif target_bw_khz < 2500:
            model.vars.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_2500KHz
        else:
            model.vars.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_3000KHz

    def calc_lpfbwtx_reg(self, model):
        """
        calculate frequency synthesizer's LPF bandwidth for TX and write to register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        pll_bandwidth_tx = model.vars.pll_bandwidth_tx.value

        if pll_bandwidth_tx == model.vars.pll_bandwidth_tx.var_enum.BW_750KHz:
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1BWTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1COMPTX, 13)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RZVALTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RPVALTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RFBVALTX, 0)

            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFSWENTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFINCAPTX, 2)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFGNDSWENTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CASELTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CAVALTX, 15)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CFBSELTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZSELTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZVALTX, 126)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_MODESELTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_VCMLVLTX, 0)

            self._reg_write(model.vars.SYNTH_DSMCTRLTX_REQORDERTX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_MASHORDERTX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DEMMODETX, 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_LSBFORCETX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DSMMODETX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDACTX, 3)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMOUTPUTTX, 3)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMINPUTTX, 1)
        elif pll_bandwidth_tx == model.vars.pll_bandwidth_tx.var_enum.BW_1000KHz:
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1BWTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1COMPTX, 13)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RZVALTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RPVALTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RFBVALTX, 0)

            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFSWENTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFINCAPTX, 2)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFGNDSWENTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CASELTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CAVALTX, 15)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CFBSELTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZSELTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZVALTX, 126)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_MODESELTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_VCMLVLTX, 0)

            self._reg_write(model.vars.SYNTH_DSMCTRLTX_REQORDERTX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_MASHORDERTX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DEMMODETX, 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_LSBFORCETX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DSMMODETX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDACTX, 3)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMOUTPUTTX, 3)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMINPUTTX, 1)

        elif pll_bandwidth_tx == model.vars.pll_bandwidth_tx.var_enum.BW_1200KHz:
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1BWTX, 2)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1COMPTX, 13)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RZVALTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RPVALTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RFBVALTX, 0)

            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFSWENTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFINCAPTX, 2)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFGNDSWENTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CASELTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CAVALTX, 12)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CFBSELTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZSELTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZVALTX, 102)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_MODESELTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_VCMLVLTX, 0)

            self._reg_write(model.vars.SYNTH_DSMCTRLTX_REQORDERTX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_MASHORDERTX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DEMMODETX, 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_LSBFORCETX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DSMMODETX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDACTX, 3)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMOUTPUTTX, 3)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMINPUTTX, 1)

        elif pll_bandwidth_tx == model.vars.pll_bandwidth_tx.var_enum.BW_1500KHz:
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1BWTX, 5)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1COMPTX, 13)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RZVALTX, 3)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RPVALTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RFBVALTX, 0)

            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFSWENTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFINCAPTX, 2)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFGNDSWENTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CASELTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CAVALTX, 8)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CFBSELTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZSELTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZVALTX, 70)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_MODESELTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_VCMLVLTX, 0)

            self._reg_write(model.vars.SYNTH_DSMCTRLTX_REQORDERTX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_MASHORDERTX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DEMMODETX, 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_LSBFORCETX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DSMMODETX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDACTX, 3)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMOUTPUTTX, 3)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMINPUTTX, 1)
        elif pll_bandwidth_tx == model.vars.pll_bandwidth_tx.var_enum.BW_2000KHz:
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1BWTX, 8)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1COMPTX, 13)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RZVALTX, 6)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RPVALTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RFBVALTX, 0)

            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFSWENTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFINCAPTX, 2)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFGNDSWENTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CASELTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CAVALTX, 6)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CFBSELTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZSELTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZVALTX, 40)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_MODESELTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_VCMLVLTX, 0)

            self._reg_write(model.vars.SYNTH_DSMCTRLTX_REQORDERTX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_MASHORDERTX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DEMMODETX, 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_LSBFORCETX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DSMMODETX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDACTX, 3)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMOUTPUTTX, 3)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMINPUTTX, 1)

        elif pll_bandwidth_tx == model.vars.pll_bandwidth_tx.var_enum.BW_2500KHz:
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1BWTX, 11)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1COMPTX, 14)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RZVALTX, 9)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RPVALTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RFBVALTX, 0)

            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFSWENTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFINCAPTX, 2)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFGNDSWENTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CASELTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CAVALTX, 4)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CFBSELTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZSELTX, 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZVALTX, 22)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_MODESELTX, 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2TX_VCMLVLTX, 0)

            self._reg_write(model.vars.SYNTH_DSMCTRLTX_REQORDERTX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_MASHORDERTX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DEMMODETX, 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_LSBFORCETX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DSMMODETX, 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDACTX, 3)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMOUTPUTTX, 3)
            self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMINPUTTX, 1)
        elif pll_bandwidth_tx == model.vars.pll_bandwidth_tx.var_enum.BW_3000KHz:
           self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1BWTX, 15)
           self._reg_write(model.vars.SYNTH_LPFCTRL1TX_OP1COMPTX, 15)
           self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RZVALTX, 11)
           self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RPVALTX, 0)
           self._reg_write(model.vars.SYNTH_LPFCTRL1TX_RFBVALTX, 0)

           self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFSWENTX, 1)
           self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFINCAPTX, 2)
           self._reg_write(model.vars.SYNTH_LPFCTRL2TX_LPFGNDSWENTX, 0)
           self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CASELTX, 1)
           self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CAVALTX, 2)
           self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CFBSELTX, 0)
           self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZSELTX, 1)
           self._reg_write(model.vars.SYNTH_LPFCTRL2TX_CZVALTX, 6)
           self._reg_write(model.vars.SYNTH_LPFCTRL2TX_MODESELTX, 0)
           self._reg_write(model.vars.SYNTH_LPFCTRL2TX_VCMLVLTX, 0)

           self._reg_write(model.vars.SYNTH_DSMCTRLTX_REQORDERTX, 0)
           self._reg_write(model.vars.SYNTH_DSMCTRLTX_MASHORDERTX, 0)
           self._reg_write(model.vars.SYNTH_DSMCTRLTX_DEMMODETX, 1)
           self._reg_write(model.vars.SYNTH_DSMCTRLTX_LSBFORCETX, 0)
           self._reg_write(model.vars.SYNTH_DSMCTRLTX_DSMMODETX, 0)
           self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDACTX, 3)
           self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMOUTPUTTX, 3)
           self._reg_write(model.vars.SYNTH_DSMCTRLTX_DITHERDSMINPUTTX, 1)
 
    def calc_lpfbwrx_reg(self, model):
        """
        calculate frequency synthesizer's LPF bandwidth for TX and write to register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        pll_bandwidth_rx = model.vars.pll_bandwidth_rx.value

        if pll_bandwidth_rx == model.vars.pll_bandwidth_rx.var_enum.BW_100KHz:
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_OP1BWRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_OP1COMPRX , 7)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RZVALRX , 8)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RPVALRX , 6)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RFBVALRX , 0)

            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFSWENRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFINCAPRX , 2)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFGNDSWENRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CASELRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CAVALRX , 22)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CFBSELRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CZSELRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CZVALRX , 254)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_MODESELRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_VCMLVLRX , 0)

            self._reg_write(model.vars.SYNTH_DSMCTRLRX_REQORDERRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_MASHORDERRX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DEMMODERX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_LSBFORCERX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DSMMODERX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDACRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDSMOUTPUTRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDSMINPUTRX , 0)
        if pll_bandwidth_rx == model.vars.pll_bandwidth_rx.var_enum.BW_150KHz:
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_OP1BWRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_OP1COMPRX , 7)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RZVALRX , 8)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RPVALRX , 6)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RFBVALRX , 0)

            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFSWENRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFINCAPRX , 2)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFGNDSWENRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CASELRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CAVALRX , 22)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CFBSELRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CZSELRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CZVALRX , 254)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_MODESELRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_VCMLVLRX , 0)

            self._reg_write(model.vars.SYNTH_DSMCTRLRX_REQORDERRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_MASHORDERRX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DEMMODERX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_LSBFORCERX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DSMMODERX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDACRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDSMOUTPUTRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDSMINPUTRX , 0)
        if pll_bandwidth_rx == model.vars.pll_bandwidth_rx.var_enum.BW_200KHz:
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_OP1BWRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_OP1COMPRX , 7)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RZVALRX , 12)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RPVALRX , 7)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RFBVALRX , 0)

            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFSWENRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFINCAPRX , 2)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFGNDSWENRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CASELRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CAVALRX , 22)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CFBSELRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CZSELRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CZVALRX , 254)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_MODESELRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_VCMLVLRX , 0)

            self._reg_write(model.vars.SYNTH_DSMCTRLRX_REQORDERRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_MASHORDERRX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DEMMODERX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_LSBFORCERX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DSMMODERX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDACRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDSMOUTPUTRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDSMINPUTRX , 0)
        if pll_bandwidth_rx == model.vars.pll_bandwidth_rx.var_enum.BW_250KHz:
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_OP1BWRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_OP1COMPRX , 7)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RZVALRX , 13)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RPVALRX , 7)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RFBVALRX , 0)

            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFSWENRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFINCAPRX , 2)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFGNDSWENRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CASELRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CAVALRX , 16)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CFBSELRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CZSELRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CZVALRX , 229)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_MODESELRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_VCMLVLRX , 0)

            self._reg_write(model.vars.SYNTH_DSMCTRLRX_REQORDERRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_MASHORDERRX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DEMMODERX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_LSBFORCERX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DSMMODERX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDACRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDSMOUTPUTRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDSMINPUTRX , 0)
        if pll_bandwidth_rx == model.vars.pll_bandwidth_rx.var_enum.BW_300KHz:
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_OP1BWRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_OP1COMPRX , 7)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RZVALRX , 14)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RPVALRX , 7)
            self._reg_write(model.vars.SYNTH_LPFCTRL1RX_RFBVALRX , 0)

            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFSWENRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFINCAPRX , 2)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_LPFGNDSWENRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CASELRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CAVALRX , 16)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CFBSELRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CZSELRX , 1)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_CZVALRX , 128)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_MODESELRX , 0)
            self._reg_write(model.vars.SYNTH_LPFCTRL2RX_VCMLVLRX , 0)

            self._reg_write(model.vars.SYNTH_DSMCTRLRX_REQORDERRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_MASHORDERRX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DEMMODERX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_LSBFORCERX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DSMMODERX , 1)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDACRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDSMOUTPUTRX , 0)
            self._reg_write(model.vars.SYNTH_DSMCTRLRX_DITHERDSMINPUTRX , 0)

