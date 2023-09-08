# Configuring the Soveren Agent

!!! info "Refer to the [separate guide](../configuring-agent/) for configuration options that are specifically related to security."

We use Helm for managing the deployment of Soveren Agents. To customize values sent to your Soveren Agent, you need to create the `values.yaml` file in the folder that you use for custom Helm configuration.

!!! info "Refer to [our current helm chart](https://github.com/soverenio/helm-charts/tree/master/charts/soveren-agent) for all values that can be tuned up for the Soveren Agent."

You can change a number of things regarding the Soveren Agent deployment. But don't forget to run a `helm upgrade` command after you've updated the `values.yaml` file, providing the `-f path_to/values.yaml` as a command line option (see [Updating Agents](../managing-agents/#updating-agents)).

!!! danger "Only use `values.yaml` to override specific values!"
    Avoid using a complete copy of our `values.yaml` from the [repository](https://github.com/soverenio/helm-charts/tree/master/charts/soveren-agent). This can lead to numerous issues in production that are difficult and time-consuming to resolve. Use `values.yaml` only for overriding specific values.


## Agent token

To save you some keystrokes when installing or updating the Agent, we suggest placing the following snippet into the `values.yaml`:

```yaml
digger:
  token: <TOKEN>
```

!!! danger "Use unique Agents and tokens for different clusters"
    If you're managing multiple clusters, please create unique Agents for each one, with distinct tokens. Using the same token for different clusters will result in them appearing as a single deployment perimeter on the data map, making it challenging to discern which flow belongs to which cluster.

Digger is a component of the Agent that actually sends metadata to the Soveren Cloud. Detection-tool gets over-the-air updates of the part of the model from the Soveren Cloud. These are the places where the token value is used. (Detection-tool gets the token value from Digger.)

## Multi-cluster deployment

For each Kubernetes cluster, you'll need a separate Soveren Agent. When deploying Soveren Agents across multiple clusters, they will be identified by the tokens and names assigned during their creation. For more information, refer to [Managing agents](../managing-agents/).

There may be instances where you want to automate the naming process for your clusters in Soveren during deployment. In this case, you can specify the following in your `values.yaml` file:

```yaml
digger:
  statsclient:
    clustername: <NAME>
```

Here, Soveren will use `<NAME>` as the cluster's identifier when presenting data map information. If `<NAME>` isn't specified, Soveren will default to using the Agent's name defined in the [Soveren app](https://app.soveren.io/agents).

## Resource limits

You can adjust resource usage limits for each of the Soveren Agent's components.

As a rule of thumb, we **_do not_** recommend to change the `requests` values. They are set with regard to a minimum reasonable functionality that the component can provide given that much resources.

The `limits` however differ widely between Agent's components, and are heavily traffic dependent. There is no universal recipe for determining them, except to keep an eye on the actual usage and check how fast the data map is built by the product. General tradeoff here is this: the more resources you allow, the faster the map is built.

Soveren Agent does not persist any data, it is completely normal if any component restarts and virtual storage is flushed. The `ephemeral-storage` values are just for making sure that the virtual disk space is not overused.

### Interceptors

The Interceptors are placed on each node of the cluster as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/). Their ability to collect the traffic is proportional to how many resources they are allowed to use.

Interceptors collect `HTTP` requests and responses with `Content-type: application/json`, reading from virtual network interfaces of the host and building request/response pairs (read more in the [Interceptors: capturing the traffic](../../architecture/traffic-interception/)). Thus, the memory they use is directly proportional to how large those `JSON`s are.

The reading is done in a non-blocking fashion, leveraging the [`libpcap`](https://www.tcpdump.org/) library, or more precisely the `rpcapd` fork. So in effect each Interceptor pod hosts two containers: the `rpcapd`, which handles the actual traffic capturing, and the `interceptor` which processes the captured data.

The default configuration is the following:

For `interceptors`:

```yaml
interceptor:
  resources:
    requests:
      cpu: "100m"
      memory: "128Mi"
    limits:
      cpu: "1000m"
      memory: "2048Mi"
      ephemeral-storage: "100Mi"
```

For `rpcapd`:

```yaml
rpcapd:
  resources:
    requests:
      cpu: "100m"
      memory: "64Mi"
    limits:
      cpu: "250m"
      memory: "256Mi"
      ephemeral-storage: "100Mi"
```

You are encouraged to observe the actual usage for a while and tune the `limits` for the `interceptors` containers up or down. If there is not enough CPU the Interceptors may not have enough time to read the traffic and build enough request/response pairs relevant for building the data map.

You will most probably not need to tune anything for the `rpcapd` container.

### Kafka

[Kafka](https://kafka.apache.org/) is the component not built by Soveren and used pretty much as is. It can grow very large in terms of the `ephemeral-storage`.

There is also a `kafka-exporter` container in the Kafka pod for sending metrics to Prometheus Agent.

The default values for `kafka` and `kafka-exporter` containers are as follows (`kafka-exporter` is in the metrics section):

```yaml
kafka:
  embedded:
    resources:
      requests:
        cpu: "100m"
        memory: "650Mi"
        ephemeral-storage: "5Gi"
      limits:
        cpu: "400m"
        memory: "1024Mi"
        ephemeral-storage: "10Gi"
    metrics:
      resources:
        requests:
          cpu: "100m"
          memory: "650Mi"
          ephemeral-storage: "5Gi"
        limits:
          cpu: "400m"
          memory: "1024Mi"
          ephemeral-storage: "10Gi"
```

#### Heap usage by Kafka

In our testing, Kafka was found to be somewhat heap-hungry. That's why we limited the heap usage separately from the main memory usage limits. Here's what is set as the default:

```yaml
kafka:
  embedded:
    env:
    - name: KAFKA_HEAP_OPTS
      value: -Xmx512m -Xms512m
```

The rule of thumb is this: if you increased the `limits` `memory` value for the `kafka` container ×N-fold, also increase the heap ×N-fold.

### Digger

Digger is a component which reads the data from Kafka, sends relevant requests and responses to the Detection-tool and collect the results. Then it forms a metadata packet and sends it to the Soveren Cloud which creates all those beautiful product dashboards.

Digger employs all sorts of data sampling algorithms to make sure that all endpoints and assets in the data map are uniformly covered. In particular, Digger looks into the Kafka topics and moves offsets in there according to what has already been covered.

The resource defaults for Digger are:

```yaml
digger:
  resources:
    requests:
      cpu: "100m"
      memory: "100Mi"
    limits:
      cpu: "1500m"
      memory: "768Mi"
      ephemeral-storage: "100Mi"
```

### Detection-tool

The Detection-tool does all the heavy lifting when it comes to detecting data types in the flows and their sensitivity. It runs a custom-built machine learning models using Python for that.

The values for the Detection-tool resource consumption are adjusted for optimal performance regardless of the traffic nature. However, in some cases with a lot of heavy traffic it might make sense to increase the `limits`, so we encourage you to monitor the actual usage and adjust accordingly.

```yaml
detectionTool:
  resources:
    requests:
      cpu: "200m"
      memory: "1680Mi"
    limits:
      cpu: "2200m"
      memory: "2304Mi"
      ephemeral-storage: "200Mi"
```

### Prometheus-agent

We run a Prometheus Agent to collect some metrics to check basic performance of the Soveren Agent. Here are the default resource values:

```yaml
prometheusAgent:
  resources: 
    requests:
      memory: "192Mi"
      cpu: "75m"
    limits:
      memory: "400Mi"
      cpu: "75m"
      ephemeral-storage: "100Mi"
```

## Sending metrics to local Prometheus

If you want to monitor the metrics that the Soveren Agent collects, here's how to do that:

```yaml
prometheusAgent:
  additionalMetrics: 
    enabled: "true"
    name: "<PROMETHEUS_NAME>"
    url: "<PROMETHEUS_URL>"
```

where:

* `<PROMETHEUS_NAME>` is the name that you want to give here to your local Prometheus,

* `<PROMETHEUS_URL>` is the URL which will be receiving the metrics.

## Namespace filtering

At times, you may want to limit the Soveren Agent to specific namespaces for monitoring. You can achieve this by either specifying allowed namespaces (the "allow list") or by excluding particular ones (the "exclude list").

The syntax is as follows:

* If nothing is specified, all namespaces will be monitored.
* An asterisk (*) represents "everything."
* `action: allow` includes the specified namespace for monitoring.
* `action: deny` excludes the specified namespace from monitoring.

Here's an example to demonstrate:

```yaml
digger:
  cfg:
    kubernetesfilterlist:
      definitions:
        # - namespace: default
        #   action: allow
        # - namespace: kube-system
        #   action: deny
        - namespace: "*"
          action: allow
```

When defining names, you can use wildcards and globs such as `foo*`, `/dev/sd?`, and `devspace-[1-9]`, as defined in the [Go path package](https://pkg.go.dev/path#Match).

The Agent's default policy is to work only with explicitly mentioned namespaces, ignoring all others.

!!! info "End with `allow *` if you have any `deny` definitions"
    If you've included `deny` definitions in your filter list and want to monitor all other namespaces, make sure to conclude the list with:
    ```shell
          - namespace: "*"
          action: allow
    ```
    Failing to do so could result in the Agent not monitoring any namespaces if only `deny` definitions are present.

## Service mesh and encryption

Soveren can monitor connections encrypted through service meshes like [Linkerd](https://linkerd.io/) or [Istio](https://istio.io/).

The agent will automatically detect if a service mesh is deployed in the cluster or on the node. Fine-tuning is only necessary if your mesh implementation uses non-standard ports.

For instance, with Linkerd, you may need to include the following in your `values.yaml`:

```yaml
interceptor:
  cfg:
    # if the port of Linkerd differs from the default (4140)
    conntracker:
      linkerdPort: <PORT>
```

## Changing the log level

By default, the log levels for all Soveren Agent components are set to `error`. You can modify this by specifying different log levels for individual components, as shown below:

```yaml
[digger|interceptor|detectionTool|prometheusAgent]:
  cfg:
    log:
      level: error
```

(You'll need to create separate config sections for different components — `digger`, `interceptor`, `detectionTool` or `prometheusAgent` — but the syntax remains the same.)

We do not manage the log level for Kafka; it is set to `info` by default.

## Binding of components to specific nodes

The Soveren Agent [consists of](../../architecture/overview/#soveren-agent) two types of components:

* Interceptors, which are **distributed to each node** via DaemonSet.

* Components instantiated only once per cluster; these include Digger, Detection-Tool, Kafka, and Prometheus-Agent. These can be thought of as the **centralized components**.

The centralized components [consume](#resource-limits) a relatively large yet steady amount of resources. Their resource consumption is not significantly affected by variations in traffic volume and patterns. In contrast, the resource requirements for Interceptors can vary depending on traffic.

Given these considerations, it may be beneficial to isolate the centralized components on specific nodes. For example, you might choose nodes that are more focused on infrastructure monitoring rather than on business processes. Alternatively, you could select nodes that offer more resources than the average node.

If you know exactly which nodes host the workloads you wish to monitor with Soveren, you can also limit the deployment of Interceptors to those specific nodes.

First, you'll need to label the nodes that Soveren components will utilize:

```shell
kubectl label nodes <your-node-name> nodepool=soveren
```

After labeling, you have two options for directing the deployment of components: using `nodeSelector` or `affinity`.

### `nodeSelector`

!!! info "For more information, consult the Kubernetes documentation on `nodeSelector` [here](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector)."

In your `values.yaml` file, specify the following for each component you wish to bind to designated nodes:

```yaml
nodeSelector:
  nodepool: soveren
```

### `affinity`

!!! info "For more information, consult the Kubernetes documentation on `affinity` [here](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity)."

In your `values.yaml` file, specify the following for each component you wish to bind to designated nodes:

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
        - key: nodepool
        operator: In
        values:
        - soveren
```

The `affinity` option is conceptually similar to `nodeSelector` but allows for a broader set of constraints.
