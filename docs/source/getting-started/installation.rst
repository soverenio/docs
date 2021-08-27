Installation
============

`As you've learned <../index.html#how-soveren-works>`_, Soveren consists of two parts: Soveren Gateway that lives on prem and Soveren Cloud that lives in the cloud.

You need to install Soveren Gateway within your perimeter.

Currently, Soveren gateway available for installation in your Kubernetes cluster. For other deployment options contact us at support@soveren.io.

.. image:: ../images/architecture/deployment-scheme.png
   :width: 800


Requirements
------------

You need to install `Kubernetes <https://kubernetes.io/docs/setup/>`_.

Configure, install, and set up Soveren Gateway
----------------------------------------------

1. `Register a Soveren account <link-to-soveren>`_.

2. Go to your account settings, find and copy the API key (Soveren token).

3. Add the API key to the Kubernetes cluster:

   ::

          kubectl create secret generic soveren-proxy-token --from-literal=token=<soveren-token-from-your-account-on-soveren.io>

4. Install and set up Soveren Gateway using the preconfigured manifest file:

   ::

        kubectl apply -f https://github.com/soverenio/smat/<path-to-the-manifest-file>


5. Сonfigure Soveren Gateway to proxy traffic for your services: edit the ``replicator`` ConfigMap and set the ``url`` parameter in the section ``services`` to point to your service:

   ::

        kubectl edit cm replicator

   ``replicator`` ConfigMap example:

   ::

          # Add the service
          services:
            test-service:
              loadBalancer:
                servers:
                  - url: http://address-of-your-service:port/


   .. admonition:: Tip
      :class: tip

      You can add multiple instances of the same service adding more lines with the ``url`` parameter.

      For routing incoming traffic to multiple services of different types, read the `routing section of Traefik docs <https://doc.traefik.io/traefik/routing/overview/>`_.

6. Configure your service(s) to route traffic to Soveren Gateway. Nobody knows your infrastructure like you.

   Decide where to deploy Soveren Gateway against your system services and edge router/proxy if you have one. Take the example deployment scheme below as a reference and remember this is only one of the various options and doesn't include your service layout.

   .. admonition:: Tip
      :class: tip

      Read `Fallback plan <fallback.html>`_ for a fallback example.

7. `Go to the dashboard <link-to-soveren-dashboard>`_ and check the PIIs detected in your traffic and your compound risk score.

   .. image:: ../images/dashboard/pii-types-overview.png
      :width: 800