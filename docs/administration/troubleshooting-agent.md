# Troubleshooting the Agent

If you've deployed Soveren Agent and everything _should be_ working properly, but you don't see any data in the [Soveren app](https://app.soveren.io/), or you there's something still not right from your perspective, here ar eseveral things that you can do.

## Verifying the deployment

The first thing to make sure of is that you are running the latest version. The following command helps with that:

```shell
helm search repo soveren
````

You can verify the output of this command with our support team.

Then, it makes sense to verify that all Soveren Agent components have been deployed:

```shell
helm -n soverenio list
```

Your are looking for the following:

* `interceptor`: there should be several instances, according to how many nodes you have in your cluster. Interceptors collect the traffic from nodes and send it to Kafka;
* `kafka`: one instance, gets the traffic from interceptors;
* `digger`: once instance, reads data from Kafka, sends it to detection-tool, collects results and communicates appropriate metadata to Soveren Cloud;
* `detectionTool`: one instance, does all the heavy lifting of detecting sensitive data;
* `prometheusAgent`: one instance, observes some basic metrics from all other Agent components.


## Verifying individual components

## Checking the logs
