# Configuring the Soveren Agent

We use Helm for managing the deployment of Soveren Agents. To pass custom values to your Soveren Agent, you need to create the `values.yaml` file in the folder that you use for custom Helm configuration.

You can change a number of things regarding the Soveren Agent deployment. But don't forget to run a `helm upgrade` command after you've updated the `values.yaml` file.

## The token

To save you some keystrokes when installing or updating the Agent, we suggest placing the following snippet into the `values.yaml`.

Digger is a component of an Agent that actually sends metadata to the Soveren Cloud, this is where the token value is used.

```shell
digger:
  token: <TOKEN>
```

## Resource limits

You can adjust resource usage limits for each of the Soveren Agent's components.

As a rule of thumb, we **_do not_** recommend to change the `requests` values. They are set with regard to a minimum reasonable functionality that the component can provide given that much resources.

The `limits` however differ widely between Agent's components, and are heavily traffic dependent. There is no universal recipe for determining them, excapt to keep an eye on the actual usage and check how fast the data map is built by the product. General tradeoff here is this: the more resources you can allow, the faster the map is built.

### Interceptors

The interceptors are placed on each node of the cluster. Their ability to collect traffic is proportional to how much resources they are allowed to use. Both CPU and memory are important.
