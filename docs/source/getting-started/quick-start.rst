Quick start
===========

Soveren consists of two parts: Soveren gateway that lives on prem and Soveren cloud that lives in the cloud. If you need more information on that, read the `solution details <concepts.html>`_.

When ready, go through the simple installation process below.


Installation
------------

You need to install Soveren gateway within your perimeter. Soveren gateway supports Kubernetes.

Requirements
^^^^^^^^^^^^

1. `Kubernetes <https://kubernetes.io/docs/setup/>`_.
2. Soveren token to set up Soveren gateway.

.. admonition:: Tip
   :class: tip

   You can find your Soveren token in your Soveren account. If you don't yet have a Soveren account, `register one <https://soveren.io/sign-up>`_.

Configure, install, and set up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Add your Soveren token to your Kubernetes cluster:

   ``kubectl create secret generic soveren-proxy-token --from-literal=token=<soveren_token_from_your_account_on_soveren.io>``

2. Set up your upstream: configure Soveren gateway to proxy traffic for your services.

3. Install and set up Soveren gateway using our manifest file:

   ``kubectl apply -f https://github.com/soverenio/smat/<path_to_the_manifest_file>``

Reroute your traffic
^^^^^^^^^^^^^^^^^^^^

Route traffic from your services to Soveren gateway. You know the best your infrastructure and can decide how to position Soveren gateway against your system services and edge router/proxy if you have one.

.. admonition:: Tip
   :class: tip

   Read `auto live check and fallback plan <fallback.html>`_. in case Soveren gateway fails and you need to reroute your traffic on the spot.