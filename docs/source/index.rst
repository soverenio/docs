.. toctree::
   :hidden:

   getting-started/quick-start
   getting-started/integration-options
   administration/failover
   administration/administration
   administration/troubleshooting
   dashboards/dashboards

.. raw:: html

    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-TCK46V7');</script>
    <!-- End Google Tag Manager -->

.. raw:: html

  <style>
    .row.docutils {
      margin-left: -8px;
      margin-right: -8px;
    }

    .card.shadow.docutils {
      background-color: transparent !important;
      border: 1px solid #e5e9ef; /* Rock light 50 */
      border-radius: 6px;
      box-shadow: none !important;
      transition-duration: 200ms;
      transition-timing-function: ease-out;
      transition-property: box-shadow, background-color, border-color;
    }

    .card.shadow.docutils:hover {
      box-shadow: 0px 4px 40px rgba(10, 39, 99, 0.08),
        0px 16px 24px rgba(10, 39, 99, 0.02), 0px 2px 8px rgba(10, 39, 99, 0.04),
        0px 0px 1px rgba(10, 39, 99, 0.04) !important;
      border-color: transparent;
    }

    .card.shadow.docutils .card-body {
      padding: 24px 32px;
    }

    .card.shadow.docutils a.btn {
      font-style: normal;
      font-weight: normal !important;
      font-size: 18px;
      line-height: 24px;
      color: #232c40; /* Rock light 800 */
      padding: 0;
    }

    .card.shadow.docutils a.btn:hover {
      text-decoration: none;
    }

    .card.shadow.docutils .card-text {
      margin-bottom: 4px;
    }

    .card.shadow.docutils .text-muted {
      color: #6a768f !important; /* Rock light 400 */
    }

    @media (prefers-color-scheme: dark) {
      [data-theme=auto] .card.shadow.docutils {
        border-color: #192131; /* Rock dark 50 */
      }

      [data-theme=auto] .card.shadow.docutils:hover {
        background-color: #131a28 !important; /* Rock dark 25 */
      }

      [data-theme=auto] .card.shadow.docutils a.btn {
        color: #d7dadf; /* Rock dark 800 */
      }

      [data-theme=auto] .card.shadow.docutils .text-muted {
        color: #6f7c96 !important; /* Rock dark 400 */
      }
    }

    [data-theme=dark] .card.shadow.docutils {
      border-color: #192131; /* Rock dark 50 */
    }

    [data-theme=dark] .card.shadow.docutils:hover {
      background-color: #131a28 !important; /* Rock dark 25 */
    }

    [data-theme=dark] .card.shadow.docutils a.btn {
      color: #d7dadf; /* Rock dark 800 */
    }

    [data-theme=dark] .card.shadow.docutils .text-muted {
      color: #6f7c96 !important; /* Rock dark 400 */
    }

  </style>

Introduction
-------------

Soveren helps uncover personally identifiable information, also known as PII or personal data, in structured API flows. Throughout this documentation, we will be using PII and personal data interchangeably.

Soveren monitors and parses traffic between the services, identifying personal information along with its sensitivity, with sensitivity graded in accordance with the consequences that might arise if that information was leaked or used inappropriately.
Preconfigured dashboards provide a view into risks related to PII so that engineering and security leaders can make informed security and privacy decisions.

.. panels::
    :card: shadow

    .. link-button:: getting-started/quick-start
       :type: ref
       :text: Quick start
       :classes: btn-link stretched-link font-weight-bold

    .. div:: text-muted

        Configure and deploy Soveren gateway in 5 minutes

    ---

    .. link-button:: getting-started/integration-options
        :type: ref
        :text: Integration options
        :classes: btn-link stretched-link font-weight-bold

    .. div:: text-muted

        Learn how to fit Soveren gateway into your perimeter

How Soveren works
-----------------

Soveren has a hybrid architecture:

* Soveren gateway is a box solution installed in the client’s perimeter. It parses structured HTTP JSON traffic, extracts PIIs, and sends metadata to the cloud.
* Soveren сloud is a SaaS managed by Soveren. It provides dashboards to gain visibility into different PII-related statistical data and metrics.

.. image:: /images/architecture/architecture-concept.jpg
   :width: 900


Soveren gateway
^^^^^^^^^^^^^^^
Soveren gateway is a box solution. It is deployed on premise as a pre-packaged container and configured to receive the relevant part of inter-service HTTP API requests and responses.
The Gateway then processes those requests and responses asynchronously and extracts PII from the payloads.

Metadata about the requests and responses is collected and sent to Soveren сloud.
The metadata contains information about how the payload was structured (what fields), which PII types were detected, and which services were involved in the communication.
No part of the actual payload contents is included in the metadata.

Technically, the Gateway consists of a standard proxy (a `Traefik <https://doc.traefik.io/traefik/>`_ fork), messaging system (`Apache Kafka <https://kafka.apache.org/documentation/>`_), and analytics component which detects PII based on custom machine learning algorithms.

Soveren сloud
^^^^^^^^^^^^^

Soveren сloud is a SaaS. It is deployed in the cloud by Soveren.
It offers a set of dashboards that provide various views into the metadata collected by Soveren gateway.
That includes analytics and stats on which PIIs have been observed and how sensitive they are, what services are involved, and what are the potential limitations in the API structure from the privacy standpoint.