# Architecture

Soveren is composed of two primary components:

* **Soveren Agent**: Deployed within your Kubernetes cluster, the Agent [intercepts and analyzes](../../getting-started/quick-start/) structured HTTP JSON traffic. It collects metadata about data flows, identifying field structures, detected sensitive data types, and involved services. Importantly, the metadata **does not include any actual payload values**. The collected information is then relayed to the Soveren Cloud.
* **Soveren Cloud**: Hosted and managed by Soveren, this cloud platform presents user-friendly [dashboards](../../user-guide/overview/) that provide visualization of sensitive data flows and summary statistics and metrics.

## Soveren Agent

The Soveren Agent comprises several key parts:

* [**Interceptors**](../traffic-interception/): Distributed across all nodes in the cluster via a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/), Interceptors capture traffic from pod virtual interfaces using a [packet capturing](https://www.tcpdump.org/) mechanism.
* [**Processing and messaging system**](../traffic-processing/): This system includes a [Kafka](https://kafka.apache.org/) instance that stores request/response data and a component called Digger which forwards data for detection and eventually to the Soveren Cloud.
* **Sensitive data detector** (Detector): Employs proprietary machine learning algorithms to identify data types and gauge their sensitivity.

In Kubernetes terms, the Soveren Agent introduces the following pods to the cluster:

* _Interceptors_: One per worker node;
* _Kafka_: Part of the Processing and messaging system, deployed once per setup;
* _Digger_: Another component of the Processing and messaging system, deployed once per setup;
* _Detection-tool_ (Detector): Deployed once per setup.

We also employ Prometheus Agent for metrics collection, this component is not shown here.

Let's delve deeper into the main components' operations and communications.

![The end-to-end flow of the Soveren Agent](../../img/architecture/agent-flow.png "The end-to-end flow of the Soveren Agent")

The Soveren Agent follows this sequence of operations:

1. Interceptors collect relevant traffic from pods, focusing on HTTP requests with the `Content-Type: application/json` header.

2. Interceptors pair requests to individual endpoints with their respective responses, creating request+response pairs.

3. Interceptors transfer these pairs to a Kafka topic using the [binary Kafka protocol](https://kafka.apache.org/protocol.html).

4. Digger reads the request/response pair from Kafka, evaluates it for detailed analysis of data types and their sensitivity (employing intelligent sampling for high load scenarios). If necessary, Digger forwards the pair to the Detection-tool and retrieves the result.

5. Digger assembles a metadata package describing the processed request/response pair and transmits it to the Soveren Cloud using gRPC protocol and protobuf.

[The Kubernetes API provides pod names and other metadata to the Digger](../k8s-metadata/). Consequently, Soveren Cloud identifies assets by their Kubernetes names rather than IP addresses, enhancing data comprehensibility in the [Soveren app](https://app.soveren.io/).

## Soveren Cloud

[Soveren Cloud](https://app.soveren.io/) is a Software as a Service (SaaS) managed by Soveren. It provides [a suite of dashboards](../../user-guide/overview/) displaying diverse views into the metadata collected by the Soveren Agent. Users can view statistics and analytics on observed data types, their sensitivity, involved services, and any violations of predefined policies and configurations for allowed data types.
