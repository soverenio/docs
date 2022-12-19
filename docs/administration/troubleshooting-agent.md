# Troubleshooting the Agent

You've deployed Soveren Agent and everything _should be_ working properly, but you don't see any data in the [Soveren app](https://app.soveren.io/), or there's something still not right from your perspective. Here are several things that you can do.

## Verifying the deployment

The first thing to make sure of is that you are running the latest version. The following command helps with that:

```shell
helm search repo soveren
```

You can confirm the versions that you get through this command with our customer success team.

Then it makes sense to verify that all Soveren Agent components have successfully deployed:

```shell
helm -n soverenio list
```

Here `soverenio` is the namespace to which you've [deployed](../../getting-started/quick-start/) the Agent.

Your are looking for _all_ of the following:

* `interceptor`: there should be several instances, equal to the number of nodes in your cluster. Interceptors collect the traffic from nodes and send it to Kafka;
* `kafka`: one instance, gets the traffic from interceptors;
* `digger`: once instance, reads data from Kafka, sends it to detection-tool, collects results and communicates appropriate metadata to Soveren Cloud;
* `detectionTool`: one instance, does all the heavy lifting of detecting sensitive data;
* `prometheusAgent`: one instance, observes some basic metrics from all other Agent components.

Further, you can check that all custom values that you've specified in your `values.yaml` have reached the deployment as well:

```shell
helm -n soverenio get values soveren-agent | grep -v token
```

!!! note "The output of those three commands provide a very basic consistency check that all's good with you Soveren Agent setup"

## Verifying individual components

## Checking the logs
