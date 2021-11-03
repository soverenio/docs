# Introduction

Soveren helps uncover personally identifiable information, also known as PII or personal data, in structured API flows. Throughout this documentation, we will be using PII and personal data interchangeably.

Soveren monitors and parses traffic between the services, identifying personal information along with its sensitivity, with sensitivity graded in accordance with the consequences that might arise if that information was leaked or used inappropriately.
Preconfigured dashboards provide a view into risks related to PII so that engineering and security leaders can make informed security and privacy decisions.

![PII dashboard](img/dashboards/pii-types-overview-cropped.png "PII dashboard")
-> Figure 1 <-

## How Soveren works

Soveren has a hybrid architecture:

* Soveren gateway is a pre-packaged container installed in your perimeter. It parses structured HTTP JSON traffic, gathers metadata about PII, and sends the metadata to the cloud.
* Soveren сloud is a SaaS managed by Soveren. It provides dashboards to gain visibility into different PII-related statistical data and metrics.

![Soveren architecture simplified](img/architecture/architecture-concept.jpg "Soveren architecture simplified")

### Soveren gateway

Soveren gateway is a pre-packaged container deployed on premise and configured to analyze the relevant part of inter-service HTTP API requests and responses that have the `application/json` content type. 
The gateway processes them asynchronously and gathers metadata about PII from the payloads.

Metadata about the requests and responses is collected and sent to Soveren сloud.
The metadata contains information about how the payload was structured (what fields), which PII types were detected, and which services were involved in the communication.
No part of the actual payload contents is included in the metadata.

Technically, the gateway consists of a standard proxy (a [Traefik](https://doc.traefik.io/traefik/) fork), messaging system ([Apache Kafka](https://kafka.apache.org/documentation/>)), and detection component, which discovers PII based on custom machine learning algorithms.
As shown in the diagram below, it can be deployed at different locations in your perimeter and can receive traffic from services that are deployed on any platform. 

![Integration options](img/architecture/integration.png "Integration options")

### Soveren сloud

Soveren сloud is a SaaS managed by Soveren.
It offers a set of dashboards that provide various views into the metadata collected by Soveren gateway.
That includes analytics and stats on which PIIs have been observed and how sensitive they are, what services are involved, and what the potential limitations in the API structure are from the privacy standpoint.
