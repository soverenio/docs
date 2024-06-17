# Architecture

Soveren is composed of two primary components:

* **Soveren Sensor**: Deployed within your Kubernetes cluster, the Sensor intercepts and analyzes structured HTTP JSON traffic. It collects metadata about data flows, identifying field structures, detected sensitive data types, and involved services. Importantly, the metadata **does not include any actual payload values**. The collected information is then relayed to the Soveren Cloud.
* **Soveren Cloud**: Hosted and managed by Soveren, this cloud platform presents user-friendly dashboards that provide visualization of sensitive data flows and summary statistics and metrics.

## Soveren Sensor

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Data-in-motion (DIM) Sensor__

    ---

    Data-in-motion (DIM)

    [:octicons-arrow-right-24: Getting started](dim/)

-   :material-database-search-outline:{ .lg .middle } __Data-at-rest (DAR) Sensor__

    ---

    Data-at-rest (DAR)

    [:octicons-arrow-right-24: Reference](dar/)

</div>

## Soveren Cloud

[Soveren Cloud](https://app.soveren.io/) is a Software as a Service (SaaS) managed by Soveren. It provides [a suite of dashboards](../../user-guide/overview/) displaying diverse views into the metadata collected by the Soveren Sensor. Users can view statistics and analytics on observed data types, their sensitivity, involved services, and any violations of predefined policies and configurations for allowed data types.
