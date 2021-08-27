Quick start guide
=================

Here’s what you need to get started with Soveren:

1. Register a new `Soveren account <https://soveren.io/sign-up>`_.

2. Go to your `account settings <https://soveren.io/account/api-key>`_, find and copy your Soveren token.

3. Add the Soveren token to your Kubernetes cluster.

Currently, Soveren only supports Kubernetes deployments. For other deployment options contact us at support@soveren.io.

::

     kubectl create secret generic soveren-proxy-token --from-literal=token=<soveren-token-from-your-account-on-soveren.io>

4. Apply the Soveren Gateway manifest:

::

     kubectl apply -f https://github.com/soverenio/smat/<path-to-the-manifest-file>

5. Сonfigure Soveren Gateway to proxy the traffic for your services
Edit the ``replicator`` ConfigMap and set the ``url`` parameter in the section ``services`` to point to your service:

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

   Soveren Gateway is based on Traefik. Refer the `Traefik routing section <https://doc.traefik.io/traefik/routing/overview/>`_ if you need more routing options.

6. Configure your services to route traffic to Soveren Gateway.

Refer to the `deployment scheme <deployment.html>`_ for more details on how the deployment is structured.

7. That's it! `Go to the dashboards <https://soveren.io/dashboard>`_ and start getting insights.

Check the `description of available dashboards <../dashboards/dashboards.html>`_.
