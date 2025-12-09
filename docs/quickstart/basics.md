# Stream Applications

Learn about stream application concepts, a programming language made for stream applications, and get started developing and running these types of applications.

## Concepts

Review [Development concepts](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/streaming_application_basics.html) to learn about stream applications and
what they're comprised of.

Specifically, learn about:

- [What a stream application is](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/stream_applications.html)
- [Data streams, tuples, their attributes, and types](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/data_streams.html)
- [How windows logically group tuples and how punctuation act as stream control signals](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/windows_and_punctuation.html)
- [What an operator is](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/operators.html), [their different types](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/types_of_operators.html), and [what an operator invocation is](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/streaming_applications.html)

## Streams Processing Language (SPL)

**SPL** is a programming language designed for streaming data and distributed data flow applications. See the [language overview](https://doc.streams.teracloud.com/com.ibm.streams.ref.doc/doc/langoverview.html) to get an introduction to the language.

Applications written in SPL must be compiled using the SPL compiler (which is shipped with Teracloud Streams) before they can be run.

## Set up a development environment

To develop stream applications, you need a Teracloud Streams installation.
An install can be obtained using any of the following methods:

- Quick Start Edition (QSE)
: The **Quick Start Edition** container provides a free, non-production version of Teracloud Streams.
: The system you wish to run the QSE on must have a container runtime. See the [QSE Requirements and Restrictions](https://hub.docker.com/r/teracloudaps/streams-qse#requirements) sections for more information.

- Product installer
: Installs a full installation of **Teracloud Streams** suitable for production and multi-node deployments.
: See the [hardware](https://doc.streams.teracloud.com/com.ibm.streams.install.doc/doc/ibminfospherestreams-hardware-requirements.html) and [software requirements](https://doc.streams.teracloud.com/com.ibm.streams.install.doc/doc/ibminfospherestreams-install-prerequisites.html) for supported systems.

To write applications, you can use Visual Studio Code (VS Code) and the [Teracloud Streams extension](https://marketplace.visualstudio.com/items?itemName=teracloud-aps.teracloud-streams), or use a text editor and command-line interface (CLI).

Choose your preferred installation method and development tool, then follow one of the options below:
=== "All-in-one (QSE + VS Code)"
    !!! abstract ""
        Try out Streams quickly and in a full-featured environment
    
    1. Follow [these instructions](https://github.com/teracloud-streams/devcontainer-templates?tab=readme-ov-file#using-a-template) to get a VS Code window pre-configured and ready for Streams application development.

=== "QSE (VS Code or CLI)"
    !!! abstract ""
        Try out Streams quickly and manually manage the QSE container

    1. Follow the [QSE Getting Started](https://hub.docker.com/r/teracloudaps/streams-qse#getting-started) section to start the container.
    1. Follow the instructions for your development tool:

        === "VS Code"
            1. Install the [VS Code Dev Container extension](https://code.visualstudio.com/docs/devcontainers/containers?originUrl=%2Fdocs%2Fdevcontainers%2Ftutorial#_getting-started)
            1. Open the Command Palette (Click `View -> Command Palette...`)
            1. Type in and select `Attach to Running Container...`
            1. Select the QSE container
            1. Install the [Streams VS Code extension](https://marketplace.visualstudio.com/items?itemName=teracloud-aps.teracloud-streams)
            1. Configure the extension to point to your Streams install
        === "CLI"
            1. Follow the [QSE's Accessing the container](https://hub.docker.com/r/teracloudaps/streams-qse#accessing-the-container-to-run-streamtool) section

=== "Product install (VS Code or CLI)"
    !!! abstract ""
        Install Streams on one or more hosts

    1. [Contact the Streams team](https://streams.teracloud.com/contact) for a product installer.
    1. Follow [Preparing to install Teracloud Streams](https://doc.streams.teracloud.com/com.ibm.streams.install.doc/doc/ibminfospherestreams-preinstall-roadmap.html) to plan and perform the install.
    1. Follow the instructions for your development tool:

        === "VS Code"
            1. Install the [VS Code Remote Development extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
            1. Open the Command Palette (Click `View -> Command Palette...`)
            1. Type in and select `Add New SSH Host...`
            1. Follow the prompt to enter your username and hostname (e.g., `user1@example.com`)
            1. Follow the prompt to choose a config file to save these settings to
            1. In the Command Palette, enter `Connect Current Window to Host...`
            1. Follow the prompt to enter your password
            1. Once you have a VS Code window to your remote machine, install the [Streams VS Code extension](https://marketplace.visualstudio.com/items?itemName=teracloud-aps.teracloud-streams)
            1. Configure the extension to point to your Streams install
        === "CLI"
            1. Access a host with Streams installed via SSH or another method
            1. Set up your environment for Streams:<br/>`source <streams-install>/bin/streamsprofile.sh`

## Write, build, and run your first application

Follow the [HelloWorld SPL tutorial](https://doc.streams.teracloud.com/com.ibm.streams.tutorials.doc/doc/gettingstarted.html) to create and run an application.

!!! tip "QSE users"
    You can skip the first step because the Streams environment is already set up.

!!! note "VS Code users"
    You can compile the SPL application by:

    - Right-clicking and selecting the `Build` action, or
    - Using the `sc` command in a Terminal

    You must use a Terminal to run the application.
    ??? info "Opening a Terminal"
        - Navigate to `Terminal > New Terminal` in the menu bar
        - Enter ++ctrl+shift+grave++ (Windows/Linux) or ++cmd+shift+grave++ (macOS).
