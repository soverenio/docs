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

Proxy settings
--------------

The proxy is part of Soveren gateway and serves as an edge router for client's traffic.
Technically, it is a a `Traefik <https://doc.traefik.io/traefik/>`_ fork with an added middleware.

Here's how what you need to know to set up the proxy.


SSL termination
^^^^^^^^^^^^^^^

The proxy supports HTTPS protocol over an encrypted SSL/TLS connection.
You  can enable SSL termination by adding a TLS certificate, even when the proxy is already running, to the dynamic configuration in the ``tls {}`` section.

For example:
::

       http:
         routers:
           defaults:
             entryPoints:
               - web
             rule: PathPrefix(`/`)
             middlewares:
               - soveren
             service: upstream
             tls: {}

.. admonition:: Tip
   :class: tip

   To learn specific ``tls{}`` parameters fitting your case, and other encryption options, refer to `TLS <https://doc.traefik.io/traefik/https/tls/>`_ in Traeik documentation.
   To learn more about routing options in the context of SSL termination, refer to `Routers <https://doc.traefik.io/traefik/routing/routers/#tls>`_ in Traeik documentation.

.. tab:: Kubernetes

   To add a TLS certificate, edit the ``replicator`` configmap:

   ::

        kubectl edit cm replicator

.. tab:: Docker Compose

   1. Clone the repo containing the configuration files:

      ::

           git clone https://github.com/soverenio/deployment

   2. Edit the ``configs/traefik_configs/conf.d/30-routers.yaml`` configmap.


Update process
--------------

Soveren gateway
^^^^^^^^^^^^^^^
Once you know the update is out, we recommend you update Soveren gateway to the latest version.
Otherwise, your old version may lose connection with Soveren cloud that supports only the latest Soveren gateway version.

.. admonition:: Tip
   :class: tip

   At the early adopter stage, we personally let our adopters know when a new Soveren gateway version is out.


.. tab:: Kubernetes

   To update Soveren gateway, apply the Soveren gateway manifest:

   ::

       kubectl apply -f https://raw.githubusercontent.com/soverenio/deployment/master/gateway/kubernetes/install.yaml


.. tab:: Docker Compose

   To update Soveren gateway:

   1. Clone the repo containing the configuration files:

      ::

           git clone https://github.com/soverenio/deployment

   2. Apply the Soveren gateway manifest running the command below in the ``compose`` repo folder:

      ::

           docker-compose up -d


Soveren cloud
^^^^^^^^^^^^^

Soveren cloud is managed by the Soveren team and doesn't require updates from the user side.

.. admonition:: Tip
   :class: tip

   Soveren cloud supports only the latest Soveren gateway version. Learn how to update Soveren gateway above to avoid any incompatibility issues.





