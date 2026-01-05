# Connecting to a runtime environment

To enable distributed application workflows, configure VS Code to connect to your Teracloud Streams domain.

!!! warning "Running Streams domain required"
    You will need a running Streams domain before you can connect the extension to one. Follow the steps in the [Set up a runtime environment](../gettingstarted/distributed-apps.md#set-up-a-runtime-environment) section if you do not already have one.

!!! note "Note"
    Only one domain can be connected to the extension at a time.

## Configuring VS Code proxy

Streams domains by default have self-signed certificates. In order for the VS Code extension to communicate with domains with self-signed certificates, you need to set `http.proxySupport` to allow self-signed communication.

1. Click [here](vscode://settings/http.proxySupport) to open the setting in VS Code, or navigate to Settings and search for `http.proxySupport`
1. Double-check the scope you want the setting at: `User`, `Remote`, or `Workspace`
1. Change the value to `fallback`

## Connecting to a domain

1. Click the :teracloud-streams: (Streams Explorer) icon in the Activity Bar
1. Click the **Add Domain** button to bring up a series of prompts
1. Enter the REST API URL for the domain

    !!! tip "Tip"
        You can get this value by running `streamtool geturl --api` in your deployed environment.

1. Enter your username
1. Enter your password

After connecting to a Streams domain, you can [administer Streams instances](./administering-instances.md) and [submit distributed applications](./running-distributed.md) if you have a running instance.

## Disconnecting from a domain

1. Click on the :material-account-circle: (Accounts) icon in the lower-left of the Activity Bar
1. Hover over the account with **(Teracloud Streams Domain)**
1. Click **Sign Out**