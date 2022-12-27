# Overview

## Dashboards summary

Soveren provides [a number of dashboards](https://app.soveren.io/). Most of them should be self explanatory, but in a nutshell here's what you find on them. Pictures below are just to convey a general idea, they are constantly updated along with all the product enhancements that we are doing.

### Overview

The [Overview](https://app.soveren.io/overview) provides you with [a 7-day summary stats](#how-soveren-works-with-your-data) about what has happened in your infrastructure. It shows last important events, how many events there were, discovered data types, the most sensitive assets and the most common data type combinations.

The numbers show how many events or assets or endpoints and such are there currently, and also there are changes with respect to the previous period (Soveren works in [7-day periods](#how-soveren-works-with-your-data), old data gets washed away as the time passes).

The sensitivity of each found data type is reflected with color: red means very sensitive, yellow means not so much, green means little to worry about _unless_ coupled with some other data types leading to increased sensitivity of a combination.

![Overview: summary](../../img/user-guide/overview-01.png "Overview: summary")
![Overview: assets and type combinations](../../img/user-guide/overview-02.png "Overview: assets and type combinations")

### Assets

[Assets](https://app.soveren.io/data-inventory/) are

### Data map

The [Data map](https://app.soveren.io/data-map) provides a view of your landscape

### Events

[Events](https://app.soveren.io/events) are

### Data types

[Data types](https://app.soveren.io/pii-types) are

### Violations

Violations are coming soon. They are

## How Soveren works with your data

* Soveren Agent does not send any personal or sentive data — in fact _any_ actual data — outside your environment. Everything that you see on the dashboards is just metadata about what the Agent observed. For example, which service has been calling what other service, which sensitive data types were present — without any actual data.

* In the metadata that we show on the dashboards, we mask textual and numerical and complex data types so that you can see what sort of data was actually there from the form of it. This masking is done in your perimeter and sent to the Soveren Cloud as part of the metadata.

* The dashboards give you an overview of the last 7 days. Data older than 7 days is discarded.

* Sometimes you may see calls to hosts and endpoints that don't actually exist in your environment, resulting in response codes 4xx or 5xx. These are made by robots crawling the internet or by hackers trying to find vulnerabilities in the internet resources.
