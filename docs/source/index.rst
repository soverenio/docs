.. toctree::
   :hidden:

   getting-started/installation
   getting-started/fallback
   administration/throubleshooting
   pii-detection/pii-types-and-sensitivity


What is Soveren?
----------------

Soveren helps uncover personal data in structured API flows. Soveren parses the traffic between services and identifies personal data along with its sensitivity, meaning the consequences that might arise if that data was leaked or used inappropriately.
Preconfigured dashboards provide a view into a company's risks related to personal data, so that engineering and security leaders could make informed security and privacy decisions.


It detects where personal data, or PII, is coming from, how it is consumed, and which services are involved.

It determines PII sensitivity both for standalone PIIs and combinations of different PII types.

It provides means to assess company's risks related to personal data and helps engineering and security leaders make informed security and privacy decisions.


How Soveren works
-----------------

Soveren has a hybrid architecture:

* Soveren Gateway is installed on premise, in the client’s perimeter. It parses structured HTTP JSON traffic, extracts PII and sends metadata to the cloud
* Soveren Cloud provides dashboards to gain visibility into different PII-related statistical data and metrics.

.. image:: /images/architecture/architecture-concept.png
   :width: 900


Soveren Gateway
^^^^^^^^^^^^^^^

Soveren Gateway is a box solution that is deployed within customer's perimeter, in a K8s cluster.

It gets part of the traffic and detects PIIs in it. Detecting PIIs, it forms metadata with all request details except the actual request payload data.

Architecture-wise, Soveren Gateway includes:

* A proxy
* A messaging system
* A PII detection service
* A service for URL clustering and relaying the metadata to Soveren Cloud

.. admonition:: Note
   :class: note

   Proxied traffic isn't delayed by PII detection, and Soveren Gateway doesn't increase latency in any significant way.

   Currently, Soveren supports PII detection in JSON traffic.


Soveren Cloud
^^^^^^^^^^^^^

Soveren Cloud is a SaaS hosted in the cloud.

It provides dashboards with insights into all sorts of data privacy related stats and metrics, including compound risk score, information about PII types and system APIs.

Next, proceed with the `installation guide <getting-started/installation.html>`_.






