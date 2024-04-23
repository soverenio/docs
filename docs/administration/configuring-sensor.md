# Configuring Sensors

## Common considerations and fine-tuning

!!! info "Refer to the [separate guide](../securing-sensor/) for security-related configuration options."

We use Helm for managing the deployment of Soveren Sensors. Refer to [our Helm chart](https://github.com/soverenio/helm-charts/) for all values that can be tuned up for the Soveren Sensor.

To customize values sent to your Soveren Sensor, you need to create the `values.yaml` file in the folder that you use for custom Helm configuration.

Don't forget to run a `helm upgrade` command after you've updated the `values.yaml` file, providing the `-f path_to/values.yaml` as a command line option (see the [updating guide](../managing-sensors/#update)).

!!! danger "Only use `values.yaml` to override specific values!"
    
    Avoid using a complete copy of our `values.yaml` from the [repository](https://github.com/soverenio/helm-charts/). This can lead to numerous issues in production that are difficult and time-consuming to resolve.

### Sensor token

#### Use `values.yaml`

To save you some keystrokes when installing or updating the Sensor, we suggest placing the following snippet into the `values.yaml`:

=== "Data-in-motion (DIM)"

    ```yaml
    digger:
      token: <TOKEN>
    ```

=== "Data-at-rest (DAR)"

    ```yaml
    crawler:
      token: <TOKEN>
    ```

!!! danger "Use unique tokens for different deployments"

    If you're managing multiple Soveren deployments, please create unique tokens for each one. Using the same token across different deployments can result in data being mixed and lead to interpretation errors that are difficult to track.

The token value is used to send metadata to the Soveren Cloud and to check for over-the-air updates of the detection model.

#### HashiCorp Vault

You can store the token value in HashiCorp Vault and retrieve it at runtime using various techniques. To do this, set the top-level `useVault` to `true` in your `values.yaml`. Then, establish communication with the Vault and export the necessary environment variables.

Below is an example of how you could implement this:

```yaml
useVault: true

digger:
  podAnnotations:
    vault.hashicorp.com/agent-inject: 'true'
    vault.hashicorp.com/role: soveren-app
    vault.hashicorp.com/log-level: info
    vault.hashicorp.com/agent-inject-secret-soverentokens: secret/data/digger/token
    vault.hashicorp.com/agent-run-as-same-user: 'true'
    # -- Environment variable export template
    vault.hashicorp.com/agent-inject-template-soverentokens: |
      {{ with secret "secret/data/digger/token" -}}
        export SVRN_DIGGER_STATSCLIENT_TOKEN="{{ .Data.data.SVRN_DIGGER_STATSCLIENT_TOKEN }}"
      {{- end }}
  image:
    # -- Default entrypoint for digger: '/usr/local/bin/digger --config /etc/config.yaml'
    # -- Example for hashcorp/vault:
    command: [ '/bin/bash', '-c' ]
    args: [ 'source /vault/secrets/soverentokens && /usr/local/bin/digger --config /etc/config.yaml' ]


detectionTool:
  podAnnotations:
    vault.hashicorp.com/agent-inject: 'true'
    vault.hashicorp.com/role: soveren-app
    vault.hashicorp.com/log-level: debug
    vault.hashicorp.com/agent-inject-secret-soverentokens: secret/data/digger/token
    vault.hashicorp.com/agent-run-as-same-user: 'true'
    # -- Environment variable export template
    vault.hashicorp.com/agent-inject-template-soverentokens: |
      {{ with secret "secret/data/digger/token" -}}
        export SVRN_DETECTION_TOOL_OTAREGISTRY_AUTH_TOKEN="{{ .Data.data.SVRN_DIGGER_STATSCLIENT_TOKEN }}"
      {{- end }}
  image:
    # -- Default entrypoint for detection-tool: './entrypoint.sh'
    # -- Example for hashcorp/vault:
    command: [ '/bin/bash', '-c' ]
    args: [ 'source /vault/secrets/soverentokens && ./entrypoint.sh' ]
```

### Resources

As a rule of thumb, we do not recommend changing the `requests` values. They are calibrated to ensure the minimum functionality required by the component with the allocated resources.

On the other hand, the `limits` for different components of the Sensor can vary significantly and are dependent on the volume of collected data. There is no one-size-fits-all approach to determining them, but it's crucial to monitor actual usage and observe how quickly the data map is constructed by the product. The general trade-off here is: the more resources you allocate, the quicker the map is built.

It's important to note that the Soveren Sensor does not persist any data. It is normal for components to restart and virtual storage to be flushed. The `ephemeral-storage` values are set to prevent the overuse of virtual disk space.

### Local metrics

If you wish to collect metrics from the Soveren Sensor locally and create your own dashboards, follow these steps:

```yaml
prometheusAgent:
  additionalMetrics: 
    enabled: "true"
    # -- The name that you want to assign to your local Prometheus
    name: "<PROMETHEUS_NAME>"
    # -- The URL which will be receiving the metrics
    url: "<PROMETHEUS_URL>"
```

### Binding components to nodes

The Soveren Sensor [consists of](../../architecture/overview/#soveren-sensor) two types of components:

* `Interceptors`, which are **distributed to each node** via [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/). Interceptors are exclusively used by the Data-in-motion (DIM) sensors.

* Components instantiated only once per cluster via [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/); these include `digger`, `crawler`, `kafka`, `detectionTool` and `prometheusAgent`. These can be thought of as the **centralized components**.

The centralized components [consume](#resource-limits) a relatively large yet steady amount of resources. Their resource consumption is not significantly affected by variations in traffic volume and patterns. In contrast, the resource requirements for Interceptors can vary depending on traffic.

Given these considerations, it may be beneficial to isolate the centralized components on specific nodes. For example, you might choose nodes that are more focused on infrastructure monitoring rather than on business processes. Alternatively, you could select nodes that offer more resources than the average node.

If you know exactly which nodes host the workloads you wish to monitor with Soveren, you can also limit the deployment of Interceptors to those specific nodes.

First, you'll need to label the nodes that Soveren components will utilize:

```shell
kubectl label nodes <your-node-name> nodepool=soveren
```

After labeling, you have two options for directing the deployment of components: using `nodeSelector` or `affinity`.

#### `nodeSelector`

!!! info "For more information, consult the Kubernetes documentation on `nodeSelector` [here](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector)."

In your `values.yaml` file, specify the following for each component you wish to bind to designated nodes:

```yaml
nodeSelector:
  nodepool: soveren
```

#### `affinity`

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

### Kafka

#### Heap

In our testing, Kafka was found to be somewhat heap-hungry. That's why we limited the heap usage separately from the main memory usage limits. Here's what is set as the default:

```yaml
kafka:
  embedded:
    env:
    - name: KAFKA_HEAP_OPTS
      value: -Xmx512m -Xms512m
```

The rule of thumb is this: if you increased the `limits` `memory` value for the `kafka` container ×N-fold, also increase the heap ×N-fold.

#### Persistent volume

The Soveren Sensor is designed to avoid persisting any information during runtime or between restarts. All containers are allocated a certain amount of `ephemeral-storage` to limit potential disk usage. `kafka` is a significant consumer of `ephemeral-storage` as it temporarily holds collected information before further processing by other components.

There may be scenarios where you'd want to use `persistentVolume` for `kafka`. For instance, the disk space might be shared among various workloads running on the same node, and your cloud provider may not differentiate between persistent and ephemeral storage usage.

To enable `persistentVolume` for `kafka`, include the following section in your `values.yaml` file and adjust the settings as needed:

```yaml
kafka:
  embedded:
    persistentVolume:
      # -- Create/use Persistent Volume Claim for server component. Uses empty dir if set to false.
      enabled: false
      # -- Array of access modes. Must match those of existing PV or dynamic provisioner. Ref: [http://kubernetes.io/docs/user-guide/persistent-volumes/](http://kubernetes.io/docs/user-guide/persistent-volumes/)
      accessModes:
        - ReadWriteOnce
      annotations: {}
      # -- Specify the StorageClass for the persistent volume.
      storageClass: ""
      # -- Bind the Persistent Volume using labels. Must match all labels of the targeted PV.
      matchLabels: {}
      # -- Size of the volume. The size should be determined based on the metrics you collect and the retention policy you set.
      size: 10Gi
```
### Log level

By default, the log levels for all Soveren Sensor components are set to `error`. To tailor the verbosity of the logs to your monitoring needs, you can specify different log levels for individual components:

```yaml
[digger|crawler|interceptor|detectionTool|prometheusAgent]:
  cfg:
    log:
      level: info
```

We do not manage the log level for Kafka components; they are set to `info` by default.

## Data-in-motoin (DIM) configuration

### Multi-cluster deployment

For each Kubernetes cluster, you'll need a separate Soveren Sensor. When deploying Soveren Sensors across multiple clusters, they will be identified by the tokens and names assigned during their creation. For more information, refer to [Managing sensors](../managing-sensors/).

There may be instances where you want to automate the naming process for your clusters in Soveren during deployment. In this case, you can specify the following in your `values.yaml` file:

```yaml
digger:
  clusterName: <NAME>
```

Here, Soveren will use `<NAME>` as the cluster's identifier when presenting data map information. If `<NAME>` isn't specified, Soveren will default to using the Sensor's name defined in the [Soveren app](https://app.soveren.io/agents).

### Interceptors

The Interceptors are placed on each node of the cluster as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/). Their ability to collect the traffic is proportional to how many resources they are allowed to use.

### Namespace filtering

At times, you may want to limit the Soveren Sensor to specific namespaces for monitoring. You can achieve this by either specifying allowed namespaces (the "allow list") or by excluding particular ones (the "exclude list").

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

The Sensor's default policy is to work only with explicitly mentioned namespaces, ignoring all others.

!!! info "End with `allow *` if you have any `deny` definitions"

    If you've included `deny` definitions in your filter list and want to monitor all other namespaces, make sure to conclude the list with:

    ```yaml
          - namespace: "*"
          action: allow
    ```

    Failing to do so could result in the Sensor not monitoring any namespaces if only `deny` definitions are present.

### Service mesh and encryption

Soveren can monitor connections encrypted through service meshes like [Linkerd](https://linkerd.io/) or [Istio](https://istio.io/).

The Sensor will automatically detect if a service mesh is deployed on the node. Fine-tuning is only necessary if your mesh implementation uses non-standard ports.

For instance, with Linkerd, you may need to include the following in your `values.yaml`:

```yaml
interceptor:
  cfg:
    # if the port of Linkerd differs from the default (4140)
    conntracker:
      linkerdPort: <PORT>
```