# Architecture

Soveren is composed of two primary parts:

* **Soveren Sensor**: Deployed within the customer’s Kubernetes cluster, the sensors monitor and analyze calls between services for sensitive data, or connect to the customer’s S3 buckets, Kafka clusters, or database instances to detect the presence of sensitive data.
* **Soveren Cloud**: Hosted and managed by Soveren, this cloud platform offers user-friendly dashboards that visualize sensitive data flows and provide summary statistics and metrics.

Soveren Sensors collect metadata about data flows and data sources contents. The collected information is then relayed to the Soveren Cloud. Importantly, **the metadata does not include any actual values from payloads or data sources, i.e. no sensitive data is shared outside of the customer’s infrastructure**.

## Soveren Sensor

There are two types of Soveren Sensors:

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Data-in-motion (DIM) Sensor__

    ---

    Data-in-motion (DIM) Sensor monitors calls between services by intercepting and analyzing structured HTTP JSON traffic.

    [:octicons-arrow-right-24: DIM Sensor architecture](../dim/)

-   :material-database-search-outline:{ .lg .middle } __Data-at-rest (DAR) Sensor__

    ---

    Data-at-rest (DAR) Sensor monitors data sources such as S3 buckets, Kafka clusters or databases like PostgreSQL.

    [:octicons-arrow-right-24: DAR Sensor architecture](../dar/)

</div>

## Soveren Cloud

[Soveren Cloud](https://app.soveren.io/) is a Software as a Service (SaaS) managed by Soveren. It provides a suite of dashboards displaying various views of the metadata collected by Soveren Sensors. Users can view statistics and analytics on observed data types, their sensitivity, involved services and data stores, and any violations of predefined policies and configurations for allowed data types.

For Kubernetes clusters, Soveren discovers and builds a catalog of services running within the cluster, detailing their API endpoints and the flows through which they interact with each other. It also provides a list of external services communicating with the cluster. Each discovered service retains its Kubernetes metadata, enabling customers to filter and group by familiar elements such as namespaces and labels.

For data stores (S3, Kafka, or databases), Soveren discovers and catalogs the list of stored buckets, topics, or tables, along with metadata available from the provider (e.g., AWS), including location and security attributes.

Additionally, Soveren provides options to set up and maintain ownership and high-level grouping of services and data stores. For all services and data stores, Soveren identifies the list of data types discovered in the flows or in the storage. With this rich set of available metadata, customers can define policies regarding which services and data flows are permitted to work with particular data types. This capability unlocks a wide range of business cases in areas such as security, compliance, and engineering.

All data discovered and systematized by Soveren is available both in the UI and via integrations, allowing customers to monitor and automate their business scenarios.

The overview of the dashboards provided by Soveren Cloud is available [in the User Guide](../../user-guide/).
