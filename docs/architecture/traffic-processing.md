# Digger: traffic processing

## Overview

The incoming traffic is processed by the processing and messaging system, utilizing Kafka as a central hub for message aggregation and Digger, a component developed by Soveren, as the primary logical processor.

Interceptors [write](../traffic-interception/#interceptor-operation) the collected request/response pairs to Kafka. Subsequently, Digger reads these pairs, enriches them with Kubernetes metadata, and forwards samples to the sensitive data detection component to gather detection results. Digger then removes all actual values from the data, replacing them with format-preserving placeholders, and transmits the resulting metadata to the Soveren Cloud.

## Digger operation

The simplified main flow of the Digger is outlined below:

![The main flow of the Digger](../../img/architecture/digger-flow.png "The main flow of the Digger")

Let's dive into more details of how Digger works:

1. Several goroutines read the request/response pairs from the Kafka topics and process them (see the steps below). When the processing of an individual pair is finished and the resulting metadata is sent to the Soveren Cloud, the goroutine moves the respective offset in Kafka.

    * Digger makes sure that Kafka topics don't consume too much space and trims them as necessary, depending on the load and the resources available for processing

2. Sources and destinations of requests are available to Digger. The processor looks up those sources and destinations in the cache that is [independently populated with actual  Kubernetes metadata](../k8s-metadata/) (names, namespaces, labels etc)

    * If the Kubernetes metadata is not available in the cache at the moment, the processing is put on hold for some time. If during that time the new data arrives in the cache, the processing is notified about that.

    * If the metadata was ultimately not available, the pair still moves on into further steps of processing because even without verbose names and labels the payload data can still be inspected for its potential sensitivity.

3. Digger sends the pair to Detection-tool for data detection and its inspection for sensitivity. Depending on the load and hence on the amount of request/response pairs, Digger employs the following sampling mechanism before sending:

    * Each new (previously unobserved) URL is inspected unconditionally

    * If this URL has already been observed, then samples from that URL are sent for detection only once in a while, depending on the load. Under really stressed conditions, it can take up to 6 hours for re-evaluation of this URL's data

4. Digger collects the results of detection from Detection-tool 

5. Values in the pair's payloads are replaced with placeholders (`*` for letters, `1` for digits) while punctuation symbols like commas and special symbols like `@` are left intact. Basically, this preserves the value formatting while stripping away all actual data.

6. The processed pair is then serialized into protobuf and sent to the Soveren Cloud over a bi-directional gRPC connection which Digger and Soveren Cloud maintain at all times. The rate of communication is capped at about 10 requests per second. The data that cannot be sent because of this limit is discarded, excluding the information of previously unobserved URLs (these data is sent unconditionally).

7. Digger also sends to the cloud a stream of heartbeats from the Agent components, as well as metrics that are collected from all of them. Those metrics give us visibility into the Agent healthiness and performance.

8. Basic traffic counters like number of observed calls are also maintained by the Digger and sent to the Soveren Cloud. Those counters take into account the data that was sampled out or dropped because of high load, or trimmed from Kafka topics, so total numbers are very close to what has been actually seen by the Agent.