# Overview of Soveren's functionality

Soveren provides [several views](https://app.soveren.io/), most of which are self-explanatory. Here is a brief summary of what you can find on them. The pictures below are examples to convey the general idea; they are regularly updated to reflect the ongoing product enhancements.

## Dashboard

The overview [Dashboard](https://app.soveren.io/overview) offers a [7-day summary of statistics](#how-soveren-works-with-your-data), highlighting recent activities in your infrastructure. It displays important recent events, the number of events during the period, discovered data types, the most sensitive [services](#services), and the most common [data type](#data-types) combinations.

The statistics show the current counts of events, services, endpoints, etc., and highlight changes compared to the [previous period](#how-soveren-works-with-your-data).

The sensitivity of each discovered data type is indicated by color: red signifies high sensitivity, yellow indicates moderate sensitivity, and green suggests low sensitivity — unless combined with other data types, increasing the overall sensitivity.

![Dashboard: summary](../../img/user-guide/dashboard-01.png "Dashboard: summary")

![Dashboard: services and data type combinations](../../img/user-guide/dashboard-02.png "Dashboard: services and data type combinations")

## Data map

The [data map](https://app.soveren.io/data-map) provides a high-level view of your landscape. It displays all clusters where you've deployed Soveren Sensors, including all [services](#services) that Soveren has identified, as well as external connections.

![Data map](../../img/user-guide/data-map-01.png "Data map")

There are numerous filtering options and toggles on the map, which help in creating focused views of different parts of the infrastructure. Additionally, there is a visual representation of sensitive data types that have been detected in the services and flows.

![Filtering on the data map](../../img/user-guide/data-map-02.png "Filtering on the data map")

You can also delve into individual services to examine their specific data flows and API endpoints:

![Flows on the data map](../../img/user-guide/data-map-03.png "Flows on the data map")

## Services

### Service catalog

Soveren builds a [service catalog](https://app.soveren.io/service-catalog/) while scanning traffic. This catalog includes services communicating through data flows, which may contain sensitive information. These services are not only data concentration points but are also actively interacting in real-time.

For instance, within your Kubernetes cluster, you might find services like:

![Services](../../img/user-guide/services.png "Services")

There are also external connections that these services make with third parties, such as data providers or consumers, under data processing agreements. Additionally, there might be bots scanning your resources periodically (e.g., search engine crawlers), or users accessing your applications through web browsers or mobile apps.

External connection parties can also be viewed as services, but with different properties:

![External connections](../../img/user-guide/external-connections.png "External connections")

### Service details

You can delve into individual services to examine associated data flows and [API endpoints](#api-endpoints).

The summary provides basic information about the service:

![Service summary info](../../img/user-guide/service-summary.png "Service summary info")

Data flows represent interactions with other services:

![Service data flows](../../img/user-guide/service-data-flows.png "Service data flows")

Each data flow entails multiple interactions with various API endpoints:

![Service data flow details](../../img/user-guide/service-data-flow-details.png "Service data flow details")

The service lists API endpoints that are actively called by other services:

![Service API endpoints](../../img/user-guide/service-api-endpoints.png "Service API endpoints")

### External connection details

Similar views are available for external connections:

Summary of the external connection:

![External connection summary info](../../img/user-guide/external-connection-summary.png "External connection summary info")

Data flows in the external connection represent its interactions with services:

![External connection data flows](../../img/user-guide/external-connection-data-flows.png "External connection data flows")

Each external connection data flow also involves multiple interactions with different [API endpoints](#api-endpoints):

![External connection data flow details](../../img/user-guide/external-connection-data-flow-details.png "External connection data flow details")

Recipients of the external connection include IP addresses and user agents that facilitate communication between services and the external connection:

![External connection recipients](../../img/user-guide/external-connection-recipients.png "External connection recipients")

You can establish selected external connections into a custom category, for instance, by IP address. This newly created custom external connection will then be displayed separately on the data map, distinct from other external connections:

![Custom external connection](../../img/user-guide/external-connection-custom.png "Custom external connection")

## API endpoints

API endpoints are essentially interfaces exposed or utilized by services for data exchange, including sensitive data.

The APIs of individual services are accessible in their detailed views. For convenience, we also present a comprehensive list of all API endpoints identified by Soveren in a separate view:

![API endpoints](../../img/user-guide/api-endpoints.png "API endpoints")

You can proceed to view a sample of data flowing to or from the endpoint:

![API endpoint sample: detected types](../../img/user-guide/api-endpoint-sample.png "API endpoint sample: detected types")

## Data storages

Currently, Soveren includes support for S3 buckets, Kafka clusters and PostgreSQL databases.

### S3 buckets

Browse the list of S3 buckets that Soveren has identified in your AWS account:

![S3 buckets list](../../img/user-guide/buckets-list.png "S3 buckets list")

Next, you can review the summary information for each bucket:

![S3 bucket summary info](../../img/user-guide/bucket-summary.png "S3 bucket summary info")

Objects stored in the bucket are grouped (or clustered) based on their key names and MIME types:

![S3 objects list](../../img/user-guide/bucket-files-01.png "S3 objects list")

Soveren analyzes samples from the bucket, running detections on their contents:

![S3 object samples](../../img/user-guide/bucket-files-02.png "S3 object samples")

You can then view a sample of the data stored in the bucket:

![S3 object sample: detected types, JSON](../../img/user-guide/bucket-sample-01.png "S3 object sample: detected types, JSON")

![S3 object sample: detected types, CSV](../../img/user-guide/bucket-sample-02.png "S3 object sample: detected types, CSV")

### Kafka

Browse the list of Kafka clusters that you've [configured for monitoring](../../administration/configuring-sensor/#kafka_1):

![Kafka clusters list](../../img/user-guide/kafka-clusters-list.png "Kafka clusters list")

Browse the list of topics that are available in the cluster:

![Kafka topics list](../../img/user-guide/kafka-topics-list.png "Kafka topics list")

### Databases

Browse the list of databases that you've [configured for monitoring](../../administration/configuring-sensor/#databases):

![Databases list](../../img/user-guide/databases-list.png "Databases list")

## Activity log

The [activity log](https://app.soveren.io/activity-log) records significant events identified by Soveren. These events can fall into [several categories](../../integration/event-objects/#event-types), notably including violations of predefined policies related to sensitive data exchanges. An example of such an event is the initial detection of a sensitive data type in a specific data flow.

Here is an example of what the activity log might include:

![Activity log](../../img/user-guide/activity-log.png "Activity log")

Most information in the activity log is accessible not only through the product's user interface but also via [integrations](../../integration/), such as webhooks or Slack alerts.

## Data types

[Data types](https://app.soveren.io/data-types) provide a summary of the sensitive data types that the Soveren Sensor has detected in your infrastructure. Soveren [supports numerous data types right out of the box](../data-model/), and the range of supported types is continually expanding.

Here's an example of what the data types view looks like:

![Data types](../../img/user-guide/data-types.png "Data types")

## Service groups

You have the option to combine selected services into a custom group, which will then be displayed as a distinct entity on the data map:

![Custom service group](../../img/user-guide/group.png "Custom service group")

## Policies

You can set up policies to automatically monitor which services or data sources are authorized to handle specific data types. Additionally, these policies can restrict the sharing of data with third parties.

![Policy configuration, part 1](../../img/user-guide/policy-01.png "Policy configuration, part 1")
![Policy configuration, part 2](../../img/user-guide/policy-02.png "Policy configuration, part 2")

## How Soveren works with your data

* The Soveren Sensor does not transmit any personal or sensitive data — in fact, any actual data — outside your environment. What you see on the dashboards is solely metadata about the activities the Sensor has observed. This includes, for example, which service has been communicating with another and what types of sensitive data were present, without including any of the actual data.

* In the metadata displayed on the dashboards, we mask textual, numerical, and complex data types. This allows you to discern the form of the data that was present without exposing the actual content. This masking is performed within your perimeter and the processed metadata is then sent to the Soveren Cloud.

* The dashboards provide an overview of the last 7 days. Data older than this period is automatically discarded.

* Occasionally, you may notice calls to hosts and endpoints that do not exist within your environment, resulting in 4xx or 5xx response codes. These are often generated by internet-crawling robots or hackers probing for vulnerabilities in online resources.