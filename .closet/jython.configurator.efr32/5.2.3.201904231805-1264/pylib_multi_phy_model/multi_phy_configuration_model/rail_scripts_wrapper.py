import os

import yaml

from pylib_multi_phy_model.multi_phy_configuration_model import fileType
from rail_scripts.generators.railConfig_sourceCodeGenerator import RAILConfig_generator
from rail_scripts.generators.railTest_rmrCommandGenerator import RailTest_rmrConfigGenerator
from rail_scripts.rail_adapter import RAILAdapter


class RAILScriptsWrapper(object):

    @staticmethod
    def run_rail_scripts(multi_phy_model, generate_debug_yaml=False):
        railAdapter = RAILAdapter(mphyConfig=multi_phy_model, adapter_name=multi_phy_model.rail_adapter_version)
        railAdapter.populateModel()

        # Debug yaml file
        if generate_debug_yaml:
            railModelContext = railAdapter.generateRailModelContext()
            rail_model_out = yaml.dump(railModelContext)
            multi_phy_model.output_files.file.append(fileType("rail_model.yml", rail_model_out))

        generator = RAILConfig_generator(railAdapter)

        rail_config_h = generator.render(generator.template_path_h)
        multi_phy_model.output_files.file.append(fileType("rail_config.h", rail_config_h))

        rail_config_c = generator.render(generator.template_path_c)
        multi_phy_model.output_files.file.append(fileType("rail_config.c", rail_config_c))

        railtest_generator = RailTest_rmrConfigGenerator(railAdapter)
        rail_railtest_commands = railtest_generator.render(railtest_generator.template_path_railtest)
        multi_phy_model.output_files.file.append(fileType("rail_test_commands.txt", rail_railtest_commands))


    @staticmethod
    def dump_output_files(multi_phy_model, output_path):

        if not os.path.exists(output_path):
            os.mkdir(output_path)

        for file in multi_phy_model.output_files.file:
            file_path = os.path.join(output_path, file.name)

            if os.path.exists(file_path):
                os.remove(file_path)

            with open(file_path, 'w') as fc:
                print ("Creating '{}'...".format(file_path))
                fc.write(file.source_code)
                fc.close()
