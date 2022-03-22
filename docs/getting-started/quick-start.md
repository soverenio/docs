# Quick start

Currently, Soveren gateway supports deployment with Kubernetes and Docker Compose. If you're eager to test the gateway using a different technology or having any problems, contact us at [support@soveren.io](mailto:support@soveren.io).



=== "Kubernetes"

    1. [Create a new Soveren gateway](../../administration/managing-gateways#create-a-gateway), copy the Soveren token displayed next to it and have it handy for the following steps.
    
    2. Define the namespace that you want to monitor in your Kubernetes cluster.
    
    3. Make sure you have two environment variables set up for the values of `TOKEN` and `NAMESPACE`:
    
            export NAMESPACE="<namespace-for-the-gateway-to-monitor>"
            export TOKEN="<soveren-token-for-the-gateway>"
    
    4. Add the Soveren token to your Kubernetes cluster.
      
            kubectl -n ${NAMESPACE:?} create secret generic soveren-proxy-token --from-literal=token=${TOKEN:?}
    
    5. Create a new service account:
    
            kubectl -n ${NAMESPACE:?} create serviceaccount soveren-digger

    6. Grant viewing rights to the created service account.
    
        This binding allows the Soveren gateway to discover information available from Kubernetes, for example about the request source.
    
            kubectl create clusterrolebinding soveren-digger-view --clusterrole=view --serviceaccount=${NAMESPACE:?}:soveren-digger

    7. Apply the Soveren gateway manifest and configmap:     

            kubectl apply -f https://raw.githubusercontent.com/soverenio/deployment/master/gateway/kubernetes/install.yaml -f https://raw.githubusercontent.com/soverenio/deployment/master/gateway/kubernetes/replicator-configmap.yaml
    
    8. Сonfigure Soveren gateway to proxy the traffic for your services. <a name="configure-soveren"></a>

          Edit the ``replicator`` configmap and set the ``url`` parameter in the section ``services`` to point to your service:

            kubectl edit cm replicator

          `replicator` configmap example:

               # Add the service
               services:
                 upstream:
                   loadBalancer:
                     servers:
                       - url: http://address-of-your-service:port/


          Soveren gateway is based on Traefik. Refer to the [Traefik docs](https://doc.traefik.io/traefik/routing/overview/) if you need more routing options. 

    9. Configure your services to route traffic to Soveren gateway.
    
          The gateway is available at `traefik-proxy:8090`. This is defined in the [manifest](https://github.com/soverenio/deployment/blob/master/gateway/kubernetes/install.yaml).
          
          Soveren gateway only analyzes traffic with the `application/json` content type. All other content types just pass through the gateway without any personal data detection.

    10. That's it! [Go to the dashboards](https://app.soveren.io/pii-types) and start getting insights.

          Also, check the [description of available dashboards](../../dashboards/overview).


          

=== "Docker Compose"

    <div class="admonition info">
    <p class="admonition-title">Requirements</p>
    <p>Soveren gateway supports Docker Compose v1.27.0 or higher.</p>
    </div>

    1. Clone the repo containing the configuration files:
          ```
          git clone https://github.com/soverenio/deployment
          ```

    2. Add the Soveren token to Docker Compose. 

          [Create a gateway](../../administration/managing-gateways#create-a-gateway), copy the Soveren token displayed next to it, and run: 
          
          ```
          export token=‘<soveren-token-from-your-account-on-soveren.io>’
          ```

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

          Soveren gateway is based on Traefik. Refer to the [Traefik docs](https://doc.traefik.io/traefik/routing/overview/) if you need more routing options.

    4. Apply the Soveren gateway manifest running the command below in the `compose` repo folder:

          ```
          docker-compose up -d
          ```         

    5. Configure your services to route traffic to Soveren gateway. The gateway listens on port `8090`.

          Soveren gateway only analyzes traffic with the `application/json` content type. All other content types just pass through the gateway without any personal data detection. 

    6. That's it! [Go to the dashboards](https://app.soveren.io/pii-types) and start getting insights.

          Also, check the [description of available dashboards](../../dashboards/overview).
