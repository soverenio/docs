Quick start
===========

...Work in progress


Deployment
----------

Soveren gateway supports Kubernetes for deployment.

Requirements
^^^^^^^^^^^^

1. `Kubernetes <hhttps://kubernetes.io/docs/setup/>`_.
2. Soveren token to set up Soveren gateway.

.. admonition:: Tip
   :class: tip

   You can find your Soveren token in your Soveren account. If you don't yet have a Soveren account, `get one <https://soveren.io/sign-up>`_.

Configure and deploy
^^^^^^^^^^^^^^^^^^^^

1. Add your Soveren token to your Kubernetes cluster.
   ``kubectl create secret generic soveren-proxy-token --from-literal=token=123e4567-e89b-12d3-a456-426655440000``

2. Set up your upstream: configure Soveren Gateway to proxy traffic to your services.

3. Set up Soveren gateway using our manifest file.
   ``kubectl apply -f https://github.com/soverenio/smat/…``

4. Run a livecheck and reroute your traffic.

Livecheck
^^^^^^^^^

Log in to your Soveren account and check tha Soveren proxy is on.


Reroute your traffic
^^^^^^^^^^^^^^^^^^^^

Route traffic from your services to Soveren Gateway.

.. admonition:: Tip
   :class: tip

   Read `deployment options <deployment-options.html>`_ to understand the best way to integrate Soveren gateway into your perimeter and reroute your traffic.










