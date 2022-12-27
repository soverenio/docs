# Overview

## Dashboards summary

Soveren provides [a number of dashboards](https://app.soveren.io/). Most of them should be self explanatory, but in a nutshell here's what you find on them. Pictures below are just to convey the general idea, they are constantly updated along with all the product enhancements that we are doing.

### Overview

The [Overview](https://app.soveren.io/overview) provides you with [a 7-day summary stats](#how-soveren-works-with-your-data) about what has happened in your infrastructure. It shows the latest important events, how many events there were during the period, what data types were discovered, the most sensitive [assets](#assets) and the most common [data type](#data-types) combinations.

The numbers show how many events or assets or endpoints and such are there currently, and they also display the changes with respect to the [previous period](#how-soveren-works-with-your-data).

The sensitivity of each found data type is shown with color. Red means pretty sensitive if disclosed, yellow means not so much, green means little to worry about _unless_ combined with some other data types leading to increased sensitivity of a combination.

![Overview: summary](../../img/user-guide/overview-01.png "Overview: summary")
![Overview: assets and type combinations](../../img/user-guide/overview-02.png "Overview: assets and type combinations")

### Assets

[Assets](https://app.soveren.io/data-inventory/) are places of data concentration that Soveren discovers in your infrastructure while looking into the traffic. They are communicating to each other through data flows which may or may not contain some sensitive data in them.

There are several types of assets: internal and external ones, and endpoints. Internal assets are found within your Kubernetes cluster, whereas external ones are located outside of it.

An example of the internal assets view:

![Internal assets](../../img/user-guide/assets-01.png "Internal assets")

An example of an external asset would be some third-party data provider or consumer that you communicate with under some data processing agreement. Or they can be robots which are scanning your resources from time to time (e.g. search engine crawlers), or they can be external users looking into your apps from their browsers or (mobile) applications.

An example of the external assets view:

![External assets](../../img/user-guide/assets-02.png "External assets")

Endpoints are essentially the APIs that are exposed or consumed by some other assets. They are points to which other assets connect and send or get some data, including sentitive data.

An example of the endpoints view:

![Endpoints](../../img/user-guide/assets-03.png "Endpoints")

You can further dive into individual assets to check the data flows and endpoints associated with them:

![Asset flows](../../img/user-guide/assets-04.png "Asset flows")
![Asset endpoints](../../img/user-guide/assets-05.png "Asset endpoints")

### Data map

[Data map](https://app.soveren.io/data-map) provides a view into your landscape, where all assets that have been found by the Soveren Agent are shown together. Those assets are split into the internal and external parts and connected by the flows.

![Data map](../../img/user-guide/data-map-01.png "Data map")

There are a number of filtering options and toggles on the map which help making focused views into different parts of the infrastructure. There is also a visual notion of sensitive data types that have been found in the assets and in the flows.

![Flow on the data map](../../img/user-guide/data-map-02.png "Flow on the data map")

You can also dive into individual assets to check their specific data flows and endpoints.

### Events

[Events](https://app.soveren.io/events) are literally some occurrences that Soveren has found and deemed as important. They may or may not lead to some violations of pre-defined rules regarding the sensitive data exchange (more on that later). An example of an event would be the first evidence of a sensitive type found in a particular data flow.

An axample of the events view:

![Events](../../img/user-guide/events-02.png "Events")

### Data types

[Data types](https://app.soveren.io/pii-types) are

### Violations

Violations are coming soon. They are

## How Soveren works with your data

* Soveren Agent does not send any personal or sentive data — in fact _any_ actual data — outside your environment. Everything that you see on the dashboards is just metadata about what the Agent observed. For example, which service has been calling what other service, which sensitive data types were present — without any actual data.

* In the metadata that we show on the dashboards, we mask textual and numerical and complex data types so that you can see what sort of data was actually there from the form of it. This masking is done in your perimeter and sent to the Soveren Cloud as part of the metadata.

* The dashboards give you an overview of the last 7 days. Data older than 7 days is discarded.

* Sometimes you may see calls to hosts and endpoints that don't actually exist in your environment, resulting in response codes 4xx or 5xx. These are made by robots crawling the internet or by hackers trying to find vulnerabilities in the internet resources.
