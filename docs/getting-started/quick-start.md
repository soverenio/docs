# Quick start

=== "Kubernetes"

    1. Add the Soveren token to your Kubernetes cluster.

         [Register an account](https://app.soveren.io/sign-up), copy the Soveren token from the **Let's get started** page, and run:
      
            kubectl create secret generic soveren-proxy-token --from-literal=token=<soveren-token-from-your-account-on-soveren.io>

         <div class="admonition tip">
         <p class="admonition-title">Tip</p>
         <p>You only see your Soveren token once, on the **Let's get started** page. If you missed it, [create a new gateway](https://app.soveren.io/gateways) and get back to Step #1.
         
         Currently, Soveren only supports Kubernetes and Docker Compose deployments. For other deployment options, contact us at [support@soveren.io](mailto:support@soveren.io).</p>
         </div>

    2. Apply the Soveren gateway manifest and configmap:     

            kubectl apply -f https://raw.githubusercontent.com/soverenio/deployment/master/gateway/kubernetes/install.yaml -f https://raw.githubusercontent.com/soverenio/deployment/master/gateway/kubernetes/replicator-configmap.yaml
    
    3. Сonfigure Soveren gateway to proxy the traffic for your services. <a name="configure-soveren"></a>

          Edit the ``replicator`` configmap and set the ``url`` parameter in the section ``services`` to point to your service:

             kubectl edit cm replicator

          `replicator` configmap example:

               # Add the service
               services:
                 upstream:
                   loadBalancer:
                     servers:
                       - url: http://address-of-your-service:port/

          <div class="admonition tip">
          <p class="admonition-title">Tip</p>
          <p>Soveren gateway is based on Traefik. Refer to the [Traefik docs](https://doc.traefik.io/traefik/routing/overview/) if you need more routing options.</p>
          </div>
          

    4. Configure your services to route traffic to Soveren gateway.

          <div class="admonition note">
          <p class="admonition-title">Note</p>
          <p>The gateway analyzes only JSON-formatted data in requests/responses body. Other data formats are proxied but not analyzed.</p>
          </div>
          

    5. That's it! [Go to the dashboards](https://app.soveren.io/pii-types) and start getting insights.

          <div class="admonition tip">
          <p class="admonition-title">Tip</p>
          <p>Check the [description of available dashboards](../../dashboards/overview).</p>
          </div>

          

=== "Docker Compose"

    1. Clone the repo containing the configuration files:
          ```
          git clone https://github.com/soverenio/deployment
          ```
          
          <div class="admonition note">
          <p class="admonition-title">Note</p>
          <p>Currently, Soveren only supports Kubernetes and Docker Compose deployments. For other deployment options, contact us at [support@soveren.io](mailto:support@soveren.io).</p>
          </div>

         

    2. Add the Soveren token to Docker.

          [Register an account](https://app.soveren.io/sign-up), copy the Soveren token from the **Let's get started** page, and run:
          
          ```
          export token=‘<soveren-token-from-your-account-on-soveren.io>’
          ```
         
         <div class="admonition tip">
         <p class="admonition-title">Tip</p>
         <p>You only see your Soveren token once, on the **Let's get started** page. If you missed it, [create a new gateway](https://app.soveren.io/gateways) and get back to Step #1.</p>
         </div>          
          
    3. Сonfigure Soveren gateway to proxy the traffic for your services.

          Edit the `configs/traefik_configs/conf.d/20-replicator.yaml` config and set the `url` parameter in the section `services` to point to your service:

          `20-replicator` config example:
       
             # Add the service
             http:
               services:
                 upstream:
                   loadBalancer:
                     servers:
                       - url: http://address-of-your-service:port/

          <div class="admonition tip">
          <p class="admonition-title">Tip</p>
          <p>Soveren gateway is based on Traefik. Refer to the [Traefik docs](https://doc.traefik.io/traefik/routing/overview/) if you need more routing options.</p>
          </div>

    4. Apply the Soveren gateway manifest running the command below in the `compose` repo folder:

          ```
          docker-compose up -d
          ```         

    5. Configure your services to route traffic to Soveren gateway.

          <div class="admonition note">
          <p class="admonition-title">Note</p>
          <p>The gateway analyzes only JSON-formatted data in requests/responses body. Other data formats are proxied but not analyzed.</p>
          </div>
         
    6. That's it! [Go to the dashboards](https://app.soveren.io/pii-types) and start getting insights.

          <div class="admonition tip">
          <p class="admonition-title">Tip</p>
          <p>Check the [description of available dashboards](../../dashboards/overview).</p>
          </div>       
