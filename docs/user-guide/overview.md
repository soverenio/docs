# Overview

## Dashboards summary

Soveren provides [a number of dashboards](https://app.soveren.io/). Most of them should be self explanatory, but in a nutshell here's what you find on them:

* **Overview** which shows last events, how many events there were, discovered data types, most sensitive assets and most common data type combinations

* **Data map** ...

* **Assets** ...

* **Events** ...

* **Data types** ...

* **Violations** ...

## How Soveren works with your data

* Soveren Agent does not send any personal data outside your environment. Everything that you see on the dashboards is just metadata about what the Agent observed in your environment. For example, which service has been calling what other service, which sensitive data types were present — without any actual data.

* In the metadata that we show on the dashboards, we mask textual and numerical and complex data types so that you can see what sort of data was actually there from the form of it. This masking is done in your perimeter and sent to the Soveren Cloud as part of the metadata.

* The dashboards give you an overview of the last 7 days. Data older than 7 days is discarded.

* Sometimes you may see calls to hosts and endpoints that don't actually exist in your environment, resulting in response codes 4xx or 5xx. These are made by robots crawling the internet or by hackers trying to find vulnerabilities in the internet resources.
