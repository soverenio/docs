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
    Please share the output of those commands in the beginning of any new conversation with our customer success team.

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

#### Permissions required by interceptors

If here you find that something's wrong specifically with the interceptors, e.g. they are failing to get to the running mode, then make sure they are allowed the necessary permissions:

```shell
kubectl -n soverenio get daemonset -l app.kubernetes.io/component=interceptor -o yaml
```

What you are looking for is `securityContext`, it should be the following:

```shell
securityContext:
      privileged: true
      dnsPolicy: ClusterFirstWithHostNet
      hostNetwork: true
      hostPID: true
```

!!! warning "Make sure the security context for interceptors is set right"
    Since interceptors listen to the host's virtual interfaces, the containers they run in require such permissions. Otherwise interceptors will fail to acquire any traffic.

### Checking pods

Having the above, you can now look deeper into pods if something looks suspicious about any of the components.

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

If something certainly went south with a particular component, it is worth checking its logs.

This command gives you the logs by component:
```shell
kubectl -n soverenio logs -l app.kubernetes.io/component=[digger|interceptor|kafka|prometheus-agent|detection-tool]
```

You need to run this command separately for `digger`, `interceptor`, `kafka`, `prometheus-agent` and `detection-tool`. And  `soverenio` is the namespace to which you've [deployed](../../getting-started/quick-start/) the Agent.

You can dig into individual pod's logs e.g. for interceptors:

```shell
kubectl -n soverenio get pod -l app.kubernetes.io/component=interceptor
```

This gives you the list of `POD_NAMES` the interceptors are running in. And then:

```shell
kubectl -n soverenio logs <POD_NAME>
```

Where `POD_NAME` is the name of a suspicious pod from the output of the command above.

To make the logs more verbose you might need to [raise the log level](../configuring-agent/#changing-the-log-level) of a particular component.
