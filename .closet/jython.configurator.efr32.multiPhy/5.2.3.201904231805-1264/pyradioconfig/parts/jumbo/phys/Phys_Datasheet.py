from pyradioconfig.calculator_model_framework.interfaces.iphy import IPhy
from pyradioconfig.parts.jumbo.phys.phy_internal_base import Phy_Internal_Base

from py_2_and_3_compatibility import *

class PHYS_Datasheet(IPhy):

    def PHY_Datasheet_2450M_2GFSK_1Mbps_500K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='2450M 2GFSK 1Mbps 500K')

        Phy_Internal_Base.GFSK_2400M_base(phy, model)

        phy.profile_inputs.bitrate.value = 1000000
        phy.profile_inputs.deviation.value = 500000
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON

    def PHY_Datasheet_2450M_2GFSK_250Kbps_125K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='2450M 2GFSK 250Kbps 125K')

        Phy_Internal_Base.GFSK_2400M_base(phy, model)

        phy.profile_inputs.bitrate.value = 250000
        phy.profile_inputs.deviation.value = 125000
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.agc_settling_delay.value = 39
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.bandwidth_hz.value = 350000


    def PHY_Datasheet_2450M_2GFSK_2Mbps_1M(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='2450M 2GFSK 2Mbps 1M')

        Phy_Internal_Base.GFSK_2400M_base(phy, model)
        phy.profile_inputs.base_frequency_hz.value = long(2400000000)

        phy.profile_inputs.bitrate.value = 2000000
        phy.profile_inputs.deviation.value = 1000000
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.agc_settling_delay.value = 39
        phy.profile_inputs.bandwidth_hz.value = 2400000
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON


    def PHY_Datasheet_868M_2GFSK_2p4Kbps_1p2K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='868M 2GFSK 2.4Kbps 1.2K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        #phy.profile_inputs.bandwidth_hz.value = 4800
        phy.profile_inputs.base_frequency_hz.value =  long(868000000)
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value = 400000

    def PHY_Datasheet_868M_2GFSK_2p4Kbps_1p2K_ETSI(self,model):
        phy=self._makePhy(model,model.profiles.Base,readable_name='868M 2GFSK 2.4kbps1.2k ETSI category1',
                          phy_description='PHY showcasing ETSI category1 Rx compliance; TCXO and SAW filter are needed')
 
        Phy_Internal_Base.GFSK_915M_base(phy,model)

        phy.profile_inputs.base_frequency_hz.value= long(868000000)
        phy.profile_inputs.bitrate.value=2400
        phy.profile_inputs.deviation.value=1200
        phy.profile_inputs.frequency_comp_mode.value=model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.timing_sample_threshold.value=12
        phy.profile_inputs.src_disable.value=model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value=400000
        phy.profile_inputs.bandwidth_hz.value=10000
        phy.profile_inputs.pll_bandwidth_rx.value = model.vars.pll_bandwidth_rx.var_enum.BW_354KHz

    def PHY_Datasheet_868M_2GFSK_38p4Kbps_20K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='868M 2GFSK 38.4Kbps 20K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value =  long(868000000)
        phy.profile_inputs.bitrate.value = 38400
        phy.profile_inputs.deviation.value = 20000
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.target_osr.value = 8
        phy.profile_inputs.if_frequency_hz.value = 400000
        phy.profile_inputs.timing_sample_threshold.value = 8
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.bandwidth_hz.value = 75000


    def PHY_Datasheet_868M_2GFSK_500Kbps_125K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='868M 2GFSK 500Kbps 125K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)
        phy.profile_inputs.base_frequency_hz.value =  long(868000000)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 125000
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON

    def PHY_Datasheet_915M_2GFSK_600bps_300(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 600bps 300')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 600
        phy.profile_inputs.deviation.value = 300
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.errors_in_timing_window.value = 1
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.agc_settling_delay.value = 34

    def PHY_Datasheet_915M_2GFSK_100Kbps_50K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 100Kbps 50K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.deviation.value = 50000
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.agc_settling_delay.value = 34
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value = 300000

    def PHY_Datasheet_915M_2GFSK_100Kbps_50K_antdiv(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 100Kbps 50K antenna diversity')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.deviation.value = 50000
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value = 300000

        phy.profile_inputs.preamble_length.value = 120
        phy.profile_inputs.agc_settling_delay.value = 63
        phy.profile_inputs.number_of_timing_windows.value = 1
        phy.profile_inputs.rssi_period.value = 3
        phy.profile_inputs.timing_sample_threshold.value = 5

        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_297KHz

        phy.profile_inputs.antdivmode.value = model.vars.antdivmode.var_enum.ANTSELRSSI
        phy.profile_inputs.antdivrepeatdis.value = model.vars.antdivrepeatdis.var_enum.REPEATFIRST

    def PHY_Datasheet_915M_2GFSK_200Kbps_100K_antdiv(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 200Kbps 100K antenna diversity')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 200000
        phy.profile_inputs.deviation.value = 100000
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value = 300000

        phy.profile_inputs.preamble_length.value = 120
        phy.profile_inputs.agc_settling_delay.value = 63
        phy.profile_inputs.number_of_timing_windows.value = 1
        phy.profile_inputs.rssi_period.value = 3
        phy.profile_inputs.timing_sample_threshold.value = 10

        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_297KHz

        phy.profile_inputs.antdivmode.value = model.vars.antdivmode.var_enum.ANTSELRSSI
        phy.profile_inputs.antdivrepeatdis.value = model.vars.antdivrepeatdis.var_enum.REPEATFIRST

    def PHY_Datasheet_915M_2GFSK_500Kbps_175K_mi0p7(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 500Kbps 175K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 175000
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.agc_settling_delay.value = 29
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.if_frequency_hz.value = 750000

    def PHY_Datasheet_915M_2GFSK_50Kbps_25K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 50Kbps 25K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 50000
        phy.profile_inputs.deviation.value = 25000
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value = 400000

    # def PHY_Datasheet_915M_2GFSK_50Kbps_25K(self, model):
    #     phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 50Kbps 25K')
    #
    #     Phy_Internal_Base.GFSK_915M_base(phy, model)
    #
    #     # Add values to existing inputs
    #     phy.profile_inputs.bitrate.value = 50000
    #     phy.profile_inputs.deviation.value = 25000
    #     phy.profile_inputs.timing_detection_threshold.value = 20
    #     phy.profile_inputs.timing_sample_threshold.value = 12
    #     phy.profile_inputs.rx_xtal_error_ppm.value = 40
    #     phy.profile_inputs.errors_in_timing_window.value = 1
    #     phy.profile_inputs.freq_offset_hz.value = 0
    #     phy.profile_inputs.if_frequency_hz.value = 400000
    #     phy.profile_outputs.MODEM_AFC_AFCSCALEM.override = 12
    #     phy.profile_outputs.MODEM_MODINDEX_FREQGAINM.override = 7

    def PHY_Datasheet_915M_4GFSK_400Kbps_33p3K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 4GFSK 400Kbps 33.3K')
        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.base_frequency_hz.value =  long(915000000)
        phy.profile_inputs.bitrate.value = 400000
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.deviation.value = 33333
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK4
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 1.0

        phy.profile_inputs.bandwidth_hz.value = 370000
        phy.profile_inputs.if_frequency_hz.value = 400000
        phy.profile_inputs.agc_power_target.value = -8
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.timing_resync_period.value = 3
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.symbols_in_timing_window.value = 15
        #phy.profile_outputs.MODEM_CTRL4_DEVOFFCOMP.override = 1

    def PHY_Datasheet_915M_4GFSK_200Kbps_16p6K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 4GFSK 200Kbps 16.6K')
        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.base_frequency_hz.value =  long(915000000)
        phy.profile_inputs.bitrate.value = 200000
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.deviation.value = 16666
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK4
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 1.0

        phy.profile_inputs.bandwidth_hz.value = 185000
        phy.profile_inputs.if_frequency_hz.value = 400000
        phy.profile_inputs.agc_power_target.value = -8
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.timing_resync_period.value = 3

        phy.profile_outputs.MODEM_CTRL4_DEVOFFCOMP.override = 1

    def PHY_Datasheet_169M_2GFSK_2p4Kbps_1p2K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='169MHz 2GFSK 2.4Kbps 1.2KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.agc_settling_delay.value = 34
        phy.profile_inputs.base_frequency_hz.value =  long(169000000)
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.freq_offset_hz.value = 4000
        phy.profile_inputs.timing_detection_threshold.value = 12
        phy.profile_inputs.timing_sample_threshold.value = 8


    def PHY_Datasheet_169M_2GFSK_38p4Kbps_20K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='169MHz 2GFSK 38.4Kbps 20KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value =  long(169000000)
        phy.profile_inputs.bitrate.value = 38400
        phy.profile_inputs.deviation.value = 20000
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.bandwidth_hz.value = 75000

        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON


    def PHY_Datasheet_169M_2GFSK_500Kbps_125K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='169MHz 2GFSK 500Kbps 125KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value =  long(169000000)
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 125000

        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON


    def PHY_Datasheet_169M_2GFSK_2p4Kbps_1p2K_ETSI(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='169MHz 2GFSK 2.4Kbps 1.2KHz ETSI')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.agc_settling_delay.value = 34
        phy.profile_inputs.base_frequency_hz.value =  long(169000000)
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.etsi_cat1_compatible.value = model.vars.etsi_cat1_compatible.var_enum.Band_169
        phy.profile_inputs.freq_offset_hz.value = 4000
        phy.profile_inputs.if_frequency_hz.value = 75000
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 12
        phy.profile_inputs.timing_sample_threshold.value = 8
        phy.profile_inputs.bandwidth_hz.value = 10000

    def PHY_Datasheet_490M_2GFSK_10Kbps_5K(self,model):

        phy=self._makePhy(model,model.profiles.Base,readable_name='490MHz 2GFSK 10Kbps 5KHz')
        Phy_Internal_Base.GFSK_915M_base(phy,model)

        phy.profile_inputs.base_frequency_hz.value= long(490000000)
        phy.profile_inputs.bitrate.value=10000
        phy.profile_inputs.deviation.value=5000
        phy.profile_inputs.rx_xtal_error_ppm.value=0
        phy.profile_inputs.timing_detection_threshold.value=20

        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value=400000

        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON

    def PHY_Datasheet_490M_2GFSK_100Kbps_50K(self,model):

        phy=self._makePhy(model,model.profiles.Base,readable_name='490MHz 2GFSK 100Kbps 50KHz')
        Phy_Internal_Base.GFSK_915M_base(phy,model)

        phy.profile_inputs.base_frequency_hz.value= long(490000000)
        phy.profile_inputs.bitrate.value=100000
        phy.profile_inputs.deviation.value=50000
        phy.profile_inputs.rx_xtal_error_ppm.value=0
        phy.profile_inputs.timing_detection_threshold.value=20

        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value=400000

        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON

    def PHY_Datasheet_490M_2GFSK_2p4Kbps_1p2K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='490MHz 2GFSK 2.4Kbps 1.2KHz')
        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value =  long(490000000)
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 20

        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON

    def PHY_Datasheet_490M_2GFSK_38p4Kbps_20(self,model):

        phy=self._makePhy(model,model.profiles.Base,readable_name='490MHz 2GFSK 38.4Kbps 20KHz')
        Phy_Internal_Base.GFSK_915M_base(phy,model)

        phy.profile_inputs.base_frequency_hz.value= long(490000000)
        phy.profile_inputs.bitrate.value=38400
        phy.profile_inputs.deviation.value=20000
        phy.profile_inputs.rx_xtal_error_ppm.value=0
        phy.profile_inputs.timing_detection_threshold.value=20

        phy.profile_inputs.target_osr.value=8
        phy.profile_inputs.if_frequency_hz.value=400000
        phy.profile_inputs.timing_sample_threshold.value=8
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.bandwidth_hz.value=75000

        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON

    def PHY_Datasheet_434M_2GFSK_2p4Kbps_1p2K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='434M 2GFSK 2.4Kbps 1.2K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value =  long(434000000)
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.timing_sample_threshold.value = 8

    def PHY_Datasheet_434M_2GFSK_50Kbps_25K(self,model):
        phy=self._makePhy(model,model.profiles.Base,readable_name='434M 2GFSK 50Kbps 25K')

        Phy_Internal_Base.GFSK_915M_base(phy,model)
        phy.profile_inputs.base_frequency_hz.value= long(434000000)

        #Addvaluestoexistinginputs
        phy.profile_inputs.bitrate.value=50000
        phy.profile_inputs.deviation.value=25000
        phy.profile_inputs.timing_sample_threshold.value=8
        phy.profile_inputs.frequency_comp_mode.value=model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value=400000

    def PHY_Datasheet_434M_2GFSK_100Kbps_50K(self,model):
        phy=self._makePhy(model,model.profiles.Base,readable_name='434M 2GFSK 100Kbps 50K')

        Phy_Internal_Base.GFSK_915M_base(phy,model)
        phy.profile_inputs.base_frequency_hz.value= long(434000000)

        #Addvaluestoexistinginputs
        phy.profile_inputs.bitrate.value=100000
        phy.profile_inputs.deviation.value=50000
        phy.profile_inputs.timing_sample_threshold.value=8
        phy.profile_inputs.frequency_comp_mode.value=model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value=400000

    def PHY_Datasheet_434M_4GFSK_9p6Kbps_0p8K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='434M 4GFSK 9.6Kbps 0.8KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.base_frequency_hz.value =  long(434000000)
        phy.profile_inputs.bitrate.value = 9600
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.deviation.value = 800

        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK4
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 1.0

        phy.profile_inputs.bandwidth_hz.value = 8500
        phy.profile_inputs.if_frequency_hz.value = 400000
        phy.profile_inputs.agc_power_target.value = -8
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.timing_resync_period.value = 3

    def PHY_Datasheet_315M_2GFSK_2p4Kbps_1p2K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='315MHz 2GFSK 2.4Kbps 1.2KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value =  long(315000000)
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 12
        phy.profile_inputs.freq_offset_hz.value = 4000
        phy.profile_inputs.timing_sample_threshold.value = 8
        phy.profile_inputs.agc_settling_delay.value = 34

    def PHY_Datasheet_315M_2GFSK_38p4Kbps_20K(self,model):

        phy=self._makePhy(model,model.profiles.Base,readable_name='315MHz 2GFSK 38.4Kbps 20KHz')

        Phy_Internal_Base.GFSK_915M_base(phy,model)

        phy.profile_inputs.base_frequency_hz.value =  long(315000000)
        phy.profile_inputs.bitrate.value = 38400
        phy.profile_inputs.deviation.value = 20000
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.bandwidth_hz.value = 75000

    def PHY_Datasheet_315M_2GFSK_500Kbps_125K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='315MHz 2GFSK 500Kbps 125KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value =  long(315000000)
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 125000
        phy.profile_inputs.agc_settling_delay.value = 29
        phy.profile_inputs.number_of_timing_windows.value = 2
        phy.profile_inputs.symbols_in_timing_window.value = 8
        phy.profile_inputs.afc_step_scale.value = 0.75


    def PHY_Datasheet_285M_2GFSK_2p4Kbps_1p2K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='285MHz 2GFSK 2.4Kbps 1.2KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value =  long(285000000)
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 12
        phy.profile_inputs.freq_offset_hz.value = 4000
        phy.profile_inputs.timing_sample_threshold.value = 8
        phy.profile_inputs.agc_settling_delay.value = 34

    def PHY_Datasheet_285M_2GFSK_500Kbps_125K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='285MHz 2GFSK 500Kbps 125KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value =  long(285000000)
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 125000
        phy.profile_inputs.agc_settling_delay.value = 29
        phy.profile_inputs.number_of_timing_windows.value = 2
        phy.profile_inputs.symbols_in_timing_window.value = 8
        phy.profile_inputs.afc_step_scale.value = 0.75
