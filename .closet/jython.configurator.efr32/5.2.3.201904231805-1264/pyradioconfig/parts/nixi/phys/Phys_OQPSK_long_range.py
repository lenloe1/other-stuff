from pyradioconfig.calculator_model_framework.interfaces.iphy import IPhy

from py_2_and_3_compatibility import *

class PHYS_OQPSK_LoRa_Nixi(IPhy):
    # inherit from none
    ################################################################################################
    # "base" definitions of the non-FEC PHY. allows usage in multiple PHYs

    def OQPSK_long_range_base(self, phy, model):
        phy.profile_inputs.agc_settling_delay.value = 40
        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.deviation.value = 2400
        phy.profile_inputs.base_frequency_hz.value = long(915000000)
        phy.profile_inputs.bitrate.value = 1200
        phy.profile_inputs.dsss_chipping_code.value = long(1951056795)
        phy.profile_inputs.dsss_len.value = 32
        phy.profile_inputs.dsss_spreading_factor.value = 8
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.timing_sample_threshold.value = 0
        phy.profile_inputs.symbols_in_timing_window.value = 12
        phy.profile_inputs.number_of_timing_windows.value = 7
        phy.profile_inputs.agc_power_target.value = -11
        phy.profile_inputs.rssi_period.value = 8
        phy.profile_inputs.preamble_pattern.value = 0
        phy.profile_inputs.preamble_pattern_len.value = 4
        phy.profile_inputs.preamble_length.value = 40
        phy.profile_inputs.syncword_0.value = long(229)
        phy.profile_inputs.syncword_1.value = long(0)
        phy.profile_inputs.syncword_length.value = 12
        phy.profile_inputs.syncword_tx_skip.value = False
        phy.profile_inputs.asynchronous_rx_enable.value = False
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.OQPSK
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.DISABLED
        phy.profile_inputs.target_osr.value = 5
        phy.profile_inputs.agc_scheme.value = model.vars.agc_scheme.var_enum.SCHEME_3
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Custom_OQPSK
        phy.profile_inputs.shaping_filter_param.value = 0.3
        phy.profile_inputs.channel_spacing_hz.value = 5000000
        phy.profile_inputs.test_ber.value = False
        phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.CCITT_16
        phy.profile_inputs.crc_seed.value = long(0)
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_pad_input.value = False
        phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.LSB_FIRST
        phy.profile_inputs.crc_invert.value = False
        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.LSB_FIRST
        phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
        phy.profile_inputs.payload_white_en.value = False
        phy.profile_inputs.payload_crc_en.value = True
        phy.profile_inputs.header_en.value = True
        phy.profile_inputs.header_size.value = 1
        phy.profile_inputs.header_calc_crc.value = False
        phy.profile_inputs.header_white_en.value = False
        phy.profile_inputs.fixed_length_size.value = 1
        phy.profile_inputs.var_length_numbits.value = 8
        phy.profile_inputs.var_length_byteendian.value = model.vars.var_length_byteendian.var_enum.LSB_FIRST
        phy.profile_inputs.var_length_bitendian.value = model.vars.var_length_bitendian.var_enum.LSB_FIRST
        phy.profile_inputs.var_length_shift.value = 0
        phy.profile_inputs.var_length_minlength.value = 5
        phy.profile_inputs.var_length_maxlength.value = 127
        phy.profile_inputs.var_length_includecrc.value = True
        phy.profile_inputs.var_length_adjust.value = 0
        phy.profile_inputs.frame_type_loc.value = 0
        phy.profile_inputs.frame_type_bits.value = 0
        phy.profile_inputs.frame_type_lsbit.value = 0
        phy.profile_inputs.frame_type_0_length.value = 0
        phy.profile_inputs.frame_type_1_length.value = 0
        phy.profile_inputs.frame_type_2_length.value = 0
        phy.profile_inputs.frame_type_3_length.value = 0
        phy.profile_inputs.frame_type_4_length.value = 0
        phy.profile_inputs.frame_type_5_length.value = 0
        phy.profile_inputs.frame_type_6_length.value = 0
        phy.profile_inputs.frame_type_7_length.value = 0
        phy.profile_inputs.frame_type_0_valid.value = False
        phy.profile_inputs.frame_type_1_valid.value = False
        phy.profile_inputs.frame_type_2_valid.value = False
        phy.profile_inputs.frame_type_3_valid.value = False
        phy.profile_inputs.frame_type_4_valid.value = False
        phy.profile_inputs.frame_type_5_valid.value = False
        phy.profile_inputs.frame_type_6_valid.value = False
        phy.profile_inputs.frame_type_7_valid.value = False
        phy.profile_inputs.frame_type_0_filter.value = True
        phy.profile_inputs.frame_type_1_filter.value = True
        phy.profile_inputs.frame_type_2_filter.value = True
        phy.profile_inputs.frame_type_3_filter.value = True
        phy.profile_inputs.frame_type_4_filter.value = True
        phy.profile_inputs.frame_type_5_filter.value = True
        phy.profile_inputs.frame_type_6_filter.value = True
        phy.profile_inputs.frame_type_7_filter.value = True
        phy.profile_inputs.symbol_encoding.value = model.vars.symbol_encoding.var_enum.DSSS
        phy.profile_inputs.manchester_mapping.value = model.vars.manchester_mapping.var_enum.Default
        phy.profile_inputs.white_poly.value = model.vars.white_poly.var_enum.NONE
        phy.profile_inputs.white_seed.value = 0
        phy.profile_inputs.white_output_bit.value = 0
        phy.profile_inputs.frame_coding.value = model.vars.frame_coding.var_enum.NONE


    def PHY_Datasheet_915MHz_OQPSK_1p2kbps_2p4k(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915MHz OQPSK 1p2kbps 2p4k long range')

        self.OQPSK_long_range_base(phy, model)
        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE

    def PHY_Datasheet_915MHz_OQPSK_1p2kbps_2p4k_FEC(self, model):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915MHz OQPSK 1p2kbps 2p4k FEC long range')

        self.OQPSK_long_range_base(phy, model)
        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.FEC_154G_K7

        phy.profile_inputs.timing_detection_threshold.value = 98