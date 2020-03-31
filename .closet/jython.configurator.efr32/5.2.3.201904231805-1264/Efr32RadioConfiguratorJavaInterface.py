# This is a python adapter that adapts to the IChipConfigurator java interface
# via the ChipConfiguratorJavaInterface python class

# These are required to tie in java
from com.ember.workbench.chip_config import ChipConfiguratorData
from com.silabs.ss.platform.api.rcp.core import OptionList, OptionType
from com.ember.workbench.efr32_radio_config.options import Efr32OptionId
from com.ember.workbench.gui.profile import EnumDataItem
from enum import Enum, unique, EnumMeta
from ChipConfiguratorJavaInterface import ChipConfiguratorJavaInterface
from types import *
import __builtin__
import sys

from efr32config import Efr32Configurator

# Class implementation
class Efr32RadioConfiguratorJavaInterface(ChipConfiguratorJavaInterface):

    def __init__ (self):
        self.configurator = Efr32Configurator()

    def calculate(self, chipId, configInput):
        debugPrint = False
        profile = configInput.get(Efr32OptionId.PROFILE.id())
        railApi = configInput.get(Efr32OptionId.RAIL_API.id())
        self.configurator.setup(chipId, None, profile, railApi)
        
        # Prepare the arguments for configure(). This is different from the 
        # radio configurator inputs.
        phyName = configInput.get(Efr32OptionId.PHY_NAME.id())
        optInputs = configInput.get(Efr32OptionId.OPTIONAL_INPUTS.id())
        args = {Efr32OptionId.PHY_NAME.id(): phyName, Efr32OptionId.OPTIONAL_INPUTS.id(): optInputs}

        if (debugPrint):
            print("    def testConfiguration(self):")
            print("        c = Efr32Configurator()")
        
        for item in configInput.keys():
            if not(item == Efr32OptionId.PHY_NAME.id() or 
                   item == Efr32OptionId.OPTIONAL_INPUTS.id() or
                   item == Efr32OptionId.PROFILE.id() or
                   item == Efr32OptionId.RAIL_API.id()):
                try:
                    value = configInput.get(item)
                    if (debugPrint):
                        #print("#        Set {} to {}".format(item, value))
                        print("        c.set_option(\"{}\", {})".format(item, value))
                    self.configurator.set_option(item, value)
                except:
                    e = sys.exc_info()[0]
                    v = sys.exc_info()[1]
                    print("#       {}: {} : Failed to set option {} to {} of type {}".format(e, v, item, value, type(value)))
                    print("#       Got exception {}: {} in Studio".format(e, v))
                    print("")
        if (debugPrint):
            print(args)
        data = self.configurator.configure(**args)
        return self._dict_as_chip_configurator_data(data)
        
    def inputOptions(self, chipId, category):
        optionList = OptionList.empty()
        for k, v in self.configurator.instance(chipId).get_options(category).items():
            optionList.add(k, k, "", self._getOptionType(v), "{}".format(v))
        return optionList
        
    def categories(self, chipId):
        # Set the devce configuration (jumbo, dumbo, nerio,...) and set to Base profile
        self.configurator.setup(chipId, None, "Base")
        return self.configurator.get_categories()
    
    def profileIds(self, chipId):
        return self.configurator.get_profile_ids()
    
    def profileData(self, chipId, profileId):
        pData = self.configurator.get_profile_data(profileId)
        return self._dict_as_chip_configurator_data(pData)
    
    def isOptionIdValid(self, chipId, optionId):
        return True
    
    def version(self, chipId):
        return self.configurator._radio_configurator.version
