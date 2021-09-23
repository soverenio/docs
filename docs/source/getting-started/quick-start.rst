.. raw:: html

    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-TCK46V7');</script>
    <!-- End Google Tag Manager -->

Quick start
===========

`Register an account <https://app.soveren.io/sign-up>`_, then get started with Soveren:

.. tab:: Kubernetes

    1. Add the Soveren token to your Kubernetes cluster.

       Go to your `Soveren account settings <https://app.soveren.io/get-started>`_, find and copy your Soveren token, and run:

       ::

            kubectl create secret generic soveren-proxy-token --from-literal=token=<soveren-token-from-your-account-on-soveren.io>


       .. admonition:: Note
             :class: note

             Currently, Soveren only supports Kubernetes deployments. For other deployment options, contact us at support@soveren.io

    2. Apply the Soveren gateway manifest and configmap:

       ::

            kubectl apply -f https://raw.githubusercontent.com/soverenio/deployment/master/gateway/kubernetes/install.yaml -f https://raw.githubusercontent.com/soverenio/deployment/master/gateway/kubernetes/replicator-configmap.yaml

    3. Сonfigure Soveren gateway to proxy the traffic for your services.

       Edit the ``replicator`` configmap and set the ``url`` parameter in the section ``services`` to point to your service:

       ::

            kubectl edit cm replicator

       ``replicator`` configmap example:

       ::

              # Add the service
              services:
                upstream:
                  loadBalancer:
                    servers:
                      - url: http://address-of-your-service:port/

       .. admonition:: Tip
          :class: tip

          Soveren gateway is based on Traefik. Refer to the `Traefik docs <https://doc.traefik.io/traefik/routing/overview/>`_ if you need more routing options.

    4. Configure your services to route traffic to Soveren gateway.

       .. admonition:: Tip
          :class: tip

          Refer to the `deployment scheme <deployment.html>`_ for more details on how the deployment is structured.

    5. That's it! `Go to the dashboards <https://app.soveren.io/pii-types>`_ and start getting insights.

       .. admonition:: Tip
          :class: tip

          Check the `description of available dashboards <../dashboards/dashboards.html>`_.

.. tab:: Docker Compose

   Work in progress...
