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

from efr32multiphyconfig import Efr32MultiPHYConfigurator

# Class implementation
class Efr32MultiPhyRadioConfiguratorJavaInterface(ChipConfiguratorJavaInterface):

    def __init__ (self):
        self.configurator = Efr32MultiPHYConfigurator()

    def calculate(self, chipId, configInput):
        debugPrint = False
        
        # Prepare the arguments for configure(). This is different from the 
        # radio configurator inputs.
        inputConfig = configInput.get(Efr32OptionId.INPUT.id())
        args = {Efr32OptionId.INPUT.id(): inputConfig}
        
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
        return self.configurator.version
