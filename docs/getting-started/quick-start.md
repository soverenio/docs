# Quick start

Installing Soveren is really simple:


    1. [Create a new Soveren token](../../administration/managing-gateways#create-a-gateway), copy the Soveren token displayed next to it and have it handy for the following steps.
     
    2. Make sure you export the `TOKEN` as an environment variable:
    
            export TOKEN="<soveren-token>"
    
    3. Apply the Soveren manifest:     

            kubectl apply -k https://github.com/soverenio/deployment.git/interceptor/base
    
    4. Add the Soveren token to your Kubernetes cluster.

            kubectl -n soveren-interceptor create secret generic soveren-token --from-literal=token=${TOKEN:?}
    
    5. That's it! [Go to the dashboards](https://app.soveren.io/pii-types) and start getting insights.

        Also, check the [description of available dashboards](../../dashboards/overview).
