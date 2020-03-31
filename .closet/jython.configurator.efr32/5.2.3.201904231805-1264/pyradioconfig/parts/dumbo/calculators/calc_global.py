from pyradioconfig.parts.common.calculators.calc_global import CALC_Global
from pycalcmodel.core.variable import ModelVariableFormat, CreateModelVariableEnum
from enum import Enum

class CALC_Global_dumbo(CALC_Global):

    def buildAdditionalVariables(self, model):
	    # Chip Identifier
	    self._addModelVariable(model, 'family',                           str,   ModelVariableFormat.ASCII)
	
    def calc_family_name(self, model):
        model.vars.family.value = "dumbo"

    # Example override
    #def calc_global_hello_world(self, model):
    #    print("HELLO from Dumbo Calculator!")