# Managing Agents

## Creating Agents

For each Kubernetes cluster you want Soveren to monitor, you'll require a Soveren Agent.

You can create, modify, and delete Agents via the [agents page](https://app.soveren.io/agents) in the Soveren app.

![Agents](../../img/administration/agents.png "Agents")

Each Agent is characterized by its `name` and `token`.

### Name

If you have multiple clusters, and thus multiple Agents, Soveren will display them separately on the [data map](https://app.soveren.io/data-map). The Agent's name will define the name of the cluster on the data map.

You can also automate the naming of your clusters in Soveren [by setting the names of the clusters](../configuring-agent/#multi-cluster-deployment) in your configuration files.

### Token

The `token` allows the Soveren app to identify the Agent during communication.

We [recommend](../configuring-agent/#the-token) adding the `token` to your own configuration file, such as `values.yaml`, to simplify operational procedures.

!!! danger "Use unique Agents and tokens for different clusters"

    If you're managing multiple clusters, please create unique Agents for each one, with distinct tokens. Using the same token for different clusters will result in them appearing as a single deployment perimeter on the data map, making it challenging to discern which flow belongs to which cluster.

## Deploying Agents

We utilize Helm for deployment. The installation procedure is as follows:

```shell
kubectl create namespace soverenio
helm repo add soveren https://soverenio.github.io/helm-charts
helm install -n soverenio soveren-agent soveren/soveren-agent --set digger.token="<TOKEN>"
```

We [recommend](../configuring-agent/#the-token) that instead of adding `<TOKEN>` to the command line, you incorporate the `token` into your own configuration file, such as `values.yaml`. Then, use the following commands instead of the ones above:

```shell
kubectl create namespace soverenio
helm repo add soveren https://soverenio.github.io/helm-charts
helm install -n soverenio soveren-agent soveren/soveren-agent -f path_to/values.yaml
```

## Updating Agents

Updating the Agent to the latest version is straightforward:

```shell
helm repo update soveren
helm upgrade soveren-agent soveren/soveren-agent -n soverenio -f path_to/values.yaml
```

You can check the latest version information [in the current chart](https://github.com/soverenio/helm-charts/blob/master/charts/soveren-agent/Chart.yaml).

## Scaling down or removing Agents

To completely uninstall the Agent, use the following command:

```shell
helm -n soverenio uninstall soveren-agent
```

If you wish to address performance issues with any individual component, you can temporarily scale it down using the following command: 

```shell
kubectl -n soverenio scale deployment.apps/<DEPLOYMENT_NAME> --replicas=0
```

`<DEPLOYMENT_NAME>` can be one of the following:

* `soveren-agent-kafka`

* `soveren-agent-digger`

* `soveren-agent-detectionTool`

* `soveren-agent-prometheusAgent`

To scale it back up, use:

```shell
kubectl -n soverenio scale deployment.apps/<DEPLOYMENT_NAME> --replicas=1
```

Scaling down interceptors does not offer any practical benefits. It is more effective to completely remove the Agent and then bring it back up using the standard update or deploy command.
