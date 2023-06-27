# Architecture

Soveren consists of two major parts:

* **Soveren Agent** which you [deploy](../../getting-started/quick-start/) in your Kubernetes cluster. It intercepts and parses structured HTTP JSON traffic, gathers metadata about the flows and sends it to the Soveren Cloud. This metadata contains information about how the payload was structured (what fields), which sensitive data types were detected, and which services were involved in the communication. **No part of the actual payload values is included in the metadata**.
* [**Soveren Cloud**](https://app.soveren.io/) is hosted and managed by Soveren. It provides [dashboards](../../user-guide/overview/) to gain visibility into sensitive data flows, as well as summary statistics and metrics.

## Soveren Agent

### Architecture

Soveren Agent consists of several parts:

* **Interceptors** which are distributed to all worker nodes of the cluster through the [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/). They capture the traffic from virtual interfaces of the pods with the help of a [packet capturing](https://www.tcpdump.org/) mechanism;
* **Messaging system** which receives data from the Interceptors. Consists of a [Kafka](https://kafka.apache.org/) instance which stores request/response data, and Digger which passes data to the detection and further to the Soveren Cloud;
* **Sensitive Data Detector** (or simply Detector) which discovers data types and their sensitivity with the help of proprietary machine learning algorithms.

In Kubernetes (K8s) terms, all components of the Soveren Agent are pods which are deployed to the worker nodes.

In general, Interceptors are present on each node of the cluster. Kafka, Digger and Detector are deployed onto a separate node.

So speaking in Kubernetes terms, there are the following pods:

* _Interceptors_: many of them, one per each worker node;
* _Kafka_ as part of the Messaging system, one per deployment;
* _Digger_ as another part of the Messaging system, one per deployment;
* _Detection-tool_ as Detector, one per deployment.

Let’s look in more detail into what those components do and how they talk to each other.

### The end-to-end flow

![The end-to-end flow of the Soveren Agent](../../img/architecture/agent-flow.png "The end-to-end flow of the Soveren Agent")

The flow of the Soveren Agent looks like this:

1. Interceptors collect relevant traffic from the pods. They observe only HTTP requests with `Content-Type: application/json` set.

2. Interceptors match requests to individual endpoints with responses coming from them, and build request+response pairs.

3. Interceptors write the request/response pairs to the Kafka topic using [binary Kafka protocol](https://kafka.apache.org/protocol.html).

4. (The Interceptor is present as well on the node where Kafka and Digger and Detection-tool might be deployed because there can also be other pods with the traffic subject to monitoring.)

5. Digger reads the request/response pair from the topic and decides whether it’s subject to the detailed analysis of present data types and their sensitivity. (Intelligent sampling may be involved here if the load becomes really high). If yes, Digger sends the pair to the Detection-tool and gets back the result.

6. Digger forms a metadata package describing the processed request/response pair and sends it to the Soveren Cloud. This connection uses gRPC and protobuf.

### Traffic interception

![Traffic interception](../../img/architecture/interception.png "Traffic interception")

Interceptors are deployed as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/). Normally they are present as pods on each worker node of the cluster.

Pods with the Interceptors have `hostNetwork` set to `true` (more on that [below](#required-permissions)). That gives them access to the underlying host, that is to the virtual machine they are running on. Given that, the Interceptors read data from network namespaces of the host, leveraging the [PCAP library](https://www.tcpdump.org/) for that.

Then, the Interceptors should know which interfaces to read. For that they are given the list of relevant IP addresses that should be present on their host, they could then match them with the interfaces that they actually observe on the host. Digger — a part of the messaging system — leverages the Kubernetes (K8s) API to obtain the addressing information.

Interceptors then read data from the virtual interfaces available to them in the network namespace of the host. _**This reading happens in a non-blocking fashion**_. If it so happens that the host is loaded with higher priority tasks, then the OS may deprive the Interceptor of CPU and memory resources, which in turn may result in partial coverage of the traffic by the Interceptor.

The K8s API also provides naming of pods and other metadata to the Interceptors. As a result, later on in the Soveren Cloud the assets are called by their DNS/K8s names instead of IP addresses, which makes data that the [Soveren app](https://app.soveren.io/) displays more accessible.

#### Required permissions

For Interceptors to be able to read from the host, the containers they run in require the following permissions (you can't really change them without breaking the interception, but just in case):

```shell
securityContext:
  privileged: true
  dnsPolicy: ClusterFirstWithHostNet
  hostNetwork: true
  hostPID: true
```

## Soveren Cloud

[Soveren Cloud](https://app.soveren.io/) is a SaaS managed by Soveren. It offers [a set of dashboards](../../user-guide/overview/) that provide various views into the metadata collected by Soveren Agent. There are analytics and stats on which relevant data types have been observed and how sensitive they were, what services were involved, were there any violations of pre-set policies and configurations in terms of allowed data types.
