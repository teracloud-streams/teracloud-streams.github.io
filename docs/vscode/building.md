# Building applications

Build SPL applications using the extension with or without configuring compile options. Build configurations are automatically saved to `.vscode/.streams.json` for future builds.

Before building, choose whether to use the saved build configuration or specify a new one. If no configuration is provided on first build, default settings are used.

!!! warning "Ensure toolkit paths are configured"
    Builds will fail if your application uses toolkits the extension is not aware of. You can [configure toolkit paths](../vscode/configuring-paths.md) to inform the extension of used toolkits.

!!! warning "Compile-time parameters"
    Applications containing [compile-time parameters](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/compileargs.html) require at least one build with custom parameters to set initial values. Otherwise, the build will fail.

## Building with saved config

To build an SPL application using the previous build configuration (or defaults on first build):

=== "Context Menu"
    1. In File Explorer, right-click the SPL file containing your application
    1. Select **Build**
=== "Streams Development view"
    1. Open the SPL file containing your application
    1. Click the :teracloud-streams-dev: (Streams Development) icon in the Activity Bar
    1. Click the :symbol-property: (Build) icon

## Building with custom parameters

To configure compilation settings, build with parameters:

=== "Context Menu"
    1. In File Explorer, right-click the SPL file containing your application
    1. Click **Build with Parameters**
    1. Complete the wizard form
    1. Click the **Build Application** button
=== "Streams Development view"
    1. Open the SPL file containing your application
    1. Click the :teracloud-streams-dev: (Streams Development) icon in the Activity Bar
    1. Click the :symbol-tools: (Build with Parameters) icon
    1. Complete the wizard form
    1. Click the **Build Application** button

## Viewing build output

1. Enter ++ctrl+shift+u++ (Windows/Linux) or ++cmd+shift+u++ (macOS) to open the OUTPUT panel.
1. From the channel dropdown, select **Teracloud Streams | SPL**.

## Viewing build configurations

The Streams Development view displays the saved build configuration for your application.

1. Open the SPL file containing your application
1. Click the :teracloud-streams-dev: (Streams Development) icon in the Activity Bar

The configuration will be under the **Main Composites** section.

## Cleaning build artifacts

Remove build artifacts by running a clean operation:

=== "Context Menu"
    1. In File Explorer, right-click the SPL file containing your application
    1. Click **Clean Build Artifacts**
=== "Streams Development view"
    1. Open the SPL file containing your application
    1. Click the :teracloud-streams-dev: (Streams Development) icon in the Activity Bar
    1. Click the :octicons-trash-24: (Clean build artifacts) icon

## Next steps

Once an application is built, you can [run it in standalone mode](./running-standalone.md) or [submit it to a runtime environment](./running-distributed.md).