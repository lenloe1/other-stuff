from pyradioconfig.calculator_model_framework.interfaces.iphy import IPhy

from py_2_and_3_compatibility import *

class PHYS_MBus_Studio(IPhy):

    #
    #
    #
    def PHY_wMbus_ModeT_M2O_100k_no_postamble_frameA(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus T 100k, no postamble')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeT_M2O_100k
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameA
        phy.profile_inputs.base_frequency_hz.value = long(868950000)
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        #Does need some workarounds, but we do need it
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.MBUS_3OF6
        phy.profile_inputs.syncword_dualsync.value = False

    def PHY_wMbus_ModeT_O2M_32p768k_frameA(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus T O2M 32.768k')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeT_O2M_32p768k
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameA
        phy.profile_inputs.base_frequency_hz.value = long(868300000)
        phy.profile_inputs.channel_spacing_hz.value = 300000
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.Manchester
        phy.profile_inputs.syncword_dualsync.value = False

    #same as T mode, but with disabled block coder, dfl and crc. Needs software decoder, dfl, crc, decision can be made by first 6 bits of payload
    def PHY_wMbus_ModeTC_M2O_100k_noFrame(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus T+C 100k, no 3of6, no crc')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeT_M2O_100k
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.NoFormat
        phy.profile_inputs.base_frequency_hz.value = long(868950000)
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        #phy.profile_inputs.fixed_length_size.value = 18 #first block in C mode: 2B sync + 10B +2B crc=14B. in T mode: (10B+2B crc)*1.5=18
        phy.profile_inputs.syncword_dualsync.value = False

    #
    #
    #
    def PHY_wMbus_ModeC_M2O_100k_frameA(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus C 100k, frameA')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeC_M2O_100k
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameA
        phy.profile_inputs.base_frequency_hz.value = long(868950000)
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_dualsync.value = False

    def PHY_wMbus_ModeC_M2O_100k_frameB(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus C 100k, frameB')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeC_M2O_100k
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameB
        phy.profile_inputs.base_frequency_hz.value = long(868950000)
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_dualsync.value = False

    #
    #
    #
    def PHY_wMbus_ModeC_O2M_50k_frameA(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus C 50k, frameA')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeC_O2M_50k
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameA
        phy.profile_inputs.base_frequency_hz.value = long(869525000)
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_dualsync.value = False

    def PHY_wMbus_ModeC_O2M_50k_frameB(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus C 50k, frameB')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeC_O2M_50k
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameB
        phy.profile_inputs.base_frequency_hz.value = long(869525000)
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_dualsync.value = False

    #
    #
    #
    def PHY_wMbus_ModeS_32p768k_frameA(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus S Mode 32.768k')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeS_32p768k
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameA
        phy.profile_inputs.base_frequency_hz.value = long(868300000)
        phy.profile_inputs.channel_spacing_hz.value = 300000
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.Manchester
        phy.profile_inputs.syncword_dualsync.value = False

    #
    #
    #
    def PHY_wMbus_ModeNabef_4p8K_frameA(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus Mode Na, Nb, Ne, Nf 4p8K, frameA')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeN1a_4p8K
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameA
        phy.profile_inputs.base_frequency_hz.value = long(169406250)
        phy.profile_inputs.channel_spacing_hz.value = 12500
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_dualsync.value = False

    def PHY_wMbus_ModeNabef_4p8K_frameB(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus Mode Na, Nb, Ne, Nf 4p8K, frameB')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeN1a_4p8K
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameB
        phy.profile_inputs.base_frequency_hz.value = long(169406250)
        phy.profile_inputs.channel_spacing_hz.value = 12500
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_dualsync.value = False

    #
    #
    #
    def PHY_wMbus_ModeNcd_2p4K_frameA(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus Mode Nc Nd 2p4K, frameA')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeN1c_2p4K
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameA
        phy.profile_inputs.base_frequency_hz.value = long(169431250)
        phy.profile_inputs.channel_spacing_hz.value = 12500
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_dualsync.value = False

    def PHY_wMbus_ModeNcd_2p4K_frameB(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus Mode Nc Nd 2p4K, frameB')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeN1c_2p4K
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameB
        phy.profile_inputs.base_frequency_hz.value = long(169431250)
        phy.profile_inputs.channel_spacing_hz.value = 12500
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_dualsync.value = False

    #
    #
    #
    def PHY_wMbus_ModeN2g_19p2k_frameA(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus Ng, frameA')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeNg
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameA
        phy.profile_inputs.base_frequency_hz.value = long(169437500)
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_dualsync.value = False

    def PHY_wMbus_ModeN2g_19p2k_frameB(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus Ng, frameB')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeNg
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameB
        phy.profile_inputs.base_frequency_hz.value = long(169437500)
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_dualsync.value = False

    #
    #
    #
    def PHY_wMbus_ModeR_4p8k_frameA(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus Mode R 4p8k, frameA')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeR_4p8k
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameA
        phy.profile_inputs.base_frequency_hz.value = long(868330000)
        phy.profile_inputs.channel_spacing_hz.value = 60000
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.Manchester
        phy.profile_inputs.syncword_dualsync.value = False

    #
    #
    #
    def PHY_wMbus_ModeF_2p4k_frameA(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus Mode F 2p4k, frameA')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeF_2p4k
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameA
        phy.profile_inputs.base_frequency_hz.value = long(433820000)
        phy.profile_inputs.channel_spacing_hz.value = 50000
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_dualsync.value = False

    #
    #
    #
    def PHY_wMbus_ModeF_2p4k_frameB(self, model):
        phy = self._makePhy(model, model.profiles.Mbus, 'PHY WMbus Mode F 2p4k, frameB')

        phy.profile_inputs.mbus_mode.value = model.vars.mbus_mode.var_enum.ModeF_2p4k
        phy.profile_inputs.mbus_frame_format.value = model.vars.mbus_frame_format.var_enum.FrameB
        phy.profile_inputs.base_frequency_hz.value = long(433820000)
        phy.profile_inputs.channel_spacing_hz.value = 50000
        phy.profile_inputs.mbus_symbol_encoding.value = model.vars.mbus_symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_dualsync.value = False
