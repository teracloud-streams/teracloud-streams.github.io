# Running applications in standalone mode

Run applications without a runtime environment by running them in standalone mode. This mode is ideal for testing and debugging applications.

!!! warning "Application Eligibility"
    Not all applications can be run in standalone mode. If operators require different runtime options (like JVM options) or require
    location restrictions, then an application may fail to run. See [other standalone limitations](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/runningrelocatableapplications.html) in the product documentation.

## Launching an application

Start a standalone app in the Streams Development view:

1. Open the SPL file containing your application
1. Click the :teracloud-streams-dev: icon in the Activity Bar
1. Click the :play: icon

The extension will open a new Terminal and invoke a command to start the application.

## Terminating an application

Stop a standalone application (if it doesn't self-terminate):

* Click in the terminal, then enter ++ctrl+c++
* In the terminal list, hover over the terminal (prefixed with `Standalone`) and click the :octicons-trash-24: icon