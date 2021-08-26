Quick start
===========

Soveren consists of two parts: Soveren Gateway that lives on prem and Soveren Cloud that lives in the cloud. If you need more information on that, read `Soveren overview <concepts.html>`_.

When ready, go through the simple installation process below.


Installation
------------

You need to install Soveren Gateway within your perimeter. Soveren Gateway supports Kubernetes.

Requirements
^^^^^^^^^^^^

1. `Kubernetes <https://kubernetes.io/docs/setup/>`_.
2. Soveren token to set up Soveren Gateway.

.. admonition:: Tip
   :class: tip

   You can find your Soveren token in your Soveren account. If you don't yet have a Soveren account, create one.

Configure, install, and set up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Add your Soveren token to your Kubernetes cluster:

   ``kubectl create secret generic soveren-proxy-token --from-literal=token=<soveren-token-from-your-account-on-soveren.io>``

2. Сonfigure Soveren Gateway to proxy traffic for your services. Edit the ``replicator`` ConfigMap and set the ``url`` parameter in the section ``services`` to point to your service.

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



3. Install and set up Soveren Gateway using our manifest file:

   ``kubectl apply -f https://github.com/soverenio/smat/<path-to-the-manifest-file>``

Reroute your traffic
^^^^^^^^^^^^^^^^^^^^

Route traffic from your services to Soveren Gateway. You know your infrastructure the best and can decide how to position Soveren Gateway against your system services and edge router if you have one.

.. admonition:: Tip
   :class: tip

   Read `Deployment and fallback <fallback.html>`_. in case Soveren Gateway fails and you need to reroute your traffic on the go.