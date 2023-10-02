"""
BFS (Build From Source) Package Manager

Main driver file
"""
## Built-in Functions
import os
import sys

## Classes
from lib.cli import CLIParser
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

    def body(self):
        """
        Begin CLI argument processing
        """
        ## Switch-case CLI optionals
        for k,v in optionals.items():
            # Get keyword and value
            curr_opt = k
            curr_opt_val = v

            # Process and check
            if (curr_opt == "help"):
                if (curr_opt_val == True):
                    display_help()
                    display_Options()
                    exit(1)
            elif (curr_opt == "display-options"):
                if (curr_opt_val == True):
                    display_Options()
                    exit(1)
            elif (curr_opt == "generate-config"):
                if (curr_opt_val == True):
                    # Get the new custom configuration file name (if any)
                    cfg_name = cliparser.configurations["optionals"]["CUSTOM_CONFIGURATION_FILENAME"]
                    setup.generate_config(cfg_name)
                    exit(1)
            elif (curr_opt == "print-config"):
                if (curr_opt_val == True):
                    # Get the new custom configuration file name (if any)
                    cfg_name = cliparser.configurations["optionals"]["CUSTOM_CONFIGURATION_FILENAME"]

                    # Import configuration file, load it and print
                    setup.cfg = setup.load_config(cfg_name)

                    # Print out configuration dictionary object
                    for k,v in setup.cfg.items():
                        print("{} : {}".format(k,v))
                    exit(1)
            elif (curr_opt == "MODE"):
                if (curr_opt_val != None):
                    # Get the new mode (if any)
                    new_mode = cliparser.configurations["optionals"]["MODE"]

                    # Set the new mode into the Environment Variable class variable
                    setup.env.MODE = new_mode

        ## Switch-case CLI positionals
        for i in range(len(positionals)):
            curr_pos = positionals[i]
            if (curr_pos == "build"):
                """
                Start the Building/Make/Compilation
                """
                # Initialize and perform pre-processing and pre-startup checks
                init_check()

                print("")
                print("(+) Beginning Compilation...")
                print("")
            elif (curr_pos == "clone"):
                """
                Start cloning the project
                """
                print("")
                print("(+) Beginning project clone...")
                print("")
            elif (curr_pos == "download"):
                """
                Start downloading a package's configuration file (config.yaml)
                """
                print("")
                print("(+) Downloading package configuration file...")
                print("")
            elif (curr_pos == "install"):
                """
                Start installing the package from source to the system
                """
                print("")
                print("(+) Beginning package installation...")
                print("")
            elif (curr_pos == "uninstall"):
                """
                Start uninstalling the package from the system
                """
                print("")
                print("(+) Beginning package uninstallation...")
                print("")

    def run(self):
        """
        Main application driver function
        """
        self.body()

def setup():
    global app, config, yaml, optionals, positionals

    # Initialize Classes
    app = App()
    cliparser = CLIParser()

    # Initialize Variables
    config = app.config
    yaml = config.yaml
    optionals = cliparser.optionals
    positionals = cliparser.positionals

def main():
    # Perform initial setup
    app.config_Import()

    # Begin application
    app.run()

if __name__ == "__main__":
    setup()
    main()


