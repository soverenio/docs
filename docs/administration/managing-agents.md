# Managing Agents

You need one Soveren Agent per each of your Kubernetes clusters that you want Soveren to monitor.

You can create, modify and delete Agents on the [agents page](https://app.soveren.io/agents) in the Soveren app.

![Agents](../../img/administration/agents.png "Agents")

Each Agent is defined by its `name` and `token`.

## Agent's name

If you have several clusters and hence several Agents, Soveren will show them separately on the [data map](https://app.soveren.io/data-map). The name of the Agent will define the name of the cluster on the data map.

You can also automate naming of your clusters in Soveren [by setting the names of the clusters](../configuring-agent/#multi-cluster-deployment) in your configuration files.

## Agent's token

The `token` allows Soveren app to identify the Agent during communication.

We [recommend](../configuring-agent/#the-token) adding the `token` to your own configuration file, for instance `values.yaml`. This simplifies the updating and support procedures.
