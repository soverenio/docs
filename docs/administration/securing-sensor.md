# Securing the Sensor

!!! info "Refer to the [separate guide](../configuring-sensor/) for configuration options that are not related to security."

!!! info "Refer to [our current helm chart](https://github.com/soverenio/helm-charts/tree/master/charts/soveren-agent) for all values that can be tuned up for the Soveren Sensor."

## Proxying the Traffic

There may be instances when you want to route the traffic between the Soveren Sensor and the Cloud through a proxy. This could be for reasons such as gaining additional control over the traffic leaving your cluster.

To do this, simply specify the top-level value in your `values.yaml`:

```shell
httpsProxy: <PROXY_ADDRESS>:<PROXY_PORT>
```

Here, `<PROXY_ADDRESS>` and `<PROXY_PORT>` represent the address of your proxy service and the dedicated listening port, respectively.

You can also specify the `NO_PROXY` top-level variable to allow some of your traffic to bypass the proxy:

```shell
httpsProxyNoProxy: ""
```

## Network policy

You may want to specify the network policy for the Soveren Sensor. It is not enabled by default.

Here's how to do it:

```shell
networkPolicy:
  # -- Specifies whether Network Policies should be created
  enabled: false
  # -- Specify when the httpsProxy is enabled
  proxyIp: ""
  k8sApi:
    # -- Specify the k8s API endpoint port
    port: 443
```

## Container security

### Components that don't intercept traffic

All containers of the Soveren Sensor, except for the Interceptors, have the following `securityContext` by default:

```shell
securityContext:
  runAsUser: 1000 # 65534 for prometheusAgent
  runAsGroup: 1000 # 65534 for prometheusAgent
  allowPrivilegeEscalation: false
  runAsNonRoot: true
```

### Components that do traffic interception

Interceptors capture traffic by monitoring the virtual interfaces of the host.

In each Interceptor pod, there are two containers: the `rpcapd`, which handles the actual traffic capturing, and the `interceptor` itself, which processes the captured data.

To allow Interceptors to read from the host, both the `interceptor` and `rpcapd` containers need to run in privileged mode. Hence, they are assigned the following `securityContext`:

```shell
securityContext:
  privileged: true
```

Additionally, the `interceptor` container requires the following:

```shell
dnsPolicy: ClusterFirstWithHostNet
hostNetwork: true
hostPID: true
```

Modifying these settings for `interceptor` and `rpcapd` containers will disrupt traffic interception.