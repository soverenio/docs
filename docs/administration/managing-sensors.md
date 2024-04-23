# Managing Sensors

Soveren Sensors are available in two variants:

1. Data-in-motion (DIM) sensor: Discovers services in your Kubernetes clusters and identifies sensitive data in data flows between them.

2. Data-at-rest (DAR) sensor: Monitors data sources such as S3 buckets, databases, and Kafka clusters, and uncovers sensitive data stored within.

## Creating Sensors

First you need to decide which type of Sensor do you need: a Data-in-motion (DIM) or Data-at-rest (DAR).

=== "Data-in-motion (DIM)"

    You can create DIM Sensors via the [sensors page](https://app.soveren.io/sensors/data-in-motion) in the Soveren app.

    ![Data-in-motion (DIM) Sensors](../../img/administration/sensors-dim.png "Data-in-motion (DIM) Sensors")

    You need to create separate Data-in-motion (DIM) Sensors for each Kubernetes cluster you want to monitor.

    Each Sensor is characterized by its `name` and `token`. You can also specify the `region` where your cluster is situated.

    If you have multiple clusters, and thus multiple Sensors, Soveren will display them separately on the [data map](https://app.soveren.io/data-map). The Sensor's name will define the name of the cluster on the data map.

=== "Data-at-rest (DAR)"

    You can create DAR Sensors via the [sensors page](https://app.soveren.io/sensors/data-at-rest) in the Soveren app.

    ![Data-at-rest (DAR) Sensors](../../img/administration/sensors-dar.png "Data-at-rest (DAR) Sensors")

    To monitor your data sources, such as S3 buckets, databases, and Kafka clusters, you will need at least one Data-at-rest (DAR) Sensor. While not mandatory, we recommend deploying separate sensors for different types of data sources to optimize monitoring efficiency.

    Each Sensor is characterized by its `name` and `token`.

### Name

For DIM sensors, the names influence how different Kubernetes clusters are displayed on the data map. For DAR sensors, the naming is primarily for management purposes and serves as an informative label.

You can automate the naming of your Soveren Sensors [in your configuration files](../configuring-sensor/).

### Token

The `token` allows the Soveren app to identify the Sensor during communication.

We [recommend](../configuring-sensor/#sensor-token) adding the `token` to your own configuration file, such as `values.yaml`, to simplify operational procedures.

!!! danger "Use unique tokens for different deployments"

    If you're managing multiple Soveren deployments, please create unique tokens for each one. Using the same token across different deployments can result in data being mixed and lead to interpretation errors that are difficult to track.

## Deploying Sensors

We utilize Helm for deployment. The installation procedure is as follows:

=== "Data-in-motion (DIM)"

    ```shell
    kubectl create namespace soverenio
    helm repo add soveren https://soverenio.github.io/helm-charts
    helm install -n soverenio soveren-agent soveren/soveren-agent --set digger.token="<TOKEN>"
    ```

=== "Data-at-rest (DAR)"

    ```shell
    kubectl create namespace soverenio-dar-sensor
    helm repo add soveren https://soverenio.github.io/helm-charts
    helm install -n soverenio-dar-sensor soverenio-dar-sensor soveren/soverenio-dar-sensor --set crawler.token="<TOKEN>"
    ```

We [recommend](../configuring-sensor/#sensor-token) that instead of adding `<TOKEN>` to the command line, you incorporate the `token` into your own configuration file, such as `values.yaml`. Then, use the following commands instead of the ones above:

=== "Data-in-motion (DIM)"

    ```shell
    kubectl create namespace soverenio
    helm repo add soveren https://soverenio.github.io/helm-charts
    helm install -n soverenio soveren-agent soveren/soveren-agent -f path_to/values.yaml
    ```

=== "Data-at-rest (DAR)"

    ```shell
    kubectl create namespace soverenio-dar-sensor
    helm repo add soveren https://soverenio.github.io/helm-charts
    helm install -n soverenio-dar-sensor soverenio-dar-sensor soveren/soverenio-dar-sensor -f path_to/values.yaml
    ```

## Updating Sensors

Updating the Sensor to the latest version is straightforward:

=== "Data-in-motion (DIM)"

    ```shell
    helm repo update soveren
    helm upgrade soveren-agent soveren/soveren-agent -n soverenio -f path_to/values.yaml
    ```

=== "Data-at-rest (DAR)"

    ```shell
    helm repo update soveren
    helm upgrade soverenio-dar-sensor soveren/soverenio-dar-sensor -n soverenio-dar-sensor -f path_to/values.yaml
    ```

You can check the latest version information [in our Helm chart](https://github.com/soverenio/helm-charts/).

## Scaling down or removing Sensors

To completely uninstall the Sensor, use the following command:

=== "Data-in-motion (DIM)"

    ```shell
    helm -n soverenio uninstall soveren-agent
    ```

=== "Data-at-rest (DAR)"

    ```shell
    helm -n soverenio-dar-sensor uninstall soverenio-dar-sensor
    ```

If you wish to address performance issues with any individual component, you can temporarily scale it down using the following command: 

=== "Data-in-motion (DIM)"

    ```shell
    kubectl -n soverenio scale deployment.apps/<DEPLOYMENT_NAME> --replicas=0
    ```

=== "Data-at-rest (DAR)"

    ```shell
    kubectl -n soverenio-dar-sensor scale deployment.apps/<DEPLOYMENT_NAME> --replicas=0
    ```

`<DEPLOYMENT_NAME>` depends on the release name that you've used and should contain one of the following:

* `kafka`

* `digger`

* `crawler`

* `detectionTool`

* `prometheusAgent`

To scale it back up, use:

=== "Data-in-motion (DIM)"

    ```shell
    kubectl -n soverenio scale deployment.apps/<DEPLOYMENT_NAME> --replicas=1
    ```

=== "Data-at-rest (DAR)"

    ```shell
    kubectl -n soverenio-dar-sensor scale deployment.apps/<DEPLOYMENT_NAME> --replicas=1
    ```

Scaling down interceptors does not offer any practical benefits. It is more effective to completely remove the Sensor and then bring it back up using the standard update or deploy command.
