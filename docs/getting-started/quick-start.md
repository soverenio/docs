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

1. First, the namespace `soveren-interceptor` is created
2. Then, Soveren Interceptors are deployed into that namespace
3. For Soveren Interceptors to be able to gather the traffic:
   * A dedicated `ServiceAccount` is created
   * This `ServiceAccount` is given cluster-wide permissions (`ClusterRoleBinding`) to execute `get`, `watch` and `list` on the pods
4. Finally, the Personal Data Detector is deployed:
   * A dedicated `ServiceAccount` is created as well, so that the Detector is able to listen to the Interceptors
   * This `ServiceAccount` is given cluster-wide permissions (`ClusterRoleBinding`) to `view` in the `soveren-interceptor` namespace