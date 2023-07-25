# Managing Agents

For each Kubernetes cluster you want Soveren to monitor, you'll require a Soveren Agent.

You can create, modify, and delete Agents via the [agents page](https://app.soveren.io/agents) in the Soveren app.

![Agents](../../img/administration/agents.png "Agents")

Each Agent is characterized by its `name` and `token`.

## Agent's Name

If you have multiple clusters, and thus multiple Agents, Soveren will display them separately on the [data map](https://app.soveren.io/data-map). The Agent's name will define the name of the cluster on the data map.

You can also automate the naming of your clusters in Soveren [by setting the names of the clusters](../configuring-agent/#multi-cluster-deployment) in your configuration files.

## Agent's Token

The `token` allows the Soveren app to identify the Agent during communication.

We [recommend](../configuring-agent/#the-token) adding the `token` to your own configuration file, such as `values.yaml`, to simplify operational procedures.
