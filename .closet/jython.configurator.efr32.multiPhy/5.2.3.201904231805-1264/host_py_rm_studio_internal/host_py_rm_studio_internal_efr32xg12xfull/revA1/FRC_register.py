
# -*- coding: utf-8 -*-

from .static import Base_RM_Register
from .FRC_field import *


class RM_Register_FRC_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_STATUS, self).__init__(rmio, label,
            0x40080000, 0x000,
            'STATUS', 'FRC.STATUS', 'read-only',
            u"",
            0x00000000, 0x000003FF)

        self.ACTIVETXFCD = RM_Field_FRC_STATUS_ACTIVETXFCD(self)
        self.zz_fdict['ACTIVETXFCD'] = self.ACTIVETXFCD
        self.ACTIVERXFCD = RM_Field_FRC_STATUS_ACTIVERXFCD(self)
        self.zz_fdict['ACTIVERXFCD'] = self.ACTIVERXFCD
        self.RXABORTINPROGRESS = RM_Field_FRC_STATUS_RXABORTINPROGRESS(self)
        self.zz_fdict['RXABORTINPROGRESS'] = self.RXABORTINPROGRESS
        self.SNIFFDFRAME = RM_Field_FRC_STATUS_SNIFFDFRAME(self)
        self.zz_fdict['SNIFFDFRAME'] = self.SNIFFDFRAME
        self.SNIFFDCOUNT = RM_Field_FRC_STATUS_SNIFFDCOUNT(self)
        self.zz_fdict['SNIFFDCOUNT'] = self.SNIFFDCOUNT
        self.RXRAWBLOCKED = RM_Field_FRC_STATUS_RXRAWBLOCKED(self)
        self.zz_fdict['RXRAWBLOCKED'] = self.RXRAWBLOCKED
        self.FRAMEOK = RM_Field_FRC_STATUS_FRAMEOK(self)
        self.zz_fdict['FRAMEOK'] = self.FRAMEOK
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_DFLCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_DFLCTRL, self).__init__(rmio, label,
            0x40080000, 0x004,
            'DFLCTRL', 'FRC.DFLCTRL', 'read-write',
            u"",
            0x00000000, 0x001FFF7F)

        self.DFLMODE = RM_Field_FRC_DFLCTRL_DFLMODE(self)
        self.zz_fdict['DFLMODE'] = self.DFLMODE
        self.DFLBITORDER = RM_Field_FRC_DFLCTRL_DFLBITORDER(self)
        self.zz_fdict['DFLBITORDER'] = self.DFLBITORDER
        self.DFLSHIFT = RM_Field_FRC_DFLCTRL_DFLSHIFT(self)
        self.zz_fdict['DFLSHIFT'] = self.DFLSHIFT
        self.DFLOFFSET = RM_Field_FRC_DFLCTRL_DFLOFFSET(self)
        self.zz_fdict['DFLOFFSET'] = self.DFLOFFSET
        self.DFLBITS = RM_Field_FRC_DFLCTRL_DFLBITS(self)
        self.zz_fdict['DFLBITS'] = self.DFLBITS
        self.MINLENGTH = RM_Field_FRC_DFLCTRL_MINLENGTH(self)
        self.zz_fdict['MINLENGTH'] = self.MINLENGTH
        self.DFLINCLUDECRC = RM_Field_FRC_DFLCTRL_DFLINCLUDECRC(self)
        self.zz_fdict['DFLINCLUDECRC'] = self.DFLINCLUDECRC
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_MAXLENGTH(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_MAXLENGTH, self).__init__(rmio, label,
            0x40080000, 0x008,
            'MAXLENGTH', 'FRC.MAXLENGTH', 'read-write',
            u"",
            0x00000FFF, 0x00000FFF)

        self.MAXLENGTH = RM_Field_FRC_MAXLENGTH_MAXLENGTH(self)
        self.zz_fdict['MAXLENGTH'] = self.MAXLENGTH
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_ADDRFILTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_ADDRFILTCTRL, self).__init__(rmio, label,
            0x40080000, 0x00C,
            'ADDRFILTCTRL', 'FRC.ADDRFILTCTRL', 'read-write',
            u"",
            0x00000000, 0x0000FF07)

        self.EN = RM_Field_FRC_ADDRFILTCTRL_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.BRDCST00EN = RM_Field_FRC_ADDRFILTCTRL_BRDCST00EN(self)
        self.zz_fdict['BRDCST00EN'] = self.BRDCST00EN
        self.BRDCSTFFEN = RM_Field_FRC_ADDRFILTCTRL_BRDCSTFFEN(self)
        self.zz_fdict['BRDCSTFFEN'] = self.BRDCSTFFEN
        self.ADDRESS = RM_Field_FRC_ADDRFILTCTRL_ADDRESS(self)
        self.zz_fdict['ADDRESS'] = self.ADDRESS
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_DATABUFFER(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_DATABUFFER, self).__init__(rmio, label,
            0x40080000, 0x010,
            'DATABUFFER', 'FRC.DATABUFFER', 'read-write',
            u"",
            0x00000000, 0x000000FF)

        self.DATABUFFER = RM_Field_FRC_DATABUFFER_DATABUFFER(self)
        self.zz_fdict['DATABUFFER'] = self.DATABUFFER
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_WCNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_WCNT, self).__init__(rmio, label,
            0x40080000, 0x014,
            'WCNT', 'FRC.WCNT', 'read-only',
            u"",
            0x00000000, 0x00000FFF)

        self.WCNT = RM_Field_FRC_WCNT_WCNT(self)
        self.zz_fdict['WCNT'] = self.WCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_WCNTCMP0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_WCNTCMP0, self).__init__(rmio, label,
            0x40080000, 0x018,
            'WCNTCMP0', 'FRC.WCNTCMP0', 'read-write',
            u"",
            0x00000000, 0x00000FFF)

        self.FRAMELENGTH = RM_Field_FRC_WCNTCMP0_FRAMELENGTH(self)
        self.zz_fdict['FRAMELENGTH'] = self.FRAMELENGTH
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_WCNTCMP1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_WCNTCMP1, self).__init__(rmio, label,
            0x40080000, 0x01C,
            'WCNTCMP1', 'FRC.WCNTCMP1', 'read-write',
            u"",
            0x00000000, 0x00000FFF)

        self.LENGTHFIELDLOC = RM_Field_FRC_WCNTCMP1_LENGTHFIELDLOC(self)
        self.zz_fdict['LENGTHFIELDLOC'] = self.LENGTHFIELDLOC
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_WCNTCMP2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_WCNTCMP2, self).__init__(rmio, label,
            0x40080000, 0x020,
            'WCNTCMP2', 'FRC.WCNTCMP2', 'read-write',
            u"",
            0x00000000, 0x00000FFF)

        self.ADDRFIELDLOC = RM_Field_FRC_WCNTCMP2_ADDRFIELDLOC(self)
        self.zz_fdict['ADDRFIELDLOC'] = self.ADDRFIELDLOC
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_CMD, self).__init__(rmio, label,
            0x40080000, 0x024,
            'CMD', 'FRC.CMD', 'write-only',
            u"",
            0x00000000, 0x00001FFF)

        self.RXABORT = RM_Field_FRC_CMD_RXABORT(self)
        self.zz_fdict['RXABORT'] = self.RXABORT
        self.FRAMEDETRESUME = RM_Field_FRC_CMD_FRAMEDETRESUME(self)
        self.zz_fdict['FRAMEDETRESUME'] = self.FRAMEDETRESUME
        self.INTERLEAVEWRITERESUME = RM_Field_FRC_CMD_INTERLEAVEWRITERESUME(self)
        self.zz_fdict['INTERLEAVEWRITERESUME'] = self.INTERLEAVEWRITERESUME
        self.INTERLEAVEREADRESUME = RM_Field_FRC_CMD_INTERLEAVEREADRESUME(self)
        self.zz_fdict['INTERLEAVEREADRESUME'] = self.INTERLEAVEREADRESUME
        self.CONVRESUME = RM_Field_FRC_CMD_CONVRESUME(self)
        self.zz_fdict['CONVRESUME'] = self.CONVRESUME
        self.CONVTERMINATE = RM_Field_FRC_CMD_CONVTERMINATE(self)
        self.zz_fdict['CONVTERMINATE'] = self.CONVTERMINATE
        self.TXSUBFRAMERESUME = RM_Field_FRC_CMD_TXSUBFRAMERESUME(self)
        self.zz_fdict['TXSUBFRAMERESUME'] = self.TXSUBFRAMERESUME
        self.INTERLEAVEINIT = RM_Field_FRC_CMD_INTERLEAVEINIT(self)
        self.zz_fdict['INTERLEAVEINIT'] = self.INTERLEAVEINIT
        self.INTERLEAVECNTCLEAR = RM_Field_FRC_CMD_INTERLEAVECNTCLEAR(self)
        self.zz_fdict['INTERLEAVECNTCLEAR'] = self.INTERLEAVECNTCLEAR
        self.CONVINIT = RM_Field_FRC_CMD_CONVINIT(self)
        self.zz_fdict['CONVINIT'] = self.CONVINIT
        self.BLOCKINIT = RM_Field_FRC_CMD_BLOCKINIT(self)
        self.zz_fdict['BLOCKINIT'] = self.BLOCKINIT
        self.STATEINIT = RM_Field_FRC_CMD_STATEINIT(self)
        self.zz_fdict['STATEINIT'] = self.STATEINIT
        self.RXRAWUNBLOCK = RM_Field_FRC_CMD_RXRAWUNBLOCK(self)
        self.zz_fdict['RXRAWUNBLOCK'] = self.RXRAWUNBLOCK
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_WHITECTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_WHITECTRL, self).__init__(rmio, label,
            0x40080000, 0x028,
            'WHITECTRL', 'FRC.WHITECTRL', 'read-write',
            u"",
            0x00000000, 0x00001F7F)

        self.FEEDBACKSEL = RM_Field_FRC_WHITECTRL_FEEDBACKSEL(self)
        self.zz_fdict['FEEDBACKSEL'] = self.FEEDBACKSEL
        self.XORFEEDBACK = RM_Field_FRC_WHITECTRL_XORFEEDBACK(self)
        self.zz_fdict['XORFEEDBACK'] = self.XORFEEDBACK
        self.SHROUTPUTSEL = RM_Field_FRC_WHITECTRL_SHROUTPUTSEL(self)
        self.zz_fdict['SHROUTPUTSEL'] = self.SHROUTPUTSEL
        self.BLOCKERRORCORRECT = RM_Field_FRC_WHITECTRL_BLOCKERRORCORRECT(self)
        self.zz_fdict['BLOCKERRORCORRECT'] = self.BLOCKERRORCORRECT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_WHITEPOLY(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_WHITEPOLY, self).__init__(rmio, label,
            0x40080000, 0x02C,
            'WHITEPOLY', 'FRC.WHITEPOLY', 'read-write',
            u"",
            0x00000000, 0x0000FFFF)

        self.POLY = RM_Field_FRC_WHITEPOLY_POLY(self)
        self.zz_fdict['POLY'] = self.POLY
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_WHITEINIT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_WHITEINIT, self).__init__(rmio, label,
            0x40080000, 0x030,
            'WHITEINIT', 'FRC.WHITEINIT', 'read-write',
            u"",
            0x00000000, 0x0000FFFF)

        self.WHITEINIT = RM_Field_FRC_WHITEINIT_WHITEINIT(self)
        self.zz_fdict['WHITEINIT'] = self.WHITEINIT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_FECCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_FECCTRL, self).__init__(rmio, label,
            0x40080000, 0x034,
            'FECCTRL', 'FRC.FECCTRL', 'read-write',
            u"",
            0x00000000, 0x003FFFF7)

        self.BLOCKWHITEMODE = RM_Field_FRC_FECCTRL_BLOCKWHITEMODE(self)
        self.zz_fdict['BLOCKWHITEMODE'] = self.BLOCKWHITEMODE
        self.CONVMODE = RM_Field_FRC_FECCTRL_CONVMODE(self)
        self.zz_fdict['CONVMODE'] = self.CONVMODE
        self.CONVDECODEMODE = RM_Field_FRC_FECCTRL_CONVDECODEMODE(self)
        self.zz_fdict['CONVDECODEMODE'] = self.CONVDECODEMODE
        self.CONVTRACEBACKDISABLE = RM_Field_FRC_FECCTRL_CONVTRACEBACKDISABLE(self)
        self.zz_fdict['CONVTRACEBACKDISABLE'] = self.CONVTRACEBACKDISABLE
        self.CONVINV = RM_Field_FRC_FECCTRL_CONVINV(self)
        self.zz_fdict['CONVINV'] = self.CONVINV
        self.INTERLEAVEMODE = RM_Field_FRC_FECCTRL_INTERLEAVEMODE(self)
        self.zz_fdict['INTERLEAVEMODE'] = self.INTERLEAVEMODE
        self.INTERLEAVEFIRSTINDEX = RM_Field_FRC_FECCTRL_INTERLEAVEFIRSTINDEX(self)
        self.zz_fdict['INTERLEAVEFIRSTINDEX'] = self.INTERLEAVEFIRSTINDEX
        self.INTERLEAVEWIDTH = RM_Field_FRC_FECCTRL_INTERLEAVEWIDTH(self)
        self.zz_fdict['INTERLEAVEWIDTH'] = self.INTERLEAVEWIDTH
        self.CONVBUSLOCK = RM_Field_FRC_FECCTRL_CONVBUSLOCK(self)
        self.zz_fdict['CONVBUSLOCK'] = self.CONVBUSLOCK
        self.CONVSUBFRAMETERMINATE = RM_Field_FRC_FECCTRL_CONVSUBFRAMETERMINATE(self)
        self.zz_fdict['CONVSUBFRAMETERMINATE'] = self.CONVSUBFRAMETERMINATE
        self.SINGLEBLOCK = RM_Field_FRC_FECCTRL_SINGLEBLOCK(self)
        self.zz_fdict['SINGLEBLOCK'] = self.SINGLEBLOCK
        self.FORCE2FSK = RM_Field_FRC_FECCTRL_FORCE2FSK(self)
        self.zz_fdict['FORCE2FSK'] = self.FORCE2FSK
        self.CONVHARDERROR = RM_Field_FRC_FECCTRL_CONVHARDERROR(self)
        self.zz_fdict['CONVHARDERROR'] = self.CONVHARDERROR
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_BLOCKRAMADDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_BLOCKRAMADDR, self).__init__(rmio, label,
            0x40080000, 0x038,
            'BLOCKRAMADDR', 'FRC.BLOCKRAMADDR', 'read-write',
            u"",
            0x00000000, 0x0007FFFC)

        self.BLOCKRAMADDR = RM_Field_FRC_BLOCKRAMADDR_BLOCKRAMADDR(self)
        self.zz_fdict['BLOCKRAMADDR'] = self.BLOCKRAMADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_CONVRAMADDR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_CONVRAMADDR, self).__init__(rmio, label,
            0x40080000, 0x03C,
            'CONVRAMADDR', 'FRC.CONVRAMADDR', 'read-write',
            u"",
            0x00000000, 0x0007FFFC)

        self.CONVRAMADDR = RM_Field_FRC_CONVRAMADDR_CONVRAMADDR(self)
        self.zz_fdict['CONVRAMADDR'] = self.CONVRAMADDR
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_CTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_CTRL, self).__init__(rmio, label,
            0x40080000, 0x040,
            'CTRL', 'FRC.CTRL', 'read-write',
            u"",
            0x00000700, 0x00033FF7)

        self.RANDOMTX = RM_Field_FRC_CTRL_RANDOMTX(self)
        self.zz_fdict['RANDOMTX'] = self.RANDOMTX
        self.UARTMODE = RM_Field_FRC_CTRL_UARTMODE(self)
        self.zz_fdict['UARTMODE'] = self.UARTMODE
        self.BITORDER = RM_Field_FRC_CTRL_BITORDER(self)
        self.zz_fdict['BITORDER'] = self.BITORDER
        self.TXFCDMODE = RM_Field_FRC_CTRL_TXFCDMODE(self)
        self.zz_fdict['TXFCDMODE'] = self.TXFCDMODE
        self.RXFCDMODE = RM_Field_FRC_CTRL_RXFCDMODE(self)
        self.zz_fdict['RXFCDMODE'] = self.RXFCDMODE
        self.BITSPERWORD = RM_Field_FRC_CTRL_BITSPERWORD(self)
        self.zz_fdict['BITSPERWORD'] = self.BITSPERWORD
        self.RATESELECT = RM_Field_FRC_CTRL_RATESELECT(self)
        self.zz_fdict['RATESELECT'] = self.RATESELECT
        self.TXPREFETCH = RM_Field_FRC_CTRL_TXPREFETCH(self)
        self.zz_fdict['TXPREFETCH'] = self.TXPREFETCH
        self.SEQHANDSHAKE = RM_Field_FRC_CTRL_SEQHANDSHAKE(self)
        self.zz_fdict['SEQHANDSHAKE'] = self.SEQHANDSHAKE
        self.PRBSTEST = RM_Field_FRC_CTRL_PRBSTEST(self)
        self.zz_fdict['PRBSTEST'] = self.PRBSTEST
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_RXCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_RXCTRL, self).__init__(rmio, label,
            0x40080000, 0x044,
            'RXCTRL', 'FRC.RXCTRL', 'read-write',
            u"",
            0x00000000, 0x0000007F)

        self.STORECRC = RM_Field_FRC_RXCTRL_STORECRC(self)
        self.zz_fdict['STORECRC'] = self.STORECRC
        self.ACCEPTCRCERRORS = RM_Field_FRC_RXCTRL_ACCEPTCRCERRORS(self)
        self.zz_fdict['ACCEPTCRCERRORS'] = self.ACCEPTCRCERRORS
        self.ACCEPTBLOCKERRORS = RM_Field_FRC_RXCTRL_ACCEPTBLOCKERRORS(self)
        self.zz_fdict['ACCEPTBLOCKERRORS'] = self.ACCEPTBLOCKERRORS
        self.TRACKABFRAME = RM_Field_FRC_RXCTRL_TRACKABFRAME(self)
        self.zz_fdict['TRACKABFRAME'] = self.TRACKABFRAME
        self.BUFCLEAR = RM_Field_FRC_RXCTRL_BUFCLEAR(self)
        self.zz_fdict['BUFCLEAR'] = self.BUFCLEAR
        self.BUFRESTOREFRAMEERROR = RM_Field_FRC_RXCTRL_BUFRESTOREFRAMEERROR(self)
        self.zz_fdict['BUFRESTOREFRAMEERROR'] = self.BUFRESTOREFRAMEERROR
        self.BUFRESTORERXABORTED = RM_Field_FRC_RXCTRL_BUFRESTORERXABORTED(self)
        self.zz_fdict['BUFRESTORERXABORTED'] = self.BUFRESTORERXABORTED
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_TRAILTXDATACTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_TRAILTXDATACTRL, self).__init__(rmio, label,
            0x40080000, 0x048,
            'TRAILTXDATACTRL', 'FRC.TRAILTXDATACTRL', 'read-write',
            u"",
            0x00000000, 0x00000FFF)

        self.TRAILTXDATA = RM_Field_FRC_TRAILTXDATACTRL_TRAILTXDATA(self)
        self.zz_fdict['TRAILTXDATA'] = self.TRAILTXDATA
        self.TRAILTXDATACNT = RM_Field_FRC_TRAILTXDATACTRL_TRAILTXDATACNT(self)
        self.zz_fdict['TRAILTXDATACNT'] = self.TRAILTXDATACNT
        self.TRAILTXDATAFORCE = RM_Field_FRC_TRAILTXDATACTRL_TRAILTXDATAFORCE(self)
        self.zz_fdict['TRAILTXDATAFORCE'] = self.TRAILTXDATAFORCE
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_TRAILRXDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_TRAILRXDATA, self).__init__(rmio, label,
            0x40080000, 0x04C,
            'TRAILRXDATA', 'FRC.TRAILRXDATA', 'read-write',
            u"",
            0x00000000, 0x0000003F)

        self.RSSI = RM_Field_FRC_TRAILRXDATA_RSSI(self)
        self.zz_fdict['RSSI'] = self.RSSI
        self.CRCOK = RM_Field_FRC_TRAILRXDATA_CRCOK(self)
        self.zz_fdict['CRCOK'] = self.CRCOK
        self.PROTIMERCC0BASE = RM_Field_FRC_TRAILRXDATA_PROTIMERCC0BASE(self)
        self.zz_fdict['PROTIMERCC0BASE'] = self.PROTIMERCC0BASE
        self.PROTIMERCC0WRAPL = RM_Field_FRC_TRAILRXDATA_PROTIMERCC0WRAPL(self)
        self.zz_fdict['PROTIMERCC0WRAPL'] = self.PROTIMERCC0WRAPL
        self.PROTIMERCC0WRAPH = RM_Field_FRC_TRAILRXDATA_PROTIMERCC0WRAPH(self)
        self.zz_fdict['PROTIMERCC0WRAPH'] = self.PROTIMERCC0WRAPH
        self.RTCSTAMP = RM_Field_FRC_TRAILRXDATA_RTCSTAMP(self)
        self.zz_fdict['RTCSTAMP'] = self.RTCSTAMP
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_SCNT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_SCNT, self).__init__(rmio, label,
            0x40080000, 0x050,
            'SCNT', 'FRC.SCNT', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.SCNT = RM_Field_FRC_SCNT_SCNT(self)
        self.zz_fdict['SCNT'] = self.SCNT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_CONVGENERATOR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_CONVGENERATOR, self).__init__(rmio, label,
            0x40080000, 0x054,
            'CONVGENERATOR', 'FRC.CONVGENERATOR', 'read-write',
            u"",
            0x00000000, 0x00037F7F)

        self.GENERATOR0 = RM_Field_FRC_CONVGENERATOR_GENERATOR0(self)
        self.zz_fdict['GENERATOR0'] = self.GENERATOR0
        self.GENERATOR1 = RM_Field_FRC_CONVGENERATOR_GENERATOR1(self)
        self.zz_fdict['GENERATOR1'] = self.GENERATOR1
        self.RECURSIVE = RM_Field_FRC_CONVGENERATOR_RECURSIVE(self)
        self.zz_fdict['RECURSIVE'] = self.RECURSIVE
        self.NONSYSTEMATIC = RM_Field_FRC_CONVGENERATOR_NONSYSTEMATIC(self)
        self.zz_fdict['NONSYSTEMATIC'] = self.NONSYSTEMATIC
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_PUNCTCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_PUNCTCTRL, self).__init__(rmio, label,
            0x40080000, 0x058,
            'PUNCTCTRL', 'FRC.PUNCTCTRL', 'read-write',
            u"",
            0x00000101, 0x00007F7F)

        self.PUNCT0 = RM_Field_FRC_PUNCTCTRL_PUNCT0(self)
        self.zz_fdict['PUNCT0'] = self.PUNCT0
        self.PUNCT1 = RM_Field_FRC_PUNCTCTRL_PUNCT1(self)
        self.zz_fdict['PUNCT1'] = self.PUNCT1
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_PAUSECTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_PAUSECTRL, self).__init__(rmio, label,
            0x40080000, 0x05C,
            'PAUSECTRL', 'FRC.PAUSECTRL', 'read-write',
            u"",
            0x00000000, 0x001FFFFF)

        self.FRAMEDETPAUSEEN = RM_Field_FRC_PAUSECTRL_FRAMEDETPAUSEEN(self)
        self.zz_fdict['FRAMEDETPAUSEEN'] = self.FRAMEDETPAUSEEN
        self.TXINTERLEAVEWRITEPAUSEEN = RM_Field_FRC_PAUSECTRL_TXINTERLEAVEWRITEPAUSEEN(self)
        self.zz_fdict['TXINTERLEAVEWRITEPAUSEEN'] = self.TXINTERLEAVEWRITEPAUSEEN
        self.RXINTERLEAVEWRITEPAUSEEN = RM_Field_FRC_PAUSECTRL_RXINTERLEAVEWRITEPAUSEEN(self)
        self.zz_fdict['RXINTERLEAVEWRITEPAUSEEN'] = self.RXINTERLEAVEWRITEPAUSEEN
        self.INTERLEAVEREADPAUSEEN = RM_Field_FRC_PAUSECTRL_INTERLEAVEREADPAUSEEN(self)
        self.zz_fdict['INTERLEAVEREADPAUSEEN'] = self.INTERLEAVEREADPAUSEEN
        self.TXSUBFRAMEPAUSEEN = RM_Field_FRC_PAUSECTRL_TXSUBFRAMEPAUSEEN(self)
        self.zz_fdict['TXSUBFRAMEPAUSEEN'] = self.TXSUBFRAMEPAUSEEN
        self.CONVPAUSECNT = RM_Field_FRC_PAUSECTRL_CONVPAUSECNT(self)
        self.zz_fdict['CONVPAUSECNT'] = self.CONVPAUSECNT
        self.INTERLEAVEWRITEPAUSECNT = RM_Field_FRC_PAUSECTRL_INTERLEAVEWRITEPAUSECNT(self)
        self.zz_fdict['INTERLEAVEWRITEPAUSECNT'] = self.INTERLEAVEWRITEPAUSECNT
        self.INTERLEAVEREADPAUSECNT = RM_Field_FRC_PAUSECTRL_INTERLEAVEREADPAUSECNT(self)
        self.zz_fdict['INTERLEAVEREADPAUSECNT'] = self.INTERLEAVEREADPAUSECNT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_IF, self).__init__(rmio, label,
            0x40080000, 0x060,
            'IF', 'FRC.IF', 'read-only',
            u"",
            0x00000000, 0x7F07FFFF)

        self.TXDONE = RM_Field_FRC_IF_TXDONE(self)
        self.zz_fdict['TXDONE'] = self.TXDONE
        self.TXAFTERFRAMEDONE = RM_Field_FRC_IF_TXAFTERFRAMEDONE(self)
        self.zz_fdict['TXAFTERFRAMEDONE'] = self.TXAFTERFRAMEDONE
        self.TXABORTED = RM_Field_FRC_IF_TXABORTED(self)
        self.zz_fdict['TXABORTED'] = self.TXABORTED
        self.TXUF = RM_Field_FRC_IF_TXUF(self)
        self.zz_fdict['TXUF'] = self.TXUF
        self.RXDONE = RM_Field_FRC_IF_RXDONE(self)
        self.zz_fdict['RXDONE'] = self.RXDONE
        self.RXABORTED = RM_Field_FRC_IF_RXABORTED(self)
        self.zz_fdict['RXABORTED'] = self.RXABORTED
        self.FRAMEERROR = RM_Field_FRC_IF_FRAMEERROR(self)
        self.zz_fdict['FRAMEERROR'] = self.FRAMEERROR
        self.BLOCKERROR = RM_Field_FRC_IF_BLOCKERROR(self)
        self.zz_fdict['BLOCKERROR'] = self.BLOCKERROR
        self.RXOF = RM_Field_FRC_IF_RXOF(self)
        self.zz_fdict['RXOF'] = self.RXOF
        self.WCNTCMP0 = RM_Field_FRC_IF_WCNTCMP0(self)
        self.zz_fdict['WCNTCMP0'] = self.WCNTCMP0
        self.WCNTCMP1 = RM_Field_FRC_IF_WCNTCMP1(self)
        self.zz_fdict['WCNTCMP1'] = self.WCNTCMP1
        self.WCNTCMP2 = RM_Field_FRC_IF_WCNTCMP2(self)
        self.zz_fdict['WCNTCMP2'] = self.WCNTCMP2
        self.ADDRERROR = RM_Field_FRC_IF_ADDRERROR(self)
        self.zz_fdict['ADDRERROR'] = self.ADDRERROR
        self.BUSERROR = RM_Field_FRC_IF_BUSERROR(self)
        self.zz_fdict['BUSERROR'] = self.BUSERROR
        self.RXRAWEVENT = RM_Field_FRC_IF_RXRAWEVENT(self)
        self.zz_fdict['RXRAWEVENT'] = self.RXRAWEVENT
        self.TXRAWEVENT = RM_Field_FRC_IF_TXRAWEVENT(self)
        self.zz_fdict['TXRAWEVENT'] = self.TXRAWEVENT
        self.SNIFFOF = RM_Field_FRC_IF_SNIFFOF(self)
        self.zz_fdict['SNIFFOF'] = self.SNIFFOF
        self.LVDSWILLERROR = RM_Field_FRC_IF_LVDSWILLERROR(self)
        self.zz_fdict['LVDSWILLERROR'] = self.LVDSWILLERROR
        self.LVDSERROR = RM_Field_FRC_IF_LVDSERROR(self)
        self.zz_fdict['LVDSERROR'] = self.LVDSERROR
        self.FRAMEDETPAUSED = RM_Field_FRC_IF_FRAMEDETPAUSED(self)
        self.zz_fdict['FRAMEDETPAUSED'] = self.FRAMEDETPAUSED
        self.INTERLEAVEWRITEPAUSED = RM_Field_FRC_IF_INTERLEAVEWRITEPAUSED(self)
        self.zz_fdict['INTERLEAVEWRITEPAUSED'] = self.INTERLEAVEWRITEPAUSED
        self.INTERLEAVEREADPAUSED = RM_Field_FRC_IF_INTERLEAVEREADPAUSED(self)
        self.zz_fdict['INTERLEAVEREADPAUSED'] = self.INTERLEAVEREADPAUSED
        self.TXSUBFRAMEPAUSED = RM_Field_FRC_IF_TXSUBFRAMEPAUSED(self)
        self.zz_fdict['TXSUBFRAMEPAUSED'] = self.TXSUBFRAMEPAUSED
        self.CONVPAUSED = RM_Field_FRC_IF_CONVPAUSED(self)
        self.zz_fdict['CONVPAUSED'] = self.CONVPAUSED
        self.RXWORD = RM_Field_FRC_IF_RXWORD(self)
        self.zz_fdict['RXWORD'] = self.RXWORD
        self.TXWORD = RM_Field_FRC_IF_TXWORD(self)
        self.zz_fdict['TXWORD'] = self.TXWORD
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_IFS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_IFS, self).__init__(rmio, label,
            0x40080000, 0x064,
            'IFS', 'FRC.IFS', 'write-only',
            u"",
            0x00000000, 0x0007FFFF)

        self.TXDONE = RM_Field_FRC_IFS_TXDONE(self)
        self.zz_fdict['TXDONE'] = self.TXDONE
        self.TXAFTERFRAMEDONE = RM_Field_FRC_IFS_TXAFTERFRAMEDONE(self)
        self.zz_fdict['TXAFTERFRAMEDONE'] = self.TXAFTERFRAMEDONE
        self.TXABORTED = RM_Field_FRC_IFS_TXABORTED(self)
        self.zz_fdict['TXABORTED'] = self.TXABORTED
        self.TXUF = RM_Field_FRC_IFS_TXUF(self)
        self.zz_fdict['TXUF'] = self.TXUF
        self.RXDONE = RM_Field_FRC_IFS_RXDONE(self)
        self.zz_fdict['RXDONE'] = self.RXDONE
        self.RXABORTED = RM_Field_FRC_IFS_RXABORTED(self)
        self.zz_fdict['RXABORTED'] = self.RXABORTED
        self.FRAMEERROR = RM_Field_FRC_IFS_FRAMEERROR(self)
        self.zz_fdict['FRAMEERROR'] = self.FRAMEERROR
        self.BLOCKERROR = RM_Field_FRC_IFS_BLOCKERROR(self)
        self.zz_fdict['BLOCKERROR'] = self.BLOCKERROR
        self.RXOF = RM_Field_FRC_IFS_RXOF(self)
        self.zz_fdict['RXOF'] = self.RXOF
        self.WCNTCMP0 = RM_Field_FRC_IFS_WCNTCMP0(self)
        self.zz_fdict['WCNTCMP0'] = self.WCNTCMP0
        self.WCNTCMP1 = RM_Field_FRC_IFS_WCNTCMP1(self)
        self.zz_fdict['WCNTCMP1'] = self.WCNTCMP1
        self.WCNTCMP2 = RM_Field_FRC_IFS_WCNTCMP2(self)
        self.zz_fdict['WCNTCMP2'] = self.WCNTCMP2
        self.ADDRERROR = RM_Field_FRC_IFS_ADDRERROR(self)
        self.zz_fdict['ADDRERROR'] = self.ADDRERROR
        self.BUSERROR = RM_Field_FRC_IFS_BUSERROR(self)
        self.zz_fdict['BUSERROR'] = self.BUSERROR
        self.RXRAWEVENT = RM_Field_FRC_IFS_RXRAWEVENT(self)
        self.zz_fdict['RXRAWEVENT'] = self.RXRAWEVENT
        self.TXRAWEVENT = RM_Field_FRC_IFS_TXRAWEVENT(self)
        self.zz_fdict['TXRAWEVENT'] = self.TXRAWEVENT
        self.SNIFFOF = RM_Field_FRC_IFS_SNIFFOF(self)
        self.zz_fdict['SNIFFOF'] = self.SNIFFOF
        self.LVDSWILLERROR = RM_Field_FRC_IFS_LVDSWILLERROR(self)
        self.zz_fdict['LVDSWILLERROR'] = self.LVDSWILLERROR
        self.LVDSERROR = RM_Field_FRC_IFS_LVDSERROR(self)
        self.zz_fdict['LVDSERROR'] = self.LVDSERROR
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_IFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_IFC, self).__init__(rmio, label,
            0x40080000, 0x068,
            'IFC', 'FRC.IFC', 'write-only',
            u"",
            0x00000000, 0x0007FFFF)

        self.TXDONE = RM_Field_FRC_IFC_TXDONE(self)
        self.zz_fdict['TXDONE'] = self.TXDONE
        self.TXAFTERFRAMEDONE = RM_Field_FRC_IFC_TXAFTERFRAMEDONE(self)
        self.zz_fdict['TXAFTERFRAMEDONE'] = self.TXAFTERFRAMEDONE
        self.TXABORTED = RM_Field_FRC_IFC_TXABORTED(self)
        self.zz_fdict['TXABORTED'] = self.TXABORTED
        self.TXUF = RM_Field_FRC_IFC_TXUF(self)
        self.zz_fdict['TXUF'] = self.TXUF
        self.RXDONE = RM_Field_FRC_IFC_RXDONE(self)
        self.zz_fdict['RXDONE'] = self.RXDONE
        self.RXABORTED = RM_Field_FRC_IFC_RXABORTED(self)
        self.zz_fdict['RXABORTED'] = self.RXABORTED
        self.FRAMEERROR = RM_Field_FRC_IFC_FRAMEERROR(self)
        self.zz_fdict['FRAMEERROR'] = self.FRAMEERROR
        self.BLOCKERROR = RM_Field_FRC_IFC_BLOCKERROR(self)
        self.zz_fdict['BLOCKERROR'] = self.BLOCKERROR
        self.RXOF = RM_Field_FRC_IFC_RXOF(self)
        self.zz_fdict['RXOF'] = self.RXOF
        self.WCNTCMP0 = RM_Field_FRC_IFC_WCNTCMP0(self)
        self.zz_fdict['WCNTCMP0'] = self.WCNTCMP0
        self.WCNTCMP1 = RM_Field_FRC_IFC_WCNTCMP1(self)
        self.zz_fdict['WCNTCMP1'] = self.WCNTCMP1
        self.WCNTCMP2 = RM_Field_FRC_IFC_WCNTCMP2(self)
        self.zz_fdict['WCNTCMP2'] = self.WCNTCMP2
        self.ADDRERROR = RM_Field_FRC_IFC_ADDRERROR(self)
        self.zz_fdict['ADDRERROR'] = self.ADDRERROR
        self.BUSERROR = RM_Field_FRC_IFC_BUSERROR(self)
        self.zz_fdict['BUSERROR'] = self.BUSERROR
        self.RXRAWEVENT = RM_Field_FRC_IFC_RXRAWEVENT(self)
        self.zz_fdict['RXRAWEVENT'] = self.RXRAWEVENT
        self.TXRAWEVENT = RM_Field_FRC_IFC_TXRAWEVENT(self)
        self.zz_fdict['TXRAWEVENT'] = self.TXRAWEVENT
        self.SNIFFOF = RM_Field_FRC_IFC_SNIFFOF(self)
        self.zz_fdict['SNIFFOF'] = self.SNIFFOF
        self.LVDSWILLERROR = RM_Field_FRC_IFC_LVDSWILLERROR(self)
        self.zz_fdict['LVDSWILLERROR'] = self.LVDSWILLERROR
        self.LVDSERROR = RM_Field_FRC_IFC_LVDSERROR(self)
        self.zz_fdict['LVDSERROR'] = self.LVDSERROR
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_IEN, self).__init__(rmio, label,
            0x40080000, 0x06C,
            'IEN', 'FRC.IEN', 'read-write',
            u"",
            0x00000000, 0x7F07FFFF)

        self.TXDONE = RM_Field_FRC_IEN_TXDONE(self)
        self.zz_fdict['TXDONE'] = self.TXDONE
        self.TXAFTERFRAMEDONE = RM_Field_FRC_IEN_TXAFTERFRAMEDONE(self)
        self.zz_fdict['TXAFTERFRAMEDONE'] = self.TXAFTERFRAMEDONE
        self.TXABORTED = RM_Field_FRC_IEN_TXABORTED(self)
        self.zz_fdict['TXABORTED'] = self.TXABORTED
        self.TXUF = RM_Field_FRC_IEN_TXUF(self)
        self.zz_fdict['TXUF'] = self.TXUF
        self.RXDONE = RM_Field_FRC_IEN_RXDONE(self)
        self.zz_fdict['RXDONE'] = self.RXDONE
        self.RXABORTED = RM_Field_FRC_IEN_RXABORTED(self)
        self.zz_fdict['RXABORTED'] = self.RXABORTED
        self.FRAMEERROR = RM_Field_FRC_IEN_FRAMEERROR(self)
        self.zz_fdict['FRAMEERROR'] = self.FRAMEERROR
        self.BLOCKERROR = RM_Field_FRC_IEN_BLOCKERROR(self)
        self.zz_fdict['BLOCKERROR'] = self.BLOCKERROR
        self.RXOF = RM_Field_FRC_IEN_RXOF(self)
        self.zz_fdict['RXOF'] = self.RXOF
        self.WCNTCMP0 = RM_Field_FRC_IEN_WCNTCMP0(self)
        self.zz_fdict['WCNTCMP0'] = self.WCNTCMP0
        self.WCNTCMP1 = RM_Field_FRC_IEN_WCNTCMP1(self)
        self.zz_fdict['WCNTCMP1'] = self.WCNTCMP1
        self.WCNTCMP2 = RM_Field_FRC_IEN_WCNTCMP2(self)
        self.zz_fdict['WCNTCMP2'] = self.WCNTCMP2
        self.ADDRERROR = RM_Field_FRC_IEN_ADDRERROR(self)
        self.zz_fdict['ADDRERROR'] = self.ADDRERROR
        self.BUSERROR = RM_Field_FRC_IEN_BUSERROR(self)
        self.zz_fdict['BUSERROR'] = self.BUSERROR
        self.RXRAWEVENT = RM_Field_FRC_IEN_RXRAWEVENT(self)
        self.zz_fdict['RXRAWEVENT'] = self.RXRAWEVENT
        self.TXRAWEVENT = RM_Field_FRC_IEN_TXRAWEVENT(self)
        self.zz_fdict['TXRAWEVENT'] = self.TXRAWEVENT
        self.SNIFFOF = RM_Field_FRC_IEN_SNIFFOF(self)
        self.zz_fdict['SNIFFOF'] = self.SNIFFOF
        self.LVDSWILLERROR = RM_Field_FRC_IEN_LVDSWILLERROR(self)
        self.zz_fdict['LVDSWILLERROR'] = self.LVDSWILLERROR
        self.LVDSERROR = RM_Field_FRC_IEN_LVDSERROR(self)
        self.zz_fdict['LVDSERROR'] = self.LVDSERROR
        self.FRAMEDETPAUSED = RM_Field_FRC_IEN_FRAMEDETPAUSED(self)
        self.zz_fdict['FRAMEDETPAUSED'] = self.FRAMEDETPAUSED
        self.INTERLEAVEWRITEPAUSED = RM_Field_FRC_IEN_INTERLEAVEWRITEPAUSED(self)
        self.zz_fdict['INTERLEAVEWRITEPAUSED'] = self.INTERLEAVEWRITEPAUSED
        self.INTERLEAVEREADPAUSED = RM_Field_FRC_IEN_INTERLEAVEREADPAUSED(self)
        self.zz_fdict['INTERLEAVEREADPAUSED'] = self.INTERLEAVEREADPAUSED
        self.TXSUBFRAMEPAUSED = RM_Field_FRC_IEN_TXSUBFRAMEPAUSED(self)
        self.zz_fdict['TXSUBFRAMEPAUSED'] = self.TXSUBFRAMEPAUSED
        self.CONVPAUSED = RM_Field_FRC_IEN_CONVPAUSED(self)
        self.zz_fdict['CONVPAUSED'] = self.CONVPAUSED
        self.RXWORD = RM_Field_FRC_IEN_RXWORD(self)
        self.zz_fdict['RXWORD'] = self.RXWORD
        self.TXWORD = RM_Field_FRC_IEN_TXWORD(self)
        self.zz_fdict['TXWORD'] = self.TXWORD
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_BUFFERMODE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_BUFFERMODE, self).__init__(rmio, label,
            0x40080000, 0x070,
            'BUFFERMODE', 'FRC.BUFFERMODE', 'read-write',
            u"",
            0x00000000, 0x00000007)

        self.TXBUFFERMODE = RM_Field_FRC_BUFFERMODE_TXBUFFERMODE(self)
        self.zz_fdict['TXBUFFERMODE'] = self.TXBUFFERMODE
        self.RXBUFFERMODE = RM_Field_FRC_BUFFERMODE_RXBUFFERMODE(self)
        self.zz_fdict['RXBUFFERMODE'] = self.RXBUFFERMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_ROUTEPEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_ROUTEPEN, self).__init__(rmio, label,
            0x40080000, 0x074,
            'ROUTEPEN', 'FRC.ROUTEPEN', 'read-write',
            u"",
            0x00000000, 0x00000007)

        self.DOUTPEN = RM_Field_FRC_ROUTEPEN_DOUTPEN(self)
        self.zz_fdict['DOUTPEN'] = self.DOUTPEN
        self.DCLKPEN = RM_Field_FRC_ROUTEPEN_DCLKPEN(self)
        self.zz_fdict['DCLKPEN'] = self.DCLKPEN
        self.DFRAMEPEN = RM_Field_FRC_ROUTEPEN_DFRAMEPEN(self)
        self.zz_fdict['DFRAMEPEN'] = self.DFRAMEPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_ROUTELOC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_ROUTELOC0, self).__init__(rmio, label,
            0x40080000, 0x078,
            'ROUTELOC0', 'FRC.ROUTELOC0', 'read-write',
            u"",
            0x00000000, 0x003F3F3F)

        self.DOUTLOC = RM_Field_FRC_ROUTELOC0_DOUTLOC(self)
        self.zz_fdict['DOUTLOC'] = self.DOUTLOC
        self.DCLKLOC = RM_Field_FRC_ROUTELOC0_DCLKLOC(self)
        self.zz_fdict['DCLKLOC'] = self.DCLKLOC
        self.DFRAMELOC = RM_Field_FRC_ROUTELOC0_DFRAMELOC(self)
        self.zz_fdict['DFRAMELOC'] = self.DFRAMELOC
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_SNIFFCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_SNIFFCTRL, self).__init__(rmio, label,
            0x40080000, 0x07C,
            'SNIFFCTRL', 'FRC.SNIFFCTRL', 'read-write',
            u"",
            0x000007FC, 0x0001FFFF)

        self.SNIFFMODE = RM_Field_FRC_SNIFFCTRL_SNIFFMODE(self)
        self.zz_fdict['SNIFFMODE'] = self.SNIFFMODE
        self.SNIFFBITS = RM_Field_FRC_SNIFFCTRL_SNIFFBITS(self)
        self.zz_fdict['SNIFFBITS'] = self.SNIFFBITS
        self.SNIFFRXDATA = RM_Field_FRC_SNIFFCTRL_SNIFFRXDATA(self)
        self.zz_fdict['SNIFFRXDATA'] = self.SNIFFRXDATA
        self.SNIFFTXDATA = RM_Field_FRC_SNIFFCTRL_SNIFFTXDATA(self)
        self.zz_fdict['SNIFFTXDATA'] = self.SNIFFTXDATA
        self.SNIFFRSSI = RM_Field_FRC_SNIFFCTRL_SNIFFRSSI(self)
        self.zz_fdict['SNIFFRSSI'] = self.SNIFFRSSI
        self.SNIFFSTATE = RM_Field_FRC_SNIFFCTRL_SNIFFSTATE(self)
        self.zz_fdict['SNIFFSTATE'] = self.SNIFFSTATE
        self.SNIFFAUXDATA = RM_Field_FRC_SNIFFCTRL_SNIFFAUXDATA(self)
        self.zz_fdict['SNIFFAUXDATA'] = self.SNIFFAUXDATA
        self.SNIFFBR = RM_Field_FRC_SNIFFCTRL_SNIFFBR(self)
        self.zz_fdict['SNIFFBR'] = self.SNIFFBR
        self.SNIFFSLEEPCTRL = RM_Field_FRC_SNIFFCTRL_SNIFFSLEEPCTRL(self)
        self.zz_fdict['SNIFFSLEEPCTRL'] = self.SNIFFSLEEPCTRL
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_AUXDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_AUXDATA, self).__init__(rmio, label,
            0x40080000, 0x080,
            'AUXDATA', 'FRC.AUXDATA', 'read-write',
            u"",
            0x00000000, 0x000001FF)

        self.AUXDATA = RM_Field_FRC_AUXDATA_AUXDATA(self)
        self.zz_fdict['AUXDATA'] = self.AUXDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_RAWCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_RAWCTRL, self).__init__(rmio, label,
            0x40080000, 0x084,
            'RAWCTRL', 'FRC.RAWCTRL', 'read-write',
            u"",
            0x00000000, 0x00000FBF)

        self.TXRAWMODE = RM_Field_FRC_RAWCTRL_TXRAWMODE(self)
        self.zz_fdict['TXRAWMODE'] = self.TXRAWMODE
        self.RXRAWMODE = RM_Field_FRC_RAWCTRL_RXRAWMODE(self)
        self.zz_fdict['RXRAWMODE'] = self.RXRAWMODE
        self.RXRAWRANDOM = RM_Field_FRC_RAWCTRL_RXRAWRANDOM(self)
        self.zz_fdict['RXRAWRANDOM'] = self.RXRAWRANDOM
        self.RXRAWTRIGGER = RM_Field_FRC_RAWCTRL_RXRAWTRIGGER(self)
        self.zz_fdict['RXRAWTRIGGER'] = self.RXRAWTRIGGER
        self.RXRAWPRSSEL = RM_Field_FRC_RAWCTRL_RXRAWPRSSEL(self)
        self.zz_fdict['RXRAWPRSSEL'] = self.RXRAWPRSSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_RXRAWDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_RXRAWDATA, self).__init__(rmio, label,
            0x40080000, 0x088,
            'RXRAWDATA', 'FRC.RXRAWDATA', 'read-only',
            u"",
            0x00000000, 0xFFFFFFFF)

        self.RXRAWDATA = RM_Field_FRC_RXRAWDATA_RXRAWDATA(self)
        self.zz_fdict['RXRAWDATA'] = self.RXRAWDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_PAUSEDATA(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_PAUSEDATA, self).__init__(rmio, label,
            0x40080000, 0x08C,
            'PAUSEDATA', 'FRC.PAUSEDATA', 'read-only',
            u"",
            0x00000000, 0xFFFFFFFF)

        self.PAUSEDATA = RM_Field_FRC_PAUSEDATA_PAUSEDATA(self)
        self.zz_fdict['PAUSEDATA'] = self.PAUSEDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_LIKELYCONVSTATE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_LIKELYCONVSTATE, self).__init__(rmio, label,
            0x40080000, 0x090,
            'LIKELYCONVSTATE', 'FRC.LIKELYCONVSTATE', 'read-only',
            u"",
            0x00000000, 0x0000003F)

        self.LIKELYCONVSTATE = RM_Field_FRC_LIKELYCONVSTATE_LIKELYCONVSTATE(self)
        self.zz_fdict['LIKELYCONVSTATE'] = self.LIKELYCONVSTATE
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENTNEXT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENTNEXT, self).__init__(rmio, label,
            0x40080000, 0x094,
            'INTELEMENTNEXT', 'FRC.INTELEMENTNEXT', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENTNEXT = RM_Field_FRC_INTELEMENTNEXT_INTELEMENTNEXT(self)
        self.zz_fdict['INTELEMENTNEXT'] = self.INTELEMENTNEXT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTWRITEPOINT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTWRITEPOINT, self).__init__(rmio, label,
            0x40080000, 0x098,
            'INTWRITEPOINT', 'FRC.INTWRITEPOINT', 'read-write',
            u"",
            0x00000000, 0x0000001F)

        self.INTWRITEPOINT = RM_Field_FRC_INTWRITEPOINT_INTWRITEPOINT(self)
        self.zz_fdict['INTWRITEPOINT'] = self.INTWRITEPOINT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTREADPOINT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTREADPOINT, self).__init__(rmio, label,
            0x40080000, 0x09C,
            'INTREADPOINT', 'FRC.INTREADPOINT', 'read-write',
            u"",
            0x00000000, 0x0000001F)

        self.INTREADPOINT = RM_Field_FRC_INTREADPOINT_INTREADPOINT(self)
        self.zz_fdict['INTREADPOINT'] = self.INTREADPOINT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_FCD0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_FCD0, self).__init__(rmio, label,
            0x40080000, 0x0A0,
            'FCD0', 'FRC.FCD0', 'read-write',
            u"",
            0x000000FF, 0x0000FFFF)

        self.WORDS = RM_Field_FRC_FCD0_WORDS(self)
        self.zz_fdict['WORDS'] = self.WORDS
        self.BUFFER = RM_Field_FRC_FCD0_BUFFER(self)
        self.zz_fdict['BUFFER'] = self.BUFFER
        self.INCLUDECRC = RM_Field_FRC_FCD0_INCLUDECRC(self)
        self.zz_fdict['INCLUDECRC'] = self.INCLUDECRC
        self.CALCCRC = RM_Field_FRC_FCD0_CALCCRC(self)
        self.zz_fdict['CALCCRC'] = self.CALCCRC
        self.SKIPCRC = RM_Field_FRC_FCD0_SKIPCRC(self)
        self.zz_fdict['SKIPCRC'] = self.SKIPCRC
        self.SKIPWHITE = RM_Field_FRC_FCD0_SKIPWHITE(self)
        self.zz_fdict['SKIPWHITE'] = self.SKIPWHITE
        self.ADDTRAILTXDATA = RM_Field_FRC_FCD0_ADDTRAILTXDATA(self)
        self.zz_fdict['ADDTRAILTXDATA'] = self.ADDTRAILTXDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_FCD1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_FCD1, self).__init__(rmio, label,
            0x40080000, 0x0A4,
            'FCD1', 'FRC.FCD1', 'read-write',
            u"",
            0x000000FF, 0x0000FFFF)

        self.WORDS = RM_Field_FRC_FCD1_WORDS(self)
        self.zz_fdict['WORDS'] = self.WORDS
        self.BUFFER = RM_Field_FRC_FCD1_BUFFER(self)
        self.zz_fdict['BUFFER'] = self.BUFFER
        self.INCLUDECRC = RM_Field_FRC_FCD1_INCLUDECRC(self)
        self.zz_fdict['INCLUDECRC'] = self.INCLUDECRC
        self.CALCCRC = RM_Field_FRC_FCD1_CALCCRC(self)
        self.zz_fdict['CALCCRC'] = self.CALCCRC
        self.SKIPCRC = RM_Field_FRC_FCD1_SKIPCRC(self)
        self.zz_fdict['SKIPCRC'] = self.SKIPCRC
        self.SKIPWHITE = RM_Field_FRC_FCD1_SKIPWHITE(self)
        self.zz_fdict['SKIPWHITE'] = self.SKIPWHITE
        self.ADDTRAILTXDATA = RM_Field_FRC_FCD1_ADDTRAILTXDATA(self)
        self.zz_fdict['ADDTRAILTXDATA'] = self.ADDTRAILTXDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_FCD2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_FCD2, self).__init__(rmio, label,
            0x40080000, 0x0A8,
            'FCD2', 'FRC.FCD2', 'read-write',
            u"",
            0x000000FF, 0x0000FFFF)

        self.WORDS = RM_Field_FRC_FCD2_WORDS(self)
        self.zz_fdict['WORDS'] = self.WORDS
        self.BUFFER = RM_Field_FRC_FCD2_BUFFER(self)
        self.zz_fdict['BUFFER'] = self.BUFFER
        self.INCLUDECRC = RM_Field_FRC_FCD2_INCLUDECRC(self)
        self.zz_fdict['INCLUDECRC'] = self.INCLUDECRC
        self.CALCCRC = RM_Field_FRC_FCD2_CALCCRC(self)
        self.zz_fdict['CALCCRC'] = self.CALCCRC
        self.SKIPCRC = RM_Field_FRC_FCD2_SKIPCRC(self)
        self.zz_fdict['SKIPCRC'] = self.SKIPCRC
        self.SKIPWHITE = RM_Field_FRC_FCD2_SKIPWHITE(self)
        self.zz_fdict['SKIPWHITE'] = self.SKIPWHITE
        self.ADDTRAILTXDATA = RM_Field_FRC_FCD2_ADDTRAILTXDATA(self)
        self.zz_fdict['ADDTRAILTXDATA'] = self.ADDTRAILTXDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_FCD3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_FCD3, self).__init__(rmio, label,
            0x40080000, 0x0AC,
            'FCD3', 'FRC.FCD3', 'read-write',
            u"",
            0x000000FF, 0x0000FFFF)

        self.WORDS = RM_Field_FRC_FCD3_WORDS(self)
        self.zz_fdict['WORDS'] = self.WORDS
        self.BUFFER = RM_Field_FRC_FCD3_BUFFER(self)
        self.zz_fdict['BUFFER'] = self.BUFFER
        self.INCLUDECRC = RM_Field_FRC_FCD3_INCLUDECRC(self)
        self.zz_fdict['INCLUDECRC'] = self.INCLUDECRC
        self.CALCCRC = RM_Field_FRC_FCD3_CALCCRC(self)
        self.zz_fdict['CALCCRC'] = self.CALCCRC
        self.SKIPCRC = RM_Field_FRC_FCD3_SKIPCRC(self)
        self.zz_fdict['SKIPCRC'] = self.SKIPCRC
        self.SKIPWHITE = RM_Field_FRC_FCD3_SKIPWHITE(self)
        self.zz_fdict['SKIPWHITE'] = self.SKIPWHITE
        self.ADDTRAILTXDATA = RM_Field_FRC_FCD3_ADDTRAILTXDATA(self)
        self.zz_fdict['ADDTRAILTXDATA'] = self.ADDTRAILTXDATA
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT0, self).__init__(rmio, label,
            0x40080000, 0x0C0,
            'INTELEMENT0', 'FRC.INTELEMENT0', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT0_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT1, self).__init__(rmio, label,
            0x40080000, 0x0C4,
            'INTELEMENT1', 'FRC.INTELEMENT1', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT1_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT2, self).__init__(rmio, label,
            0x40080000, 0x0C8,
            'INTELEMENT2', 'FRC.INTELEMENT2', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT2_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT3, self).__init__(rmio, label,
            0x40080000, 0x0CC,
            'INTELEMENT3', 'FRC.INTELEMENT3', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT3_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT4, self).__init__(rmio, label,
            0x40080000, 0x0D0,
            'INTELEMENT4', 'FRC.INTELEMENT4', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT4_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT5(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT5, self).__init__(rmio, label,
            0x40080000, 0x0D4,
            'INTELEMENT5', 'FRC.INTELEMENT5', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT5_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT6(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT6, self).__init__(rmio, label,
            0x40080000, 0x0D8,
            'INTELEMENT6', 'FRC.INTELEMENT6', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT6_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT7(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT7, self).__init__(rmio, label,
            0x40080000, 0x0DC,
            'INTELEMENT7', 'FRC.INTELEMENT7', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT7_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT8(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT8, self).__init__(rmio, label,
            0x40080000, 0x0E0,
            'INTELEMENT8', 'FRC.INTELEMENT8', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT8_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT9(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT9, self).__init__(rmio, label,
            0x40080000, 0x0E4,
            'INTELEMENT9', 'FRC.INTELEMENT9', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT9_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT10(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT10, self).__init__(rmio, label,
            0x40080000, 0x0E8,
            'INTELEMENT10', 'FRC.INTELEMENT10', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT10_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT11(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT11, self).__init__(rmio, label,
            0x40080000, 0x0EC,
            'INTELEMENT11', 'FRC.INTELEMENT11', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT11_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT12(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT12, self).__init__(rmio, label,
            0x40080000, 0x0F0,
            'INTELEMENT12', 'FRC.INTELEMENT12', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT12_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT13(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT13, self).__init__(rmio, label,
            0x40080000, 0x0F4,
            'INTELEMENT13', 'FRC.INTELEMENT13', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT13_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT14(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT14, self).__init__(rmio, label,
            0x40080000, 0x0F8,
            'INTELEMENT14', 'FRC.INTELEMENT14', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT14_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_INTELEMENT15(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_INTELEMENT15, self).__init__(rmio, label,
            0x40080000, 0x0FC,
            'INTELEMENT15', 'FRC.INTELEMENT15', 'read-only',
            u"",
            0x00000000, 0x000000FF)

        self.INTELEMENT = RM_Field_FRC_INTELEMENT15_INTELEMENT(self)
        self.zz_fdict['INTELEMENT'] = self.INTELEMENT
        self.__dict__['zz_frozen'] = True


class RM_Register_FRC_MIRRORIF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_FRC_MIRRORIF, self).__init__(rmio, label,
            0x40080000, 0x100,
            'MIRRORIF', 'FRC.MIRRORIF', 'read-write',
            u"",
            0x00000000, 0x0003FFFF)

        self.TXDONEM = RM_Field_FRC_MIRRORIF_TXDONEM(self)
        self.zz_fdict['TXDONEM'] = self.TXDONEM
        self.TXAFTERFRAMEDONEM = RM_Field_FRC_MIRRORIF_TXAFTERFRAMEDONEM(self)
        self.zz_fdict['TXAFTERFRAMEDONEM'] = self.TXAFTERFRAMEDONEM
        self.TXABORTEDM = RM_Field_FRC_MIRRORIF_TXABORTEDM(self)
        self.zz_fdict['TXABORTEDM'] = self.TXABORTEDM
        self.TXUFM = RM_Field_FRC_MIRRORIF_TXUFM(self)
        self.zz_fdict['TXUFM'] = self.TXUFM
        self.RXDONEM = RM_Field_FRC_MIRRORIF_RXDONEM(self)
        self.zz_fdict['RXDONEM'] = self.RXDONEM
        self.RXABORTEDM = RM_Field_FRC_MIRRORIF_RXABORTEDM(self)
        self.zz_fdict['RXABORTEDM'] = self.RXABORTEDM
        self.FRAMEERRORM = RM_Field_FRC_MIRRORIF_FRAMEERRORM(self)
        self.zz_fdict['FRAMEERRORM'] = self.FRAMEERRORM
        self.BLOCKERRORM = RM_Field_FRC_MIRRORIF_BLOCKERRORM(self)
        self.zz_fdict['BLOCKERRORM'] = self.BLOCKERRORM
        self.RXOFM = RM_Field_FRC_MIRRORIF_RXOFM(self)
        self.zz_fdict['RXOFM'] = self.RXOFM
        self.ADDRERRORM = RM_Field_FRC_MIRRORIF_ADDRERRORM(self)
        self.zz_fdict['ADDRERRORM'] = self.ADDRERRORM
        self.BUSERRORM = RM_Field_FRC_MIRRORIF_BUSERRORM(self)
        self.zz_fdict['BUSERRORM'] = self.BUSERRORM
        self.SNIFFOFM = RM_Field_FRC_MIRRORIF_SNIFFOFM(self)
        self.zz_fdict['SNIFFOFM'] = self.SNIFFOFM
        self.FRAMEDETPAUSEDM = RM_Field_FRC_MIRRORIF_FRAMEDETPAUSEDM(self)
        self.zz_fdict['FRAMEDETPAUSEDM'] = self.FRAMEDETPAUSEDM
        self.INTERLEAVEWRITEPAUSEDM = RM_Field_FRC_MIRRORIF_INTERLEAVEWRITEPAUSEDM(self)
        self.zz_fdict['INTERLEAVEWRITEPAUSEDM'] = self.INTERLEAVEWRITEPAUSEDM
        self.INTERLEAVEREADPAUSEDM = RM_Field_FRC_MIRRORIF_INTERLEAVEREADPAUSEDM(self)
        self.zz_fdict['INTERLEAVEREADPAUSEDM'] = self.INTERLEAVEREADPAUSEDM
        self.TXSUBFRAMEPAUSEDM = RM_Field_FRC_MIRRORIF_TXSUBFRAMEPAUSEDM(self)
        self.zz_fdict['TXSUBFRAMEPAUSEDM'] = self.TXSUBFRAMEPAUSEDM
        self.CONVPAUSEDM = RM_Field_FRC_MIRRORIF_CONVPAUSEDM(self)
        self.zz_fdict['CONVPAUSEDM'] = self.CONVPAUSEDM
        self.IFMIRRORCLEAR = RM_Field_FRC_MIRRORIF_IFMIRRORCLEAR(self)
        self.zz_fdict['IFMIRRORCLEAR'] = self.IFMIRRORCLEAR
        self.__dict__['zz_frozen'] = True


