from pyradioconfig.parts.common.phys.phy_common import PHY_COMMON_FRAME_INTERNAL
from pycalcmodel.core.output import ModelOutput, ModelOutputType

class Phy_Internal_Base(object):
    """
    Common Internal Phy functions live here
    """

    @staticmethod
    def MODEM_to_ZIF_for_FPGA_OTA_card(phy, model):
        """MODEM_to_ZIF_for_FPGA_OTA_card

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        # Put modem in zero IF as that is how the ota card needs to be configured.
        phy.profile_outputs.MODEM_MIXCTRL_DIGIQSWAPEN.override = 0
        phy.profile_outputs.MODEM_DIGMIXCTRL_DIGMIXFREQ.override = 0
        phy.profile_outputs.MODEM_DCCOMP_DCCOMPEN.override = 0
        phy.profile_outputs.SYNTH_IFFREQ_LOSIDE.override = 0 # low side
        phy.profile_outputs.SYNTH_IFFREQ_IFFREQ.override = 0

    @staticmethod
    def AGC_FAST_LOOP_base(phy, model):
        phy.profile_outputs.AGC_CTRL0_PWRTARGET.override = 245
        phy.profile_outputs.AGC_CTRL0_MODE.override = 2
        phy.profile_outputs.AGC_CTRL0_RSSISHIFT.override = 78
        phy.profile_outputs.AGC_CTRL0_DISCFLOOPADJ.override = 1
        phy.profile_outputs.AGC_CTRL0_ADCATTENCODE.override = 0
        phy.profile_outputs.AGC_CTRL0_ADCATTENMODE.override = 0
        phy.profile_outputs.AGC_CTRL0_DISPNGAINUP.override = 0
        phy.profile_outputs.AGC_CTRL0_DISPNDWNCOMP.override = 0
        phy.profile_outputs.AGC_CTRL0_DISRESETCHPWR.override = 0
        phy.profile_outputs.AGC_CTRL0_AGCRST.override = 0
		
        phy.profile_outputs.AGC_CTRL1_CCATHRSH.override = 145
        phy.profile_outputs.AGC_CTRL1_RSSIPERIOD.override = 3
        phy.profile_outputs.AGC_CTRL1_PWRPERIOD.override = 1
        phy.profile_outputs.AGC_CTRL1_SUBPERIOD.override = 0
        phy.profile_outputs.AGC_CTRL1_SUBNUM.override = 0
        phy.profile_outputs.AGC_CTRL1_SUBDEN.override = 0
        phy.profile_outputs.AGC_CTRL1_SUBINT.override = 0
		
        phy.profile_outputs.AGC_CTRL2_PRSDEBUGEN.override = 0
        phy.profile_outputs.AGC_CTRL2_DMASEL.override = 0
        phy.profile_outputs.AGC_CTRL2_SAFEMODE.override = 0
        phy.profile_outputs.AGC_CTRL2_SAFEMODETHD.override = 3
        phy.profile_outputs.AGC_CTRL2_REHICNTTHD.override = 7
        phy.profile_outputs.AGC_CTRL2_RELOTHD.override = 4
        phy.profile_outputs.AGC_CTRL2_RELBYCHPWR.override = 3
        phy.profile_outputs.AGC_CTRL2_RELTARGETPWR.override = 236
        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 0
		
        phy.profile_outputs.AGC_CTRL3_RFPKDDEB.override = 1
        phy.profile_outputs.AGC_CTRL3_RFPKDDEBTHD.override = 1
        phy.profile_outputs.AGC_CTRL3_RFPKDDEBPRD.override = 40
        phy.profile_outputs.AGC_CTRL3_RFPKDDEBRST.override = 10
        phy.profile_outputs.AGC_CTRL3_IFPKDDEB.override = 1
        phy.profile_outputs.AGC_CTRL3_IFPKDDEBTHD.override = 1
        phy.profile_outputs.AGC_CTRL3_IFPKDDEBPRD.override = 40
        phy.profile_outputs.AGC_CTRL3_IFPKDDEBRST.override = 10
		
        phy.profile_outputs.AGC_GAINSTEPLIM_CFLOOPSTEPMAX.override = 4
        phy.profile_outputs.AGC_GAINSTEPLIM_CFLOOPDEL.override = 0
        phy.profile_outputs.AGC_GAINSTEPLIM_HYST.override = 3
        phy.profile_outputs.AGC_GAINSTEPLIM_MAXPWRVAR.override = 0
        phy.profile_outputs.AGC_GAINSTEPLIM_TRANRSTAGC.override = 0
		
        phy.profile_outputs.AGC_AGCPERIOD_PERIODHI.override = 14
        phy.profile_outputs.AGC_AGCPERIOD_PERIODLO.override = 45
        phy.profile_outputs.AGC_AGCPERIOD_MAXHICNTTHD.override = 9
        phy.profile_outputs.AGC_AGCPERIOD_SETTLETIMEIF.override = 6
        phy.profile_outputs.AGC_AGCPERIOD_SETTLETIMERF.override = 14
		
        phy.profile_outputs.AGC_GAINRANGE_LNAINDEXBORDER.override = 7
        phy.profile_outputs.AGC_GAINRANGE_PGAINDEXBORDER.override = 8
        phy.profile_outputs.AGC_GAINRANGE_GAININCSTEP.override = 1
        phy.profile_outputs.AGC_GAINRANGE_LATCHEDHISTEP.override = 0
        phy.profile_outputs.AGC_GAINRANGE_PNGAINSTEP.override = 4
        phy.profile_outputs.AGC_GAINRANGE_HIPWRTHD.override = 3
        
        phy.profile_outputs.AGC_MANGAIN_MANGAINEN.override = 0
        phy.profile_outputs.AGC_MANGAIN_MANGAINIFPGA.override = 7
        phy.profile_outputs.AGC_MANGAIN_MANGAINLNA.override = 1
        phy.profile_outputs.AGC_MANGAIN_MANGAINPN.override = 1
        
        phy.profile_outputs.AGC_HICNTREGION_HICNTREGION0.override = 4
        phy.profile_outputs.AGC_HICNTREGION_HICNTREGION1.override = 5
        phy.profile_outputs.AGC_HICNTREGION_HICNTREGION2.override = 6
        phy.profile_outputs.AGC_HICNTREGION_HICNTREGION3.override = 7
        phy.profile_outputs.AGC_HICNTREGION_HICNTREGION4.override = 8
        
        phy.profile_outputs.AGC_STEPDWN_STEPDWN0.override = 1
        phy.profile_outputs.AGC_STEPDWN_STEPDWN1.override = 2
        phy.profile_outputs.AGC_STEPDWN_STEPDWN2.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN3.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN4.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN5.override = 5
        
        phy.profile_outputs.AGC_RSSISTEPTHR_DEMODRESTARTPER.override = 0
        phy.profile_outputs.AGC_RSSISTEPTHR_DEMODRESTARTTHR.override = 0
        phy.profile_outputs.AGC_RSSISTEPTHR_POSSTEPTHR.override = 0

		##### RF peak detector threshold configuration
        phy.profile_outputs.RAC_PGACTRL_LNAMIXRFPKDTHRESHSEL.override = 2

		##### IF peak detector configuration
		# enable I/Q latch
        phy.profile_outputs.RAC_PGACTRL_PGAENLATCHI.override = 1
        phy.profile_outputs.RAC_PGACTRL_PGAENLATCHQ.override = 1
		# set IF peak detector threshold
        phy.profile_outputs.RAC_PGACTRL_PGATHRPKDHISEL.override = 5
        phy.profile_outputs.RAC_PGACTRL_PGATHRPKDLOSEL.override = 1

		
		
    @staticmethod
    def AGC_SLOW_LOOP_base(phy, model):
        phy.profile_outputs.AGC_CTRL0_PWRTARGET.override = 245
        phy.profile_outputs.AGC_CTRL0_MODE.override = 2
        phy.profile_outputs.AGC_CTRL0_RSSISHIFT.override = 78
        phy.profile_outputs.AGC_CTRL0_DISCFLOOPADJ.override = 0
        phy.profile_outputs.AGC_CTRL0_ADCATTENCODE.override = 0
        phy.profile_outputs.AGC_CTRL0_ADCATTENMODE.override = 0
        phy.profile_outputs.AGC_CTRL0_DISPNGAINUP.override = 0
        phy.profile_outputs.AGC_CTRL0_DISPNDWNCOMP.override = 0
        phy.profile_outputs.AGC_CTRL0_DISRESETCHPWR.override = 0
        phy.profile_outputs.AGC_CTRL0_AGCRST.override = 0

        phy.profile_outputs.AGC_CTRL1_CCATHRSH.override = 145
        phy.profile_outputs.AGC_CTRL1_RSSIPERIOD.override = 8
        phy.profile_outputs.AGC_CTRL1_PWRPERIOD.override = 1
        phy.profile_outputs.AGC_CTRL1_SUBPERIOD.override = 0
        phy.profile_outputs.AGC_CTRL1_SUBNUM.override = 0
        phy.profile_outputs.AGC_CTRL1_SUBDEN.override = 0
        phy.profile_outputs.AGC_CTRL1_SUBINT.override = 0

        phy.profile_outputs.AGC_CTRL2_PRSDEBUGEN.override = 0
        phy.profile_outputs.AGC_CTRL2_DMASEL.override = 0
        phy.profile_outputs.AGC_CTRL2_SAFEMODE.override = 0
        phy.profile_outputs.AGC_CTRL2_SAFEMODETHD.override = 3
        phy.profile_outputs.AGC_CTRL2_REHICNTTHD.override = 7
        phy.profile_outputs.AGC_CTRL2_RELOTHD.override = 4
        phy.profile_outputs.AGC_CTRL2_RELBYCHPWR.override = 3
        phy.profile_outputs.AGC_CTRL2_RELTARGETPWR.override = 236
        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 0

        phy.profile_outputs.AGC_CTRL3_RFPKDDEB.override = 1
        phy.profile_outputs.AGC_CTRL3_RFPKDDEBTHD.override = 2
        phy.profile_outputs.AGC_CTRL3_RFPKDDEBPRD.override = 40
        phy.profile_outputs.AGC_CTRL3_RFPKDDEBRST.override = 10
        phy.profile_outputs.AGC_CTRL3_IFPKDDEB.override = 0
        phy.profile_outputs.AGC_CTRL3_IFPKDDEBTHD.override = 2
        phy.profile_outputs.AGC_CTRL3_IFPKDDEBPRD.override = 40
        phy.profile_outputs.AGC_CTRL3_IFPKDDEBRST.override = 10

        phy.profile_outputs.AGC_GAINSTEPLIM_CFLOOPSTEPMAX.override = 4
        phy.profile_outputs.AGC_GAINSTEPLIM_CFLOOPDEL.override = 40
        phy.profile_outputs.AGC_GAINSTEPLIM_HYST.override = 3
        phy.profile_outputs.AGC_GAINSTEPLIM_MAXPWRVAR.override = 0
        phy.profile_outputs.AGC_GAINSTEPLIM_TRANRSTAGC.override = 0

        phy.profile_outputs.AGC_AGCPERIOD_PERIODHI.override = 14
        phy.profile_outputs.AGC_AGCPERIOD_PERIODLO.override = 45
        phy.profile_outputs.AGC_AGCPERIOD_MAXHICNTTHD.override = 7
        phy.profile_outputs.AGC_AGCPERIOD_SETTLETIMEIF.override = 6
        phy.profile_outputs.AGC_AGCPERIOD_SETTLETIMERF.override = 14

        phy.profile_outputs.AGC_GAINRANGE_LNAINDEXBORDER.override = 7
        phy.profile_outputs.AGC_GAINRANGE_PGAINDEXBORDER.override = 8
        phy.profile_outputs.AGC_GAINRANGE_GAININCSTEP.override = 1
        phy.profile_outputs.AGC_GAINRANGE_LATCHEDHISTEP.override = 0
        phy.profile_outputs.AGC_GAINRANGE_PNGAINSTEP.override = 3
        phy.profile_outputs.AGC_GAINRANGE_HIPWRTHD.override = 3

        phy.profile_outputs.AGC_MANGAIN_MANGAINEN.override = 0
        phy.profile_outputs.AGC_MANGAIN_MANGAINIFPGA.override = 7
        phy.profile_outputs.AGC_MANGAIN_MANGAINLNA.override = 1
        phy.profile_outputs.AGC_MANGAIN_MANGAINPN.override = 1

        phy.profile_outputs.AGC_HICNTREGION_HICNTREGION0.override = 3
        phy.profile_outputs.AGC_HICNTREGION_HICNTREGION1.override = 4
        phy.profile_outputs.AGC_HICNTREGION_HICNTREGION2.override = 5
        phy.profile_outputs.AGC_HICNTREGION_HICNTREGION3.override = 6
        phy.profile_outputs.AGC_HICNTREGION_HICNTREGION4.override = 8

        phy.profile_outputs.AGC_STEPDWN_STEPDWN0.override = 0
        phy.profile_outputs.AGC_STEPDWN_STEPDWN1.override = 1
        phy.profile_outputs.AGC_STEPDWN_STEPDWN2.override = 2
        phy.profile_outputs.AGC_STEPDWN_STEPDWN3.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN4.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN5.override = 3

        phy.profile_outputs.AGC_RSSISTEPTHR_POSSTEPTHR.override = 3
        phy.profile_outputs.AGC_RSSISTEPTHR_DEMODRESTARTTHR.override = 0xab
        phy.profile_outputs.AGC_RSSISTEPTHR_DEMODRESTARTPER.override = 5

        ##### RF peak detector threshold configuration
        phy.profile_outputs.RAC_PGACTRL_LNAMIXRFPKDTHRESHSEL.override = 2

		##### IF peak detector configuration
		# enable I/Q latch
        phy.profile_outputs.RAC_PGACTRL_PGAENLATCHI.override = 1
        phy.profile_outputs.RAC_PGACTRL_PGAENLATCHQ.override = 1
		# set IF peak detector threshold
        phy.profile_outputs.RAC_PGACTRL_PGATHRPKDHISEL.override = 5
        phy.profile_outputs.RAC_PGACTRL_PGATHRPKDLOSEL.override = 1

		