"""
Collection of classes
"""
## Built-in Functions
import os
import sys

## External Functions
from lib.configs import Configuration, YAMLConfig

class AppConfig():
    """
    Configurations class
    """
    def __init__(self, yaml_cfg_filename="config.yaml"):
        """
        Class Constructor

        - Performs the actions when the class is created
        """
        self.yaml = YAMLConfig(yaml_cfg_filename)
        self.cfg_filename = yaml_cfg_filename
        self.config_Contents = None
        self.keys = [
            ## Build File keywords
            "platform",
            "compiler",
            "package",
            "build"
        ]

    def __exit__(self):
        """
        Class Destructor

        - Performs the actions when the class is destroyed after usage and completion of instructions
        - Required to use the word 'with'
        """

    def check_config_exists(self):
        """
        Check if configuration file exists
        """
        is_exist = os.path.isfile(self.cfg_filename)
        return is_exist

    def set_configuration_Contents(self, config_Contents):
        """
        Set Configuration File Contents
        """
        self.config_Contents = config_Contents

    def get_key_Value(self, base_key, *keywords):
        """
        Get the value of the configuration file key-values based on keywords provided; Takes in variable length number of keywords

        :: Params
        - keywords : List of all keywords to print out
        """
        cfg = self.config_Contents
        res = {}

        # Check if any contents
        if cfg != None:
            # Loop through all keywords
            for key in keywords:
                # Get corresponding value

                # Check if key is in configuration file
                if (base_key in cfg) or (key in cfg):
                    # Key is in configuration file
                    # Check if base key is empty
                    if base_key == "":
                        # Get Value
                        v = cfg[key]

                        # Map result
                        res[key] = v
                    else:
                        # Get Value
                        v = cfg[base_key][key]

                        # Check if key in dictionary
                        if base_key not in res:
                            # Initialize Key
                            res[base_key] = {}
                        
                        # Map result
                        res[base_key][key] = v
                else:
                    print("Key {} is not in configuration file".format(key))

                    # Map key to None
                    res[key] = None

        return res

    def print_yaml_details(self):
        print("Current File Name: {}".format(self.yaml.file_name))
        print("Current File Mode: {}".format(self.yaml.mode))

    def print_yaml_Pretty(self):
        """
        Pretty print configuration file dictionary
        """
        cfg = self.config_Contents

        # Check if any contents
        if cfg != None:
            for k,v in cfg.items():
                print("{} => {}".format(k,v))

    def print_yaml_key_Pretty(self, base_key, *keywords):
        """
        Pretty print configuration file key-values based on keywords provided; Takes in variable length number of keywords

        :: Params
        - keywords : List of all keywords to print out
        """
        cfg = self.config_Contents

        # Check if any contents
        if cfg != None:
            # Loop through all keywords
            for key in keywords:
                # Get corresponding value
                v = cfg[base_key][key]

                # Print value
                print("{} => {}".format(key, v))


