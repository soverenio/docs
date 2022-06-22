# Quick start

Installing Soveren is extremely simple:

1. Install the Soveren Agent in your Kubernetes cluster

2. [Go to dashboards](https://app.soveren.io/pii-types) in the Soveren Cloud and start getting insights!


## Installing the Agent

1. [Create a new Soveren token](../../administration/managing-agents#create-an-agent) and have it handy for the following steps. The token identifies and authorizes your Agent within the Soveren Cloud.
 

2. Create a namespace for Soveren installation:
    ```shell
    kubectl create namespace soverenio
    ```
   You can use any other valid namespace name instead of `soverenio`.


4. Add the Soveren Helm repository:
    ```shell
    helm repo add soveren https://soverenio.github.io/helm-charts
    ```

5. Install the Soveren Agent using the `<TOKEN>` that you obtained on the step 1:
    ```shell
    helm install -n soverenio soveren-agent soveren/soveren-agent --set digger.token="<TOKEN>"
    ```
   You can use any other valid release name instead of `soveren-agent`.


7. That's it! You may [go to dashboards](https://app.soveren.io/pii-types) now.

   Also you may want to check the [description of available dashboards](../../dashboards/overview).

## What happens under the hood

There are several things which happen automatically in the cluster when you apply the manifest.

2. The Soveren Agent is deployed into the namespace `soverenio`. The Soveren Agent contains the Interceptors and the Personal Data Detector (which itself consists of several components).
3. For the Soveren Agent to be able to read relevant information from the Kubernetes API, the following happens:
     * A dedicated `ServiceAccount` is created for the Personal Data Detector
     * This `ServiceAccount` is given [cluster-wide permissions](https://github.com/soverenio/deployment/blob/master/interceptor/base/digger-sa-crb.yaml) (`ClusterRoleBinding`) to `view`