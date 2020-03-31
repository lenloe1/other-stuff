from functools import cmp_to_key

from rail_scripts.rail_adapter import *
from rail_scripts._version import __version__

class RAILAdapter_MultiPhy(RAILAdapter):

  def __init__(self, **kwargs):
    self.rc_version = kwargs["rc_version"] if "rc_version" in kwargs else None
    setattr(self, "version", __version__)
    self.mphyConfig = kwargs["mphyConfig"]
    regex = re.compile(r'rail_api_(\d+).x')
    # Captures RAIL major version into an int
    # We use "get", to avoid raising "KeyError"; default to "rail_api_2.x"
    adapter_name = kwargs.get("adapter_name", "rail_api_2.x")
    re_match = regex.match(adapter_name)
    if re_match:
      self.rail_version= int(re_match.group(1))
    else:
      raise Exception("Unknown RAIL Adapter name: {}".format(adapter_name))
    with open(os.path.join(RAILAdapter.current_dir,"rail_model_multi_phy.yml")) as f:
      self.yamlobject = yaml.load(f.read())
    self.railModel = RAILModel(self.yamlobject)
    self._railModelPopulated = False

  def _encodeAction(self, modemConfig, address, length, values=[]):
    if length > 0:
      newModemConfigEntry = modemConfig.addNewElement()
      encodedAddress = self._encodeWriteAddress(address, length)
      firstValue = values[0]
      newModemConfigEntry.encodedAction.value = encodedAddress
      newModemConfigEntry.encodedValues.value = [firstValue]
      for val in values[1:]:
        newModemConfigEntry.encodedValues.value.append(val)

  def optimizeRadioConfig(self, base_info):
    def _optimizeWrite(base_streak, regs_channels, expensive, cheap):
      # Compute cost to move write in word units. The write costs 1 + len words.
      # This results in a net cost based on the number of places it's added vs.
      # the one place it's removed.
      net_cost_to_add = (len(regs_channels) - 1) * (1 + len(base_streak))
      # Now lower our cost. For every add that has a neighboring write on the
      # high or low side, we subtract one word due to continuous write synergy
      for add in regs_channels:
        above = False
        below = False
        for address, _ in add:
          above |= (address == base_streak[0][0] + 4 * len(base_streak))
          below |= (address == base_streak[0][0] - 4)
        net_cost_to_add -= 1 if above else 0
        net_cost_to_add -= 1 if below else 0
      # If the net cost is 0, it probably saves time due to write synergy
      if (net_cost_to_add <= 0):
        cheap.extend(base_streak)
      else:
        expensive.extend(base_streak)

    # This algorithm handles a single add poorly. Leave everything in the base
    if len(base_info["add"]) <= 1:
      return

    regs_channels = [x[0] for x in base_info["add"]]
    new_base = []
    add_to_entries = []
    # Chunk base into it's continuous writes, and see
    base_streak = [base_info["base"][0]]
    for registerAddress, registerValue in base_info["base"][1:]:
      if base_streak == [] or registerAddress == (base_streak[0][0] + 4 * len(base_streak)):
        base_streak.append((registerAddress, registerValue))
      else:
        _optimizeWrite(base_streak, regs_channels, new_base, add_to_entries)
        base_streak = [(registerAddress, registerValue)]
    _optimizeWrite(base_streak, regs_channels, new_base, add_to_entries)

    for add in regs_channels:
      add.extend(add_to_entries)
      add.sort()
    base_info["base"] = new_base

  def formatModemConfigEntries(self, configName, phyConfigEntry, registerEntries, base=False, subtract=False):
    if self.rail_version == 1:
      # RAIL 1.x requires an action for every write
      for registerAddress, registerValue in registerEntries:
        self._encodeAction(phyConfigEntry, registerAddress, 1, [registerValue])
    else:
      # RAIL 2.x supports packed radio configurations
      currentAddress = 0
      length = 0
      values = []

      # Create a new modemConfig element, and grab appropriate references based on
      # whether this is a regular or subtract node.
      if base == True:
        newModemConfig = self.railModel.multiPhyConfig.commonStructures.modemConfigEntriesBase.newElement(configName + "_modemConfigBase")
        currentModemConfigs = self.railModel.multiPhyConfig.commonStructures.modemConfigEntriesBase
        currentPhyConfigEntryModemConfigEntry = phyConfigEntry.modemConfigEntryBase
      elif subtract == True:
        newModemConfig = self.railModel.multiPhyConfig.commonStructures.modemConfigEntriesSubtract.newElement(configName + "_modemConfigSubtract")
        currentModemConfigs = self.railModel.multiPhyConfig.commonStructures.modemConfigEntriesSubtract
        currentPhyConfigEntryModemConfigEntry = phyConfigEntry.modemConfigEntrySubtract
      else:
        newModemConfig = self.railModel.multiPhyConfig.commonStructures.modemConfigEntries.newElement(phyConfigEntry.name + "_modemConfig")
        currentModemConfigs = self.railModel.multiPhyConfig.commonStructures.modemConfigEntries
        currentPhyConfigEntryModemConfigEntry = phyConfigEntry.modemConfigEntry

      for registerAddress, registerValue in registerEntries:
        if (registerAddress - currentAddress) == (4 * length):
          length += 1
          values.append(registerValue)
        else:
          self._encodeAction(newModemConfig, currentAddress, length, values)
          currentAddress = registerAddress
          length = 1
          values = [registerValue]
      # One final write for whatever is left
      self._encodeAction(newModemConfig, currentAddress, length, values)

      # Check the size of the newModemConfig is greater than 0 before adding it
      # to the currentModemConfigs structure
      if len(newModemConfig._elements) > 0:

        # Traverse existing modemConfigEntries and check for duplicates
        entryFound = False
        for modemConfig in currentModemConfigs._elements:
          if modemConfig == newModemConfig:
            # Register the entry with the current phyConfigEntry
            currentPhyConfigEntryModemConfigEntry.value = modemConfig
            entryFound = True
            break

        if not entryFound:
          # Found no duplicates, so add the newModemConfig to the phyInfoEntries object
          currentModemConfigs.addElement(newModemConfig)
          # Register the entry with the current phyConfigEntry
          currentPhyConfigEntryModemConfigEntry.value = newModemConfig

  def _generateModemConfigEntries(self, phyConfigEntry, model, regs):
    if len(regs) > 0:
      # Write the address of the phyInfo structure to SEQ.PHYINFO.ADDRESS
      address = self._getRegAddress("SEQ","PHYINFO")
      regs.append((address, phyConfigEntry.phyInfoEntry.value))

      # Write the address of the block decoding table to BLOCKRAMADDR when
      # BLOCKWHITEMODE == BLOCKLOOKUP. Include the register even when the table
      # is absent for speed with continuous write, and make the potential
      # future implementation of RAIL_LIB-1138 easier
      address = self._getRegAddress("FRC","BLOCKRAMADDR")
      regs.append((address, phyConfigEntry.frameCodingTableEntry.value or 0))

      # Write the address of the convDecodeBuffer to CONVRAMADDR when
      # fecEnabled, include even when absent for speed
      address = self._getRegAddress("FRC","CONVRAMADDR")
      if phyConfigEntry.fecEnabled.value:
        # On Panther, we decided to ALWAYS write the FRC_CONVRAMADDR to HIGH RAM offset 0
        regs.append((address, "convDecodeBuffer" if self.partFamily != "panther" else 0))
      else:
        regs.append((address, 0))

      # Write the address of the last Dynamic Slicer Configuration link
      # if there are any present, exclude the write if false
      dynamicSlicerTableEntry = phyConfigEntry.dynamicSlicerTableEntry.value
      if dynamicSlicerTableEntry and len(dynamicSlicerTableEntry._elements) > 0:
          address = self._getRegAddress("SEQ","DYNAMIC_CHPWR_TABLE")
          regs.append((address, phyConfigEntry.dynamicSlicerTableEntry.value.lastElement))

      regs.sort() # Put the registers in the right order again

    return regs

  # Takes a model instance and writes it to a rm object
  def _writeModelToRmDevice(self, isBaseConfig, baseChannelConfig, channelConfigEntry, phyConfigEntry, rm):

    if isBaseConfig:

      if baseChannelConfig.base_channel_reference:
        # If "base_channel_reference" feature is being used, (it's not 'None')
        # we need to make sure the phy_config_base is indeed empty
        assert len(baseChannelConfig.phy_config_base) == 0, \
          "Length of baseChannelConfig.phy_config_base ({}) is not 0".format(len(baseChannelConfig.phy_config_base))
        try:
          # Attempt to get the phy_config_base from the base_channel_configuration
          # in mphyConfig that matches the name of base_channel_reference;
          # use the first element returned by the filter (index 0)
          baseChannelConfig.phy_config_base = \
          list(filter(lambda x: x.name == baseChannelConfig.base_channel_reference, \
                 self.mphyConfig.base_channel_configurations.base_channel_configuration))[0].phy_config_base
        except:
          raise Exception("Invalid configuration for base_channel_configuration '{}'".format(baseChannelConfig.name))

      registers_base = baseChannelConfig.phy_config_base
      registers_channel = channelConfigEntry.phy_config_delta_add
      registers_subtract = baseChannelConfig.phy_config_delta_subtract
    else:
      registers_base = {}
      registers_channel = channelConfigEntry.phy_config_delta_add
      registers_subtract = {}

    # Don't let the configurator dictate channel information to us. We use the
    # RAIL_ChannelConfig_t via SYNTH_Config to determine the below registers_channel,
    # so removing them saves space and potential headache.
    # Also, BLOCKRAMADDR and CONVRAMADDR should only be written by us (RAIL)
    # We use pop(X, None) to avoid raising KeyError in case the register is not
    # in the dictionary
    registers_base.pop('SYNTH.FREQ', None)
    registers_base.pop('SYNTH.CHCTRL', None)
    registers_base.pop('SYNTH.CHSP', None)
    registers_base.pop('FRC.BLOCKRAMADDR', None)
    registers_base.pop('FRC.CONVRAMADDR', None)

    registers_channel.pop('SYNTH.FREQ', None)
    registers_channel.pop('SYNTH.CHCTRL', None)
    registers_channel.pop('SYNTH.CHSP', None)
    registers_channel.pop('FRC.BLOCKRAMADDR', None)
    registers_channel.pop('FRC.CONVRAMADDR', None)

    self.registers_base = registers_base
    self.registers_subtract = registers_subtract
    self.registers_channel = registers_channel

  def _generatePhyInfoStructure(self, phyConfigEntry, baseConfigOptions, channelConfigOptions, model):
    # Get a local reference to model.profile.outputs to use here
    outputs = model.profile.outputs

    # For antenna diversity, first grab the relevant outputs from the calculator
    antDivMode = outputs.get_output('div_antdivmode').var_value
    antDivRepeatDisable = outputs.get_output('div_antdivrepeatdis').var_value

    # Then, generate the register value than maps to the fields we care about
    antDivConfiguration = 0x0
    antDivConfiguration |= (antDivMode << self.rm.MODEM.CTRL3.ANTDIVMODE.bitOffset)
    antDivConfiguration |= (antDivRepeatDisable << self.rm.MODEM.CTRL3.ANTDIVREPEATDIS.bitOffset)

    # Create a new phyInfo element
    newPhyInfoEntry = self.railModel.multiPhyConfig.commonStructures.phyInfoEntries.newElement("phyInfo")

    newPhyInfoEntry.phyInfoMetadata.freqOffsetFactor_fxp.value = outputs.get_output('frequency_offset_factor_fxp').var_value
    newPhyInfoEntry.phyInfoMetadata.baudPerSymbol.value = outputs.get_output('baud_per_symbol_actual').var_value
    newPhyInfoEntry.phyInfoMetadata.bitsPerSymbol.value = outputs.get_output('bits_per_symbol_actual').var_value

    newPhyInfoEntry.phyInfoData.version.value = 0 if self.rail_version == 1 else 3
    newPhyInfoEntry.phyInfoData.freqOffsetFactor.value = outputs.get_output('frequency_offset_factor').var_value
    newPhyInfoEntry.phyInfoData.frameTypeConfig.value = phyConfigEntry.frameTypeEntry.value
    newPhyInfoEntry.phyInfoData.irCalConfig.value = phyConfigEntry.irCalConfigEntry.value
    # For the timingConfig, we give priority to the channelConfigOptions, and then
    # the baseConfigOptions; we use "get" to avoid raising exception if the key
    # is not defined; we use the phyConfigEntry.name as the fallback/default.
    newPhyInfoEntry.phyInfoData.timingConfig.value = channelConfigOptions.get("channel_timing_name", \
    baseConfigOptions.get("channel_timing_name", phyConfigEntry.name))
    newPhyInfoEntry.phyInfoData.antDivRxAutoConfig.value = antDivConfiguration
    newPhyInfoEntry.phyInfoData.src1Denominator.value = outputs.get_output('src1_calcDenominator').var_value
    newPhyInfoEntry.phyInfoData.src2Denominator.value = outputs.get_output('src2_calcDenominator').var_value
    newPhyInfoEntry.phyInfoData.txBaudRate.value = outputs.get_output('tx_baud_rate_actual').var_value
    newPhyInfoEntry.phyInfoData.rateInfo.value = outputs.get_output('tx_baud_rate_actual').var_value

    # Traverse existing irCalConfigEntries and check for duplicates
    entryFound = False
    for phyInfoEntry in self.railModel.multiPhyConfig.commonStructures.phyInfoEntries._elements:
      if phyInfoEntry == newPhyInfoEntry:
        # Register the entry with the current phyConfigEntry
        phyConfigEntry.phyInfoEntry.value = phyInfoEntry
        entryFound = True
        break

    if not entryFound:
      # Found no duplicates, so add the newPhyInfoEntry to the phyInfoEntries object
      self.railModel.multiPhyConfig.commonStructures.phyInfoEntries.addElement(newPhyInfoEntry)
      # Register the entry with the current phyConfigEntry
      phyConfigEntry.phyInfoEntry.value = newPhyInfoEntry


  def _generateDynamicSlicerConfiguration(self, phyConfigEntry, model):
    # Check the feature is enabled in the model output
    if model.profile.outputs.get_output('dynamic_slicer_enabled').var_value == True:
      # Get the two arrays that must be defined
      dynamicSlicerThresholdValues = model.profile.outputs.get_output('dynamic_slicer_threshold_values').var_value
      dynamicSlicerLevelValues = model.profile.outputs.get_output('dynamic_slicer_level_values').var_value

      # Create a new dynamicSlicerTableEntry object where to add the actual configs
      dynamicSlicerTableEntries = self.railModel.multiPhyConfig.commonStructures.dynamicSlicerTableEntries
      dynSlicerTableEntriesLen = len(dynamicSlicerTableEntries._elements)
      newDynamicSlicerTableEntryName = "dynamicSlicerTable"+str(dynSlicerTableEntriesLen)
      newDynamicSlicerTableEntry = dynamicSlicerTableEntries.newElement(newDynamicSlicerTableEntryName)

      # Use dynamicSlicerLevelValues to traverse the loop since
      # it has one more item than dynamic_slicer_threshold_values
      for i, level in enumerate(dynamicSlicerLevelValues):

        # We need to define the links in reverse order because they need to
        # reference the previous one (linked list), by doing this we avoid the
        # need for forward declarations in the C code.
        dynSlicerConfigNum = len(dynamicSlicerLevelValues)-i-1
        newDynamicSlicerConfigName = newDynamicSlicerTableEntryName+"Config"+str(dynSlicerConfigNum)

        # The threshold is stored using 2's complement in the LSB, thus the short mask (0xFF)
        # The value is stored in a uint16_t to optimize packing.
        threshold = (dynamicSlicerThresholdValues[-1] if i == 0 else dynamicSlicerThresholdValues[-i]) & 0xFF

        # The level is stored as a uint16_t, properly aligned to make the sequencer
        # code more efficient; thus the shiftValue-16.
        level = (dynamicSlicerLevelValues[-i-1] << self.rm.MODEM.CTRL1.FREQOFFESTLIM.bitOffset-16) & 0xFFFF

        # Create a new Dynamic Slicer Config
        newDynamicSlicerConfig = newDynamicSlicerTableEntry.addNewElement(newDynamicSlicerConfigName)
        newDynamicSlicerConfig.threshold.value = threshold
        newDynamicSlicerConfig.level.value = level
        newDynamicSlicerConfig.next.value = None if i == 0 else newDynamicSlicerTableEntry._elements[i-1]

      # Traverse the existing Dynamic Slicer Table Entries, and check this is not
      # a duplicate (same set of dynamicSlicerConfig entries)
      entryFound = False
      for i, dynamicSlicerTableEntry in enumerate(dynamicSlicerTableEntries._elements):
        if dynamicSlicerTableEntry._elements == newDynamicSlicerTableEntry._elements:
          # Register the entry with the current phyConfigEntry
          phyConfigEntry.dynamicSlicerTableEntry.value = dynamicSlicerTableEntry
          entryFound = True
          break

      if not entryFound:
        # Add newDynamicSlicerTableEntry entry in common structures
        dynamicSlicerTableEntries.addElement(newDynamicSlicerTableEntry)
        # Register the new entry with the current phyConfigEntry
        phyConfigEntry.dynamicSlicerTableEntry.value = newDynamicSlicerTableEntry

  # For a particular PHY get the frame config
  def _generateFrameTypeStructures(self, phyConfigEntry, model):

    newFrameLength = model.vars.frame_type_lengths.value
    if newFrameLength:
      # Traverse existing frameLengthEntries and check for duplicates
      entryFound = False
      commonStructures = self.railModel.multiPhyConfig.commonStructures
      for i, frameLengthEntry in enumerate(commonStructures.frameLengthEntries._elements):
        if frameLengthEntry.values == newFrameLength:
          # Register the entry with the current phyConfigEntry
          phyConfigEntry.frameLengthEntry.value = frameLengthEntry
          entryFound = True
          break
      if not entryFound:
        # Create a new frameLength entry in common structures
        newFrameLengthEntry = commonStructures.frameLengthEntries.addNewElement("frameLengthList")
        newFrameLengthEntry.values = newFrameLength
        # Register the new entries with the current phyConfigEntry
        phyConfigEntry.frameLengthEntry.value = newFrameLengthEntry

      # Create new frameTypeConfig entry
      newFrameTypeEntry = commonStructures.frameTypeEntries.newElement("frameTypeConfig")
      newFrameTypeEntry.offset.value = model.vars.frame_type_loc.value
      newFrameTypeEntry.mask.value = model.vars.frame_type_mask.value
      newFrameTypeEntry.frameLen.value = phyConfigEntry.frameLengthEntry
      newFrameTypeEntry.isValid.value = model.vars.frame_type_valid.value
      newFrameTypeEntry.addressFilter.value = model.vars.frame_type_filter.value
      newFrameTypeEntry.variableAddrLoc.value = False

      # Traverse existing frameTypeEntries and check for duplicates
      entryFound = False
      for i, frameTypeEntry in enumerate(commonStructures.frameTypeEntries._elements):
        if frameTypeEntry == newFrameTypeEntry:
          # Register the entry with the current phyConfigEntry
          phyConfigEntry.frameTypeEntry.value = frameTypeEntry
          entryFound = True
          break
      if not entryFound:
        # Create a new frameType entry in common structures
        commonStructures.frameTypeEntries.addElement(newFrameTypeEntry)
        # Register the new entry with the current phyConfigEntry
        phyConfigEntry.frameTypeEntry.value = newFrameTypeEntry

  def _generateIrCalStructure(self, phyConfigEntry, model):
    # Get a local reference to model.profile.outputs to use here
    outputs = model.profile.outputs

    newIrCalConfig = [
      outputs.get_output('ircal_auxndiv').var_value,
      outputs.get_output('ircal_auxlodiv').var_value,
      outputs.get_output('ircal_rampval').var_value,
      outputs.get_output('ircal_rxamppll').var_value,
      outputs.get_output('ircal_rxamppa').var_value,
      outputs.get_output('ircal_manufconfigvalid').var_value,
      outputs.get_output('ircal_pllconfigvalid').var_value,
      outputs.get_output('ircal_paconfigvalid').var_value,
      outputs.get_output('ircal_bestconfig').var_value,
      outputs.get_output('ircal_useswrssiaveraging').var_value,
      outputs.get_output('ircal_numrssitoavg').var_value,
      outputs.get_output('ircal_throwawaybeforerssi').var_value,
      outputs.get_output('ircal_delayusbeforerssi').var_value % 256,
      outputs.get_output('ircal_delayusbeforerssi').var_value / 256,
      outputs.get_output('ircal_delayusbetweenswrssi').var_value % 256,
      outputs.get_output('ircal_delayusbetweenswrssi').var_value / 256,
      outputs.get_output('ircal_agcrssiperiod').var_value,

      # recreate these Jumbo settings at the end for backwards compatibility with RAIL 1.x
      outputs.get_output('ircal_useswrssiaveraging2').var_value,
      outputs.get_output('ircal_numrssitoavg2').var_value,
      outputs.get_output('ircal_throwawaybeforerssi2').var_value,
      outputs.get_output('ircal_delayusbeforerssi2').var_value % 256,
      outputs.get_output('ircal_delayusbeforerssi2').var_value / 256,
      outputs.get_output('ircal_delayusbetweenswrssi2').var_value % 256,
      outputs.get_output('ircal_delayusbetweenswrssi2').var_value / 256,
    ]

    # Traverse existing irCalConfigEntries and check for duplicates
    entryFound = False
    commonStructures = self.railModel.multiPhyConfig.commonStructures

    for i, irCalConfigEntry in enumerate(commonStructures.irCalConfigEntries._elements):
      if irCalConfigEntry.values == newIrCalConfig:
        # Register the entry with the current phyConfigEntry
        phyConfigEntry.irCalConfigEntry.value = irCalConfigEntry
        phyConfigEntry.channelConfigEntryAttr.value = commonStructures.railChannelConfigEntryAttrEntries._elements[i]
        entryFound = True
        break

    if not entryFound:
      # Create a new irCalConfig entry in common structures
      newIrCalConfigEntry = commonStructures.irCalConfigEntries.addNewElement("irCalConfig")
      newIrCalConfigEntry.values = newIrCalConfig
      # Create a new RAIL_ChannelConfigEntryAttr_t entry in common structures
      newRailChannelConfigEntryAttr = commonStructures.railChannelConfigEntryAttrEntries.addNewElement("channelConfigEntryAttr")
      # Register the new entries with the current phyConfigEntry
      phyConfigEntry.irCalConfigEntry.value = newIrCalConfigEntry
      phyConfigEntry.channelConfigEntryAttr.value = newRailChannelConfigEntryAttr

  def _generateFrameCodingTable(self, phyConfigEntry, model):

    codingArray = model.profile.outputs.get_output('frame_coding_array_packed').var_value
    if codingArray:
      # Traverse existing frameCodingTableEntries and check for duplicates
      entryFound = False
      commonStructures = self.railModel.multiPhyConfig.commonStructures

      for i, frameCodingTableEntry in enumerate(commonStructures.frameCodingTableEntries._elements):
        if frameCodingTableEntry.values == codingArray:
          # Register the entry with the current phyConfigEntry
          phyConfigEntry.frameCodingTableEntry.value = frameCodingTableEntry
          entryFound = True
          break

      if not entryFound:
        # Create a new frameCodingTable entry in common structures
        newframeCodingTableEntry = commonStructures.frameCodingTableEntries.addNewElement("frameCodingTable")
        newframeCodingTableEntry.values = codingArray
        # Register the new entry with the current phyConfigEntry
        phyConfigEntry.frameCodingTableEntry.value = newframeCodingTableEntry

  def _generateChannelStructures(self, multiPhyConfigEntry, phyConfigEntry, channelConfigEntry):

    # Create a new Channel Config Entry
    newChannelConfigEntry = multiPhyConfigEntry.channelConfigEntries.newElement()
    newChannelConfigEntry.modemConfigDeltaAdd.value = phyConfigEntry.modemConfigEntry.value if len(channelConfigEntry.phy_config_delta_add) > 0 else None
    newChannelConfigEntry.baseFrequency.value = channelConfigEntry.base_frequency
    newChannelConfigEntry.channelSpacing.value = channelConfigEntry.channel_spacing
    newChannelConfigEntry.physicalChannelOffset.value = channelConfigEntry.physical_channel_offset
    newChannelConfigEntry.channelNumberStart.value = channelConfigEntry.channel_number_start
    newChannelConfigEntry.channelNumberEnd.value = channelConfigEntry.channel_number_end
    newChannelConfigEntry.maxPower.value = channelConfigEntry.max_power #"RAIL_TX_POWER_MAX"
    newChannelConfigEntry.attr.value = phyConfigEntry.channelConfigEntryAttr.value

    # Traverse existing channelConfigEntries and check for duplicates
    entryFound = False
    for channelConfigEntry in multiPhyConfigEntry.channelConfigEntries._elements:
      if channelConfigEntry == newChannelConfigEntry:
        entryFound = True
        break

    if not entryFound:
      # Found no duplicates, so add the newChannelConfigEntry to the channelConfigEntries object
      multiPhyConfigEntry.channelConfigEntries.addElement(newChannelConfigEntry)

  def _generateChannelConfigs(self, railModel):

    for multiPhyConfigEntry in railModel.multiPhyConfig.multiPhyConfigEntries._elements:
      # Populate the channelConfig object
      channelConfig = multiPhyConfigEntry.channelConfig
      channelConfig.modemConfigBase.value = multiPhyConfigEntry.phyConfigEntries._elements[0].modemConfigEntryBase.value
      channelConfig.modemConfigDeltaSubtract.value = multiPhyConfigEntry.phyConfigEntries._elements[0].modemConfigEntrySubtract.value
      channelConfig.channelConfigEntries.value = multiPhyConfigEntry.channelConfigEntries
      channelConfig.length.value = len(multiPhyConfigEntry.channelConfigEntries._elements)
      channelConfig.signature.value = 0

  def _orderChannelConfigEntries(self, railModel):

    # The algorithm to order the channels is as follows:

    # Sort all channel entries using the channelNumberStart first, by maxPower
    # second, and by channelNumberEnd last.

    # First step, sort the channelConfigEntries, define a custom compare function
    def compareChannelConfigEntries(a, b):
      if a.channelNumberStart.value < b.channelNumberStart.value:
        return -1
      elif a.channelNumberStart.value > b.channelNumberStart.value:
        return 1
      else:
        # Now look at maxPower
          if a.maxPower.value < b.maxPower.value:
            return -1
          elif a.maxPower.value > b.maxPower.value:
            return 1
          else:
            if a.channelNumberEnd.value < b.channelNumberEnd.value:
                return -1
            elif a.channelNumberEnd.value > b.channelNumberEnd.value:
                return 1
            else:
              return 0

    for multiPhyConfigEntry in railModel.multiPhyConfig.multiPhyConfigEntries._elements:

      # Now, do the actual sort, using the compare function defined above
      channelConfigEntries = multiPhyConfigEntry.channelConfigEntries._elements
      channelConfigEntriesSorted = sorted(channelConfigEntries, key=cmp_to_key(compareChannelConfigEntries))

      # Next, set the reference entry to the first element of the newly sorted
      # array, and call this the reference channel config entry. Iterate through
      # the remaining channel entries and check those that have maxPower <= than
      # the current reference; if the channelNumberEnd is <= to the one in the
      # reference, AND the the channelNumberStart is > the one in the reference
      # entry, move the current channel entry to the position currently occupied
      # by the reference config entry. When an item is moved, start over the loop
      # with the moved item now becoming the reference channel config entry.
      # If we traverse all the remaining items, and no changes in position occur,
      # we need to move the reference to the next channel config entry.

      # We need a variable to kick us out of this loop
      changed = False
      reference = 0
      while reference < len(channelConfigEntriesSorted):

        # Grab the maxPower for the current reference entry
        referenceChannelEntry = channelConfigEntriesSorted[reference]

        for idx, channelConfigEntry in enumerate(channelConfigEntriesSorted[reference+1:]):
          # Set this variable to False to kick us out in case nothing gets updated
          changed = False
          if channelConfigEntry.maxPower.value <= referenceChannelEntry.maxPower.value:
            if channelConfigEntry.channelNumberEnd.value <= referenceChannelEntry.channelNumberEnd.value and \
              channelConfigEntry.channelNumberStart.value > referenceChannelEntry.channelNumberStart.value:
              itemToMove = channelConfigEntriesSorted.pop(idx + reference+1)
              channelConfigEntriesSorted.insert(reference, itemToMove)
              changed = True
              break
        if not changed:
          reference += 1

      # Now that all the entries are correctly sorted, replace the elements in the
      # multiPhyConfigEntry.channelConfigEntries._elements list
      multiPhyConfigEntry.channelConfigEntries._elements = channelConfigEntriesSorted

  def _resolveConvDecoderBuffer(self, railModel):

    maxConvDecodeBufferSize = 0
    # On Panther, we decided to ALWAYS write the FRC_CONVRAMADDR to HIGH RAM offset 0
    if self.partFamily != "panther":
      for multiPhyConfigEntry in railModel.multiPhyConfig.multiPhyConfigEntries._elements:
        for phyConfigEntry in multiPhyConfigEntry.phyConfigEntries._elements:
          if phyConfigEntry.convDecodeBufferSize.value > maxConvDecodeBufferSize:
            maxConvDecodeBufferSize = phyConfigEntry.convDecodeBufferSize.value

    railModel.multiPhyConfig.commonStructures.convDecodeBufferSize.value = maxConvDecodeBufferSize


  def _convertRmToRegisterList(self, registers):
    regs = []
    if registers is not None:
      for registerName in registers.keys():
        (block, register) = registerName.split(".")
        if block not in EXCLUDE_BLOCK_LIST:
          # registers[registerName].access == 'read-only'
          # if registers[registerName] != "":
          #   # This is a workaround for write only registers
          #   regs.append(self._regOutput(block, register, registers[registerName]))
          # else:
            eval_string = "registers[registerName].io"
            value = eval(eval_string)
            regs.append(self._regOutput(block, register, value))

      # Check for duplicates since we won't know what to do with them
      regs = sorted(regs)

      prevAddr = None
      prevValue = None
      for reg in regs:
        if prevAddr != None and reg[0] == prevAddr:
          if prevValue != reg[1]:
            # raise Exception("Duplicate non-identical set of register 0x%.8x!" % reg[0])
            print("Error: Conflicting definition for register 0x%.8x (%s)" % (reg[0], filePath))
          else:
            print("Warning: Duplicate definition of register 0x%.8x (%s)" % (reg[0], filePath))
        prevAddr = reg[0]
        prevValue = reg[1]

    return regs

  # -------- External ---------------------------------------------------------
  def setInstanceDict(self, mphyConfig):
    self.mphyConfig = mphyConfig

  def setSignatures(self, signatures):
    mPhyEntries = self.railModel.multiPhyConfig.multiPhyConfigEntries._elements
    for sig, multiPhyConfigEntry in zip(signatures, mPhyEntries):
      multiPhyConfigEntry.channelConfig.signature.value = sig

  def populateModel(self):

    #Check if we have an mphyConfig
    if self.mphyConfig == None:
      print("No mphyConfig configured. Please call the setInstanceDict method.")

    # In case populateModel gets called multiple times, start the internal
    # railModel object from scratch
    if self.railModel or self._railModelPopulated:
      self.railModel = RAILModel(self.yamlobject)
      self._railModelPopulated = False

    self.partFamily = self.mphyConfig.part_family

    # Create a proper rm object depending on partFamily
    rm_factory = RM_Factory(self.partFamily.upper())
    self.rm = rm_factory()

    # Create a structure that will be added to on a per-base channel reference basis.
    # We use this to move writes between base and add to optimize keeping
    # continuous writes as a block
    radio_configs = OrderedDict()

    # Go through all base channel configurations (NOTE!, ask Rick to rename!)
    for baseChannelConfig in self.mphyConfig.base_channel_configurations.base_channel_configuration:

      configName = baseChannelConfig.name

      baseConfigOptions = {}
      # Extract the optional arguments for this baseChannelConfig
      for argument in baseChannelConfig.optional_arguments.argument:
        baseConfigOptions[argument.key] = argument.value

      # Start off by creating a new instance of multiPhyConfigEntry, use the baseChannelConfig name
      multiPhyConfigEntry = self.railModel.multiPhyConfig.multiPhyConfigEntries.addNewElement(configName)
      # multiPhyConfigEntry.signature.signature.value = 0

      # Now, iterate through all the channel configs and mark the "base" (right now, it's always the first entry)
      for index, channelConfigEntry in enumerate(baseChannelConfig.channel_config_entries.channel_config_entry):
        isBaseConfig = index == 0

        channelConfigOptions = {}
        # Extract the optional arguments for this channelConfigEntry
        for argument in channelConfigEntry.optional_arguments.argument:
          channelConfigOptions[argument.key] = argument.value

        # Create a new phy configEntry config
        phyConfigEntry = multiPhyConfigEntry.phyConfigEntries.addNewElement(channelConfigEntry.name)

        radioConfigModel = channelConfigEntry.radio_configurator_output_model

        if self.rc_version is None:
          self.rc_version = radioConfigModel.calc_version

        # Write model instance to RM device
        self._writeModelToRmDevice(isBaseConfig, baseChannelConfig, channelConfigEntry, phyConfigEntry, self.rm)

        #Handle Frame Type Configurations
        self._generateFrameTypeStructures(phyConfigEntry, radioConfigModel)

        #Handle IR Cal Settings
        self._generateIrCalStructure(phyConfigEntry, radioConfigModel)

        self._generatePhyInfoStructure(phyConfigEntry, baseConfigOptions, channelConfigOptions, radioConfigModel)

        #Handle Frame Coding tables
        self._generateFrameCodingTable(phyConfigEntry, radioConfigModel)

        # Handle Dynamic Slicer Configuration (for OOK PHYs)
        self._generateDynamicSlicerConfiguration(phyConfigEntry, radioConfigModel)

        # Generic Model Info
        phyConfigEntry.xtalFrequency.value = radioConfigModel.vars.xtal_frequency.value
        phyConfigEntry.baseFrequency.value = radioConfigModel.vars.base_frequency.value
        phyConfigEntry.bitrate.value = radioConfigModel.vars.bitrate.value
        phyConfigEntry.modType.value = radioConfigModel.vars.modulation_type.value
        phyConfigEntry.deviation.value = radioConfigModel.vars.deviation.value
        phyConfigEntry.synthResolution.value = radioConfigModel.vars.synth_res_actual.value
        phyConfigEntry.fecEnabled.value = bool(radioConfigModel.profile.outputs.get_output('fec_enabled').var_value)
        phyConfigEntry.convDecodeBufferSize.value = radioConfigModel.profile.outputs.get_output('frc_conv_decoder_buffer_size').var_value

        # Check fecEnabled flag and convDecodeBufferSize are correctly configured
        if phyConfigEntry.fecEnabled.value:
          assert phyConfigEntry.convDecodeBufferSize.value > 0, "Incorrect configuration for FEC Enabled"

        regs_channel = self._convertRmToRegisterList(self.registers_channel)
        regs_base = self._convertRmToRegisterList(self.registers_base)
        regs_subtract = self._convertRmToRegisterList(self.registers_subtract)

        regs_channel = self._generateModemConfigEntries(phyConfigEntry, radioConfigModel, regs_channel)
        # NOTE! Special case: If regs_channel is empty, and the base is not, it means we need to include
        # the registers normally in the channel specific modemConfig in the base
        if not regs_channel:
          regs_base = self._generateModemConfigEntries(phyConfigEntry, radioConfigModel, regs_base)
        regs_subtract = self._generateModemConfigEntries(phyConfigEntry, radioConfigModel, regs_subtract)

        # Package metadata in a struct for unpacking after optimization
        meta = (configName, phyConfigEntry, multiPhyConfigEntry, channelConfigEntry)
        reference = baseChannelConfig.base_channel_reference
        reference = configName if reference is None else reference

        if not reference in radio_configs:
          radio_configs[reference] = {
            "base": regs_base,
            "subtract": regs_subtract,
            "add": [(regs_channel, meta)],
          }
        else:
          radio_configs[reference]["add"].append((regs_channel, meta))

    # Optimize and write radio configs
    for _, radio_config in radio_configs.items():
      self.optimizeRadioConfig(radio_config)

      regs_base = radio_config["base"]
      regs_subtract = radio_config["subtract"]

      for regs_channel, meta in radio_config["add"]:
        configName = meta[0]
        phyConfigEntry = meta[1]
        multiPhyConfigEntry = meta[2]
        channelConfigEntry = meta[3]

        self.formatModemConfigEntries(configName, phyConfigEntry, regs_base, True)
        self.formatModemConfigEntries(configName, phyConfigEntry, regs_channel)
        self.formatModemConfigEntries(configName, phyConfigEntry, regs_subtract, False, True)

        #Handle Channel Lists
        self._generateChannelStructures(multiPhyConfigEntry, phyConfigEntry, channelConfigEntry)

    # Populate the channelConfigs objects
    self._generateChannelConfigs(self.railModel)

    # Sort all the channel config entries in the model
    self._orderChannelConfigEntries(self.railModel)

    # Resolve convDecoderBuffer
    self._resolveConvDecoderBuffer(self.railModel)

    # We can now mark the _railModelPopulated flag as True
    self._railModelPopulated = True
