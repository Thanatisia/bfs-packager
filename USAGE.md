# Quickstart Usage Reference Guide

## Steps
### Usage
- Research
    - Planning
        - What package to install
- Design
    - Generate a configuration template from the CLI
        + This configuration file will be the "recipe" of the package's build structure
        - Default
            + System will generate a default config file 'config.yaml'
            ```console
            sudo python main.py -g
            ```
        - Custom configuration file name
            ```console
            sudo python main.py -c [new-config-file-name] -g
            ```
    - Update the configuration file with your requirements
        + Please refer to [Configuration](#configuration) for more information on the configuration documentation and template structure
- Running
    - Much like more package manager, running is quite straightforward
        - Basic Syntax Structure is as such
            ```console
            python main.py {options} <arguments> [commands]
            ```
        - You can even append the commands back to back to execute them consecutively
    - Commands
        - build: This will build/make/compile according to the steps specified in the package recipe/configuration
        - clone : This will clone the specified package from the specified remote git repository server containing the package source code
        - download : This will download a specified package's recipe file from a target remote repository server containing the recipe
        - setup : This will perform pre-requisite system checks and setup the host for development
        - install: This will install the built files from the source code local repository to the installation directory
        - uninstall: This will uninstall/remove the built files from the installation directory
    - Usage Examples
        - Single Steps
            - To setup the host only
                + This will setup the host and prepare for cloning and development as accordance to the instructions specified
                ```console
                python main.py -c [source-directory]/config.yaml setup
                ```
            - To clone a package only
                + This will clone the package source code from the remote git repository server to your local system according to the steps
                ```console
                python main.py -c [source-directory]/config.yaml clone
                ```
            - To download a recipe only
                + This will download a recipe configuration file from a specified remote repository server containing the recipe
                ```console
                python main.py -c [source-directory]/config.yaml download
                ```
            - To build a package only
                + This will build the package in the source code directly according to the steps
                + Note that this will not clone for you as you only specified to build
                ```console
                python main.py -c [source-directory]/config.yaml build
                ```
            - To install a package only
                + This will enter into the source code repository and install the built files into system according to the steps specified in the recipe
                - Note that this will **not** build the package in the source code directly according to the steps
                    + Thus, please ensure that you have built the package before performing this action, and/or specify the build step before this keyword
                ```console
                python main.py -c [source-directory]/config.yaml install
                ```
            - To uninstall a package only
                - This will uninstall and remove the built files from the system according to the steps specified in the recipe
                    - If steps are not specified
                        + The program will check for the binaries in the system and remove them
                        - If the location of the manuals, files and executables are specifies
                            + The program will skip the check and delete those directly
                ```console
                python main.py -c [source-directory]/config.yaml uninstall
                ```
        - Consecutive Steps
            - To clone and build
                + This will clone AND build the package in the source code directly according to the steps of both actions
                ```console
                python main.py -c [source-directory]/config.yaml clone build
                ```
            - To clone, build and install
                + This will clone AND build the package in the source code directly according to the steps of both actions
                + Afterwhich, this will enter into the source code repository and install the built files into system according to the steps specified in the recipe
                ```console
                python main.py -c [source-directory]/config.yaml clone build install
                ```
            - Full Sequence
                - Steps
                    - Pre-Requisites
                        1. This will setup the host and perform pre-requisites as required
                    - Initial Build/Make/Compilation
                        2. This will then clone the repository from the remote git repository server to the local host repository 
                        3. The system will then change directory into the package and build the package in the source code directly according to the steps of both actions
                    - System Installation
                        4. The system will then install the built files specfied in the recipe from the local repository after building to the system
                ```console
                python main.py -c [source-directory]/config.yaml setup clone build install
                ```

## Configuration
### Template
#### Components
- Key-Values
    - specifications: This contains a dictionary/key-value mappings of the configurations and specifications for the target package/project
        - Format:
            ```yaml
            specifications:
                [keywords]:
                    [values]
            ```
        - environment: Specify all environment variables here
            - Format
                - As a List
                    ```yaml
                    specifications:
                        environment:
                            ## Environment Variables here
                            - ENV_VAR=VALUE
                    ```
                - As a Dictionary
                    ```yaml
                    specifications:
                        environment:
                            ## Environment Variables here
                            ENV_VAR: VALUE
                    ```

        - platform: Specify the specifications and details of the target system platform/architecture this recipe is designed for
            - Format
                ```yaml
                specifications:
                    platform:
                        ## System Platform Information here
                        architecture: [cpu-architecture (i.e. x86_64)]
                        system: [operating-system (i.e. linux, windows, macos)]
                        distribution: [variants of the operating system (i.e. linux => debian, arch etc, windows => windows-10, macos => mojave)]
                ```
            - architecture: This specifies the cpu-architecture that the recipe is designed for (i.e. build process, installation host system architecture)
                - Possible Values
                    + x86_64
            - system: This specifies the core operating system that the package is designed to be built for 
                - Possible Values
                    - linux
                    - windows
                    - macos
            - distribution: This specifies the variants of the operating system 
                - i.e. 
                    + linux => debian, arch etc
                    + windows => windows-10
                    + macos => mojave

        - compiler: Specify details and information relating to the compiler (to be) used; If you are compiling
            - Format
                ```yaml
                ## Compiler information here
                CC: "your-cross-compiler-executable-here (i.e. make, ninja, ...)"
                CFLAGS:
                  ## Compile Flags
                  - flag
                  - here
                ```
            - CC: Stands for 'Cross-Compiler'; Specify the cross compiler executable that you will be using; This is used commonly in build systems like Makefile
                + Input Type: String
                - Possible Values
                    + make
                    + ninja
            - CFLAGS: Stands for 'Compiler Flags'; Specify a list of all flags you wish to parse into the compiler on compile-time
                + Input Type: List

        - runner: Specify details and information relating to the runner that is (to be) used; If you are running the binary/application/script
            - Format
                ```yaml
                ## Runner information here
                exec: "your-runner-executable-here (i.e. python)"
                flags:
                  ## Executable Flags
                  - flag
                  - here
                ```
            - exec : The runner executable file/binary used to run
                + Input Type: String
                - Possible Values
                    + python : For Python
                    + go run : For Golang
            - flags : List of all flags you wish to parse into the runner on boot-time
                + Input Type: List

        - package: Specification and details relating to the target package such as dependencies, pre-requisites and contents it will create
            - Format
                ```yaml
                specifications:
                    package:
                        author: "package/repository-author"
                        name: "package/repository-name"
                        remote:
                          server: github
                          source: "https://github.com/[repository-author]/[repository-name]"
                        dependencies: 
                          package-manager: "your-dependency-package-manager (possible values: apt, pacman, xbps, none => not download dependencies; download manually)
                          packages:
                            - your
                            - packages
                            - here
                        contents:
                            ## Contains the built contents, such as 
                            ## - Executables/Binaries
                            ## - Files
                            ## - Manuals
                            ## - Documentations
                            ## - Resources
                            ## - etc etc
                            bin:
                              ## Binaries
                              - your
                              - binaries
                              - and
                              - executables
                              - here
                            locations:
                              ## Specify Installation paths here
                              executables: ${PREFIX}/bin
                              manuals: /usr/man/man.1/
                              documentations: ${PREFIX}/share/doc/[package-name]
                ```
            - author: The author of the package/repository
            - name  : The name of the package/repository
            - remote : Contains a key-value (Dictionary) mapping of details about the remote repository server containing the target repository
                - server: Specifies the name of the remote repository server domain containing the target repository
                    - Possible Values
                        - Supported
                            + github
                        - WIP
                            + gitlab
                            + gitea
                            + codeberg
                            + bitbucket
                - source: Specifies the URL of the remote git repository server containing the target repository
            - dependencies : Contains a key-value (Dictionary) mapping of details about the dependency management for this recipe
                - package-manager : Contains the package manager you wish to use to install the dependencies
                    - Package Manager Options and Possible Values
                        + apt
                        + pacman
                        + xbps
                        + none : Will not download dependencies; To download manually
                - packages : Contains the list of dependencies (packages) required by the repository
            - contents : Contains key-value (Dictionary) mappings of details and information about the main contents from the target project
                - Content types includes
                    + Executables/Binaries
                    + Files
                    + Manuals
                    + Documentations
                    + Resources
                    + etc etc
                - bin: Contains a list of all binaries that will be output by the project
                - locations: Contains key-value (Dicitonary) mappings of the $PREFIX (Installation) locations/paths by each category
                    - executables: Files that can be executed; Binaries, Shellscripts, applications, object files etc
                        - Example Locations:
                            + ${PREFIX}/bin
                    - manuals: Typically referring to the manuals .tar.gz files used by the 'man' command; This can also be documentation files used for cross-platform compatibility
                        - Recommended: 
                            + /usr/man/man.1/
                    - documentations: Documentations files can be help commands and or other resources provided by the maintainers/developers of the project
                        - Recommended: 
                            + ${PREFIX}/share/doc/[package-name]
                    - resources: other resources provided by the maintainers/developers of the project for usage
                        - Recommended: 
                            + ${PREFIX}/share/resources/[package-name]
        - instructions: Contains key-value (Dictionary) mappings of instructions specified by the maintainer/developer of the project to perform the mapped actions (aka 'sections', named for readability)
            - Format
                ```yaml
                specifications:
                  instructions:
                    setup:
                      [section-label]:
                        ## New section/entry
                        steps:
                            - new_line
                            - new_line
                            - new_line
                            - new_line
                            - ...

                    download:
                      [section-label]:
                        ## New section/entry
                        steps:
                            - new_line
                            - new_line
                            - new_line
                            - new_line
                            - ...

                    clone:
                      [section-label]:
                        ## New section/entry
                        steps:
                            - new_line
                            - new_line
                            - new_line
                            - new_line
                            - ...

                    build:
                      [section-label]:
                        ## New section/entry
                        steps:
                            - new_line
                            - new_line
                            - new_line
                            - new_line
                            - ...

                    install:
                      [section-label]:
                        ## New section/entry
                        steps:
                            - new_line
                            - new_line
                            - new_line
                            - new_line
                            - ...

                    uninstall:
                      [section-label]:
                        ## New section/entry
                        steps:
                            - new_line
                            - new_line
                            - new_line
                            - new_line
                            - ...
                ```
            - action-target: This specifies the name/target of the action to be mapped in this instruction set entry; Accepted values includes: [setup, download, clone, build, install, uninstall]; Each target has to be the specified values only because they determine the target's actions
                - section-label: Each section label acts as a new instruction entry for the target action; Every section is effectively a new "name" assigned to the action for tracking
                    - steps: List of all commands to be ran per line; Each step is effectively a new code line to be executed by the application

#### Template Structure
- JSON
    + WIP
- YAML
    ```yaml
    specifications:
      environment:
        ## Environment Variables here
        - PREFIX=/usr/local/

      platform:
        ## System Platform Information here
        architecture: [cpu-architecture (i.e. x86_64)]
        system: [operating-system (i.e. linux, windows, macos)]
        distribution: [variants of the operating system (i.e. linux => debian, arch etc, windows => windows-10, macos => mojave)]

      compiler:
        ## Compiler information here
        CC: "your-cross-compiler-executable-here (i.e. make, ninja, ...)"
        CFLAGS:
          ## Compile Flags
          - flag
          - here

      runner:
        ## Runner information here
        exec: "your-runner-executable-here (i.e. python)"
        flags:
          ## Executable Flags
          - flag
          - here

      package:
        author: "package/repository-author"
        name: "package/repository-name"
        remote:
          server: github
          source: "https://github.com/[repository-author]/[repository-name]"
        dependencies: 
          package-manager: "your-dependency-package-manager (possible values: apt, pacman, xbps, none => not download dependencies; download manually)
          packages:
            - your
            - packages
            - here
        contents:
            ## Contains the built contents, such as 
            ## - Executables/Binaries
            ## - Files
            ## - Manuals
            ## - Documentations
            ## - Resources
            ## - etc etc
            bin:
              ## Binaries
              - your
              - binaries
              - and
              - executables
              - here
            locations:
              ## Specify Installation paths here
              executables: ${PREFIX}/bin
              manuals: /usr/man/man.1/
              documentations: ${PREFIX}/share/doc/[package-name]

      instructions:
        setup:
          [section-label]:
            ## New section/entry
            steps:

        download:
          [section-label]:
            ## New section/entry
            steps:

        clone:
          [section-label]:
            ## New section/entry
            steps:

        build:
          [section-label]:
            ## New section/entry
            steps:

        install:
          [section-label]:
            ## New section/entry
            steps:

        uninstall:
          [section-label]:
            ## New section/entry
            steps:
    ```

### For Developers


