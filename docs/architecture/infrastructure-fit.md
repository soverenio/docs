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

The components of the Soveren Agent exhibit diverse resource usage patterns. The guiding principle for all of them is: the more resources allocated, the more efficiently the data map is constructed. In extreme scenarios, some components might restart. While this impacts the duration of data map building, it doesn't affect the core functionality of Soveren or the stability of your cluster.

To better understand how many resources you should allocate to the Soveren Agent, consider the following simple load testing scenario:

Assume the testing dataset consists of relatively small requests (around 8KB each). Send these requests at varying rates to the echo server within the cluster hosting the Soveren Agent.

Below is the resource usage graph for the Soveren Agent components under the described scenario:

![Soveren Agent under stepped load](../../img/architecture/load-agent-summary.png "Soveren Agent under stepped load")

First, there is no traffic at all till about 07:30. Then the load increases at the following rate:

* 500 RPS for 20 minutes: 07:30-07:50

* 1500 RPS for 10 minutes: 07:50-08:00

* 3000 RPS for 10 minutes: 08:00-08:10

* 1500 RPS for 20 minutes: 08:10-08:30

After 08:30, the load drops to zero.

Let's examine in detail how the individual components of the Soveren Agent handle this load.

### Interceptors

[Interceptors](../traffic-interception/) use [resources](../../administration/configuring-agent/#interceptors) according to their main goal to aggressively capture all available HTTP traffic. The CPU usage by Interceptors is directly influenced by the requests per second (RPS) of the traffic.

The memory consumed by Interceptors is primarily for storing packets while assembling the request/response pairs. Thus, their MEM usage is tied to the size of requests.

Based on the scenario described above, here's the pattern we observe:

![Interceptors stepped load profile](../../img/architecture/load-interceptor.png "Interceptors stepped load profile")

We can see that Interceptors are more affected by RPS than by volume, especially since the volume is small in this test.

When hitting 3000 RPS, the Interceptors start to max out on their resources. There are clear jumps in both CPU and memory use. Also, in very high traffic situations, they might restart.

So basically during the traffic burst Interceptors consume a lot while capturing the traffic, then their usage go back to the low levels. And under no circumstances they will go beyond the assigned `limits` — they rather will skip a portion of the traffic if deprived of resources.

Keep in mind that Interceptors exist on every node as a `DaemonSet`. To understand the complete resource impact, multiply their `requests` (and `limits`) by the total number of nodes in the cluster.

### Kafka

[Kafka](../../administration/configuring-agent/#kafka) is set up as one instance for each cluster. It uses a lot of memory since it stores all the traffic Soveren collects until Digger and other parts process it.

Here's how Kafka uses resources in the scenario we talked about:

![Kafka stepped load profile](../../img/architecture/load-kafka.png "Kafka stepped load profile")

Kafka's resource use depends on both how many request/response pairs (RPS) there are and how big they are (volume). Even with low traffic, Kafka keeps some memory ready so it can quickly manage new data coming in.

From the above, we can see that Kafka uses more CPU when there's more RPS, because it has to deal with more request/response pairs. The CPU use is still pretty low overall. Memory use, though, goes up steadily until it has stored all the data. After two hours, any old data that hasn't been processed gets cleared out.

It's important to know that Kafka will stick to its [set](../../administration/configuring-agent/#kafka) `limits`. If it gets close to its max capacity, Kafka will clean up by removing the oldest pairs.

### Digger

Digger typically requires [more resources](../../administration/configuring-agent/#digger) than any of the Interceptors, but there's only one instance of Digger in the cluster.

Digger requires memory to read the collected payloads from Kafka, [process](../traffic-processing/) them, and send the results to the Soveren Cloud. If the cluster is large and the load is significant, resource usage will become noticeable, reaching the `limits` that [you've set](../../administration/configuring-agent/#digger). However, Digger will never breach the assigned `limits`.

Here's the resource usage of Digger in the scenario described above:

![Digger stepped load profile](../../img/architecture/load-digger.png "Digger stepped load profile")

To understand how Digger and the Detection-tool behave as traffic increases, it's essential to consider the [sampling mechanism](.../traffic-processing/#url-clustering-sampling-and-data-detection). In essence, Digger evaluates the frequency of data from a specific URL undergoing data detection and then samples based on the total requests under the given load.

When traffic for a previously unobserved URL arrives, it goes through the entire pipeline, including detection. Since all the data is unique and requires processing, sampling isn't activated yet. Digger retrieves the data from Kafka, does minimal processing on its end, and forwards the data to the Detection-tool, which handles the more intensive tasks.

To break it down:

* With unique traffic, Digger does minimal processing. This period lasts until about 07:50, marked by low and consistent CPU usage.

* From around 07:50 to 08:45, the traffic begins to feature recurring URLs. Digger then has the task of categorizing them, activating the sampling mechanism. This task demands more CPU power, leading to spikes up to the predefined limits. Detection-tool receives minimal data during this time.

* After categorizing the recurring URLs, Digger resumes sending data samples to detection, again using minimal CPU.

The resource usage of Digger is influenced more by the number of request/response pairs stored in Kafka, the uniqueness of URLs associated with those pairs, and their sizes, rather than direct traffic metrics like RPS.

The above scenario really pushes Digger to its limits: with all the traffic repeating at a very high RPS, Digger ends up doing a lot of work. Typically, the mix of unique and non-unique data is more even, leading to steady and moderate CPU usage.

### Detection-tool

[Detection-tool](../../administration/configuring-agent/#detection-tool) is the most resource-intensive component of the Soveren Agent because it hosts the data detection model. There is also one instance per cluster.

Detection-tool processes only a portion of the traffic — the part that [Digger samples and sends for data detection](../traffic-processing/#url-clustering-sampling-and-data-detection). Because of this, the data map needs some time to build.

Lets' look at the resource consumption of Detection-tool in the given scenario:

![Detection-tool stepped load profile](../../img/architecture/load-detection-tool.png "Detection-tool stepped load profile")

When you look at the graphs, Detection-tool operates in exact contrast to [Digger](#digger):

* With unique traffic, Detection-tool needs to handle a lot of processing, leading to high CPU usage, often reaching its limits.

* For non-unique traffic, since not much data is forwarded to detection, CPU usage remains low.

* The CPU doesn't show spikes based on RPS. This is because Detection-tool consistently processes a set number of request/resource pairs handed over by Digger in limited streams.

* Memory doesn't fluctuate much either, mainly because the traffic has fairly similar and small payloads in this example. Most of the usage we see comes from the model's built-in features, with a minor increase due to the data structures being analyzed.

* Detection-tool caps the number of `JSON` keys processed by different sections of its embedded machine learning model, giving us more control over memory needs. But remember, memory use might be higher than shown in this graph, as we purposefully kept both the key count and value sizes low for this test.

The way Detection-tool uses resources stays pretty much the same, no matter if there's a lot or a little traffic, both in terms of RPS and volume. It's because Detection-tool is always working on a continuous stream of request/resource pairs provided by Digger. So, its performance doesn't waver with traffic changes; it only depends on whether there are pairs left in the [processing and messaging system](../traffic-processing/).

It's typical for Detection-tool to use 1 CPU and over 1 Gb of memory. This is the highest resource use you'll see from any Soveren Agent component, even with just a regular load. But, like all parts, it sticks to the [defined](../../administration/configuring-agent/#detection-tool) `limits`.

