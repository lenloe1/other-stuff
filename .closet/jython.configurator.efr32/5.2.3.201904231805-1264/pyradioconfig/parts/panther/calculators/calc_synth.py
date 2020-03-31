from pyradioconfig.parts.nixi.calculators.calc_synth import CALC_Synth_nixi


class CALC_Synth_panther(CALC_Synth_nixi):

    def calc_lo_side_regs(self, model):
        """
        Starting with Panther, make this selectable by optional model.vars.lo_injection_side
        calculate LOSIDE register in synth and matching one in modem

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        lo_injection_side = model.vars.lo_injection_side.value

        if lo_injection_side == model.vars.lo_injection_side.var_enum.HIGH_SIDE:
            self._reg_write(model.vars.SYNTH_IFFREQ_LOSIDE,  1)

            self._reg_write(model.vars.MODEM_MIXCTRL_ANAMIXMODE, 0)
            self._reg_write(model.vars.MODEM_MIXCTRL_DIGIQSWAPEN,    1)

        if lo_injection_side == model.vars.lo_injection_side.var_enum.LOW_SIDE:
            self._reg_write(model.vars.SYNTH_IFFREQ_LOSIDE,  0)

            # TODO: Need Design to confirm if Series 2MODEM_MIXCTRL_ANAMIXMODE
            # value 2 "IPQN" "I path is positive, Q path is negative"
            # is same as Series 1 MODEM_MIXCTRL_MODE
            # value 2 "CONJUGATE" "The analog IF signal output from the analog receiver mixer is conjuga-
            # ted, for high-side LO injection (use when SYNTH->IFFREQ->LOSIDE is HIGH)"
            # For now, presuming it is.
            self._reg_write(model.vars.MODEM_MIXCTRL_ANAMIXMODE, 2)
            self._reg_write(model.vars.MODEM_MIXCTRL_DIGIQSWAPEN,    0)