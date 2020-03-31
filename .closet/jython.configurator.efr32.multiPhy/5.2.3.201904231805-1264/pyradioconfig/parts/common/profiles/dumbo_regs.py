from pycalcmodel.core.output import ModelOutput, ModelOutputType


def build_modem_regs_dumbo(model,profile, family):
    profile.outputs.append(ModelOutput(model.vars.MODEM_CF_CFOSR, '',                ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CF.CFOSR'                  ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CF_DEC0, '',                 ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CF.DEC0'                   ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CF_DEC1, '',                 ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CF.DEC1'                   ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CF_DEC1GAIN, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CF.DEC1GAIN'               ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CF_DEC2, '',                 ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CF.DEC2'                   ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL0_CODING, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL0.CODING'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL0_DIFFENCMODE, '',       ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL0.DIFFENCMODE'         ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL0_DSSSDOUBLE, '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL0.DSSSDOUBLE'          ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL0_DSSSLEN, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL0.DSSSLEN'             ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL0_DSSSSHIFTS, '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL0.DSSSSHIFTS'          ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL0_FDM0DIFFDIS, '',       ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL0.FDM0DIFFDIS'         ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL0_FRAMEDETDEL, '',       ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL0.FRAMEDETDEL'         ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL0_MAPFSK, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL0.MAPFSK'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL0_MODFORMAT, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL0.MODFORMAT'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL0_SHAPING, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL0.SHAPING'             ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL1_COMPMODE, '',          ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL1.COMPMODE'            ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL1_DUALSYNC, '',          ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL1.DUALSYNC'            ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL1_FREQOFFESTLIM, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL1.FREQOFFESTLIM'       ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL1_FREQOFFESTPER, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL1.FREQOFFESTPER'       ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL1_PHASEDEMOD, '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL1.PHASEDEMOD'          ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL1_RESYNCPER, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL1.RESYNCPER'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL1_SYNC1INV, '',          ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL1.SYNC1INV'            ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL1_SYNCBITS, '',          ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL1.SYNCBITS'            ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL1_SYNCERRORS, '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL1.SYNCERRORS'          ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL1_SYNCDATA, '',          ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL1.SYNCDATA'            ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL2_BRDIVA, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL2.BRDIVA'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL2_BRDIVB, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL2.BRDIVB'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL2_DATAFILTER, '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL2.DATAFILTER'          ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL2_DEVWEIGHTDIS, '',      ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL2.DEVWEIGHTDIS'        ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL2_SQITHRESH, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL2.SQITHRESH'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL3_TSAMPDEL, '',          ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL3.TSAMPDEL'            ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL3_TSAMPLIM, '',          ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL3.TSAMPLIM'            ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL3_TSAMPMODE, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL3.TSAMPMODE'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL4_ADCSATDENS, '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL4.ADCSATLEVEL'         ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL4_ADCSATLEVEL, '',       ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL4.ADCSATLEVEL'         ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL4_DEVOFFCOMP, '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL4.DEVOFFCOMP'          ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL4_ISICOMP, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL4.ISICOMP'             ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL4_OFFSETPHASEMASKING,'', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL4.OFFSETPHASEMASKING'  ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL5_BRCALAVG, '',          ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL5.BRCALAVG'            ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL5_BRCALEN, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL5.BRCALEN'             ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL5_BRCALMODE, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL5.BRCALMODE'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL5_DETDEL, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL5.DETDEL'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL5_TDEDGE, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL5.TDEDGE'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL5_TREDGE, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL5.TREDGE'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_MODINDEX_FREQGAINE, '',      ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.MODINDEX.FREQGAINE'        ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_MODINDEX_FREQGAINM, '',      ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.MODINDEX.FREQGAINM'        ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_MODINDEX_MODINDEXE, '',      ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.MODINDEX.MODINDEXE'        ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_MODINDEX_MODINDEXM, '',      ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.MODINDEX.MODINDEXM'        ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_PRE_BASE, '',                ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PRE.BASE'                  ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_PRE_BASEBITS, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PRE.BASEBITS'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_PRE_DSSSPRE, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PRE.DSSSPRE'               ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_PRE_PREERRORS, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PRE.PREERRORS'             ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_PRE_TXBASES, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PRE.TXBASES'               ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_RXBR_RXBRDEN, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.RXBR.RXBRDEN'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_RXBR_RXBRINT, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.RXBR.RXBRINT'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_RXBR_RXBRNUM, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.RXBR.RXBRNUM'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SHAPING0_COEFF0, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SHAPING0.COEFF0'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SHAPING0_COEFF1, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SHAPING0.COEFF1'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SHAPING0_COEFF2, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SHAPING0.COEFF2'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SHAPING0_COEFF3, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SHAPING0.COEFF3'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SHAPING1_COEFF4, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SHAPING1.COEFF4'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SHAPING1_COEFF5, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SHAPING1.COEFF5'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SHAPING1_COEFF6, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SHAPING1.COEFF6'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SHAPING1_COEFF7, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SHAPING1.COEFF7'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SHAPING2_COEFF8, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SHAPING2.COEFF8'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNC0_SYNC0, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNC0.SYNC0'               ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNC1_SYNC1, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNC1.SYNC1'               ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TIMING_ADDTIMSEQ, '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TIMING.ADDTIMSEQ'          ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TIMING_FASTRESYNC, '',       ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TIMING.FASTRESYNC'         ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TIMING_FDM0THRESH, '',       ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TIMING.FDM0THRESH'         ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TIMING_OFFSUBDEN, '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TIMING.OFFSUBDEN'          ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TIMING_OFFSUBNUM, '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TIMING.OFFSUBNUM'          ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TIMING_TIMINGBASES, '',      ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TIMING.TIMINGBASES'        ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TIMING_TIMSEQSYNC, '',       ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TIMING.TIMSEQSYNC'         ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TIMING_TIMTHRESH, '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TIMING.TIMTHRESH'          ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TIMING_TSAGCDEL, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TIMING.TSAGCDEL'           ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXBR_TXBRDEN, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXBR.TXBRDEN'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXBR_TXBRNUM, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXBR.TXBRNUM'              ))

    profile.outputs.append(ModelOutput(model.vars.MODEM_DSSS0_DSSS0, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DSSS0.DSSS0'               ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_AFCADJLIM_AFCADJLIM, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.AFCADJLIM.AFCADJLIM'       ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_AFC_AFCAVGPER, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.AFC.AFCAVGPER'             ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_AFC_AFCDEL, '',              ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.AFC.AFCDEL'                ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_AFC_AFCRXCLR, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.AFC.AFCRXCLR'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_AFC_AFCRXMODE, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.AFC.AFCRXMODE'             ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_AFC_AFCSCALEE, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.AFC.AFCSCALEE'             ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_AFC_AFCSCALEM, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.AFC.AFCSCALEM'             ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_AFC_AFCTXMODE, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.AFC.AFCTXMODE'             ))

    profile.outputs.append(ModelOutput(model.vars.MODEM_MIXCTRL_MODE, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.MIXCTRL.MODE'              ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_MIXCTRL_DIGIQSWAPEN, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.MIXCTRL.DIGIQSWAPEN'       ))

    profile.outputs.append(ModelOutput(model.vars.RAC_IFADCCTRL_REALMODE, '',        ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFADCCTRL.REALMODE'          ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFADCCTRL_VLDOCLKGEN, '',      ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFADCCTRL.VLDOCLKGEN'        ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFADCCTRL_REGENCLKDELAY, '',   ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFADCCTRL.VLDOCLKGEN'        ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFADCCTRL_INPUTSCALE, '',      ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFADCCTRL.INPUTSCALE'        ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFADCCTRL_OTA1CURRENT, '',     ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFADCCTRL.OTA1CURRENT'       ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFADCCTRL_OTA2CURRENT, '',     ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFADCCTRL.OTA2CURRENT'       ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFADCCTRL_OTA3CURRENT, '',     ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFADCCTRL.OTA3CURRENT'       ))

    profile.outputs.append(ModelOutput(model.vars.RAC_IFADCCTRL_VCM, '',             ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFADCCTRL.VCM'               ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFADCCTRL_VLDOSERIES, '',      ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFADCCTRL.VLDOSERIES'        ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFADCCTRL_VLDOSERIESCURR, '',  ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFADCCTRL.VLDOSERIESCURR'    ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFADCCTRL_VLDOSHUNT, '',       ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFADCCTRL.VLDOSHUNT'         ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFADCCTRL_INVERTCLK, '',       ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFADCCTRL.INVERTCLK'         ))

    profile.outputs.append(ModelOutput(model.vars.RAC_IFFILTCTRL_VCM, '',            ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFFILTCTRL.VCM'              ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFFILTCTRL_VREG, '',           ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFFILTCTRL.VREG'             ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFFILTCTRL_BANDWIDTH, '',      ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFFILTCTRL.BANDWIDTH'        ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFFILTCTRL_CENTFREQ, '',       ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFFILTCTRL.CENTFREQ'         ))

    profile.outputs.append(ModelOutput(model.vars.SEQ_SYNTHLPFCTRLTX_SYNTHLPFCTRLTX, '', ModelOutputType.SEQ_REG_FIELD, readable_name='SEQ.SYNTHLPFCTRLTX.SYNTHLPFCTRLTX'  ))
    profile.outputs.append(ModelOutput(model.vars.SEQ_SYNTHLPFCTRLRX_SYNTHLPFCTRLRX, '', ModelOutputType.SEQ_REG_FIELD, readable_name='SEQ.SYNTHLPFCTRLRX.SYNTHLPFCTRLRX'  ))

    profile.outputs.append(ModelOutput(model.vars.RAC_IFPGACTRL_VLDO, '',            ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFPGACTRL.VLDO'              ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFPGACTRL_BANDSEL, '',         ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFPGACTRL.BANDSEL'           ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFPGACTRL_CASCBIAS, '',        ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFPGACTRL.CASCBIAS'          ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFPGACTRL_TRIMVCASLDO, '',     ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFPGACTRL.TRIMVCASLDO'       ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFPGACTRL_TRIMVCM, '',         ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFPGACTRL.TRIMVCM'           ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFPGACTRL_TRIMVREFLDO, '',     ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFPGACTRL.TRIMVREFLDO'       ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFPGACTRL_TRIMVREGMIN, '',     ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFPGACTRL.TRIMVREGMIN'       ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFPGACTRL_ENHYST, '',          ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFPGACTRL.ENHYST'            ))
    profile.outputs.append(ModelOutput(model.vars.RAC_IFPGACTRL_ENOFFD, '',          ModelOutputType.SVD_REG_FIELD, readable_name='RAC.IFPGACTRL.ENOFFD'            ))

    profile.outputs.append(ModelOutput(model.vars.RAC_RFENCTRL_DEMEN, '',            ModelOutputType.SVD_REG_FIELD, readable_name='RAC.RFENCTRL.DEMEN'              ))
    profile.outputs.append(ModelOutput(model.vars.RAC_RFENCTRL_IFADCCAPRESET, '',    ModelOutputType.SVD_REG_FIELD, readable_name='RAC.RFENCTRL.IFADCCAPRESET'      ))

    profile.outputs.append(ModelOutput(model.vars.SYNTH_CALOFFSET_CALOFFSET, '',     ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.CALOFFSET.CALOFFSET'       ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_CHCTRL_CHNO, '',             ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.CHCTRL.CHNO'               ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_CHSP_CHSP, '',               ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.CHSP.CHSP'                 ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DIVCTRL_LODIVFREQCTRL, '',   ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.DIVCTRL.LODIVFREQCTRL'     ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FREQ_FREQ, '',               ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.FREQ.FREQ'                 ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_IFFREQ_IFFREQ, '',           ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.IFFREQ.IFFREQ'             ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_IFFREQ_LOSIDE, '',           ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.IFFREQ.LOSIDE'             ))

    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL0_ADCRESETDURATION, '',    ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL0.ADCRESETDURATION'      ))
    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL0_RSSISHIFT, '',           ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL0.RSSISHIFT'             ))
    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL0_PWRTARGET, '',           ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL0.PWRTARGET'             ))
    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL0_MODE, '',                ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL0.MODE'                  ))

    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL1_AGCPERIOD, '',           ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL1.AGCPERIOD'             ))
    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL1_RSSIPERIOD, '',          ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL1.RSSIPERIOD'            ))
    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL1_SUBPERIOD, '',           ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL1.SUBPERIOD'             ))
    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL1_SUBINT, '',              ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL1.SUBINT'                ))
    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL1_SUBNUM, '',              ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL1.SUBNUM'                ))
    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL1_SUBDEN, '',              ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL1.SUBDEN'                ))

    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL2_ADCRSTSTARTUP, '',       ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL2.ADCRSTSTARTUP'         ))
    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL2_MAXPWRVAR, '',           ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL2.MAXPWRVAR'             ))
    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL2_HYST, '',                ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL2.HYST'                  ))
    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL2_FASTLOOPDEL, '',         ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL2.FASTLOOPDEL'           ))
    profile.outputs.append(ModelOutput(model.vars.AGC_CTRL2_CFLOOPDEL, '',           ModelOutputType.SVD_REG_FIELD, readable_name='AGC.CTRL2.CFLOOPDEL'             ))

    profile.outputs.append(ModelOutput(model.vars.AGC_GAINSTEPLIM_CFLOOPSTEPMAX, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.GAINSTEPLIM.CFLOOPSTEPMAX'   ))
    profile.outputs.append(ModelOutput(model.vars.AGC_GAINSTEPLIM_FASTSTEPUP, '',    ModelOutputType.SVD_REG_FIELD, readable_name='AGC.GAINSTEPLIM.FASTSTEPUP'      ))
    profile.outputs.append(ModelOutput(model.vars.AGC_GAINSTEPLIM_FASTSTEPDOWN, '',  ModelOutputType.SVD_REG_FIELD, readable_name='AGC.GAINSTEPLIM.FASTSTEPDOWN'    ))

    profile.outputs.append(ModelOutput(model.vars.AGC_LOOPDEL_LNASLICESDEL, '',      ModelOutputType.SVD_REG_FIELD, readable_name='AGC.LOOPDEL.LNASLICESDEL'        ))
    profile.outputs.append(ModelOutput(model.vars.AGC_LOOPDEL_IFPGADEL, '',          ModelOutputType.SVD_REG_FIELD, readable_name='AGC.LOOPDEL.IFPGADEL'            ))
    profile.outputs.append(ModelOutput(model.vars.AGC_LOOPDEL_PKDWAIT, '',           ModelOutputType.SVD_REG_FIELD, readable_name='AGC.LOOPDEL.PKDWAIT'             ))

    profile.outputs.append(ModelOutput(model.vars.AGC_GAINRANGE_MAXGAIN, '',         ModelOutputType.SVD_REG_FIELD, readable_name='AGC.GAINRANGE.MAXGAIN'           ))
    profile.outputs.append(ModelOutput(model.vars.AGC_GAINRANGE_MINGAIN, '',         ModelOutputType.SVD_REG_FIELD, readable_name='AGC.GAINRANGE.MINGAIN'           ))

    profile.outputs.append(ModelOutput(model.vars.AGC_GAININDEX_MININDEXDEGEN, '',   ModelOutputType.SVD_REG_FIELD, readable_name='AGC.GAININDEX.MININDEXDEGEN'     ))
    profile.outputs.append(ModelOutput(model.vars.AGC_GAININDEX_MININDEXPGA, '',     ModelOutputType.SVD_REG_FIELD, readable_name='AGC.GAININDEX.MININDEXPGA'       ))
    profile.outputs.append(ModelOutput(model.vars.AGC_GAININDEX_NUMINDEXATTEN, '',   ModelOutputType.SVD_REG_FIELD, readable_name='AGC.GAININDEX.NUMINDEXATTEN'     ))
    profile.outputs.append(ModelOutput(model.vars.AGC_GAININDEX_NUMINDEXSLICES, '',  ModelOutputType.SVD_REG_FIELD, readable_name='AGC.GAININDEX.NUMINDEXSLICES'    ))
    profile.outputs.append(ModelOutput(model.vars.AGC_GAININDEX_NUMINDEXDEGEN, '',   ModelOutputType.SVD_REG_FIELD, readable_name='AGC.GAININDEX.NUMINDEXDEGEN'     ))
    profile.outputs.append(ModelOutput(model.vars.AGC_GAININDEX_NUMINDEXPGA, '',     ModelOutputType.SVD_REG_FIELD, readable_name='AGC.GAININDEX.NUMINDEXPGA'       ))

    profile.outputs.append(ModelOutput(model.vars.AGC_MININDEX_INDEXMINPGA, '',      ModelOutputType.SVD_REG_FIELD, readable_name='AGC.MININDEX.INDEXMINPGA'        ))
    profile.outputs.append(ModelOutput(model.vars.AGC_MININDEX_INDEXMINDEGEN, '',    ModelOutputType.SVD_REG_FIELD, readable_name='AGC.MININDEX.INDEXMINDEGEN'      ))
    profile.outputs.append(ModelOutput(model.vars.AGC_MININDEX_INDEXMINSLICES, '',   ModelOutputType.SVD_REG_FIELD, readable_name='AGC.MININDEX.INDEXMINSLICES'     ))
    profile.outputs.append(ModelOutput(model.vars.AGC_MININDEX_INDEXMINATTEN, '',    ModelOutputType.SVD_REG_FIELD, readable_name='AGC.MININDEX.INDEXMINATTEN'      ))

    profile.outputs.append(ModelOutput(model.vars.AGC_MANGAIN_MANGAININDEX, '',      ModelOutputType.SVD_REG_FIELD, readable_name='AGC.MANGAIN.MANGAININDEX'        ))
    profile.outputs.append(ModelOutput(model.vars.AGC_MANGAIN_MANGAININDEXEN, '',    ModelOutputType.SVD_REG_FIELD, readable_name='AGC.MANGAIN.MANGAININDEXEN'      ))

    profile.outputs.append(ModelOutput(model.vars.AGC_MANGAIN_MANGAINLNAATTEN, '',     ModelOutputType.SVD_REG_FIELD, readable_name='AGC.MANGAIN.MANGAINLNAATTEN'    ))
    profile.outputs.append(ModelOutput(model.vars.AGC_MANGAIN_MANGAINLNASLICES, '',    ModelOutputType.SVD_REG_FIELD, readable_name='AGC.MANGAIN.MANGAINLNASLICES'   ))
    profile.outputs.append(ModelOutput(model.vars.AGC_MANGAIN_MANGAINLNASLICESREG, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.MANGAIN.MANGAINLNASLICESREG'))

    profile.outputs.append(ModelOutput(model.vars.RAC_LNAMIXCTRL1_TRIMAUXPLLCLK, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.LNAMIXCTRL1.TRIMAUXPLLCLK'  ))
    profile.outputs.append(ModelOutput(model.vars.RAC_LNAMIXCTRL1_TRIMTRSWGATEV, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.LNAMIXCTRL1.TRIMTRSWGATEV'  ))
    profile.outputs.append(ModelOutput(model.vars.RAC_LNAMIXCTRL1_TRIMVCASLDO  , '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.LNAMIXCTRL1.TRIMVCASLDO'    ))
    profile.outputs.append(ModelOutput(model.vars.RAC_LNAMIXCTRL1_TRIMVREFLDO  , '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.LNAMIXCTRL1.TRIMVREFLDO'    ))
    profile.outputs.append(ModelOutput(model.vars.RAC_LNAMIXCTRL1_TRIMVREGMIN  , '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.LNAMIXCTRL1.TRIMVREGMIN'    ))
    profile.outputs.append(ModelOutput(model.vars.RAC_LNAMIXCTRL1_TRIMAUXBIAS  , '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.LNAMIXCTRL1.TRIMAUXBIAS'    ))
    profile.outputs.append(ModelOutput(model.vars.RAC_LNAMIXCTRL1_ENBIASCAL    , '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.LNAMIXCTRL1.ENBIASCAL'      ))

    profile.outputs.append(ModelOutput(model.vars.RAC_VCOCTRL_VCOAMPLITUDE     , '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.VCOCTRL.VCOAMPLITUDE'       ))
    profile.outputs.append(ModelOutput(model.vars.RAC_VCOCTRL_VCODETAMPLITUDE  , '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.VCOCTRL.VCODETAMPLITUDE'    ))
    profile.outputs.append(ModelOutput(model.vars.RAC_VCOCTRL_VCODETEN         , '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.VCOCTRL.VCODETEN'           ))
    profile.outputs.append(ModelOutput(model.vars.RAC_VCOCTRL_VCODETMODE       , '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.VCOCTRL.VCODETMODE'         ))


    profile.outputs.append(ModelOutput(model.vars.RAC_VCOCTRL_VCOAREGCURR      , '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.VCOCTRL.VCOAREGCURR'        ))
    profile.outputs.append(ModelOutput(model.vars.RAC_VCOCTRL_VCOCREGCURR      , '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.VCOCTRL.VCOCREGCURR'        ))
    profile.outputs.append(ModelOutput(model.vars.RAC_VCOCTRL_VCODIVCURR       , '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.VCOCTRL.VCODIVCURR'         ))

    profile.outputs.append(ModelOutput(model.vars.SYNTH_CTRL_DITHERDSMOUTPUT   , '', ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.CTRL.DITHERDSMOUTPUT'     ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_CTRL_DITHERDAC         , '', ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.CTRL.DITHERDAC'           ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_CTRL_DITHERDSMINPUT    , '', ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.CTRL.DITHERDSMINPUT'      ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_CTRL_DSMMODE           , '', ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.CTRL.DSMMODE'             ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_CTRL_LSBFORCE          , '', ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.CTRL.LSBFORCE'            ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_CTRL_LOCKTHRESHOLD     , '', ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.CTRL.LOCKTHRESHOLD'       ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_CTRL_AUXLOCKTHRESHOLD  , '', ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.CTRL.AUXLOCKTHRESHOLD'    ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_CTRL_PRSMUX0           , '', ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.CTRL.PRSMUX0'             ))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_CTRL_PRSMUX1           , '', ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.CTRL.PRSMUX1'             ))
    profile.outputs.append(ModelOutput(model.vars.SEQ_MISC_SQBMODETX           , '', ModelOutputType.SEQ_REG_FIELD, readable_name='SEQ.MISC.SQBMODETX'             ))
    profile.outputs.append(ModelOutput(model.vars.SEQ_MISC_DYNAMIC_SLICER_SW_EN, '', ModelOutputType.SEQ_REG_FIELD, readable_name='SEQ.MISC.DYNAMIC_SLICER_SW_EN'  ))

