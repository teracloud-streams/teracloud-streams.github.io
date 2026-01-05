# Administering Streams Instances

Create, manage, and delete Streams instances with the extension.

!!! note "Note"
    All operations are performed in the Streams Explorer view. Click on the :teracloud-streams: icon in the Activity Bar to open the view.

## Managing instance lifecycles

### Creating an instance

1. Click the :octicons-plus-circle-24: (Add Instance) icon in the **Instances** section
1. Provide a name for the instance and configure any other fields in the form
1. Click the **Create Instance** button

### Starting an instance

1. Hover over the name of the stopped instance you want to start
1. Click the :play: (Start Instance) icon

### Stopping an instance

1. Hover over the running instance you want to stop
1. Click the :material-crop-square: (Stop Instance) icon
1. Click **Yes** in the dialog box to confirm operation

### Deleting an instance

1. Hover over the stopped instance you want to delete
1. Click the :material-minus-circle-outline: (Remove Instance) icon
1. Click **Yes** in the dialog box to confirm operation

## Setting an instance as the default

If a Streams domain only has one instance, the extension will automatically mark the instance as the default. If a domain has multiple instances, you must set an instance as the default for operations:

1. Hover over the name of the instance you want to make the default
1. Click the :octicons-check-circle-24: (Set Instance as Default) icon

## Managing environment variables

Applications submitted to an instance may use environment variables to get information or control behavior. You can manage environment variables and their values available to applications in the Streams Explorer view.

!!! danger "Danger"
    Do not store credentials or sensitive connection information in environment variables. Use [application configurations](#managing-application-configurations) instead.

### Create an environment variable

1. Hover over the **Environment Variables** item under the instance you want to modify
1. Click the :octicons-plus-circle-24: (Add Environment Variable) icon
1. Fill in the name and value of the environment variable
1. Click the **Add** button

### Modify an environment variable

1. Hover over the environment variable you want to change
1. Click the :octicons-pencil-24: (Update Environment Variable) icon
1. Update the variable name or value
1. Click the **Update** button

### Remove an environment variable

1. Hover over the environment variable you want to remove
1. Click the :material-minus-circle-outline: (Remove Environment Variable) icon
1. Click **Yes** in the dialog box to confirm operation

## Managing application configurations

[Application configurations](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/creating-secure-app-configs-dev.html) (app configs) are sets of securely stored properties recommended for applications to receive sensitive information. You can manage app configs and their properties available to applications in the Streams Explorer view.

### Create an app config

1. Hover over the **Application Configurations** item under the instance you want to modify
1. Click the :octicons-plus-circle-24: (Add Application Configuration) icon
1. Fill in the name and properties
1. Click the **Add** button

### Modify an app config

1. Hover over the app config you want to change
1. Click the :octicons-pencil-24: (Update Application Configuration) icon
1. Update the name, description, or properties
1. Click the **Update** button

### Remove an app config

1. Hover over the app config you want to remove
1. Click the :material-minus-circle-outline: (Remove Application Configuration) icon
1. Click **Yes** in the dialog box to confirm operation

## Opening Streams Console

While the extension provides a lot of administration workflows, you can open the Streams Console (Web UI) from the Streams Explorer view
for additional workflows:

1. Hover over the instance 
1. Click the :open-dashboard: (Open Streams Console) icon
1. Click **Open** in the dialog box to confirm