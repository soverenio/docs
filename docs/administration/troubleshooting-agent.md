# Troubleshooting the Agent

You've deployed the Soveren Agent and everything should be working properly. However, if you don't see any data in the [Soveren app](https://app.soveren.io/), or something seems amiss, here are several troubleshooting steps you can follow.

## Verifying the deployment

Ensure that you're running the latest version of the Soveren Agent. You can verify this with the following command:

```shell
helm search repo soveren
```

You can then compare the versions listed in the output with our customer success team for confirmation.

Next, it's advisable to confirm that all Soveren Agent components have been successfully deployed:

```shell
helm -n soverenio list
```

In this command, `soverenio` is the namespace where you've [deployed](../../getting-started/quick-start/) the Agent.

Ensure you observe _all_ of the following:

* `interceptor`: There should be several instances, equal to the number of nodes in your cluster. Interceptors collect the traffic from nodes and relay it to `kafka`.
* `kafka`: Only one instance should exist, which receives traffic from the `interceptors`;
* `digger`: One instance, reads data from `kafka`, sends it to the `detection-tool`, collects results, and forwards relevant metadata to the Soveren Cloud.
* `detection-tool`: A single instance, performs the bulk of the work detecting sensitive data.
* `prometheus-agent`: A single instance, monitors basic metrics from all other Agent components.

Additionally, ensure that all custom values specified in your `values.yaml` have been incorporated into the deployment:

```shell
helm -n soverenio get values soveren-agent | grep -v token
```

!!! info "These commands offer a basic check of the Soveren Agent setup's consistency"
    Be prepared to share the output of these commands when discussing issues with our customer success team.

## Verifying individual components

If the basic setup appears correct but issues persist, consider inspecting individual components.

### Checking Deployments and DaemonSet

First, review the configurations of each component:

```shell
kubectl -n soverenio describe deployment -l app.kubernetes.io/component=[digger|kafka|prometheus-agent|detection-tool]
```

Run the aforementioned command multiple times, substituting in `digger`, `kafka`, `prometheus-agent`, and `detection-tool`. These components are considered _Deployments_ in Kubernetes, and the command provides detailed information about each.

Since Interceptors function as a Kubernetes _DaemonSet_, they require a different command:

```shell
kubectl -n soverenio describe daemonset -l app.kubernetes.io/component=interceptor
```

#### Permissions required by Interceptors

If issues arise specifically with the Interceptors, such as difficulties transitioning to running mode, confirm they possess the requisite permissions::

```shell
kubectl -n soverenio get daemonset -l app.kubernetes.io/component=interceptor -o yaml
```

Each Interceptor pod houses two containers: the `rpcapd`, responsible for actual traffic capture, and the `interceptor` itself, which processes this data. Examine the `securityContext` for both `interceptor` and `rpcapd`:

```shell
securityContext:
  privileged: true
```

For `interceptor` container, ensure the output includes:

```shell
dnsPolicy: ClusterFirstWithHostNet
hostNetwork: true
hostPID: true
```

!!! warning "Ensure the `securityContext` for Interceptors is properly set"
    Interceptors listen to the host's virtual interfaces, necessitating their operation in privileged mode. Otherwise, they'll fail to capture traffic.

### Checking pods

If a particular component raises concerns, delve deeper into its associated pods.

For pods by component:

```shell
kubectl -n soverenio describe pod -l app.kubernetes.io/component=[digger|interceptor|kafka|prometheus-agent|detection-tool]
```

Repeat the command above for `digger`, `interceptor`, `kafka`, `prometheus-agent` and `detection-tool`.

To view all the Agent's pods:

```shell
kubectl -n soverenio describe pod -l app.kubernetes.io/name=soveren-agent
```

## Checking logs

If a specific component seems problematic, consider inspecting its logs.

To view logs by component:

```shell
kubectl -n soverenio logs -l app.kubernetes.io/component=[digger|interceptor|kafka|prometheus-agent|detection-tool]
```

This command should be executed individually for `digger`, `interceptor`, `kafka`, `prometheus-agent` and `detection-tool`.

To investigate logs from individual pods, such as the Interceptors:

```shell
kubectl -n soverenio get pod -l app.kubernetes.io/component=interceptor
```

This provides a list of `POD_NAMES` associated with the Interceptors. You can then retrieve logs from a specific pod:

```shell
kubectl -n soverenio logs <POD_NAME>
```

To enhance log verbosity, you may need to [adjust the log level](../configuring-agent/#changing-the-log-level) for the concerned component.
