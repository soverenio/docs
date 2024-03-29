# Overview of Soveren's functionality

Soveren provides [several views](https://app.soveren.io/), most of which are self-explanatory. Here is a brief summary of what you can find on them. The pictures below are examples to convey the general idea; they are regularly updated to reflect the ongoing product enhancements.

## Dashboard

The overview [Dashboard](https://app.soveren.io/overview) offers a [7-day summary of statistics](#how-soveren-works-with-your-data), highlighting recent activities in your infrastructure. It displays important recent events, the number of events during the period, discovered data types, the most sensitive [services](#services), and the most common [data type](#data-types) combinations.

The statistics show the current counts of events, services, endpoints, etc., and highlight changes compared to the [previous period](#how-soveren-works-with-your-data).

The sensitivity of each discovered data type is indicated by color: red signifies high sensitivity, yellow indicates moderate sensitivity, and green suggests low sensitivity — unless combined with other data types, increasing the overall sensitivity.

![Dashboard: summary](../../img/user-guide/dashboard-01.png "Dashboard: summary")

![Dashboard: services and data type combinations](../../img/user-guide/dashboard-02.png "Dashboard: services and data type combinations")

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

## API endpoints

API endpoints are essentially interfaces exposed or utilized by services for data exchange, including sensitive data.

The APIs of individual services are accessible in their detailed views. For convenience, we also present a comprehensive list of all API endpoints identified by Soveren in a separate view:

![API endpoints](../../img/user-guide/api-endpoints.png "API endpoints")

## Data map

[Data map](https://app.soveren.io/data-map) provides a view into your landscape, where all assets that have been found by the Soveren Sensor are shown together. Those assets are split into the internal and external parts and connected by the flows.

![Data map](../../img/user-guide/data-map-01.png "Data map")

There are a number of filtering options and toggles on the map which help making focused views into different parts of the infrastructure. There is also a visual notion of sensitive data types that have been found in the assets and in the flows.

![Flow on the data map](../../img/user-guide/data-map-02.png "Flow on the data map")

You can also dive into individual assets to check their specific data flows and endpoints.

## Events

[Events](https://app.soveren.io/events) are literally some occurrences that Soveren has found and deemed as important. They may or may not lead to some violations of pre-defined rules regarding the sensitive data exchange (more on that later). An example of an event would be the first evidence of a sensitive type found in a particular data flow.

An example of the events view:

![Events](../../img/user-guide/events-01.png "Events")

## Data types

[Data types](https://app.soveren.io/pii-types) are a summary of sensitive types that the Soveren Sensor has observed in your infrastructure. Soveren [suppors a number of data types out of the box](../data-model/), and the set of supported types is constantly growing.

An example of the data types view:

![Data types](../../img/user-guide/data-types-01.png "Data types")

## Violations

This part of the product is coming really soon, stay tuned!

# How Soveren works with your data

* Soveren Sensor does not send any personal or sentive data — in fact _any_ actual data — outside your environment. Everything that you see on the dashboards is just metadata about what the Sensor has observed. For example, which service has been calling what other service, which sensitive data types were present — without any actual data.

* In the metadata that we show on the dashboards, we mask textual and numerical and complex data types so that you can see what sort of data was actually there from the form of it. This masking is done in your perimeter and sent to the Soveren Cloud as part of the metadata.

* The dashboards give you an overview of the last 7 days. Data older than 7 days is discarded.

* Sometimes you may see calls to hosts and endpoints that don't actually exist in your environment, resulting in response codes 4xx or 5xx. These are made by robots crawling the internet or by hackers trying to find vulnerabilities in the internet resources.
