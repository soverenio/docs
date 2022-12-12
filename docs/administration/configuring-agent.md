# Configuring the Soveren Agent

We use Helm for managing the deployment of Soveren Agents. To pass custom values to your Soveren Agent, you need to create the `values.yaml` file in the folder that you use for custom Helm configuration.

You can change a number of things regarding the Soveren Agent deployment. But don't forget to run a `helm upgrade` command after you've updated the `values.yaml` file.

## The token

To save you some keystrokes when installing or updating the Agent, we suggest placing the following snippet into the `values.yaml`.

Digger is a component of an Agent that actually sends metadata to the Soveren Cloud, this is where the token value is used.

```shell
digger:
  token: <TOKEN>
```

## Resource limits

You can adjust resource usage limits for each of the Soveren Agent's components.

As a rule of thumb, we **_do not_** recommend to change the `requests` values. They are set with regard to a minimum reasonable functionality that the component can provide given that much resources.

The `limits` however differ widely between Agent's components, and are heavily traffic dependent. There is no universal recipe for determining them, except to keep an eye on the actual usage and check how fast the data map is built by the product. General tradeoff here is this: the more resources you allow, the faster the map is built.

### Interceptors

The interceptors are placed on each node of the cluster as a `DaemonSet`. Their ability to collect the traffic is proportional to how much resources they are allowed to use.

Interceptors collect `HTTP` requests and responses with `Content-type: application/json`, reading from virtual network interfaces of the host and building request/response pairs. Thus the memory they use is directly proportional to how large those `JSON`s are.

The reading is done in a non-blocking fashion, leveraging the [`libpcap`](https://www.tcpdump.org/) library.  If there is not enough CPU the interceptors may not have enough time to read the traffic and build enough request/response pairs relevant for building the data map.

The default configuration is the following. You are encouraged to observe the actual usage for a while and tune the `limits` up or down.

```shell
interceptor:
  resources:
    requests:
      cpu: "100m"
      memory: "128Mi"
    limits:
      cpu: "1000m"
      memory: "2048Mi"
      ephemeral-storage: 100Mi
```

The `ephemeral-storage` is for making sure that the virtual disk space is not overused.

#### Permissions for the interceptors

For interceptors to be able to read from the host, the containers they run in require the following permissions (you can't really change them without breaking the interception, but just in case):

```shell
securityContext:
      privileged: true
      dnsPolicy: ClusterFirstWithHostNet
      hostNetwork: true
      hostPID: true
```
