# Introduction

Soveren discovers [sensitive information](user-guide/data-model/), such as PII (personally identifiable information, or just personal data), PHI (health information), PCI (card data) or developers secrets, in structured API flows.

Soveren discovers services in a Kubernetes cluster, parses the traffic flowing between them and into or out of the cluster. We identify data types present in those flows, and grade their sensitivity according to consequences that might arise if that data was leaked or used inappropriately.

Preconfigured dashboards provide a view into the discovered data and risks related to it, so that engineering and security leaders can make informed security and privacy decisions.

## How Soveren works

Soveren has a hybrid architecture:

* Soveren Agent is [installed](getting-started/quick-start/) in your perimeter. It intercepts and parses structured HTTP JSON traffic, gathers metadata about sensitive data types it dicsovers, and sends the metadata to the Soveren Cloud.
* [Soveren Cloud](https://app.soveren.io/) is a SaaS managed by Soveren. It provides dashboards to gain visibility into sensitive data flows, as well as summary statistics and metrics.

### Soveren Agent

Soveren Agent is [deployed](getting-started/quick-start/) on premise and [configured](administration/configuring-agent/) to analyze the relevant part of inter-service HTTP API requests and responses that have the `application/json` content type. The Agent processes them asynchronously and gathers metadata about PII from the payloads.

The Soveren Agent consists of several parts:

* **Interceptors** which are distributed to all worker nodes of the cluster through the DaemonSet. They capture the traffic from virtual interfaces of the pods with the help of a packet capturing mechanism;
* **Messaging system** which receives data from the Interceptors. Consists of a [Kafka](https://kafka.apache.org/) instance (stores request/response data) and Digger (passes data to the detection and further to the Soveren Cloud)
* **Sensitive Data Detector** (or simply Detector) which discovers data types and their sensitivity with the help of proprietary machine learning algorithms.

Metadata about the requests and responses is sent to Soveren Cloud. This metadata contains information about how the payload was structured (what fields), which sensitive data types were detected, and which services were involved in the communication. No part of the actual payload values is included in the metadata.

### Soveren Cloud

[Soveren Cloud](https://app.soveren.io/) is a SaaS managed by Soveren. It offers [a set of dashboards](user-guide/overview/) that provide various views into the metadata collected by Soveren Agent. There are analytics and stats on which relevant data types have been observed and how sensitive they were, what services were involved, were there any violations of pre-set policies and configurations in terms of allowed data types.
