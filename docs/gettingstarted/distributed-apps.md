# Distributed applications

Learn about distributed applications, the runtime platform offered by Teracloud Streams, get a runtime environment started, and walk through the distributed application lifecycle.

## Concepts

In [Stream application basics](basics.md#write-build-and-run-your-first-application), a simple HelloWorld application was built and run as a binary program.
Running the application this way is called **Standalone** because it runs on a single host and doesn't require a runtime environment.

An application can also be run in **Distributed** mode. Distributed applications enable logic to run across one or more hosts, but require a runtime environment to orchestrate the applications and hosts. This approach is beneficial for several reasons:

* Distributes workload
* Enables operators to be scheduled to specific resources
* Monitors health and metrics
* Automatically recovers from app or host failures

### Jobs

When you submit a stream application to the runtime environment, it creates a **Job** which represents your running, distributed application.

!!! info
    Jobs can process continuous streams of data, so they run until you cancel them.

To efficiently distribute processing across available resources, the runtime environment divides a job into one or more **Processing Elements (PEs)**. Each PE is a Linux process that executes one or more operators from your application and communicates data streams to other PEs as necessary.

For more details, see [Running applications](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/runningrelocatableapplications.html) and [Runtime environment overview](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/infosphere_streams_environment.html) in the product documentation.

## Teracloud Streams runtime platform
Teracloud Streams offers a distributed runtime platform to perform host and application orchestration. The runtime platform exposes [APIs and a web UI](https://doc.streams.teracloud.com/com.ibm.streams.welcome.doc/doc/interfaces.html) to assist in platform and application monitoring and management.

Stream's runtime platform is comprised of a **[Domain](https://doc.streams.teracloud.com/com.ibm.streams.welcome.doc/doc/domains.html "A logical group of hosts with a user authentication context")** and one or more **[Instances](https://doc.streams.teracloud.com/com.ibm.streams.welcome.doc/doc/ibminfospherestreams-introduction-instances.html "A runtime environment")**.

To run a distributed application, you need an active Teracloud Streams instance.

## Set up a runtime environment

### Create and start an instance
!!! tip
    If you're using the QSE container, continue to [Configure VS Code](#configure-vs-code). The QSE container automatically creates and starts an instance for you.

For product installs, a Streams instance can be created on a single node or across multiple nodes.

=== "Single-node instance"
    See [Creating a basic domain and instance](https://doc.streams.teracloud.com/com.ibm.streams.cfg.doc/doc/creating-basic-domain-and-instance.html) in the product documentation for instructions to set up a basic, single-node instance.

=== "Multi-node instance"

    To create an enterprise instance across multiple nodes, complete the following steps:

    1. Review [Setting up an enterprise domain on multiple resources](https://doc.streams.teracloud.com/com.ibm.streams.cfg.doc/doc/setting-up-enterprise-domain.html).  
    2. Set up an external ZooKeeper server or cluster.  
    3. [Create a domain](https://doc.streams.teracloud.com/com.ibm.streams.cfg.doc/doc/creating-enterprise-domain-streamtool.html).  
    4. [Add resources to the domain](https://doc.streams.teracloud.com/com.ibm.streams.cfg.doc/doc/setting-up-resources.html).  
    5. [Create and start an instance in the enterprise domain](https://doc.streams.teracloud.com/com.ibm.streams.cfg.doc/doc/creating-enterprise-instance.html).   

### Configure VS Code
!!! tip
    If you're not using VS Code, continue to the next section.

To create a job through VS Code, you must configure it to point to your instance:

1. Determine your REST API URL
    - For QSE environments, use `https://localhost:9714/streams/resources`
    - For product install environments, use the output of `streamtool geturl --api`
1. Click the :teracloud-streams: (Streams Explorer) icon in the Activity Bar
1. Click the `Add Domain` button
1. Enter the REST API URL
1. Enter your username
1. Enter your password

## Create a job by submitting an application 

When you compile an SPL application, the compiler creates a standalone binary program as well as a **Streams Application Bundle (SAB)** under the `output/` directory. This bundle can be submitted to a Streams instance to create a job.

For this tutorial, we'll use the SAB compiled from the HelloWorld application in [Stream application basics](basics.md#write-build-and-run-your-first-application).

Use your favorite interface to submit the SAB to your runtime environment:
=== "VS Code"

    1. Navigate to SAB file under `output/` in the File Explorer 
    1. Right-click on the SAB file
    1. Select `Submit Job` to bring up the submission wizard
    1. Scroll the bottom of the form and click the 'Submit Job' button

    The job will appear in the list of jobs under your instance.
    !!! note
        If you want to recompile and submit your application all in one step, right-click an SPL file and select `Build and Submit Job`

=== "CLI"

    1. Set up your environment for Streams:<br/>`source <streams-install>/bin/streamsprofile.sh`
    1. Run `streamtool submitjob <workspace>/output/HelloWorld.sab`

    The output messages will inform you if the submission was successful or not.
    !!! note
        If your submission is successful, the output messages will tell you the Job ID. This ID is useful for other commands going forward.

## Monitor the job

Now that a job is created, you can now:

* Monitor job and PE health
* View the job graph
* View metrics
* View or download logs

You can monitor a job using your favorite interface.

### Monitor the job and PE health

A job's health is important to monitor and identify if a distributed application is having issues. If any PE in the job is not healthy, then the job will not be healthy.

=== "VS Code"

    The health of the job appears next to the job name in the Streams Explorer:

    ![VS Code Job Health](../assets/vscode-job-health.png)

    !!! warning
        Because VS Code is a developer-first tool, VS Code does not show PE health. Use the Streams Console or the CLI to get PE info if needed.

=== "CLI"

    To list out jobs and their health within an instance, use the following command:
    ```
    streamtool lsjobs
    ```
    To list out PEs and their health for a specific job, use the following command:
    ```
    streamtool lspes -j <job-id>
    ```

### View the job graph in Streams Console

Streams Console is the Web UI for managing, monitoring, and performing operations on the Streams platform. Additionally, the web UI has application-specific dashboards that
allow users to monitor jobs and PEs and also provides a graph representation of the job.

=== "VS Code"

    1. Navigate to the Streams Explorer
    1. Navigate to the job you want to see
    1. Click the 'Show Job Graph' :job-graph: button
    1. Click Open to automatically open it in a browser
    1. Sign in using your username and password

=== "CLI"

    1. Run `streamtool geturl`
    1. Copy the URL from the output
    1. Open a web browser and go to the URL
    1. Sign in using your username and password
    1. Navigate to the Application Dashboard

!!! info
    The job graph also has a color scheme to color the operators based on different factors like what PE or resource it's located in, CPU utilization, and many others.

### View or download logs

To inspect PE stdout/err output, help debug, or investigate errors, you can view or download job and PE logs.

=== "VS Code"
    To view logs directly in VS Code, use the Streams Log Watcher:

    1. Click the `STREAMS LOG WATCHER` tab in the lower right panel

    ![Streams Log Watcher](../assets/vscode-log-watcher.png)

    To download the logs:

    1. Navigate to the Streams Explorer
    1. Navigate to the job you want to see
    1. Click the 'Download Job Logs' :document--download: button

=== "CLI"

    To view logs directly in stdout/err of your command terminal, use `streamtool viewlog`:
    ```
    streamtool viewlog --console --pe <pe-id>
    ```

    To download the logs:
    ```
    streamtool getlog --includeapps
    ```

## Stop the job

=== "VS Code"
    Click the 'Cancel Job' :material-trash-can-outline: icon next to the job
=== "CLI"
    Run `streamtool canceljob <jobId>`
