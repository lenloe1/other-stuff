"""Core CALC_Misc Package

Calculator functions are pulled by using their names.
Calculator functions must start with "calc_", if they are to be consumed by the framework.
    Or they should be returned by overriding the function:
        def getCalculationList(self):
"""

from pyradioconfig.parts.jumbo.calculators.calc_misc import CALC_Misc_jumbo

from py_2_and_3_compatibility import *

class CALC_Misc_nerio(CALC_Misc_jumbo):

    def calc_misc(self, model):
        """
        These aren't really calculating right now.  Just using defaults or forced values.

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        self._reg_write(model.vars.MODEM_CTRL0_FRAMEDETDEL, 0)
        self._reg_write(model.vars.MODEM_CTRL0_FDM0DIFFDIS, 0)

        self._reg_write(model.vars.MODEM_CTRL1_SYNCERRORS, 0)
        self._reg_write(model.vars.MODEM_CTRL1_SYNC1INV, 0)

        self._reg_write(model.vars.MODEM_CTRL2_BRDIVB, 0)
        self._reg_write(model.vars.MODEM_CTRL2_BRDIVA, 0)
        self._reg_write(model.vars.MODEM_CTRL2_RATESELMODE, 0)

        self._reg_write(model.vars.MODEM_CTRL4_ADCSATDENS, 0)
        self._reg_write(model.vars.MODEM_CTRL4_ADCSATLEVEL, 6)
        self._reg_write(model.vars.MODEM_CTRL4_SOFTDSSSMODE, 0)
        self._reg_write(model.vars.MODEM_CTRL4_PREDISTRST, 0)
        self._reg_write(model.vars.MODEM_CTRL4_PREDISTAVG, 0)
        self._reg_write(model.vars.MODEM_CTRL4_PREDISTDEB, 0)
        self._reg_write(model.vars.MODEM_CTRL4_PREDISTGAIN, 0)

        self._reg_write(model.vars.MODEM_PRE_DSSSPRE, 0)

        self._reg_write(model.vars.MODEM_TIMING_TSAGCDEL, 0)
        self._reg_write(model.vars.MODEM_TIMING_TIMSEQSYNC, 0)
        self._reg_write(model.vars.MODEM_TIMING_FASTRESYNC, 0)

        self._reg_write(model.vars.MODEM_AFC_AFCTXMODE,       0)

        self._reg_write(model.vars.SEQ_MISC_SQBMODETX, 0)

        self._reg_write(model.vars.MODEM_DSATHD0_SPIKETHD, 0x64)
        self._reg_write(model.vars.MODEM_DSATHD0_UNMODTHD, 4)
        self._reg_write(model.vars.MODEM_DSATHD0_FDEVMINTHD, 12)
        self._reg_write(model.vars.MODEM_DSATHD0_FDEVMAXTHD, 0x78)

        self._reg_write(model.vars.MODEM_DSATHD1_POWABSTHD, 0x1388)
        self._reg_write(model.vars.MODEM_DSATHD1_POWRELTHD, 0)
        self._reg_write(model.vars.MODEM_DSATHD1_DSARSTCNT, 2)
        self._reg_write(model.vars.MODEM_DSATHD1_RSSIJMPTHD, 6)
        self._reg_write(model.vars.MODEM_DSATHD1_FREQLATDLY, 1)
        self._reg_write(model.vars.MODEM_DSATHD1_PWRFLTBYP, 1)
        self._reg_write(model.vars.MODEM_DSATHD1_AMPFLTBYP, 1)
        self._reg_write(model.vars.MODEM_DSATHD1_PWRDETDIS, 1)
        self._reg_write(model.vars.MODEM_DSATHD1_FREQSCALE, 0)

        #self._reg_write(model.vars.MODEM_DSACTRL_DSAMODE, 0)

        self._reg_write(model.vars.MODEM_DSACTRL_ARRTOLERTHD0, 2)
        self._reg_write(model.vars.MODEM_DSACTRL_ARRTOLERTHD1, 4)
        self._reg_write(model.vars.MODEM_DSACTRL_SCHPRD, 0)
        self._reg_write(model.vars.MODEM_DSACTRL_FREQAVGSYM, 1)
        self._reg_write(model.vars.MODEM_DSACTRL_DSARSTON, 1)
        self._reg_write(model.vars.MODEM_DSACTRL_TIMEST, 0)
        self._reg_write(model.vars.MODEM_DSACTRL_AGCDEBOUNDLY, 0)
        self._reg_write(model.vars.MODEM_DSACTRL_LOWDUTY, 0)

        self._reg_write(model.vars.MODEM_VTTRACK_FREQTRACKMODE, 0)
        self._reg_write(model.vars.MODEM_VTTRACK_TIMTRACKTHD, 2)
        self._reg_write(model.vars.MODEM_VTTRACK_TIMEACQUTHD, 0xEE)
        self._reg_write(model.vars.MODEM_VTTRACK_TIMCHK, 0)
        self._reg_write(model.vars.MODEM_VTTRACK_TIMEOUTMODE, 1)
        self._reg_write(model.vars.MODEM_VTTRACK_TIMGEAR, 0)
        self._reg_write(model.vars.MODEM_VTTRACK_FREQBIAS, 0)

        self._reg_write(model.vars.MODEM_VTCORRCFG1_CORRSHFTLEN, 0x20)
        self._reg_write(model.vars.MODEM_VTCORRCFG1_VTFRQLIM, 0xC0)
        self._reg_write(model.vars.MODEM_VTCORRCFG0_EXPECTPATT, long(0x556B7))
        self._reg_write(model.vars.MODEM_VTCORRCFG0_EXPSYNCLEN, 8)
        self._reg_write(model.vars.MODEM_VTCORRCFG0_BUFFHEAD, 2)

        self._reg_write(model.vars.MODEM_VITERBIDEMOD_VTDEMODEN, 0)
        self._reg_write(model.vars.MODEM_VITERBIDEMOD_HARDDECISION, 0)
        self._reg_write(model.vars.MODEM_VITERBIDEMOD_VITERBIKSI1, 0x40)
        self._reg_write(model.vars.MODEM_VITERBIDEMOD_VITERBIKSI2, 0x30)
        self._reg_write(model.vars.MODEM_VITERBIDEMOD_VITERBIKSI3, 0x20)
        self._reg_write(model.vars.MODEM_VITERBIDEMOD_SYNTHAFC, 0)
        self._reg_write(model.vars.MODEM_VITERBIDEMOD_CORRCYCLE, 0)
        self._reg_write(model.vars.MODEM_VITERBIDEMOD_CORRSTPSIZE, 0)


        self._reg_write(model.vars.MODEM_CTRL5_DSSSCTD, 0)
        self._reg_write(model.vars.MODEM_CTRL5_BBSS, 0)
        self._reg_write(model.vars.MODEM_CTRL5_POEPER, 0)
        self._reg_write(model.vars.MODEM_CTRL5_FOEPREAVG, 0)
        self._reg_write(model.vars.MODEM_CTRL5_LINCORR, 0)
        self._reg_write(model.vars.MODEM_CTRL5_PRSDEBUG, 0)
        self._reg_write(model.vars.MODEM_CTRL5_RESYNCLIMIT, 0)

        self._reg_write(model.vars.MODEM_CTRL6_TDREW, 0)
        self._reg_write(model.vars.MODEM_CTRL6_PREBASES, 0)
        self._reg_write(model.vars.MODEM_CTRL6_PSTIMABORT0, 0)
        self._reg_write(model.vars.MODEM_CTRL6_PSTIMABORT1, 0)
        self._reg_write(model.vars.MODEM_CTRL6_PSTIMABORT2, 0)
        self._reg_write(model.vars.MODEM_CTRL6_PSTIMABORT3, 0)
        self._reg_write(model.vars.MODEM_CTRL6_ARW, 0)
        self._reg_write(model.vars.MODEM_CTRL6_TIMTHRESHGAIN, 0)
        self._reg_write(model.vars.MODEM_CTRL6_CPLXCORREN, 0)
        self._reg_write(model.vars.MODEM_CTRL6_RXBRCALCDIS, 0)
        self._reg_write(model.vars.MODEM_CTRL6_DEMODRESTARTALL, 0)

        self._reg_write(model.vars.MODEM_DSACTRL_AGCBAUDEN, 0)
        self._reg_write(model.vars.MODEM_DSACTRL_RESTORE, 0)

        self._reg_write(model.vars.MODEM_CTRL0_DUALCORROPTDIS, 0)

        self._reg_write(model.vars.AGC_GAINSTEPLIM_EN2XFASTSTEPDOWN, 0)

        self._reg_write(model.vars.MODEM_INTAFC_FOEPREAVG0, 0)
        self._reg_write(model.vars.MODEM_INTAFC_FOEPREAVG1, 0)
        self._reg_write(model.vars.MODEM_INTAFC_FOEPREAVG2, 0)
        self._reg_write(model.vars.MODEM_INTAFC_FOEPREAVG3, 0)

        self._reg_write(model.vars.MODEM_CGCLKSTOP_FORCEOFF, 0)

        self._reg_write(model.vars.MODEM_SHAPING2_COEFF9, 0)
        self._reg_write(model.vars.MODEM_SHAPING2_COEFF10, 0)
        self._reg_write(model.vars.MODEM_SHAPING2_COEFF11, 0)
        self._reg_write(model.vars.MODEM_SHAPING3_COEFF12, 0)
        self._reg_write(model.vars.MODEM_SHAPING3_COEFF13, 0)
        self._reg_write(model.vars.MODEM_SHAPING3_COEFF14, 0)
        self._reg_write(model.vars.MODEM_SHAPING3_COEFF15, 0)
        self._reg_write(model.vars.MODEM_SHAPING4_COEFF16, 0)
        self._reg_write(model.vars.MODEM_SHAPING4_COEFF17, 0)
        self._reg_write(model.vars.MODEM_SHAPING4_COEFF18, 0)
        self._reg_write(model.vars.MODEM_SHAPING4_COEFF19, 0)
        self._reg_write(model.vars.MODEM_SHAPING4_COEFF20, 0)
        self._reg_write(model.vars.MODEM_SHAPING4_COEFF21, 0)
        self._reg_write(model.vars.MODEM_SHAPING5_COEFF22, 0)
        self._reg_write(model.vars.MODEM_SHAPING5_COEFF23, 0)
        self._reg_write(model.vars.MODEM_SHAPING5_COEFF24, 0)
        self._reg_write(model.vars.MODEM_SHAPING5_COEFF25, 0)
        self._reg_write(model.vars.MODEM_SHAPING5_COEFF26, 0)
        self._reg_write(model.vars.MODEM_SHAPING5_COEFF27, 0)
        self._reg_write(model.vars.MODEM_SHAPING5_COEFF28, 0)
        self._reg_write(model.vars.MODEM_SHAPING5_COEFF29, 0)
        self._reg_write(model.vars.MODEM_SHAPING6_COEFF30, 0)
        self._reg_write(model.vars.MODEM_SHAPING6_COEFF31, 0)
        self._reg_write(model.vars.MODEM_SHAPING6_COEFF32, 0)
        self._reg_write(model.vars.MODEM_SHAPING6_COEFF33, 0)
        self._reg_write(model.vars.MODEM_SHAPING6_COEFF34, 0)
        self._reg_write(model.vars.MODEM_SHAPING6_COEFF35, 0)
        self._reg_write(model.vars.MODEM_SHAPING6_COEFF36, 0)
        self._reg_write(model.vars.MODEM_SHAPING6_COEFF37, 0)
        self._reg_write(model.vars.MODEM_SHAPING6_COEFF38, 0)
        self._reg_write(model.vars.MODEM_SHAPING6_COEFF39, 0)

        self._reg_write(model.vars.AGC_RSSISTEPTHR_DEMODRESTARTPER, 0)
        self._reg_write(model.vars.AGC_RSSISTEPTHR_DEMODRESTARTTHR, 0)
        self._reg_write(model.vars.AGC_RSSISTEPTHR_POSSTEPTHR     , 0)
        self._reg_write(model.vars.AGC_RSSISTEPTHR_NEGSTEPTHR     , 0)
        self._reg_write(model.vars.AGC_RSSISTEPTHR_STEPPER        , 0)

        self._reg_write(model.vars.SYNTH_CTRL_DEMMODE        , 1)

        self._reg_write(model.vars.SEQ_SYNTH_CTRL_DITHER_SETTINGS_DITHERDACRX, 3)
        self._reg_write(model.vars.SEQ_SYNTH_CTRL_DITHER_SETTINGS_DITHERDACTX, 3)
        self._reg_write(model.vars.SEQ_SYNTH_CTRL_DITHER_SETTINGS_DITHERDSMINPUTRX, 1)
        self._reg_write(model.vars.SEQ_SYNTH_CTRL_DITHER_SETTINGS_DITHERDSMINPUTTX, 1)
        self._reg_write(model.vars.SEQ_SYNTH_CTRL_DITHER_SETTINGS_DITHERDSMOUTPUTRX, 7)


    def	calc_ble_lr_regs(self, model):
        self._reg_write(model.vars.MODEM_CTRL6_CODINGB, 0)


        self._reg_write(model.vars.MODEM_LONGRANGE_LRCORRTHD,       0x3E8)
        self._reg_write(model.vars.MODEM_LONGRANGE_LRTIMCORRTHD,    0x0FA)
        self._reg_write(model.vars.MODEM_LONGRANGE_LRCORRSCHWIN,    0xA)
        self._reg_write(model.vars.MODEM_LONGRANGE_LRBLE,           0)
        self._reg_write(model.vars.MODEM_LRFRC_CI500,                1)
        self._reg_write(model.vars.MODEM_LRFRC_FRCACKTIMETHD,        0)
        self._reg_write(model.vars.MODEM_LONGRANGE_LRDEC,           0)
        self._reg_write(model.vars.MODEM_LONGRANGE_LRBLEDSA,        0)
        self._reg_write(model.vars.MODEM_LONGRANGE1_LRSS,           0)
        self._reg_write(model.vars.MODEM_LONGRANGE1_LRTIMEOUTTHD,   0)
        self._reg_write(model.vars.MODEM_LONGRANGE6_LRCHPWRSPIKETH, 0)
        self._reg_write(model.vars.MODEM_LONGRANGE6_LRSPIKETHD,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE1_LRSPIKETHADD,   0)
        self._reg_write(model.vars.MODEM_LONGRANGE1_CHPWRACCUDEL,   0)
        self._reg_write(model.vars.MODEM_LONGRANGE1_HYSVAL,         0)
        self._reg_write(model.vars.MODEM_LONGRANGE1_AVGWIN,         0)
        self._reg_write(model.vars.MODEM_LONGRANGE2_LRCHPWRTH1,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE2_LRCHPWRTH2,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE2_LRCHPWRTH3,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE2_LRCHPWRTH4,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE3_LRCHPWRTH5,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE3_LRCHPWRTH6,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE3_LRCHPWRTH7,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE3_LRCHPWRTH8,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE4_LRCHPWRTH9,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE4_LRCHPWRTH10,    0)
        self._reg_write(model.vars.MODEM_LONGRANGE4_LRCHPWRSH1,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE4_LRCHPWRSH2,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE4_LRCHPWRSH3,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE4_LRCHPWRSH4,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE5_LRCHPWRSH5,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE5_LRCHPWRSH6,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE5_LRCHPWRSH7,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE5_LRCHPWRSH8,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE5_LRCHPWRSH9,     0)
        self._reg_write(model.vars.MODEM_LONGRANGE5_LRCHPWRSH10,    0)
        self._reg_write(model.vars.MODEM_LONGRANGE5_LRCHPWRSH11,    0)

        self._reg_write(model.vars.FRC_CTRL_RATESELECT,             0)

