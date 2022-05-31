# Quick start

## Installing the Agent

Installing Soveren is really simple:

1. [Create a new Soveren token](../../administration/managing-gateways#create-a-gateway) and have it handy for the following steps.
 
2. Make sure you export the `TOKEN` as an environment variable:
    ```shell
    export TOKEN="<soveren-token>"
    ```

3. Apply the Soveren manifest:
    ```shell
    kubectl apply -k https://github.com/soverenio/deployment.git/interceptor/base
    ```

4. Add the Soveren token to your Kubernetes cluster:
    ```shell
    kubectl -n soveren-interceptor create secret generic soveren-token --from-literal=token=${TOKEN:?}
    ```

5. That's it! [Go to the dashboards](https://app.soveren.io/pii-types) and start getting insights.

    Also, check the [description of available dashboards](../../dashboards/overview).

## What happens under the hood

There are several things which happen automatically in the cluster when you apply the manifest.

1. First, the namespace `soveren-interceptor` is created.
2. Then, the Soveren Agent is deployed into that namespace. The Soveren Agent contains the Interceptors and the Personal Data Detector (which itself consists of several components).
3. For the Soveren Agent to be able to read relevant information from the Kubernetes API, the following happens:
     * Dedicated `ServiceAccount`s are created both for Interceptors and for the Personal Data Detector
     * `ServiceAccount` for Interceptors is given cluster-wide permissions (`ClusterRoleBinding`) to execute `get`, `watch` and `list` on the pods
     * `ServiceAccount` for the Personal Data Detector is given cluster-wide permissions (`ClusterRoleBinding`) to `view`