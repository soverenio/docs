.. toctree::
   :hidden:

   getting-started/quick-start
   getting-started/deployment
   dashboards/dashboards
   administration/throubleshooting

.. raw:: html

    <!-- Hotjar Tracking Code for https://docs.soveren.io/ -->
    <script>
        (function(h,o,t,j,a,r){
            h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
            h._hjSettings={hjid:2580378,hjsv:6};
            a=o.getElementsByTagName('head')[0];
            r=o.createElement('script');r.async=1;
            r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
            a.appendChild(r);
        })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
    </script>


Introduction
-------------

Soveren helps uncover personally identifiable information, also known as PII or personal data, in structured API flows. Throughout this documentation, we will be using PII and personal data interchangeably.

Soveren monitors and parses traffic between the services, identifying personal information along with its sensitivity, with sensitivity graded in accordance with the consequences that might arise if that information was leaked or used inappropriately.
Preconfigured dashboards provide a view into risks related to PII so that engineering and security leaders can make informed security and privacy decisions.

.. panels::
    :card: shadow

    .. link-button:: getting-started/quick-start
       :type: ref
       :text: Quick start guide
       :classes: btn-link stretched-link font-weight-bold

    .. div:: text-muted

        :opticon:`book` Configure and deploy Soveren Gateway in 5 minutes

    ---

    .. link-button:: getting-started/deployment
        :type: ref
        :text: Deployment
        :classes: btn-link stretched-link font-weight-bold

    .. div:: text-muted

        :opticon:`book` Learn how to fit Soveren Gateway in your perimeter

How Soveren works
-----------------

Soveren has a hybrid architecture:

* Soveren Gateway is a box solution installed in the client’s perimeter. It parses structured HTTP JSON traffic, extracts PIIs and sends metadata to the cloud.
* Soveren Cloud is a SaaS and managed by Soveren. It provides dashboards to gain visibility into different PII-related statistical data and metrics.

.. image:: /images/architecture/architecture-concept-latest.jpg
   :width: 900


Soveren Gateway
^^^^^^^^^^^^^^^
Soveren Gateway is a box solution. It is deployed on premise as a pre-packaged container and configured to receive the relevant part of inter-service HTTP API requests.
The Gateway then processes those requests asynchronously and extracts PII from the payloads.

Metadata about the requests is collected and sent to Soveren Cloud.
The metadata contains information about how the payload was structured (what fields), which PII types were detected, and which services were involved in the communication.
No part of the actual payload contents is included in the metadata.

Technically, the Gateway consists of a standard proxy (a `Traefik <https://doc.traefik.io/traefik/>`_ fork), messaging system (`Apache Kafka <https://kafka.apache.org/documentation/>`_), and analytics component which detects PII based on custom machine learning algorithms.

Soveren Cloud
^^^^^^^^^^^^^

Soveren Cloud is a SaaS. It is deployed in the cloud by Soveren.
It offers a set of dashboards that provide various views into the metadata collected by Soveren Gateway.
That includes analytics and stats on which PIIs have been observed and how sensitive they are, what services are involved, and what are the potential limitations in the API structure from the privacy standpoint.






