# Configuring the Soveren Agent

We use Helm for managing the deployment of Soveren Agents. To pass custom values to your Soveren Agent, you need to create the `values.yaml` file in the folder that you use for custom Helm configuration.

You can change a number of things regarding the Soveren Agent deployment. But don't forget to run a `helm upgrade` command after you've updated the `values.yaml` file.

## Passing the token

To save you some keystrokes when installing or updating the Agent, we suggest placing the following snippet into the `values.yaml`.

Digger is a component of an Agent that actually sends metadata to the Soveren Cloud, this is where the token value is used.

```shell
digger:
  token: <TOKEN>
```

