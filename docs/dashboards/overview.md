# Overview

Soveren provides a number of dashboards that address the following questions:

* What personal data types are collected?
* Which data types are the most important?
* Which data collections are the most risky/sensitive?
* Which systems collect the data?
* Where is personal data in the API schema?
* Which services have access to personal data?
* Which APIs provide access to personal data?
* Which data is revealed in the calls?

When you visit [your Soveren account](https://app.soveren.io/pii-types) you first see an overview of the personal data detected in your environment and the gateways created for your account.

![PII dashboard](../../img/dashboards/pii-types-overview.jpg "PII dashboard")

The gateway status next to your account name shows how many gateways you created and which of them you have actually set up and connected to your environment.

The tabs are dashboard groups that give you a deeper view into the data grouping it by:

* *PII types* detected in your environment. See the [currently supported types](../../dashboards/pii-model/).
* *Endpoints* represent all events with a unique combination of a Host header, URL, and HTTP request method.
* *Hosts* that host the endpoints; determined by the Host header value in a request or response.
* *Consumers* that call the endpoints for data. A consumer is determined by the client's IP address in the header.


Important details about the content that you may see on the dashboards:

* Soveren gateway does not send any personal data outside your environment, so everything you see on the dashboards is just metadata about the data analyzed in your environment.
* The dashboards give you an overview of the last 7 days. Data older than 7 days is discarded.
* Sometimes you may see calls to hosts and endpoints that don't actually exist in your environment, resulting in response codes 4xx or 5xx. These are made by robots crawling the internet or by hackers trying to find vulnerabilities in the internet resources.
* In API call details, you may see an empty request or response, or both if the detection component failed to find any personal data or if masking the found data failed. You may also see empty JSON body `{}` for the requests and/or responses with the content-type not supported by Soveren gateway (currently, everything other than `application/json`). 




















