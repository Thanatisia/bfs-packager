"""
BFS (Build From Source) Package Manager

Main driver file
"""
## Built-in Functions
import os
import sys

## Classes
from lib.classes import AppConfig

class App():
    """
    Application class
    """
    def __init__(self, yaml_cfg_filename="config.yaml"):
        """
        Class Constructor

        - Performs the actions when the class is created
        """
        # Initialize Classes
        self.config = AppConfig(yaml_cfg_filename)
        self.yaml = self.config.yaml

    def __enter__(self):
        """
        Class Entrance

        - Performs the actions when the class is entered using a with keyword
        """

    def __exit__(self):
        """
        Class Destructor

        - Performs the actions when the class is destroyed after usage and completion of instructions
        - Required to use the word 'with'
        """

    def config_Import(self):
        """
        Import Configuration Files
        """
        # Check if configuration file exists
        cfg_file_Exists = self.config.check_config_exists()
        if cfg_file_Exists:
            # Configuration file exists

            # Open File
            self.yaml.open_file()

            # Read config file and import
            config_Contents = self.yaml.read_config()

            # Close file after use
            self.yaml.close_file()

            # Set contents into class
            self.config.set_configuration_Contents(config_Contents)
        else:
            # Configuration file does not exists
            print("Configuration file [{}] does not exists.".format(self.config.cfg_filename))

            # Exit
            exit(1)

    def test_print(self):
        # Print configurations file
        self.config.print_yaml_details()

        print("")

        # Pretty print
        self.config.print_yaml_Pretty()
        
        print("")

        # Print keys
        self.config.print_yaml_key_Pretty("specifications", *self.config.keys)

    def run(self):
        """
        Main application driver function
        """

def setup():
    global app, config, yaml

    # Initialize Classes
    app = App()

    # Initialize Variables
    config = app.config
    yaml = config.yaml

def main():
    # Perform initial setup
    app.config_Import()

    # Begin application
    app.run()

if __name__ == "__main__":
    setup()
    main()


