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
* `detection-tool`: one instance, does all the heavy lifting of detecting sensitive data;
* `prometheus-agent`: one instance, observes some basic metrics from all other Agent components.

Further, you can check that all custom values that you've specified in your `values.yaml` have reached the deployment as well:

```shell
helm -n soverenio get values soveren-agent | grep -v token
```

!!! info "Those commands provide a very basic consistency check that all's good with you Soveren Agent setup"
    Please share the output of those commands in the beginning of any new conversation with out customer success team.

## Verifying individual components

If everything is found to be good with the basic setup but something still looks off, you can dig deeper into individual components.

### Checking Deployments and DaemonSet

First let's have a look at the whole setup of each component:

```shell
kubectl -n soverenio describe deployment -l app.kubernetes.io/component=[digger|kafka|prometheus-agent|detection-tool]
```

Please run the above command several times: separately for `digger`, `kafka`, `prometheus-agent` and `detection-tool`. All those components are _Deployments_ in Kubernetes terms, and you'll get the detailed info on all of them.

Again, `soverenio` is the namespace to which you've [deployed](../../getting-started/quick-start/) the Agent.

Interceptors are a Kubernetes _DaemonSet_, so you need a different command:

```shell
kubectl -n soverenio describe daemonset -l app.kubernetes.io/component=interceptor
```

### Checking pods

Having the above, you can now look deeper into individual pods if something looks suspicious about them.

Pods by component:

```shell
kubectl -n soverenio describe pod -l app.kubernetes.io/component=[digger|interceptor|kafka|prometheus-agent|detection-tool]
```

You'll need to run the above command several times: separately for `digger`, `interceptor`, `kafka`, `prometheus-agent` and `detection-tool`

All pods of the Agent:

```shell
kubectl -n soverenio describe pod -l app.kubernetes.io/name=soveren-agent
```

## Checking the logs
