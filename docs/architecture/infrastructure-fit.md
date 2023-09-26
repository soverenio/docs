# Infrastructure fit: requirements and recommendations

How well will Soveren fit into your technical infrastructure? There are several key aspects that you need to consider when evaluating Soveren.

!!! danger "Must-haves for Soveren to work are Kubernetes and HTTP/JSON"

    At present, the Soveren Agent only works in Kubernetes and monitors only HTTP traffic with JSON payloads (setting the correct `content-type` is crucial). These are necessities for Soveren to run and start providing insights.

## Deployment

1. **Kubernetes version 1.21 and higher**: these are the versions that Soveren has been tested with. It can operate on older versions, but functionality may be suboptimal.

2. **We use Helm for deployment**. However, clients often adapt our charts to integrate the resulting manifests into their own deployment systems.

3. **4 CPU, 16 Gb nodes**. We [optimized](../../administration/configuring-agent/#resource-limits) our `limits` for nodes of this size. These are standard general-purpose nodes from popular cloud platforms:

    * Google Cloud: [c3-standard-4](https://cloud.google.com/compute/all-pricing#c3_standard_machine_types);

    * Amazon AWS: [m7g.xlarge](https://aws.amazon.com/ec2/instance-types/#General_Purpose);

    * Microsoft Azure: [Standard_D4_v3](https://learn.microsoft.com/en-us/azure/virtual-machines/dv3-dsv3-series#dv3-series).

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

The components of the Soveren Agent exhibit diverse resource usage patterns. The guiding principle for all of them is: the more resources allocated, the quicker the data map construction. In extreme scenarios, some components might restart. While this impacts the data map building duration, it doesn't affect the core functionality of Soveren or the stability of your cluster.

### Interceptors

[Interceptors](../traffic-interception/) use a significant portion of the allocated CPU [resources](../../administration/configuring-agent/#interceptors) as they aggressively capture all available HTTP traffic. The CPU usage by Interceptors is directly influenced by the requests per second (RPS) of the traffic.

The memory consumed by Interceptors is primarily for storing packets while assembling the request/response pairs. Thus, their MEM usage is tied to the size of requests.

Here's the typical resource usage pattern of Interceptors:

320Mbit/sec, low RPS:

![Interceptors, 320Mbit, low RPS](../../img/architecture/interceptors-load-320mbit-lowrps.png "Interceptors, 320Mbit, low RPS")

1500Mbit/sec, high RPS:

![Interceptors, 1500Mbit, high RPS](../../img/architecture/interceptors-load-1500mbit-highrps.png "Interceptors, 1500Mbit, high RPS")

So basically during the traffic burst Interceptors consume a lot while capturing the traffic, then their usage go back to the low levels.

Keep in mind that Interceptors exist on every node as a `DaemonSet`. To understand the complete resource impact, multiply their `requests` (and `limits`) by the total number of nodes in the cluster.


### Digger

[Digger](../traffic-processing/) is usually larger than any of the Interceptors, but there's only one instance of Digger in the cluster. Digger requires memory to read the collected payloads from Kafka, process them, and send the results to the Soveren Cloud. If the cluster is sizable and the load is high, then resource usage will be noticeable, reaching the `limits` that [you've set](../../administration/configuring-agent/#digger). If this situation persists, we recommend increasing the limits — however, as with the Interceptors, this should only affect the time it takes to build the data map.

### Kafka

[Kafka](../../administration/configuring-agent/#kafka) also exists as a single instance per cluster. It is more memory-hungry than Digger because it needs to hold all the traffic that Soveren collects until it is processed by Digger and other components.

### Detection-tool

[Detection-tool](../../administration/configuring-agent/#detection-tool) is the most resource-intensive component of the Soveren Agent because it hosts the data detection model. There is also one instance per cluster. It's not unusual for it to consume 1 CPU and 2 Gb of memory — this is the benchmark for the most resources that any of the Soveren Agent components can consume even under moderate load.

The detection-tool processes only a portion of the traffic — the part that [Digger samples and sends for data detection](../traffic-processing/#url-clustering-sampling-and-data-detection). Because of this, the data map needs some time to build.