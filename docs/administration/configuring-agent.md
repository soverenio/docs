# Configuring the Soveren Agent

We use Helm for managing the deployment of Soveren Agents. To customize values sent to your Soveren Agent, you need to create the `values.yaml` file in the folder that you use for custom Helm configuration.

You can change a number of things regarding the Soveren Agent deployment. You can always check [our repository](https://github.com/soverenio/helm-charts/blob/master/charts/soveren-agent/values.yaml) for the full list of possible values. But don't forget to run a `helm upgrade` command after you've updated the `values.yaml` file, providing the `-f path_to/values.yaml` as a command line option.

## The token

To save you some keystrokes when installing or updating the Agent, we suggest placing the following snippet into the `values.yaml`:

```shell
digger:
  token: <TOKEN>
```

Digger is a component of the Agent that actually sends metadata to the Soveren Cloud, this is where the token value is used.

## Resource limits

You can adjust resource usage limits for each of the Soveren Agent's components.

As a rule of thumb, we **_do not_** recommend to change the `requests` values. They are set with regard to a minimum reasonable functionality that the component can provide given that much resources.

The `limits` however differ widely between Agent's components, and are heavily traffic dependent. There is no universal recipe for determining them, except to keep an eye on the actual usage and check how fast the data map is built by the product. General tradeoff here is this: the more resources you allow, the faster the map is built.

Soveren Agent does not persist any data, it is completely normal if any component restarts and virtual storage is flushed. The `ephemeral-storage` is just for making sure that the virtual disk space is not overused. You can safely get rid of any of them.

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

#### Permissions required by the interceptors

For interceptors to be able to read from the host, the containers they run in require the following permissions (you can't really change them without breaking the interception, but just in case):

```shell
securityContext:
      privileged: true
      dnsPolicy: ClusterFirstWithHostNet
      hostNetwork: true
      hostPID: true
```

### Kafka

[Kafka](https://kafka.apache.org/) is the only component not built by Soveren and used pretty much as is. It can grow very large in terms of the `ephemeral-storage`.

The default values here are as follows. Under normal circumstances you don't need to touch any of them.

```shell
kafka:
  embedded:
    resources:
      requests:
        cpu: "100m"
        memory: "650Mi"
        ephemeral-storage: 5Gi
      limits:
        cpu: "200m"
        memory: "1024Mi"
        ephemeral-storage: 10Gi
```

#### Heap usage by Kafka

In our testing, Kafka was found to be somewhat heap-hungry. That's why we limited the heap usage separately from the main memory usage limits. You don't need to change it but here's what is set as the default:

```shell
kafka:
  embedded:
    env:
    - name: KAFKA_HEAP_OPTS
      value: -Xmx512m -Xms512m
```

### Digger

Digger is a component which reads the data from Kafka, sends relevant requests and responses to the Deection tool and collect the results. Then it forms a metadata packet and sends it to the Soveren Cloud which creates all those beautiful product dashboards.

Digger employs all sorts of data sampling algorithms to make sure that all endpoints and assets in the data map are uniformly covered. In particular, Digger looks into the Kafka topics and moves offsets in there according to what has already been covered.

Normally you should not want to change the resource values for Digger but here they are:

```shell
digger:
  resources:
    requests:
      cpu: "100m"
      memory: "100Mi"
    limits:
      cpu: "1500m"
      memory: "768Mi"
      ephemeral-storage: 100Mi
```

### Detection tool

The Detection tool does all the heavy lifting when it comes to detecting data types in the flows and their sensitivity. It runs a custom built machine learning models using Python for that.

The values for the Detection tool resource consumption are adjusted for optimal performance regardless of the traffic nature. However, in some cases with a lot of heavy traffic it might make sense to increase the limits, so we encourage you to monitor the actual usage and adjust accordingly.

```shell
detectionTool:
  resources:
    requests:
      cpu: "100m"
      memory: "1680Mi"
    limits:
      cpu: "1100m"
      memory: "2304Mi"
      ephemeral-storage: 200Mi
```

### Prometheus

We run a Prometheus agent to collect some metrics to check basic performance of the Soveren Agent. Values here are pretty generic for most cases.

```shell
prometheusAgent:
  resources: 
    requests:
      memory: "192Mi"
      cpu: "75m"
    limits:
      memory: "400Mi"
      cpu: "75m"
      ephemeral-storage: 100Mi
```

## Namespace filtering

Sometimes it makes sense to confine the Soveren Agent to dedicated namespaces to monitor. You can do that by explicitly stating the allowed namespaces (the allow list) or by excluding particular ones (the exclude list).

The sytnax is like this:

* if nothing is specified then all namespaces will be covered;
* asterisk means _everything_;
* `action: allow` includes this namespace into monitoring;
* `action: deny` excludes this namespace from monitoring.

Here's an example of how you can do this:

```shell
digger:
  cfg:
    kubernetesfilterlist:
      # - namespace: default
      #   action: allow
      # - namespace: kube-system
      #   action: deny
      definitions:
        - namespace: "*"
          action: allow
```

## Changing the log level

By default log levels of all Soveren Agent components is set to `error`. You can change this by specifying different log level for individual components, like this:

```shell
[digger|interceptor|detectionTool]:
  cfg:
    log:
      level: error
```

We don't manage the log levels of Kafka or Prometheus.
