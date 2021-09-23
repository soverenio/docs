Administration
==============

Logs
----


Metrics
-------

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

# Dynamic configuration

   ::

          tls:
            certificates:
              - certFile: /path/to/domain.cert
                keyFile: /path/to/domain.key
              - certFile: /path/to/other-domain.cert
                keyFile: /path/to/other-domain.key














