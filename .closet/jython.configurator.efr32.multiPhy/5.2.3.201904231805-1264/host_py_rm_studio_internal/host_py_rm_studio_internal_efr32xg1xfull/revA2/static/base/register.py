
__all__ = [ 'Base_RM_Register' ]

from collections import OrderedDict
from .. interface import IRegMapRegister
from .. common import GetFieldValue

class Base_RM_Register(IRegMapRegister):

    def __init__(self, rmio, label, baseAddress, addressOffset, name, fullname,
                 access, description, resetValue, resetMask):
        self.__dict__['zz_frozen'] = False
        self.zz_rmio = rmio
        self.zz_label = label
        self.zz_fdict = OrderedDict()
        self.baseAddress = baseAddress
        self.addressOffset = addressOffset
        self.name = name
        self.fullname = fullname
        self.pername = fullname.split('.')[0]
        self.access = access
        self.description = description
        self.resetValue = resetValue
        self.resetMask = resetMask
        self.zz_accessed_flag = False
        self.dumpActive = True

    def __repr__(self):
        out = "    {}\n".format(self.getDesc())
        field_list = []
        for key in sorted(self.zz_fdict):
            f = self.zz_fdict[key]
            lsb = f.bitOffset
            fsize = f.bitWidth
            sliceStr = "{}:{}".format(lsb+fsize-1, lsb) if fsize > 1 else "{}".format(lsb)
            line = "        [{}] {}: {} <{}>\n".format(sliceStr, f.name, f.description, f.access)
            field_list.append([int(sliceStr.split(':')[0]), line])
        for msb, line in sorted(field_list, reverse=True):
            out += line
        return out

    def __setattr__(self, name, value):
        if self.__dict__['zz_frozen']:
            if name == 'io':
                if self.zz_rmio.accessed_flag_active:
                    self.setAccessedFlag()
                self._c_log_write(value)
                self._py_log_write(value)
                self.zz_rmio.writeRegister(self, value)
            else:
                raise AttributeError("ERROR: Unable to set '{}' to '{}'".format(name, value))
        else:
            self.__dict__[name] = value

    def _c_log_read(self):
        if self.zz_rmio.c_logger_active:
            self.zz_rmio.c_logger.debug("    value = {}->{};".format(self.pername, self.name))

    def _py_log_read(self):
        if self.zz_rmio.py_logger_active:
            self.zz_rmio.py_logger.debug("    print({}{}.{}.io)".format(self.zz_rmio.py_rm_obj_prefix,
                                                                        self.pername, self.name))

    def _c_log_write(self, value):
        if self.zz_rmio.c_logger_active:
            self.zz_rmio.c_logger.debug("    {}->{} = {:#010x};".format(self.pername, self.name, value))

    def _py_log_write(self, value):
        if self.zz_rmio.py_logger_active:
            self.zz_rmio.py_logger.debug("    {}{}.{}.io = {:#010x}".format(self.zz_rmio.py_rm_obj_prefix,
                                                                             self.pername, self.name, value))

    def _getio(self):
        self._c_log_read()
        self._py_log_read()
        return self.zz_rmio.readRegister(self)

    def _setio(self, value):
        # unused due to the __setattr__ logic above
        pass

    io = property(_getio, _setio)

    def getFieldNames(self):
        nameList = []
        for key in sorted(self.zz_fdict):
            nameList.append(self.zz_fdict[key].fullname)
        return sorted(nameList)

    def isReadable(self):
        return self.access in [None, 'read-only', 'read-write', 'read-writeOnce']

    def isWriteable(self):
        return self.access in [None, 'write-only', 'read-write', 'writeOnce', 'read-writeOnce']

    def clearAccessedFlag(self):
        # clear the overall register access and all the member fields
        self.__dict__['zz_accessed_flag'] = False
        for key in sorted(self.zz_fdict):
            self.zz_fdict[key].clearAccessedFlag()

    def setAccessedFlag(self):
        self.__dict__['zz_accessed_flag'] = True

    def getAccessedFlag(self):
        return self.__dict__['zz_accessed_flag']

    def getAccessedFieldNames(self):
        nameList = []
            # access the whole register
            # only partial access
        for key in sorted(self.zz_fdict):
            if self.zz_fdict[key].getAccessedFlag():
                nameList.append(self.zz_fdict[key].fullname)
        return nameList

    def getDesc(self):
        flagStr = "**" if self.getAccessedFlag() else ""
        return "{:#010x}  {}{}: {} <{}>".format(self.baseAddress + self.addressOffset,
                                              self.name, flagStr,
                                              self.description.encode("utf8"), self.access)

    def assignRegDefault(self):
        self.zz_rmio.assignRegisterDefault(self)

    def includeInDump(self):
        self.__dict__['dumpActive'] = True

    def excludeFromDump(self):
        self.__dict__['dumpActive'] = False

    def buildRegFilterList(self, outFH, filterList):
        if self.isReadable():
            filterList.append(self.fullname)
            # store both the name and desc string to help user
            outFH.write("    '{}',\n".format(self.fullname))
            outFH.write("      # {}\n".format(self.getDesc()))

    def dump(self, outFH, valueDict):
        if self.isReadable():
            regValue = self.io
            outFH.write("    ('{}', {:#010x}),\n".format(self.fullname, regValue))
            outFH.write("      # {}\n".format(self.getDesc()))
            valueDict[self.fullname] = regValue
            fieldCommentList = []
            for key in sorted(self.zz_fdict):
                self.zz_fdict[key].dump(regValue, fieldCommentList)
            for msb, fullname, line in sorted(fieldCommentList, reverse=True):
                outFH.write(line)

    def dump_field(self, outFH, valueDict, field_name):
        if self.isReadable():
            regValue = self.io
            fieldObj = self.zz_fdict[field_name]
            fieldValue = GetFieldValue(regValue, fieldObj.bitOffset, fieldObj.bitWidth)
            outFH.write("    ('{}.{}', {:#x}),\n".format(self.fullname,
                                                          field_name,
                                                          fieldValue))
            outFH.write("      # {}\n".format(self.getDesc()))
            valueDict[self.fullname + '.' + field_name] = fieldValue
            fieldCommentList = []
            fieldObj.dump(regValue, fieldCommentList)
            outFH.write(fieldCommentList[0][2])
