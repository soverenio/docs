# Infrastructure fit: requirements and recommendations

How well will Soveren fit into your technical infrastructure? There are several key aspects that you need to consider when evaluating Soveren.

!!! danger "Must-haves for Soveren to work are Kubernetes and HTTP/JSON"

    At present, the Soveren Agent only works in Kubernetes and monitors only HTTP traffic with JSON payloads (setting the correct `content-type` is crucial). These are necessities for Soveren to run and start providing insights.

## Deployment

1. **Kubernetes starting from version 1.21 and higher**: these are the versions that Soveren has been tested with. It can operate on older versions, but functionality may be suboptimal.

2. **We use Helm for deployment**. However, clients often adapt our charts to integrate the resulting manifests into their own deployment systems.

3. **4 CPU, 16 Gb nodes**. Actual usage may vary, but this is the typical minimal node size that users deploy Soveren on. Examples include standard general-purpose nodes from popular cloud platforms:

    * [m7g.xlarge](https://aws.amazon.com/ec2/instance-types/#General_Purpose) from Amazon AWS;

    * [c3-standard-4](https://cloud.google.com/compute/all-pricing#c3_standard_machine_types) from Google Cloud;

    * [Standard_D4_v3](https://learn.microsoft.com/en-us/azure/virtual-machines/dv3-dsv3-series#dv3-series) from Microsoft Azure.

4. The [components of the Soveren Agent](../overview/#soveren-agent) are entirely self-sufficient. For instance, you don't need expertise in Kafka for our [messaging and processing system](../traffic-processing/) to operate; we handle everything.

## Traffic analysis

1. We exclusively analyze HTTP traffic.

2. If the internal cluster traffic is encrypted with a service mesh (Istio or Linkerd), we automatically recognize and monitor it.

3. The requests must have the `content-type` properly set, namely:

    * `application/json`: our preferred mode of operation;

    * `application/x-www-form-urlencoded`: we also recognize form data.

4. Both the request and response, as well as the resulting request/response pair, must be under 1 Mb in size. Anything larger is excluded from processing.

5. It's acceptable for JSON or form payloads to be compressed (e.g., gzipped), provided the resulting size doesn't exceed 1 Mb (otherwise, they're also not processed).

## Resource usage

The components of the Soveren Agent exhibit varied resource usage patterns. Here's the general rule for all of them: the more resources you can allocate, the faster the data map will be built. In extreme cases, there might be restarts of some components, but they only affect the data map building time — not the core functionality of Soveren, and certainly not your cluster's stability.

* [Interceptors](../traffic-interception/) often utilize 100% of the allocated CPU [resources](../../administration/configuring-agent/#interceptors) as they aggressively attempt to capture all the available traffic. The memory they consume is used for storing the raw `tcp` packets while assembling the request/response pairs. However, the amount of resources allocated to the Interceptors only affects the time it takes to capture enough representative traffic to build a comprehensive data map. The more resources you can allocate, the faster the map will be built, and vice versa.

Remember that the Interceptors are present on each node (they are a `DaemonSet`). To get the full picture, you need to multiply their `requests` (and `limits`!) by the number of nodes in the cluster. However, the actual load on a particular Interceptor is heavily influenced by the amount of requests and the payloads it is collecting.

* [Digger](../traffic-processing/) is usually larger than any of the Interceptors, but there's only one instance of Digger in the cluster. Digger requires memory to read the collected payloads from Kafka, process them, and send the results to the Soveren Cloud. If the cluster is sizable and the load is high, then resource usage will be noticeable, reaching the `limits` that [you've set](../../administration/configuring-agent/#digger). If this situation persists, we recommend increasing the limits — however, as with the Interceptors, this should only affect the time it takes to build the data map.

* [Kafka](../../administration/configuring-agent/#kafka) also exists as a single instance per cluster. It is more memory-hungry than Digger because it needs to hold all the traffic that Soveren handles until it is processed by Digger and other components.

* [Detection-tool](../../administration/configuring-agent/#detection-tool) is the most resource-intensive component of the Soveren Agent because it hosts the data detection model. There is also one instance per cluster. It's not unusual for it to consume 1 CPU and 2 Gb of memory — this is the benchmark for the most resources that the Soveren Agent can consume even under moderate load.

The detection-tool processes only a portion of the traffic — the part that [Digger samples and sends for data detection](../traffic-processing/#url-clustering-sampling-and-data-detection). Because of this, the data map needs some time to build.