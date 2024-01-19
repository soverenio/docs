# Quick start

!!! warning "Please read through the requirements and recommendations"

    Before you proceed with the installation of the Soveren Sensor, we strongly recommend reviewing our [requirements and recommendations page](../../architecture/infrastructure-fit/)

Installing Soveren is extremely simple:

1. Install the Soveren Sensor in your Kubernetes cluster

2. [Go to the Soveren app](https://app.soveren.io/) in the Soveren Cloud and start getting insights!


## Installing the Sensor

1. [Create a new Soveren token](../../administration/managing-sensors#creating-sensors) and have it handy for the following steps. The token identifies and authorizes your Sensor within the Soveren Cloud.
 

2. Create a namespace for Soveren installation:
    ```shell
    kubectl create namespace soverenio
    ```
   You can use any other valid namespace name instead of `soverenio`.


4. Add the Soveren Helm repository:
    ```shell
    helm repo add soveren https://soverenio.github.io/helm-charts
    ```

5. Install the Soveren Sensor using the `<TOKEN>` that you obtained on the step 1:
    ```shell
    helm install -n soverenio soveren-agent soveren/soveren-agent --set digger.token="<TOKEN>"
    ```
   You can use any other valid release name instead of `soveren-agent`.


7. That's it! You may [go to the Soveren app](https://app.soveren.io/) now and check [the dashboards](../../user-guide/overview/).

For more advanced configuration options please take a look at the [configuration page](../../administration/configuring-sensor/).

## What happens under the hood

There are several things which happen automatically in the cluster when you install the Soveren Sensor:

1. Soveren Sensor contains Interceptors, Processing and messaging system, and Sensitive data detector. (More details in the [Architecture section](../../architecture/overview/#soveren-sensor)).

2. All components of Soveren Sensor are deployed into the namespace `soverenio`. 

3. Soveren Sensor subscribes to [a lot of metadata from the Kubernetes API](../../architecture/k8s-metadata/). A dedicated `ServiceAccount` is created. This `ServiceAccount` is given [cluster-wide permissions](https://github.com/soverenio/helm-charts/blob/master/charts/soveren-agent/templates/digger-rbac.yaml) (`ClusterRoleBinding`) to `get`, `list` and `watch` on several `apiGroups`.

4. Interceptors do not need special Kubernetes RBAC permissions to capture the traffic.

5. Interceptors read data from virtual network interfaces of the host. For this, the containers in which Interceptors are running require [privileged mode](../../administration/securing-sensor/#components-that-do-traffic-interception).
