import math
from pyradioconfig.parts.nixi.calculators.calc_agc import CALC_AGC_nixi


class CALC_AGC_panther(CALC_AGC_nixi):

    def calc_agc_misc(self, model):
        """Sets the agc variables to some default state until we figure out how to set them

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        self._reg_write(model.vars.AGC_CTRL0_ADCRESETDURATION,    0)
        self._reg_write(model.vars.AGC_CTRL0_RSSISHIFT, 		   78)

        self._reg_write(model.vars.AGC_CTRL1_SUBPERIOD, 			0)
        self._reg_write(model.vars.AGC_CTRL1_SUBINT,			    0)
        self._reg_write(model.vars.AGC_CTRL1_SUBNUM,              0)
        self._reg_write(model.vars.AGC_CTRL1_SUBDEN, 				0)

        # Remove from Panther
        #self._reg_write(model.vars.AGC_CTRL2_ADCRSTSTARTUP, 		1) # no longer exists in RM
        #self._reg_write(model.vars.AGC_CTRL2_MAXPWRVAR,      		0) # RAIL tries to read this....

        self._reg_write(model.vars.AGC_MANGAIN_MANGAININDEX, 		0)
        self._reg_write(model.vars.AGC_MANGAIN_MANGAININDEXEN,	0)

        # Remove from Panther
        #MCUW_RADIO_CFG-673
        # self._reg_write(model.vars.AGC_RFPEAKDET_RFPKDSWITCHDEL, 0)

        etsi = model.vars.etsi_cat1_compatible.value
        if etsi == model.vars.etsi_cat1_compatible.var_enum.Band_169:
            self._reg_write(model.vars.AGC_IFPEAKDET_PKDTHRESH2,	12)
            self._reg_write(model.vars.AGC_IFPEAKDET_PKDTHRESH1,	6)
        else:
            self._reg_write(model.vars.AGC_IFPEAKDET_PKDTHRESH2,	8)
            self._reg_write(model.vars.AGC_IFPEAKDET_PKDTHRESH1,	2)

        # Set Panther defaults
        self._reg_write(model.vars.AGC_AGCPERIOD_MAXHICNTTHD,7)
        self._reg_write(model.vars.AGC_AGCPERIOD_PERIODHI, 14)
        self._reg_write(model.vars.AGC_AGCPERIOD_PERIODLO, 55)
        self._reg_write(model.vars.AGC_AGCPERIOD_SETTLETIMEIF,6)
        self._reg_write(model.vars.AGC_AGCPERIOD_SETTLETIMERF,13)
        # Panther-specific. Not in Lynx.
        if model.part_family.lower() in ["panther"]:
            self._reg_write(model.vars.AGC_CTRL0_AGCCLKUNDIVREQ,0)
        self._reg_write(model.vars.AGC_CTRL0_AGCRST, 0)
        self._reg_write(model.vars.AGC_CTRL0_DISCFLOOPADJ, 0)
        self._reg_write(model.vars.AGC_CTRL0_DISPNDWNCOMP, 0)
        self._reg_write(model.vars.AGC_CTRL0_DISPNGAINUP, 1)
        self._reg_write(model.vars.AGC_CTRL0_DISRESETCHPWR, 0)
        self._reg_write(model.vars.AGC_CTRL0_DSADISCFLOOP, 0)
        self._reg_write(model.vars.AGC_CTRL0_ENRSSIRESET, 0)
        self._reg_write(model.vars.AGC_CTRL0_RSSISHIFT, 78)
        self._reg_write(model.vars.AGC_CTRL1_CCATHRSH, 0)
        self._reg_write(model.vars.AGC_CTRL1_PWRPERIOD, 1)
        self._reg_write(model.vars.AGC_CTRL1_SUBDEN, 0)
        self._reg_write(model.vars.AGC_CTRL1_SUBINT, 0)
        self._reg_write(model.vars.AGC_CTRL1_SUBNUM, 0)
        self._reg_write(model.vars.AGC_CTRL1_SUBPERIOD, 0)
        self._reg_write(model.vars.AGC_CTRL2_DISRFPKD, 0)
        self._reg_write(model.vars.AGC_CTRL2_DMASEL, 0)
        self._reg_write(model.vars.AGC_CTRL2_PRSDEBUGEN, 0)
        self._reg_write(model.vars.AGC_CTRL2_REHICNTTHD, 8)
        self._reg_write(model.vars.AGC_CTRL2_RELBYCHPWR, 0)
        self._reg_write(model.vars.AGC_CTRL2_RELOTHD, 3)
        self._reg_write(model.vars.AGC_CTRL2_RELTARGETPWR, 0)
        self._reg_write(model.vars.AGC_CTRL2_SAFEMODE, 1)
        self._reg_write(model.vars.AGC_CTRL2_SAFEMODETHD, 2)
        self._reg_write(model.vars.AGC_CTRL3_IFPKDDEB, 0)
        self._reg_write(model.vars.AGC_CTRL3_IFPKDDEBPRD, 0)
        self._reg_write(model.vars.AGC_CTRL3_IFPKDDEBRST, 4)
        self._reg_write(model.vars.AGC_CTRL3_IFPKDDEBTHD, 0)
        self._reg_write(model.vars.AGC_CTRL3_RFPKDDEB, 1)
        self._reg_write(model.vars.AGC_CTRL3_RFPKDDEBPRD, 40)
        self._reg_write(model.vars.AGC_CTRL3_RFPKDDEBRST, 10)
        self._reg_write(model.vars.AGC_CTRL3_RFPKDDEBTHD,2)
        #self._reg_write(model.vars.AGC_EN_EN, '',                     ModelOutputType.SVD_REG_FIELD, readable_name='AGC.EN.EN'           ))
        self._reg_write(model.vars.AGC_GAINRANGE_BOOSTLNA, 1)       # Reduce RFVDD current (non-default value) https://jira.silabs.com/browse/MCUW_RADIO_CFG-840
        self._reg_write(model.vars.AGC_GAINRANGE_GAININCSTEP, 1)
        self._reg_write(model.vars.AGC_GAINRANGE_HIPWRTHD, 8)
        self._reg_write(model.vars.AGC_GAINRANGE_LATCHEDHISTEP, 1)
        self._reg_write(model.vars.AGC_GAINRANGE_LNABWADJ, 1)
        self._reg_write(model.vars.AGC_GAINRANGE_LNAINDEXBORDER, 7)
        self._reg_write(model.vars.AGC_GAINRANGE_PNGAINSTEP, 3)
        self._reg_write(model.vars.AGC_GAINSTEPLIM_MAXPWRVAR, 0)
        self._reg_write(model.vars.AGC_GAINSTEPLIM_TRANRSTAGC, 0)
        self._reg_write(model.vars.AGC_HICNTREGION_HICNTREGION0, 3)
        self._reg_write(model.vars.AGC_HICNTREGION_HICNTREGION1, 4)
        self._reg_write(model.vars.AGC_HICNTREGION_HICNTREGION2, 5)
        self._reg_write(model.vars.AGC_HICNTREGION_HICNTREGION3, 6)
        self._reg_write(model.vars.AGC_HICNTREGION_HICNTREGION4, 8)
        self._reg_write(model.vars.AGC_LBT_CCARSSIPERIOD, 0)
        self._reg_write(model.vars.AGC_LBT_ENCCAGAINREDUCED, 0)
        self._reg_write(model.vars.AGC_LBT_ENCCARSSIMAX, 0)
        self._reg_write(model.vars.AGC_LBT_ENCCARSSIPERIOD, 0)
        self._reg_write(model.vars.AGC_LNAMIXCODE0_LNAMIXSLICE1, 61)
        self._reg_write(model.vars.AGC_LNAMIXCODE0_LNAMIXSLICE2, 46)
        self._reg_write(model.vars.AGC_LNAMIXCODE0_LNAMIXSLICE3, 36)
        self._reg_write(model.vars.AGC_LNAMIXCODE0_LNAMIXSLICE4, 28)
        self._reg_write(model.vars.AGC_LNAMIXCODE0_LNAMIXSLICE5, 21)
        self._reg_write(model.vars.AGC_LNAMIXCODE1_LNAMIXSLICE10, 5)
        self._reg_write(model.vars.AGC_LNAMIXCODE1_LNAMIXSLICE6, 17)
        self._reg_write(model.vars.AGC_LNAMIXCODE1_LNAMIXSLICE7, 12)
        self._reg_write(model.vars.AGC_LNAMIXCODE1_LNAMIXSLICE8, 10)
        self._reg_write(model.vars.AGC_LNAMIXCODE1_LNAMIXSLICE9, 6)
        self._reg_write(model.vars.AGC_MANGAIN_MANGAINEN, 0)
        self._reg_write(model.vars.AGC_MANGAIN_MANGAINIFPGA, 0)
        self._reg_write(model.vars.AGC_MANGAIN_MANGAINLNA, 0)
        self._reg_write(model.vars.AGC_MANGAIN_MANGAINPN, 0)
        self._reg_write(model.vars.AGC_MANGAIN_MANIFHILATRST, 0)
        self._reg_write(model.vars.AGC_MANGAIN_MANIFLOLATRST, 0)
        self._reg_write(model.vars.AGC_MANGAIN_MANRFLATRST, 0)
        self._reg_write(model.vars.AGC_PGACODE0_PGAGAIN1, 0)
        self._reg_write(model.vars.AGC_PGACODE0_PGAGAIN2, 1)
        self._reg_write(model.vars.AGC_PGACODE0_PGAGAIN3, 2)
        self._reg_write(model.vars.AGC_PGACODE0_PGAGAIN4, 3)
        self._reg_write(model.vars.AGC_PGACODE0_PGAGAIN5, 4)
        self._reg_write(model.vars.AGC_PGACODE0_PGAGAIN6, 5)
        self._reg_write(model.vars.AGC_PGACODE0_PGAGAIN7, 6)
        self._reg_write(model.vars.AGC_PGACODE0_PGAGAIN8, 7)
        self._reg_write(model.vars.AGC_PGACODE1_PGAGAIN10, 9)
        self._reg_write(model.vars.AGC_PGACODE1_PGAGAIN11, 10)
        self._reg_write(model.vars.AGC_PGACODE1_PGAGAIN9, 8)
        self._reg_write(model.vars.AGC_PNRFATT0_LNAMIXRFATT1, 0)
        self._reg_write(model.vars.AGC_PNRFATT0_LNAMIXRFATT2, 1)
        self._reg_write(model.vars.AGC_PNRFATT0_LNAMIXRFATT3, 2)
        self._reg_write(model.vars.AGC_PNRFATT0_LNAMIXRFATT4, 4)
        self._reg_write(model.vars.AGC_PNRFATT0_LNAMIXRFATT5, 6)
        self._reg_write(model.vars.AGC_PNRFATT1_LNAMIXRFATT10, 24)
        self._reg_write(model.vars.AGC_PNRFATT1_LNAMIXRFATT6, 8)
        self._reg_write(model.vars.AGC_PNRFATT1_LNAMIXRFATT7, 11)
        self._reg_write(model.vars.AGC_PNRFATT1_LNAMIXRFATT8, 15)
        self._reg_write(model.vars.AGC_PNRFATT1_LNAMIXRFATT9, 18)
        self._reg_write(model.vars.AGC_PNRFATT2_LNAMIXRFATT11, 31)
        self._reg_write(model.vars.AGC_PNRFATT2_LNAMIXRFATT12, 32)
        self._reg_write(model.vars.AGC_PNRFATT2_LNAMIXRFATT13, 46)
        self._reg_write(model.vars.AGC_PNRFATT2_LNAMIXRFATT14, 61)
        self._reg_write(model.vars.AGC_RSSISTEPTHR_RSSIFAST, 0)
        self._reg_write(model.vars.AGC_STEPDWN_STEPDWN0, 1)
        self._reg_write(model.vars.AGC_STEPDWN_STEPDWN1, 2)
        self._reg_write(model.vars.AGC_STEPDWN_STEPDWN2, 4)
        self._reg_write(model.vars.AGC_STEPDWN_STEPDWN3, 6)
        self._reg_write(model.vars.AGC_STEPDWN_STEPDWN4, 6)
        self._reg_write(model.vars.AGC_STEPDWN_STEPDWN5, 6)

        # To address unit test warnings: pyradioconfig/unit_tests/test_generate_header_files.py
        # Field AGC.EN.EN does not have a valid value
        # etc...
        # Fields are being set to the reset value as found in the Register Model SVD at the time of this code being written.
        # There is a risk of the values below becoming stale (no longer equal to the SVD source) should the SVD change in the future.
        #
        # MCUW_RADIO_CFG-734 Panther: PHY/MAC Design requests more registers added (all MODEM, AGC, etc.) with re-writes of reset values

        # Panther-specific. Properly set to read-only on Lynx
        if model.part_family.lower() in ["panther"]:
            self._reg_write(model.vars.AGC_STATUS0_ADCINDEX, 0)
        self._reg_write(model.vars.AGC_GAINRANGE_PGAINDEXBORDER, 8)

    def calc_agc_reg(self, model):
        """given frequency band select between two AGC settings

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        subgig_band = model.vars.subgig_band.value

        self._reg_write(model.vars.AGC_GAININDEX_MININDEXDEGEN, 	    0)
        self._reg_write(model.vars.AGC_GAININDEX_MININDEXPGA, 		0)
        self._reg_write(model.vars.AGC_GAININDEX_NUMINDEXSLICES, 	    6)
        self._reg_write(model.vars.AGC_GAININDEX_NUMINDEXDEGEN, 	    3)
        self._reg_write(model.vars.AGC_GAININDEX_NUMINDEXPGA, 		12)
        self._reg_write(model.vars.AGC_MANGAIN_MANGAINLNASLICES,  0)
        self._reg_write(model.vars.AGC_MANGAIN_MANGAINLNASLICESREG, 0)

        if subgig_band:
            self._reg_write(model.vars.AGC_GAINRANGE_MAXGAIN, 			62)
            self._reg_write(model.vars.AGC_GAINRANGE_MINGAIN, 			112)
            self._reg_write(model.vars.AGC_GAININDEX_NUMINDEXATTEN, 	    18)
            self._reg_write(model.vars.AGC_MANGAIN_MANGAINLNAATTEN,  0)

        else:
            self._reg_write(model.vars.AGC_GAINRANGE_MAXGAIN, 			60)
            self._reg_write(model.vars.AGC_GAINRANGE_MINGAIN, 			122)
            self._reg_write(model.vars.AGC_GAININDEX_NUMINDEXATTEN, 	    12)
            self._reg_write(model.vars.AGC_MANGAIN_MANGAINLNAATTEN,  12)

    def calc_hyst_reg(self, model):
        """program HYST register

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        hyst = model.vars.agc_hysteresis.value

        if hyst > 15:
            hyst = 15

        # Moved in Panther to AGC_GAINSTEPLIM_HYST
        # self._reg_write(model.vars.AGC_CTRL2_HYST, hyst)
        self._reg_write(model.vars.AGC_GAINSTEPLIM_HYST, hyst)


    def calc_fastloopdel_reg(self, model):
        """calculate FASTLOOPDEL based on corresponding delay

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        fxo = model.vars.xtal_frequency.value
        fast_loop_delay = model.vars.fast_loop_delay.value

        # TODO: add missing -1 to equation once verified
        delay = int(math.ceil(fast_loop_delay * fxo))

        if delay < 0:
            delay = 0
        elif delay > 31:
            delay = 31

        # Does not exist in Panther
        # self._reg_write(model.vars.AGC_CTRL2_FASTLOOPDEL, delay)

    def calc_cfloopdel_reg(self, model):
        """program CFLOOPDEL based on calculated value

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        cfloopdel = model.vars.agc_settling_delay.value

        # Moved in Panther to AGC_GAINSTEPLIM_CFLOOPDEL
        #self._reg_write(model.vars.AGC_CTRL2_CFLOOPDEL, cfloopdel)
        self._reg_write(model.vars.AGC_GAINSTEPLIM_CFLOOPDEL, cfloopdel)

    def calc_agc_faststepup_reg(self, model):
        """set FASTSTEPUP based on modulation method

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        mod_format = model.vars.modulation_type.value
        etsi = model.vars.etsi_cat1_compatible.value

        # in OOK mode use max step size of 5
        if etsi == model.vars.etsi_cat1_compatible.var_enum.Band_169:
            step = 1
        else:
            step = 2

        # Does not exist in Panther
        # self._reg_write(model.vars.AGC_GAINSTEPLIM_FASTSTEPUP, step)

    def calc_faststepdown_reg(self, model):
        """choose FASTSTEPDOWN value based on agc_speed

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        agc_speed = model.vars.agc_speed.value
        etsi = model.vars.etsi_cat1_compatible.value

        if etsi == model.vars.etsi_cat1_compatible.var_enum.Band_169:
            step = 1
        else:
            if agc_speed == model.vars.agc_speed.var_enum.FAST.value:
                step = 5
            elif agc_speed == model.vars.agc_speed.var_enum.SLOW.value:
                step = 3  # TODO: come up with a value for this one
            else:
                step = 3

        # Does not exist in Panther
        # self._reg_write(model.vars.AGC_GAINSTEPLIM_FASTSTEPDOWN, step)

    def calc_agc_adcattenmode_code(self, model):

        etsi = model.vars.etsi_cat1_compatible.value

        if etsi == model.vars.etsi_cat1_compatible.var_enum.Band_169:
            # Moved in Panther to  AGC_CTRL0_ADCATTENCODE
            # self._reg_write(model.vars.AGC_GAINSTEPLIM_ADCATTENCODE, 1)
            # self._reg_write(model.vars.AGC_GAINSTEPLIM_ADCATTENMODE, 1)
            self._reg_write(model.vars.AGC_CTRL0_ADCATTENCODE, 1)
            self._reg_write(model.vars.AGC_CTRL0_ADCATTENMODE, 1)
        else:
            # Moved in Panther to  AGC_CTRL0_ADCATTENCODE
            # self._reg_write(model.vars.AGC_GAINSTEPLIM_ADCATTENCODE, 0)
            # self._reg_write(model.vars.AGC_GAINSTEPLIM_ADCATTENMODE, 0)
            self._reg_write(model.vars.AGC_CTRL0_ADCATTENCODE, 0)
            self._reg_write(model.vars.AGC_CTRL0_ADCATTENMODE, 0)


    def calc_agc_cfloopstepmax_reg(self, model):
        """set CFLOOPSTEPMAX based on modulation method

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        mod_format = model.vars.modulation_type.value

        # in OOK mode use max step size of 5
        if mod_format == model.vars.modulation_type.var_enum.OOK:
            step = 5
        elif mod_format == model.vars.modulation_type.var_enum.FSK4:
            step = 1
        else:
            step = 8

        # Moved in Panther to  AGC_GAINSTEPLIM_CFLOOPSTEPMAX
        # self._reg_write(model.vars.AGC_GAINSTEPLIM_CFLOOPSTEPMAX, step)
        self._reg_write(model.vars.AGC_GAINSTEPLIM_CFLOOPSTEPMAX, step)

    def calc_slowdecaycnt_reg(self, model):

        mod_format = model.vars.modulation_type.value
        baudrate_hz = model.vars.baudrate.value
        encoding = model.vars.symbol_encoding.value

        if encoding == model.vars.symbol_encoding.var_enum.DSSS or \
           encoding == model.vars.symbol_encoding.var_enum.Manchester:

            reg = 2

        elif mod_format == model.vars.modulation_type.var_enum.FSK2 or \
             mod_format == model.vars.modulation_type.var_enum.FSK4:

            if baudrate_hz > 500e3:
                reg = 2
            else:
                reg = 1

        else:
            reg = 8

        # Does not exist in Panther
        # self._reg_write(model.vars.AGC_GAINSTEPLIM_SLOWDECAYCNT, reg)

    def calc_fastloopdel_reg(self, model):
        """calculate FASTLOOPDEL based on corresponding delay

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        fxo = model.vars.xtal_frequency.value
        fast_loop_delay = model.vars.fast_loop_delay.value

        # TODO: add missing -1 to equation once verified
        delay = int(math.ceil(fast_loop_delay * fxo))

        if delay < 0:
            delay = 0
        elif delay > 31:
            delay = 31

        # Does not exist in Panther
        # self._reg_write(model.vars.AGC_CTRL2_FASTLOOPDEL, delay)

    def calc_lnaslicesdel_reg(self, model):
        """calculate LNASLICESDEL based on corresponding delay

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        fxo = model.vars.xtal_frequency.value
        lna_slices_delay = model.vars.lna_slices_delay.value

        # TODO: add missing -1 to equation once verified
        delay = int(math.ceil(lna_slices_delay * fxo))

        if delay < 0:
            delay = 0
        elif delay > 31:
            delay = 31

        # Does not exist in Panther
        #self._reg_write(model.vars.AGC_LOOPDEL_LNASLICESDEL, delay)

    def calc_ifpgadel_reg(self, model):
        """calculate IFPGADEL based on corresponding delay

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """
        fxo = model.vars.xtal_frequency.value
        if_pga_delay = model.vars.if_pga_delay.value

        # TODO: add missing -1 to equation once verified
        delay = int(math.ceil(if_pga_delay * fxo))

        if delay < 0:
            delay = 0
        elif delay > 31:
            delay = 31

        # Does not exist in Panther
        #self._reg_write(model.vars.AGC_LOOPDEL_IFPGADEL, delay)

    def calc_pkdwait_reg(self, model):
        """calculate PKDWAIT based on agc_speed

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        # Does not exist in Panther
        pass
        #
        # fxo = model.vars.xtal_frequency.value
        # f_if = float(model.vars.if_frequency_hz.value)
        # freq_dev_hz = model.vars.deviation.value
        #
        # rfpkd_en = model.vars.RAC_SGLNAMIXCTRL1_ENRFPKD.value
        # rfpkd_switch_del = model.vars.AGC_RFPEAKDET_RFPKDSWITCHDEL.value
        #
        # # per guideline in internal document
        # wait = fxo / (4 * (f_if - freq_dev_hz))
        #
        # #MCUW_RADIO_CFG-673
        # if rfpkd_en == 1:
        #     if rfpkd_switch_del == 0:
        #         wait = 120 + wait
        #     elif rfpkd_switch_del == 1:
        #         wait = 200 + wait
        #
        # if wait < 0:
        #     wait = 0
        # elif wait > 1023:
        #     wait = 1023

        # Does not exist in Panther
        # self._reg_write(model.vars.AGC_LOOPDEL_PKDWAIT, int(wait))