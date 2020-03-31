from pyradioconfig.calculator_model_framework.interfaces.icalculator import ICalculator
from pycalcmodel.core.output import ModelVariableEmptyValue
from pycalcmodel.core.output import ModelOutputType
import warnings
from math import log10, floor

from py_2_and_3_compatibility import *
import os

class Human_Readable(object):

    #
    # Print a modem_model object to a humanly readable file.
    #
    @staticmethod
    def print_modem_model_values(outputfilename, phy_name, modem_model):

        warnings.warn("deprecated", DeprecationWarning)
        output_lines = list()

        line = 'info.config_name = ' + phy_name
        #print(line)
        output_lines.append(line)

        for var in modem_model.vars:
            if var.svd_mapping:
                # For registers,
                #       output the value as        "rm.<svd_mapping> = <value>"
                #       output the forced value as "forced.<svd_mapping> = <value_forced>"
                register_name = var.svd_mapping
                #print("var.name = %s" % var.name)

                if var._value_forced is not None:       # gdc:  What's the right way to check this?
                    line = "forced.%s = %s" % (register_name, Human_Readable._py2_str_format(var.value_forced))                 # gdc:  Should print "forced"
                    output_lines.append(line)
                    #print(line)
                    line = "rm.%s = %s" % (register_name, Human_Readable._py2_str_format(var.value_forced))
                    output_lines.append(line)
                    #print(line)
                elif var._value_calc is not None:       # gdc:  What's the right way to check this?
                    line = "rm.%s = %s" % (register_name, Human_Readable._py2_str_format(var.value))
                    output_lines.append(line)
                    #print(line)
            else:
                # for things that aren't registers,
                #       output the actual value as    "actual.<name> = <value>"
                #       output the value as           "calculated.<name> = <value>"
                #       output the forced value as    "config.<name> = <value_forced>
                if var._value_calc is not None:
                    if '_actual' in var.name:
                        line = "actual.%s = %s" % (var.name, Human_Readable._py2_str_format(var.value))
                        #print(line)
                        output_lines.append(line)
                    else:
                        line = "calculated.%s = %s" % (var.name, Human_Readable._py2_str_format(var.value))
                        #print(line)
                        output_lines.append(line)

                if var._value_forced is not None:
                    line = "config.%s = %s" % (var.name, Human_Readable._py2_str_format(var.value_forced))
                    #print(line)
                    output_lines.append(line)

        # Sort the lines and write them to a file
        outputfile = open(outputfilename, 'wb')
        for line in sorted(output_lines):
            outputfile.write('%s\n' % line)
        #outputfile.write('\n')
        outputfile.close()


    #
    # Print a modem_model object to a humanly readable file.
    #
    @staticmethod
    def print_modem_model_values_v2(outputfilename, phy_name, modem_model):

        output_lines = list()

        line = 'info.config_name = ' + str(phy_name)
        #print(line)
        output_lines.append(line)

        profile = modem_model.profile # should only be one profile!

        for input in profile.inputs:
            if input.var_value is not None:
                line = "config.%s = %s" % (input.var_name, Human_Readable._py2_str_format(input.var_value))
                output_lines.append(line)

        for var in modem_model.vars:
            if var._value_forced is not None:
                line = "forced.%s = %s" % (var.name, Human_Readable._py2_str_format(var._value_forced))
                #output_lines.append(line)

        for output in profile.outputs:
            if output.override is not None:
                if (output.output_type is ModelOutputType.SVD_REG_FIELD) or (output.output_type is ModelOutputType.SEQ_REG_FIELD):
                    var = getattr(modem_model.vars, output.var_name)
                    line = "forced.%s = %s" % (var.svd_mapping, Human_Readable._py2_str_format(output.override))
                else:
                    line = "forced.%s = %s" % (output.var_name, Human_Readable._py2_str_format(output.override))
                output_lines.append(line)

            if output.var_value is not None:
                var = getattr(modem_model.vars, output.var_name)
                if (output.output_type is ModelOutputType.SVD_REG_FIELD) or (output.output_type is ModelOutputType.SEQ_REG_FIELD):
                    line = "rm.%s = %s" % (var.svd_mapping, Human_Readable._py2_str_format(output.var_value))
                else:
                    line = "info.%s = %s" % (output.var_name, Human_Readable._py2_str_format(output.var_value, output.var.var_type))
                if len(var._access_write) > 0:
                    tab_column = 80
                    if len(line) >= tab_column:
                        tab_column = len(line) + 1
                    line = line.ljust(tab_column) + "[" + var._access_write[0] + "]"
                output_lines.append(line)

        for var in modem_model.vars:
            if var.svd_mapping is None:
                try:
                    if var._value_calc is not None:
                        if not (hasattr(profile.inputs, var.name) or \
                           hasattr(profile.forces, var.name) or \
                           hasattr(profile.outputs, var.name)):
                            if var.name.endswith(ICalculator.actual_suffix):
                                line = "actual.%s = %s" % (var.name, Human_Readable._py2_str_format(var._value_calc))
                            else:
                                line = "calculated.%s = %s" % (var.name, Human_Readable._py2_str_format(var._value_calc, name=var.name))
                            if len(var._access_write) > 0:
                                tab_column = 80
                                if len(line) >= tab_column:
                                    tab_column = len(line) + 1
                                line = line.ljust(tab_column) + "[" + var._access_write[0] + "]"
                            output_lines.append(line)
                except ModelVariableEmptyValue:
                    pass

        # Sort the lines and write them to a file
        outputfile = open(outputfilename, 'w')
        for line in sorted(output_lines):
            outputfile.write('%s\n' % line)
        outputfile.close()

        # For easier diffing of values only between part families, output same data without [access_write] data to a second file
        outputfile = open(outputfilename.replace('.cfg','.cfg_values_only'), 'w')
        for line in sorted(output_lines):
            if (line.find('[')) > 0:
                idx = (line.find('['))
            else:
                idx = len(line)
            outputfile.write('%s\n' % line[0:idx].strip())
        outputfile.close()

        # For easier diffing of values only between part families, output same data but with _jumbo, _dumbo, etc, remapped to _FAMILY
        outputfile = open(outputfilename.replace('.cfg', '.cfg_scrub_fam'), 'w')
        for line in sorted(output_lines):
            line_scrub_fam = line
            for fam in ["dumbo", "jumbo", "nerio", "nixi", "panther", "lynx", "ocelot", "Dumbo", "Jumbo", "Nerio", "Nixi", "Panther", "Lynx", "Ocelot"]:
                line_scrub_fam = line_scrub_fam.replace("_"+fam,"_FAMILY")
            outputfile.write('%s\n' % line_scrub_fam)
        outputfile.close()

    #
    #
    #
    @staticmethod
    def compare_forced_to_calculated(modem_model):
        output_lines = list()
        for var in modem_model.vars:
            if var._value_forced is not None:       # gdc:  What's the right way to check this?
                if var._value_calc is not None:
                    if var._value_calc == var._value_forced:
                        line = "        %s = %d:  Calculated value matches forced value." % (var.name, var.value_forced)
                        #print(line)
                        output_lines.append(line)

        return output_lines

    @staticmethod
    def _py2_str_format(var_value, var_type=None, name=None):
        # special function catch differences in Python 2 and 3
        # Python 2 rounds floats to 12 significant digits when converting to string, actual values are identical
        value = var_value
        if sys.version_info[0] > 2:
            if type(var_value) == float:
                if var_value != 0.0:
                    try:
                        value = str(round(var_value, 12 - int(floor(log10(abs(var_value)))) - 1))
                    except ValueError:
                        value = var_value
            elif isinstance(var_value, list):
                if var_type == long:
                    # Py3 doesn't add the "L" suffix to long values, since there are no longs, everything is an int
                    value = str(var_value)
                    if 'L' not in value:
                        value = value.replace(',', 'L,')
                        value = value.replace(']', 'L]')
        return value