---
hide:
  - navigation
  - toc
---

# Quick start

!!! info "Please check our requirements and recommendations"

    Before you proceed with the installation, we recommend reviewing our [requirements and recommendations page](../../architecture/infrastructure-fit/)

In a nutshell, installing Soveren is extremely simple:

1. Install the Soveren Sensor in your Kubernetes cluster.

2. [Go to the Soveren app](https://app.soveren.io/) in the Soveren Cloud and start getting insights!

More detailed step-by-step procedure:

1. [Create a new Soveren token](../../administration/managing-sensors#creating-sensors) and have it handy for the following steps. The token identifies and authorizes your Sensor within the Soveren Cloud.


2. Create a namespace for Soveren installation:

    === "Data-in-motion (DIM)"
        ```shell
        kubectl create namespace soverenio
        ```

    === "Data-at-rest (DAR)"
        ```shell
        kubectl create namespace soverenio
        ```

    You can use any other valid namespace name instead of `soverenio`.


3. Add the Soveren Helm repository:
    ```shell
    helm repo add soveren https://soverenio.github.io/helm-charts
    ```


4. Install the Soveren Sensor using the `<TOKEN>` that you obtained in step 1:
    ```shell
    helm install -n soverenio soveren-agent soveren/soveren-agent --set digger.token="<TOKEN>"
    ```
   You can use any other valid release name instead of `soveren-agent`.


5. That's it! You may [go to the Soveren app](https://app.soveren.io/) now and check [the dashboards](../../user-guide/overview/).


For more advanced configuration options please take a look at the [configuration page](../../administration/configuring-sensor/). There is also a separate description of the [security options](../../administration/securing-sensor/).