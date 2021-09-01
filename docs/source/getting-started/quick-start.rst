.. raw:: html

    <!-- Hotjar Tracking Code for https://docs.soveren.io/ -->
    <script>
        (function(h,o,t,j,a,r){
            h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
            h._hjSettings={hjid:2580378,hjsv:6};
            a=o.getElementsByTagName('head')[0];
            r=o.createElement('script');r.async=1;
            r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
            a.appendChild(r);
        })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
    </script>

Quick start guide
=================

Here’s what you need to get started with Soveren:

1. Register a new `Soveren account <https://app.soveren.io/sign-up>`_.

2. Go to your `account settings <https://app.soveren.io/get-started>`_, find and copy your Soveren token.

3. Add the Soveren token to your Kubernetes cluster.

   .. admonition:: Note
      :class: note

      Currently, Soveren only supports Kubernetes deployments. For other deployment options, contact us at support@soveren.io.

   ::

        kubectl create secret generic soveren-proxy-token --from-literal=token=<soveren-token-from-your-account-on-soveren.io>

4. Apply the Soveren Gateway manifest:

   ::

        kubectl apply -f https://github.com/soverenio/smat/<path-to-the-manifest-file>

5. Сonfigure Soveren Gateway to proxy the traffic for your services.

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

      Soveren Gateway is based on Traefik. Refer to the `Traefik docs <https://doc.traefik.io/traefik/routing/overview/>`_ if you need more routing options.

6. Configure your services to route traffic to Soveren Gateway.

   .. admonition:: Tip
      :class: tip

      Refer to the `deployment scheme <deployment.html>`_ for more details on how the deployment is structured.

7. That's it! `Go to the dashboards <https://app.soveren.io/pii-types>`_ and start getting insights.

   .. admonition:: Tip
      :class: tip

      Check the `description of available dashboards <../dashboards/dashboards.html>`_.
