# Architecture

Soveren is composed of two primary components:

* **Soveren Agent**: Deployed within your Kubernetes cluster, the Agent [intercepts and analyzes](../../getting-started/quick-start/) structured HTTP JSON traffic. It collects metadata about data flows, identifying field structures, detected sensitive data types, and involved services. Importantly, the metadata **does not include any actual payload values**. The collected information is then relayed to the Soveren Cloud.
* [**Soveren Cloud**](https://app.soveren.io/): Hosted and managed by Soveren, this cloud platform presents user-friendly [dashboards](../../user-guide/overview/) that provide visualization of sensitive data flows and summary statistics and metrics.

## Soveren Agent

### Architecture

The Soveren Agent comprises several key parts:

* **Interceptors**: Distributed across all worker nodes in the cluster via a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/), Interceptors capture traffic from pod virtual interfaces using a [packet capturing](https://www.tcpdump.org/) mechanism.
* **Messaging system**: This system includes a [Kafka](https://kafka.apache.org/) instance that stores request/response data and a component called Digger which forwards data for detection and eventually to the Soveren Cloud.
* **Sensitive Data Detector** (Detector): Employs proprietary machine learning algorithms to identify data types and gauge their sensitivity.

In Kubernetes (K8s) terminology, all these components of the Soveren Agent are pods deployed to the worker nodes.

Generally, Interceptors are present on every node in the cluster, while Kafka, Digger, and Detector are housed on a separate node.

Therefore, in Kubernetes terms, the following pods exist:

* _Interceptors_: One per worker node;
* _Kafka_: Part of the Messaging system, deployed once per setup;
* _Digger_: Another component of the Messaging system, deployed once per setup;
* _Detection-tool_ (Detector): Deployed once per setup.

Let's delve deeper into these components' operations and communications.

### The end-to-end flow

![The end-to-end flow of the Soveren Agent](../../img/architecture/agent-flow.png "The end-to-end flow of the Soveren Agent")

The Soveren Agent follows this sequence of operations:

1. Interceptors collect relevant traffic from pods, focusing on HTTP requests with the `Content-Type: application/json` header.

2. Interceptors pair requests to individual endpoints with their respective responses, creating request+response pairs.

3. Interceptors transfer these pairs to a Kafka topic using the [binary Kafka protocol](https://kafka.apache.org/protocol.html).

4. (Please note, the Interceptor is also present on the node(s) hosting Kafka, Digger, and the Detection-tool, as there may also be other pods with relevant traffic on this node.)

5. Digger reads the request/response pair from the topic, evaluates it for detailed analysis of data types and their sensitivity (employing intelligent sampling for high load scenarios). If necessary, Digger forwards the pair to the Detection-tool and retrieves the result.

6. Digger assembles a metadata package describing the processed request/response pair and transmits it to the Soveren Cloud using gRPC protocol and protobuf.

The Kubernetes API provides pod names and other metadata to the Digger. Consequently, Soveren Cloud identifies assets by their DNS/Kubernetes names rather than IP addresses, enhancing data comprehensibility in the [Soveren app](https://app.soveren.io/).

### Traffic interception

![Traffic interception](../../img/architecture/interception.png "Traffic interception")

Interceptors are deployed as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/), and by default, exist as pods on all worker nodes in the cluster.

Pods with Interceptors have `hostNetwork` set to `true` ([see more on this](#required-permissions)), granting them access to the host machine. Thus, Interceptors can read data from the host's network namespaces and virtual interfaces using the [PCAP library](https://www.tcpdump.org/).

Interceptors read data from the virtual interfaces in a non-blocking manner. If the host is engaged with higher priority tasks, the OS may limit resources for the Interceptor, possibly resulting in partial traffic coverage.

#### Required permissions

To enable Interceptors to read from the host, their containers require the following permissions (modifying these might disrupt traffic interception):

```shell
securityContext:
  privileged: true
  dnsPolicy: ClusterFirstWithHostNet
  hostNetwork: true
  hostPID: true
```

## Soveren Cloud

[Soveren Cloud](https://app.soveren.io/) is a Software as a Service (SaaS) managed by Soveren. It provides [a suite of dashboards](../../user-guide/overview/) displaying diverse views into the metadata collected by the Soveren Agent. Users can view statistics and analytics on observed data types, their sensitivity, involved services, and any violations of predefined policies and configurations for allowed data types.
