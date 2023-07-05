# Digger: traffic processing

## Overview

The incoming traffic is processed by the processing and messaging system, utilizing Kafka as a central hub for message aggregation and Digger, a component developed by Soveren, as the primary logical processor.

Interceptors [write](../traffic-interception/#interceptor-operation) the collected request/response pairs to Kafka. Subsequently, Digger reads these pairs, enriches them with Kubernetes metadata, and forwards samples to the sensitive data detection component to gather detection results. Digger then removes all actual values from the data, replacing them with format-preserving placeholders, and transmits the resulting metadata to the Soveren Cloud.

## Digger operation

The simplified main flow of the Digger is outlined below:

![The main flow of the Digger](../../img/architecture/digger-flow.png "The main flow of the Digger")

Let's dive into more details of how Digger works:

1. **Processing of request/response pairs:** Multiple goroutines read and process request/response pairs from Kafka topics. Upon completion of the processing for an individual pair and delivery of the resulting metadata to the Soveren Cloud, the respective offset in Kafka is updated by the goroutine. The Digger takes the responsibility of ensuring that Kafka topics don't overflow with data, thereby managing them by trimming as needed, contingent on the load and processing resources available.

2. **Processing of source and destination information:** The sources and destinations of requests are accessible to the Digger. These are looked up in a cache that is [populated independently with the current Kubernetes metadata](../k8s-metadata/) (names, namespaces, labels, etc). If the requisite Kubernetes metadata is absent from the cache, the processing is paused temporarily. If the new data lands in the cache during this interval, the processing resumes. However, if the metadata remains unavailable, the pair advances to the subsequent steps of processing, since the payload data can still be scrutinized for potential sensitivity, even in the absence of verbose Kubernetes names and labels.

3. **Detection-tool usage:** The Digger sends the pair to the Detection-tool for data detection and sensitivity inspection, and collects the results. Depending on the workload and, consequently, the volume of request/response pairs, the Digger adopts a specific sampling mechanism before forwarding the data. This includes unconditional inspection of each new (previously unseen) URL and occasional sampling of already observed URLs based on the load. In particularly stressful conditions, a URL's data re-evaluation may take up to 6 hours.

4. **Value substitution:** Values within the pair's payloads are replaced with placeholders (`*` for letters, `1` for digits) while punctuation symbols like commas and special symbols such as `@` remain intact. This approach maintains the value formatting while eliminating all actual data.

5. **Serialization and communication:** The processed pair is serialized into protobuf and delivered to the Soveren Cloud via a bi-directional gRPC connection that is continuously active between the Digger and the Soveren Cloud. The communication rate is capped at roughly 10 requests per second. Any data that cannot be sent due to this limit is discarded, with the exception of data relating to previously unobserved URLs, which are sent unconditionally.

6. **Transmitting metrics and health checks:** The Digger also dispatches a stream of heartbeats from the Agent components to the cloud, in addition to metrics collected from all of them. This provides visibility into the health and performance of the Agent.

6. **Traffic counter management:** Basic traffic counters like the number of observed calls are also managed by the Digger and relayed to the Soveren Cloud. These counters account for data that was either sampled out or discarded due to high load, or trimmed from Kafka topics, resulting in totals that closely reflect what the Agent has truly observed.
