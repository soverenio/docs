.. raw:: html

    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-TCK46V7');</script>
    <!-- End Google Tag Manager -->

Administration
==============

Logs
----

Logging is enabled by default for Soveren gateway components, at the ``INFO`` level, including information, warning, error, and critical error events.

You may want to unload logs to check the following:
    * Proxy:
       * Proxied traffic
       * Proxy configuration errors
       * Received Apache Kafka events
    * Digger:
       * Soveren token validity, to send analysis metadata to Soveren cloud
       * Errors preparing the proxied traffic for the PII detection service
    * PII detection service:
       * Prepared traffic received for PII analysis
       * PII analysis errors

To unload logs, run:

.. tab:: Kubernetes

   Proxy:

   ::

          kubectl -n boxy logs service/traefik-proxy > traefik-proxy.log

.. tab:: Docker Compose

   Digger:

   ::

          docker-compose logs digger > digger.log

   Proxy:

   ::

          docker-compose logs traefik > traefik-proxy.log

   Kafka:

   ::

          docker-compose logs digger > kafka.log


Proxy settings
--------------

The proxy is part of Soveren gateway and serves as an edge router for client's traffic.
Technically, it is a Traefik fork with an added middleware.

Here's how what you need to know to set up the proxy.


SSL termination
^^^^^^^^^^^^^^^

The proxy supports HTTPS protocol over an encrypted SSL/TLS connection.
You  can enable SSL termination adding a TLS certificate, even when the proxy is already running, to the dynamic configuration in the [[tls.certificates]] section.

For example:
::

       # Dynamic configuration
        tls:
          certificates:
            - certFile: /path/to/domain.cert
              keyFile: /path/to/domain.key
            - certFile: /path/to/other-domain.cert
              keyFile: /path/to/other-domain.key

Update process
--------------

Work in progress...







