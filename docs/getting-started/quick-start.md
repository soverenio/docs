# Quick start

Currently, Soveren gateway supports deployment with Kubernetes and Docker Compose. If you're eager to test the gateway using a different technology, contact us at support@soveren.io.

Using Kubernetes gives you the benefits of a Kubernetes cluster, while using Docker Compose allows you to deploy a gateway image directly on any server.

=== "Kubernetes"

    1. Add the Soveren token to your Kubernetes cluster.

         [Create a gateway](../../administration/managing-gateways#create-a-gateway), copy the Soveren token displayed next to it, and run: 
      
            kubectl create secret generic soveren-proxy-token --from-literal=token=<soveren-token-for-the-gateway>    
         
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


          Soveren gateway is based on Traefik. Refer to the [Traefik docs](https://doc.traefik.io/traefik/routing/overview/) if you need more routing options.
          
          

    4. Configure your services to route traffic to Soveren gateway.

          Soveren gateway only analyzes traffic with the `application/json` content type. All other content types just pass through the gateway without any personal data detection.
          

    5. That's it! [Go to the dashboards](https://app.soveren.io/pii-types) and start getting insights.


          Also, check the [description of available dashboards](../../dashboards/overview).


          

=== "Docker Compose"

    1. Clone the repo containing the configuration files:
          ```
          git clone https://github.com/soverenio/deployment
          ```

    2. Add the Soveren token to Docker.

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

    5. Configure your services to route traffic to Soveren gateway.

          Soveren gateway only analyzes traffic with the `application/json` content type. All other content types just pass through the gateway without any personal data detection. 

    6. That's it! [Go to the dashboards](https://app.soveren.io/pii-types) and start getting insights.

          Also, check the [description of available dashboards](../../dashboards/overview).
