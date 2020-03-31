#!/usr/bin/python
#

import os
import re
from rail_scripts._version import __version__
# from  rail_scripts.rail_adapter import RAILAdapter
from rail_scripts.rail_adapter_single_phy import RAILAdapter_SinglePhy
from rail_scripts.rail_adapter_multi_phy import RAILAdapter_MultiPhy
import jinja2
import jinja2.ext

class RAILConfig_generator:

  _TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')

  """
  Class takes an input file and parses it into header file content
  """
  # ------------------------------------------------------------------------
  def __init__(self, railAdapter):
    setattr(self, "version", __version__)
    self.rail_version = railAdapter.rail_version
    self.rc_version = railAdapter.rc_version
    # Instantiate jinja environment and register template path with FileSystemLoader
    self.jinja_env = jinja2.Environment(extensions=[jinja2.ext.do],loader=jinja2.FileSystemLoader(RAILConfig_generator._TEMPLATE_PATH or './'))

    # Register custom filters with jinja
    self.jinja_env.filters['formatToEngineering'] = self.formatToEngineering
    self.jinja_env.filters['listToHexEncoding'] = self.listToHexEncoding
    self.jinja_env.filters['formatActionAddress'] = self.formatActionAddress
    self.jinja_env.filters['firstElement'] = self.firstElement

    # Register the right templates to use based on the RAILAdapter class
    if isinstance(railAdapter, RAILAdapter_SinglePhy):
      self.template_path_h = "rail_config_{}x.h.j2".format(self.rail_version)
      self.template_path_c = "rail_config_{}x.c.j2".format(self.rail_version)
    else:
      self.template_path_h = "rail_config_multi_phy.h.j2".format(self.rail_version)
      self.template_path_c = "rail_config_multi_phy.c.j2".format(self.rail_version)

    # We need the railAdapter object to be populated before we can generate the
    # context. If the railAdapter object is not populated by the caller, we can
    # try to populate it here, but if the inputs have not been set properly, it
    # may still fail.
    if not railAdapter.modelPopulated:
      railAdapter.populateModel()

    self.context = railAdapter.generateRailModelContext()
    self.context['filename'] = "rail_config"
    self.context['title'] = "Radio Config"
    self.context['rail_version'] = self.rail_version
    self.context['rc_version'] = self.rc_version
    self.context['ra_version'] = self.version

  # Allow clients to override the built-in templates; note that we are only
  # modifying the loader attribute of the jinja environment already created.
  def registerTemplatePath(self, path):
    if not os.path.isdir(path):
      raise ValueError("Supplied path is not valid: {}".format(path))
    print("Overriding internal template path with \"{}\"".format(path))
    self.jinja_env.loader = jinja2.FileSystemLoader(path)

  # This allows clients to add/modify keys in the context attribute, which can
  # be used along with custom templates to generate different outputs. This is
  # also how we allow ourselves to generate the RAIL lib internal templates.
  def overrideContext(self, **kwargs):
    for key, value in kwargs.items():
      self.context[key] = value

  # -------- Internal ---------------------------------------------------------
  # TODO: Consider using something more robust like:
  # quantiphy - https://github.com/KenKundert/quantiphy
  # engineering_notation - https://github.com/slightlynybbled/engineering_notation
  def formatToEngineering(self, value, units=''):

    if (value >= 1E6):
      value = value/1E6
      suffix = "M"+units
    elif (value >= 1E3):
      value = value/1E3
      suffix = "k"+units
    else:
      suffix = "b"+units

    charMax = 8
    valueCharMax = charMax - len(suffix)

    valueValStr = (str(value))[0:valueCharMax]
    if (valueValStr[-1:] == "."):
      valueValStr = valueValStr[:-1]

    return "{}{}".format(valueValStr, suffix)

  def listToHexEncoding(self, inputList):
    encodedList = 0
    if not isinstance(inputList, list):
      inputList = inputList.values
    for (i, valid) in enumerate(inputList):
      if valid:
        encodedList |= 1 << i
    return hex(encodedList)

  # NOTE!!
  # This custom filter was created to work around an issue (exception) caused by
  # having math operations in the template file itself. Attila encountered this
  # problem while testing the rail_config generation through Jython, via
  # Simplicity Studio.
  def formatActionAddress(self, encodedAcionValue, loopIndex):
    return ((encodedAcionValue % (2**16)) + (loopIndex*4))

  # This filter extracts the first element of an OrderedDict, and returns a
  # tuple consisting of the key/value pair, where the value itself is casted to
  # a regular dict, from of an OrderedDict, which can't be easily used by jinja
  def firstElement(self, dictionary):
    for key, value in dictionary.items():
      break
    return key, dict(value)

  # Render function to encapsulate jinja
  def render(self, tpl_path, context=None):
    path, filename = os.path.split(tpl_path)
    if context is None:
      context = self.context
    return self.jinja_env.get_template(filename).render(context)
