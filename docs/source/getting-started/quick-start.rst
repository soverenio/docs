Quick start guide
=================

Here’s what you need to get started with Soveren:

.. admonition:: Note
   :class: note

   Currently, Soveren gateway available for installation in your Kubernetes cluster. For other deployment options contact us at support@soveren.io.

1. Register
^^^^^^^^^^^

Register a new `Soveren account <https://soveren.io/sign-up>`_.

2. Copy token
^^^^^^^^^^^^^
Go to your `account settings <https://soveren.io/account/api-key>`_, find and copy your Soveren token.

3. Add token to K8s cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Add the token key to the Kubernetes cluster:

::

     kubectl create secret generic soveren-proxy-token --from-literal=token=<soveren-token-from-your-account-on-soveren.io>

4. Apply configuration
^^^^^^^^^^^^^^^^^^^^^^
Apply Soveren Gateway configuration using the preconfigured manifest file:

::

     kubectl apply -f https://github.com/soverenio/smat/<path-to-the-manifest-file>

5. Сonfigure Soveren Gateway to proxy traffic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Сonfigure Soveren Gateway to proxy traffic for your services: edit the ``replicator`` ConfigMap and set the ``url`` parameter in the section ``services`` to point to your service:

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

6. Configure your service(s)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configure your service(s) to route traffic to Soveren Gateway.

Refer to the `deployment scheme <deployment.html>`_ for more details on how the deployment is structured.

7. Check the dashboard
^^^^^^^^^^^^^^^^^^^^^^

That's it! `Go to the dashboards <https://soveren.io/dashboard>`_ and start getting insights.

Check the `description of available dashboards <../dashboards/dashboards.html>`_.
