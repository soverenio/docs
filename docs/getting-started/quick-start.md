# Quick start

Installing Soveren is extremely simple:

1. Deploy the Soveren Sensor in your Kubernetes cluster using our [Helm chart](https://github.com/soverenio/helm-charts/).

2. [Go to the Soveren app](https://app.soveren.io/) in the Soveren Cloud and start getting insights!

## Step-by-step procedure

!!! info "Before you proceed with the installation, we recommend reviewing our [requirements and recommendations page](../../architecture/infrastructure-fit/)"

1. Decide which type of Soveren Sensor you need:

    === "Data-in-motion (DIM)"

        Discovers services in your Kubernetes clusters and identifies sensitive data in data flows between them.

    === "Data-at-rest (DAR)"

        Monitors data sources such as S3 buckets, databases, and Kafka clusters, and uncovers sensitive data stored within.

2. [Create a new Soveren token](../../administration/managing-sensors#creating-sensors) and have it handy for the following steps. This token identifies and authorizes your Sensor within the Soveren Cloud.


3. Create a namespace for Soveren installation:

    === "Data-in-motion (DIM)"

        ```shell
        kubectl create namespace soverenio
        ```

    === "Data-at-rest (DAR)"

        ```shell
        kubectl create namespace soverenio-dar-sensor
        ```

    You can use any other valid namespace name instead of `soverenio` or `soverenio-dar-sensor`.


4. Add the Soveren Helm repository:

    ```shell
    helm repo add soveren https://soverenio.github.io/helm-charts
    ```


5. Install the Soveren Sensor using the `<TOKEN>` that you obtained in step 1:

    === "Data-in-motion (DIM)"

        ```shell
        helm install -n soverenio soveren-agent soveren/soveren-agent --set digger.token="<TOKEN>"
        ```

    === "Data-at-rest (DAR)"

        ```shell
        helm install -n soverenio-dar-sensor soveren-dar-sensor soveren/soveren-dar-sensor --set crawler.token="<TOKEN>"
        ```

    You can use any other valid release name instead of `soveren-agent` or `soveren-dar-sensor`.

    A more convenient way to manage tokens is by specifying them in `values.yaml` as described in our [configuration gude](../../administration/configuring-sensor/#sensor-token).


6. That's it! You may [go to the Soveren app](https://app.soveren.io/) now and check [the dashboards](../../user-guide/overview/).


## Fine print

For more advanced configuration options please take a look at the [configuration page](../../administration/configuring-sensor/). There is also a separate description of the [security options](../../administration/securing-sensor/).