# BFS (Build-From-Source) Package (Manage)r

## Information
```
Package Manager focused on "Build From Source" installations and emphasis on security, efficiency, portability, customizability and modularity as well as extensibility for users and developers alike

Plans include
- Support for multi-sourced dependency management, such as installing dependencies from selected Package Managers and/or self-handling
- External Configuration File specification : Explicitly specify a configuration file of choice to import
- Multiple configuration file Data Serializable object type support : Explicitly specify the data serialization file type; i.e. JSON support
```

## Setup
### Dependencies
+ python
- python pypi packages
    + ruamel.yaml : For YAML configuration file handling

### Pre-Requisites
- (Optional; Recommended) Setup python Virtual Environment
    - Install dependencies
        + venv/virtualenv
    - Generate virtual environment
        ```console
        python -m venv [virtual-environment]
        ```
    - Chroot/Source the virtual environment
        - *NIX
            ```console
            . [virtual-environment]/bin/activate
            ```
        - Windows
            ```console
            [virtual-environment]\Scripts\activate
            ```

- Install dependencies
    - From requirements.txt
        ```console
        python -m pip install -Ur requirements.txt
        ```

### Compiling into an executable
> Still undergoing tests
- Using PyInstaller
    - Pre-Requisites
        - Dependencies
            - Python package
                + pyinstaller
    - Compile/Build the executable
        - Parameters
            + --onefile : Generate a single executable file with everything bundled inside
        - Notes
            - Output: 
                + dist: The executable will be placed here
        - Syntax
            ```console
            {python -m} pyinstaller --onefile [main-driver-file]
            ```
        - Usage
            ```console
            {python -m} pyinstaller --onefile main.py
            ```

## Documentation
### Synopsis/Syntax
- Basic Run
    ```console
    python main.py {options} <arguments> [positionals]
    ```

### Parameters
- Positionals
    - download  : Download configuration file from a specified package from a specified remote repository server; WIP
    - clone     : Clone the repository from the specified remote repository server source; WIP
    - build     : Build the source code; WIP
    - install   : Install the built files and directories from project source code to system; WIP
    - uninstall : Uninstall the installed files from the system; WIP
- Optionals
    - With Arguments
        - `-c   | --config [config-file-name]` : Explicitly specify configuration file path and name to import
        - `-d   | --destination [destination-directory]` : Explicitly specify a target destination directory containing the install
        - `-ct  | --config-file-type [type]`   : Explicitly specify data serialization object file type; Required if parsing in with JSON or TOML as default is YAML
        - `-o   | --build-options [build-options,...]` : Explicitly specify additional build options; Separate all build options with a ',' delimiter
        - `-p   | --package [package-name]` : Explicitly specify a name of a package/project
        - `-ps  | --project-source [project-git-remote-repository-url]` : Explicitly specify the Git Remote Repository server URL containing the target's project source code to clone from
        - `-rs  | --remote-repository-server [server-domain]` : Explicitly specify the remote repository server  containing the package's config.yaml; i.e. GitHub
        - `-ru  | --remote-repository-url [server-url]` : Explicitly specify the remote repository server's URL containing the package's config.yaml; i.e. https://github.com
    - Flags
        + -h | --help    : Display help message and detailed instructions
        + -v | --version : Display system version

### Usage

### Developers
#### Dependencies and Importing
TBC

## Wiki
### Project Structure
```
project-root/
    |
    |-- app/ : Main application folder
        |-- src/ : For all project-related files
            |
            |-- lib/ : For all external/general libraries that are not application-specific
            |-- main.py  : The main runner/launcher project code
            |-- setup.py : Root setup file for the main runner/launcher
            |-- unittest.py : WIP Unit Testing source file
```

### TODO
### Features
- [ ] CLI Terminal support
- [X] Read from YAML config file
- [X] Import YAML configurations
+ [ ] Import configuration file via JSON
+ [ ] Import configuration file JSON strings via Pipes
+ [ ] Import configuration file JSON strings via Pipes through the network using CURL
- [ ] Support build and package management functionalities using the package's configurations
    - [ ] Download a specified package's YAML config file from a specified remote repository server
    - [ ] Install dependencies
    - [ ] Clone the repository
    - [ ] Build from source
    - [ ] Install to system
    - [ ] Uninstall from system
    - [ ] Clean-up source
    - [ ] Backup source file

### Quality of Life
+ [ ] Support for multi-sourced dependency management, such as installing dependencies from selected Package Managers and/or self-handling
+ [ ] External Configuration File specification : Explicitly specify a configuration file of choice to import
+ [ ] Multiple configuration file Data Serializable object type support : Explicitly specify the data serialization file type; i.e. JSON support

