from pyradioconfig.calculator_model_framework.interfaces.iphy import IPhy
from pyradioconfig.parts.dumbo.phys.phy_internal_base import Phy_Internal_Base

from py_2_and_3_compatibility import *

class PHYS_Datasheet(IPhy):

    def PHY_Datasheet_2450M_2GFSK_1Mbps_500K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='2450M 2GFSK 1Mbps 500K')

        Phy_Internal_Base.GFSK_2400M_base(phy, model)

        phy.profile_inputs.bitrate.value = 1000000
        phy.profile_inputs.deviation.value = 500000
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.freq_offset_hz.value = 90014
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.agc_settling_delay.value = 39

    def PHY_Datasheet_2450M_2GFSK_250Kbps_125K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='2450M 2GFSK 250Kbps 125K')

        Phy_Internal_Base.GFSK_2400M_base(phy, model)

        phy.profile_inputs.baudrate_tol_ppm.value = 1000
        phy.profile_inputs.bitrate.value = 250000
        phy.profile_inputs.deviation.value = 125000
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.freq_offset_hz.value = 45000
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.agc_settling_delay.value = 39

    def PHY_Datasheet_2450M_2GFSK_2Mbps_1M(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='2450M 2GFSK 2Mbps 1M')

        Phy_Internal_Base.GFSK_2400M_base(phy, model)
        phy.profile_inputs.base_frequency_hz.value = long(2440000000)

        phy.profile_inputs.bitrate.value = 2000000
        phy.profile_inputs.deviation.value = 1000000
        phy.profile_inputs.freq_offset_hz.value = 45000
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.agc_settling_delay.value = 39

    def PHY_Datasheet_868M_2GFSK_2p4Kbps_1p2K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='868M 2GFSK 2.4Kbps 1.2K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(868000000)
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.agc_power_target.value = -8
        phy.profile_inputs.bandwidth_hz.value = 4800
        phy.profile_inputs.errors_in_timing_window.value = 1
        #phy.profile_inputs.freq_offset_hz.value = 0
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.agc_settling_delay.value = 34

    def PHY_Datasheet_868M_2GFSK_38p4Kbps_20K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='868M 2GFSK 38.4Kbps 20K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(868000000)
        phy.profile_inputs.bitrate.value = 38400
        phy.profile_inputs.deviation.value = 20000
        phy.profile_inputs.freq_offset_hz.value = 30000

    def PHY_Datasheet_868M_2GFSK_500Kbps_125K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='868M 2GFSK 500Kbps 125K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)
        phy.profile_inputs.base_frequency_hz.value = long(868000000)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 125000
        phy.profile_inputs.freq_offset_hz.value = 100000
        phy.profile_inputs.agc_settling_delay.value = 29
        phy.profile_inputs.number_of_timing_windows.value = 2
        phy.profile_inputs.symbols_in_timing_window.value = 8
        phy.profile_inputs.afc_step_scale.value = 0.75

    def PHY_Datasheet_915M_2GFSK_100Kbps_50K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 100Kbps 50K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.deviation.value = 50000
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.agc_power_target.value = -8
        phy.profile_inputs.errors_in_timing_window.value = 1
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.agc_settling_delay.value = 34

    def PHY_Datasheet_915M_2GFSK_500Kbps_175K_mi0p7(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 500Kbps 175K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 175000
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.freq_offset_hz.value = 50000
        phy.profile_inputs.number_of_timing_windows.value = 2
        phy.profile_inputs.symbols_in_timing_window.value = 8
        phy.profile_inputs.agc_settling_delay.value = 29

    def PHY_Datasheet_915M_2GFSK_50Kbps_25K(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 50Kbps 25K')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 50000
        phy.profile_inputs.deviation.value = 25000
        phy.profile_inputs.rx_xtal_error_ppm.value = 10
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.agc_power_target.value = -8
        phy.profile_inputs.bandwidth_hz.value = 120000
        phy.profile_inputs.errors_in_timing_window.value = 1
        phy.profile_inputs.freq_offset_hz.value = 30004
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.agc_settling_delay.value = 34

    def PHY_Datasheet_169M_2GFSK_2p4Kbps_1p2K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='169MHz 2GFSK 2.4Kbps 1.2KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(169000000)
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 12
        phy.profile_inputs.freq_offset_hz.value = 4000
        phy.profile_inputs.timing_sample_threshold.value = 8
        phy.profile_inputs.agc_settling_delay.value = 34

    def PHY_Datasheet_169M_2GFSK_38p4Kbps_20K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='169MHz 2GFSK 38.4Kbps 20KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(169000000)
        phy.profile_inputs.bitrate.value = 38400
        phy.profile_inputs.deviation.value = 20000
        phy.profile_inputs.rx_xtal_error_ppm.value = 20

    def PHY_Datasheet_169M_2GFSK_500Kbps_125K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='169MHz 2GFSK 500Kbps 125KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(169000000)
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 125000
        phy.profile_inputs.rx_xtal_error_ppm.value = 20

    def PHY_Datasheet_490M_2GFSK_10Kbps_5K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='490MHz 2GFSK 10Kbps 5KHz')
        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(490000000)
        phy.profile_inputs.bitrate.value = 10000
        phy.profile_inputs.deviation.value = 5000
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 20

    def PHY_Datasheet_490M_2GFSK_100Kbps_50K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='490MHz 2GFSK 100Kbps 50KHz')
        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(490000000)
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.deviation.value = 50000
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 20

    def PHY_Datasheet_490M_2GFSK_2p4Kbps_1p2K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='490MHz 2GFSK 2.4Kbps 1.2KHz')
        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(490000000)
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 20

    def PHY_Datasheet_490M_2GFSK_38p4Kbps_20(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='490MHz 2GFSK 38.4Kbps 20KHz')
        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(490000000)
        phy.profile_inputs.bitrate.value = 38400
        phy.profile_inputs.deviation.value = 20000
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 20

    def PHY_Datasheet_315M_2GFSK_2p4Kbps_1p2K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='315MHz 2GFSK 2.4Kbps 1.2KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(315000000)
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 12
        phy.profile_inputs.freq_offset_hz.value = 4000
        phy.profile_inputs.timing_sample_threshold.value = 8
        phy.profile_inputs.agc_settling_delay.value = 34

    def PHY_Datasheet_315M_2GFSK_38p4Kbps_20K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='315MHz 2GFSK 38.4Kbps 20KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(315000000)
        phy.profile_inputs.bitrate.value = 38400
        phy.profile_inputs.deviation.value = 20000
        phy.profile_inputs.rx_xtal_error_ppm.value = 20

    def PHY_Datasheet_315M_2GFSK_500Kbps_125K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='315MHz 2GFSK 500Kbps 125KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(315000000)
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 125000
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.agc_settling_delay.value = 29
        phy.profile_inputs.number_of_timing_windows.value = 2
        phy.profile_inputs.symbols_in_timing_window.value = 8
        phy.profile_inputs.afc_step_scale.value = 0.75


    def PHY_Datasheet_285M_2GFSK_2p4Kbps_1p2K(self, model):

        phy = self._makePhy(model, model.profiles.Base, readable_name='285MHz 2GFSK 2.4Kbps 1.2KHz')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = long(285000000)
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 12
        phy.profile_inputs.freq_offset_hz.value = 4000
        phy.profile_inputs.timing_sample_threshold.value = 8
        phy.profile_inputs.agc_settling_delay.value = 34