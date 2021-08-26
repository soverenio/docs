Quick start
===========

Soveren consists of two parts: Soveren Gateway that lives on prem and Soveren Cloud that lives in the cloud. If you need more information on that, read `Soveren overview <overview.html>`_.

When ready, go through the simple installation process below.


Installation
------------

You need to install Soveren Gateway within your perimeter. Currently, Soveren gateway available for installation in your Kubernetes cluster.
For other deployment options contact us at mailto: support@soveren.io.

Requirements
^^^^^^^^^^^^

`Kubernetes <https://kubernetes.io/docs/setup/>`_.

Configure, install, and set up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Create a Soveren account on <link-to-soveren>.

2. Visit account settings, find your Soveren token, and copy it.

3. Add your Soveren token to your Kubernetes cluster:

   ``kubectl create secret generic soveren-proxy-token --from-literal=token=<soveren-token-from-your-account-on-soveren.io>``

4. Сonfigure Soveren Gateway to proxy traffic for your services. Edit the ``replicator`` ConfigMap and set the ``url`` parameter in the section ``services`` to point to your service.

   ::

          # Add the service
          services:
            test-service:
              loadBalancer:
                servers:
                  - url: http://address-of-your-service:port/

   One of the ways to edit the ``replicator`` is via CLI:

   ``kubectl edit cm replicator``

   .. admonition:: Tip
      :class: tip

      ``services`` is an array of arbitrary size. You can add multiple instances of the same service adding more lines with the ``url`` parameter.

      For routing incoming traffic to multiple service of different types, read the `routing section of Traefik docs <https://doc.traefik.io/traefik/routing/overview/>`_.

5. Install and set up Soveren Gateway using our manifest file:

   ``kubectl apply -f https://github.com/soverenio/smat/<path-to-the-manifest-file>``

6. Reroute your traffic

Route traffic from your services to Soveren Gateway. You know your infrastructure the best and can decide how to position Soveren Gateway against your system services and edge router if you have one.

.. admonition:: Tip
   :class: tip

   Read `Deployment and fallback <fallback.html>`_. in case Soveren Gateway fails and you need to reroute your traffic on the go.

7. Visit your Soveren account <link-to-soveren-dashboard> and see the PIIs detected in your traffic, on the dashboard.