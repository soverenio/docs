# Updating the Soveren Agent

We use Helm for managing the deployment of Soveren Agents. To update your Soveren Agent, you just need to update the Soveren Helm repository and run the upgrade command.

Before doing an upgrade, it's a good idea to create the `values.yaml` file in the folder that you use for custom Helm values configuration. You can put in the value of your Agent's token like this:

```shell
digger:
  token: <TOKEN>
```
This frees you from passing the token value in the command line or through the environment variables. And you can also tune a number of other values like CPU & MEM limits or log level of the Agent's components.

After creating the `values.yaml` file, run the following commands:

```shell
helm repo update soveren
helm -n soverenio -f path_to/values.yaml upgrade soveren-agent soveren/soveren-agent
```
That's it! You've just updated your Soveren Agent.
