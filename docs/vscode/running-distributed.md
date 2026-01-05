# Running distributed applications

Submit applications to a runtime environment for distributed execution across multiple hosts, then monitor and manage them all within VS Code. This mode is ideal for deploying in a test or staging environment.

!!! warning "Running Streams instance required"
    You will need a running Streams instance before you can submit distributed applications. See [Managing instance lifecycle](./administering-instances.md#managing-instance-lifecycles) on how to create and start one if needed.

## Submitting an application

There are several ways to submit an application to a Streams instance:

=== "Using the SPL file"
    1. In File Explorer, right-click the SPL file containing your application
    1. Click **Build and Submit**
    1. Configure any submission options in the form
    1. Click the **Submit Job** button
=== "Using the SAB file"
    1. In File Explorer, right-click the SAB file created after building your application
    1. Click **Submit Job**
    1. Configure any submission options in the form
    1. Click the **Submit Job** button
=== "Streams Explorer view"
    1. Click on the :teracloud-streams: (Streams Explorer) icon in the Activity Bar
    1. Hover over the name of the instance you want to submit the app to
    1. Click the :timer--add: (Submit Job) icon
    1. Configure any submission options in the form
    1. Click the **Submit Job** button
=== "Streams Development view"
    1. Open the SPL file containing your application
    1. Click the :teracloud-streams-dev: (Streams Development) icon in the Activity Bar
    1. Click the :material-cloud-upload: (Submit) icon
    1. Configure any submission options in the form
    1. Click the **Submit Job** button

Once a job is running, you can view its graph, inspect logs, or cancel it.

## Viewing the job graph

Running jobs can be viewed as a directed graph in the Streams Console:

1. In the :teracloud-streams: (Streams Explorer) view, navigate to the instance containing the job
1. Hover over the job you want to view the runtime graph of
1. Click the :job-graph: (Show Job Graph) icon
1. Click **Open** in the dialog box to confirm

## Viewing job logs

View PE and job logs directly in VS Code via the Streams Log Watcher panel:

1. Enter ++ctrl+shift+u++ (Windows/Linux) or ++cmd+shift+u++ (macOS) to open the OUTPUT panel
1. Click the **STREAMS LOG WATCHER** tab

You can then select which PE, job, or log channel to view.

<picture>
  <img src="../../assets/vscode-streams-log-watcher.png"
       alt="Screenshot showing Streams Log Watcher tab selected in bottom VS Code panel"
       style="max-width: 100%; height: auto;">
</picture>

## Downloading job logs

1. In the :teracloud-streams: (Streams Explorer) view, navigate to the instance containing the job
1. Hover over the job you want to download logs for
1. Click the :document--download: (Download Job Logs) icon
1. Enter the file to save the logs to
1. Click the **OK** button

## Canceling a job

1. In the :teracloud-streams: (Streams Explorer) view, navigate to the instance containing the job
1. Hover over the job you wish to cancel
1. Click the :material-trash-can-outline: (Cancel Job) icon
1. Click **Yes** in the dialog box to confirm