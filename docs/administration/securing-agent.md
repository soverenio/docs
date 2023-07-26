# Securing the Agent

## Proxying the Traffic

There may be instances when you want to route the traffic between the Soveren Agent and the Cloud through a proxy. This could be for reasons such as gaining additional control over the traffic leaving your cluster.

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

You may want to specify the network policy for the Soveren Agent. It is not enabled by default.

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

All containers of the Soveren Agent, except for the Interceptors, have the following `securityContext` by default:

```shell
securityContext:
  runAsUser: 1000
  runAsGroup: 1000
  allowPrivilegeEscalation: false
  runAsNonRoot: true
```

To enable Interceptors to read from the host, their containers require the following permissions (modifying these might disrupt traffic interception):

```shell
securityContext:
  privileged: true
  dnsPolicy: ClusterFirstWithHostNet
  hostNetwork: true
  hostPID: true
```