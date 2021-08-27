.. toctree::
   :hidden:

   getting-started/quick-start
   getting-started/deployment
   dashboards/dashboards
   administration/throubleshooting



Intoduction
-----------

Soveren helps uncover personal information (PII) in structured API flows.
It monitors and parses traffic between the services, and identifies personal information along with its sensitivity, meaning the consequences that might arise if that information was leaked or used inappropriately.
Preconfigured dashboards provide a view into company's risks related to PII so that engineering and security leaders could make informed security and privacy decisions.


How Soveren works
-----------------

Soveren has a hybrid architecture:

* Soveren Gateway is installed on premise, in the client’s perimeter. It parses structured HTTP JSON traffic, extracts PIIs and sends metadata to the cloud.
* Soveren Cloud provides dashboards to gain visibility into different PII-related statistical data and metrics.

.. image:: /images/architecture/architecture-diagram-small.jpg
   :width: 900


Soveren Gateway
^^^^^^^^^^^^^^^
Soveren Gateway is deployed on premise as a pre-packaged container and configured to receive the relevant part of inter-service HTTP API requests.
The Gateway then processes those requests asynchronously and extracts PII from the payloads.
Metadata about the requests is collected and sent to Soveren Cloud.
The metadata contains information about how the payload was structured (what fields), what sorts of PIIs were detected, what services were involved in the communication.
No part of actual payload contents is included into the metadata.

Technically, the Gateway consists of a standard proxy (a `Traefik <https://doc.traefik.io/traefik/>`_ fork), messaging system (`Apache Kafka <https://kafka.apache.org/documentation/>`_) and analytics component which detects PII based on custom machine learning algorithms.

Soveren Cloud
^^^^^^^^^^^^^

Soveren Cloud is a SaaS service managed by Soveren.
It offers a set of dashboards that provide various views into the metadata collected by Soveren Gateway.
That includes analytics and stats on what PIIs have been observed and how sensitive they were, what services were involved, what were the potential caveats in the API structure from the privacy standpoint.






