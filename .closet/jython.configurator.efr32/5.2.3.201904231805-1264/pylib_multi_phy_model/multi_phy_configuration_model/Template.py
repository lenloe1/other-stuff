#!/usr/bin/env python

#
# Generated Thu Dec 06 10:49:08 2018 by generateDS.py version 2.12d.
#
# Command line options:
#   ('-o', '..\\Bindings.py')
#   ('--super', 'Bindings')
#   ('-s', '..\\Template.py')
#   ('--subclass-suffix', '')
#   ('--member-specs', 'list')
#   ('-m', '')
#   ('-f', '')
#   ('--silence', '')
#
# Command line arguments:
#   .\multi_phy_configuration_model.xsd
#
# Command line:
#   generateDS_custom.py -o "..\Bindings.py" --super="Bindings" -s "..\Template.py" --subclass-suffix --member-specs="list" -m -f --silence .\multi_phy_configuration_model.xsd
#
# Current working directory (os.getcwd()):
#   xsd
#

import sys

import Bindings as supermod

etree_ = None
Verbose_import_ = False
(
    XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")


def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
            'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class multi_phy_configuration(supermod.multi_phy_configuration):
    def __init__(self, part_family=None, status_code=None, readable_name=None, rail_adapter_version=None, part_revision=None, xsd_version=None, status_message=None, desc=None, base_channel_configurations=None, output_files=None):
        super(multi_phy_configuration, self).__init__(part_family, status_code, readable_name, rail_adapter_version, part_revision, xsd_version, status_message, desc, base_channel_configurations, output_files, )
supermod.multi_phy_configuration.subclass = multi_phy_configuration
# end class multi_phy_configuration


class base_channel_configurationsType(supermod.base_channel_configurationsType):
    def __init__(self, base_channel_configuration=None):
        super(base_channel_configurationsType, self).__init__(base_channel_configuration, )
supermod.base_channel_configurationsType.subclass = base_channel_configurationsType
# end class base_channel_configurationsType


class base_channel_configurationType(supermod.base_channel_configurationType):
    def __init__(self, profile=None, base_channel_reference=None, name=None, force_empty_phy_config_delta_subtract=True, profile_inputs=None, phy=None, channel_config_entries=None, phy_config_base=None, phy_config_delta_subtract=None, link_layer_config=None, optional_arguments=None):
        super(base_channel_configurationType, self).__init__(profile, base_channel_reference, name, force_empty_phy_config_delta_subtract, profile_inputs, phy, channel_config_entries, phy_config_base, phy_config_delta_subtract, link_layer_config, optional_arguments, )
supermod.base_channel_configurationType.subclass = base_channel_configurationType
# end class base_channel_configurationType


class profile_inputsType(supermod.profile_inputsType):
    def __init__(self, input=None):
        super(profile_inputsType, self).__init__(input, )
supermod.profile_inputsType.subclass = profile_inputsType
# end class profile_inputsType


class inputType(supermod.inputType):
    def __init__(self, key=None, value=None):
        super(inputType, self).__init__(key, value, )
supermod.inputType.subclass = inputType
# end class inputType


class phyType(supermod.phyType):
    def __init__(self, name=None, profile_input_overrides=None):
        super(phyType, self).__init__(name, profile_input_overrides, )
supermod.phyType.subclass = phyType
# end class phyType


class profile_input_overridesType(supermod.profile_input_overridesType):
    def __init__(self, override=None):
        super(profile_input_overridesType, self).__init__(override, )
supermod.profile_input_overridesType.subclass = profile_input_overridesType
# end class profile_input_overridesType


class overrideType(supermod.overrideType):
    def __init__(self, key=None, value=None):
        super(overrideType, self).__init__(key, value, )
supermod.overrideType.subclass = overrideType
# end class overrideType


class channel_config_entriesType(supermod.channel_config_entriesType):
    def __init__(self, channel_config_entry=None):
        super(channel_config_entriesType, self).__init__(channel_config_entry, )
supermod.channel_config_entriesType.subclass = channel_config_entriesType
# end class channel_config_entriesType


class channel_config_entryType(supermod.channel_config_entryType):
    def __init__(self, name=None, base_frequency=None, channel_spacing=None, physical_channel_offset=None, channel_number_start=None, channel_number_end=None, max_power=None, profile_input_overrides=None, phy_name_override=None, phy_config_delta_add=None, radio_configurator_output_model=None, full_register_model=None, optional_arguments=None):
        super(channel_config_entryType, self).__init__(name, base_frequency, channel_spacing, physical_channel_offset, channel_number_start, channel_number_end, max_power, profile_input_overrides, phy_name_override, phy_config_delta_add, radio_configurator_output_model, full_register_model, optional_arguments, )
supermod.channel_config_entryType.subclass = channel_config_entryType
# end class channel_config_entryType


class profile_input_overridesType1(supermod.profile_input_overridesType1):
    def __init__(self, override=None):
        super(profile_input_overridesType1, self).__init__(override, )
supermod.profile_input_overridesType1.subclass = profile_input_overridesType1
# end class profile_input_overridesType1


class overrideType2(supermod.overrideType2):
    def __init__(self, key=None, value=None):
        super(overrideType2, self).__init__(key, value, )
supermod.overrideType2.subclass = overrideType2
# end class overrideType2


class phy_config_delta_addType(supermod.phy_config_delta_addType):
    def __init__(self, register=None):
        super(phy_config_delta_addType, self).__init__(register, )
supermod.phy_config_delta_addType.subclass = phy_config_delta_addType
# end class phy_config_delta_addType


class registerType(supermod.registerType):
    def __init__(self, name=None, value=None, baseAddress=None, addressOffset=None, fullname=None, access=None, description=None, resetValue=None, resetMask=None):
        super(registerType, self).__init__(name, value, baseAddress, addressOffset, fullname, access, description, resetValue, resetMask, )
supermod.registerType.subclass = registerType
# end class registerType


class optional_argumentsType(supermod.optional_argumentsType):
    def __init__(self, argument=None):
        super(optional_argumentsType, self).__init__(argument, )
supermod.optional_argumentsType.subclass = optional_argumentsType
# end class optional_argumentsType


class argumentType(supermod.argumentType):
    def __init__(self, key=None, value=None):
        super(argumentType, self).__init__(key, value, )
supermod.argumentType.subclass = argumentType
# end class argumentType


class phy_config_baseType(supermod.phy_config_baseType):
    def __init__(self, register=None):
        super(phy_config_baseType, self).__init__(register, )
supermod.phy_config_baseType.subclass = phy_config_baseType
# end class phy_config_baseType


class registerType3(supermod.registerType3):
    def __init__(self, name=None, value=None, baseAddress=None, addressOffset=None, fullname=None, access=None, description=None, resetValue=None, resetMask=None):
        super(registerType3, self).__init__(name, value, baseAddress, addressOffset, fullname, access, description, resetValue, resetMask, )
supermod.registerType3.subclass = registerType3
# end class registerType3


class phy_config_delta_subtractType(supermod.phy_config_delta_subtractType):
    def __init__(self, register=None):
        super(phy_config_delta_subtractType, self).__init__(register, )
supermod.phy_config_delta_subtractType.subclass = phy_config_delta_subtractType
# end class phy_config_delta_subtractType


class registerType4(supermod.registerType4):
    def __init__(self, name=None, value=None, baseAddress=None, addressOffset=None, fullname=None, access=None, description=None, resetValue=None, resetMask=None):
        super(registerType4, self).__init__(name, value, baseAddress, addressOffset, fullname, access, description, resetValue, resetMask, )
supermod.registerType4.subclass = registerType4
# end class registerType4


class link_layer_configType(supermod.link_layer_configType):
    def __init__(self, name=None, inputs=None, phy=None, link_layer_model=None):
        super(link_layer_configType, self).__init__(name, inputs, phy, link_layer_model, )
supermod.link_layer_configType.subclass = link_layer_configType
# end class link_layer_configType


class inputsType(supermod.inputsType):
    def __init__(self, input=None):
        super(inputsType, self).__init__(input, )
supermod.inputsType.subclass = inputsType
# end class inputsType


class inputType5(supermod.inputType5):
    def __init__(self, key=None, value=None):
        super(inputType5, self).__init__(key, value, )
supermod.inputType5.subclass = inputType5
# end class inputType5


class phyType6(supermod.phyType6):
    def __init__(self, name=None, overrides=None):
        super(phyType6, self).__init__(name, overrides, )
supermod.phyType6.subclass = phyType6
# end class phyType6


class overridesType(supermod.overridesType):
    def __init__(self, override=None):
        super(overridesType, self).__init__(override, )
supermod.overridesType.subclass = overridesType
# end class overridesType


class overrideType7(supermod.overrideType7):
    def __init__(self, key=None, value=None):
        super(overrideType7, self).__init__(key, value, )
supermod.overrideType7.subclass = overrideType7
# end class overrideType7


class optional_argumentsType8(supermod.optional_argumentsType8):
    def __init__(self, argument=None):
        super(optional_argumentsType8, self).__init__(argument, )
supermod.optional_argumentsType8.subclass = optional_argumentsType8
# end class optional_argumentsType8


class argumentType9(supermod.argumentType9):
    def __init__(self, key=None, value=None):
        super(argumentType9, self).__init__(key, value, )
supermod.argumentType9.subclass = argumentType9
# end class argumentType9


class output_filesType(supermod.output_filesType):
    def __init__(self, file=None):
        super(output_filesType, self).__init__(file, )
supermod.output_filesType.subclass = output_filesType
# end class output_filesType


class fileType(supermod.fileType):
    def __init__(self, name=None, source_code=None):
        super(fileType, self).__init__(name, source_code, )
supermod.fileType.subclass = fileType
# end class fileType


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'multi_phy_configuration'
        rootClass = supermod.multi_phy_configuration
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_='',
##             pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'multi_phy_configuration'
        rootClass = supermod.multi_phy_configuration
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
##     if not silence:
##         content = etree_.tostring(
##             rootElement, pretty_print=True,
##             xml_declaration=True, encoding="utf-8")
##         sys.stdout.write(content)
##         sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'multi_phy_configuration'
        rootClass = supermod.multi_phy_configuration
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'multi_phy_configuration'
        rootClass = supermod.multi_phy_configuration
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     if not silence:
##         sys.stdout.write('#from Bindings import *\n\n')
##         sys.stdout.write('import Bindings as model_\n\n')
##         sys.stdout.write('rootObj = model_.rootClass(\n')
##         rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
##         sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
