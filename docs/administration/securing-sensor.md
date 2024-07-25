# Securing the Sensor

Soveren Data-in-motion (DIM) and Data-at-rest (DAR) Sensors are currently deployed in a Kubernetes environment. Below is a description of specific security aspects and configuration options that you might want to consider.

Please also refer to the [separate guide](../configuring-sensor/) for configuration options that are not related to security. You may also want to check [our current helm chart](https://github.com/soverenio/helm-charts/) for all values that can be tuned for the Soveren Sensors.

## Access to Kubernetes API

The Soveren Data-in-motion (DIM) Sensor subscribes to a significant amount of metadata from the Kubernetes API. A dedicated `ServiceAccount` is created for this purpose. This `ServiceAccount` is granted cluster-wide permissions (`ClusterRoleBinding`) to `get`, `list`, and `watch` several `apiGroups`.

## Proxying the traffic

There may be instances when you want to route the traffic between the Soveren Sensor and the Cloud through a proxy. This could be for reasons such as gaining additional control over the traffic leaving your cluster.

To do this, simply specify the top-level value in your `values.yaml`:

```yaml
httpsProxy: "<PROXY_ADDRESS>:<PROXY_PORT>"
```

Here, `<PROXY_ADDRESS>` and `<PROXY_PORT>` represent the address of your proxy service and the dedicated listening port, respectively.

You can also specify the `NO_PROXY` top-level variable to allow some of your traffic to bypass the proxy:

```yaml
httpsProxyNoProxy: ""
```

## Network policy

You may want to specify the network policy for the Soveren Sensor. It is not enabled by default.

Here's how to do it:

```yaml
networkPolicy:
  # -- Specifies whether Network Policies should be created
  enabled: false
  # -- Specify IP or IP/MASK when the httpsProxy is enabled
  proxyIp: ""
```

### DIM specific policies

You might need to specify the relevant port for the K8s API endpoint:

```yaml
  # -- The below is specific to Data-in-motion (DIM) sensor
  k8sApi:
    # -- The k8s API endpoint port
    port: 443
```

### DAR specific policies

You might need to explicitly allow the DAR sensor to access data sources.

As `name`, use any generic label to mark the combination of `host`+`port`+`protocol`.

```yaml
  # -- Specify IP/MASK, PORT, PROTOCOL for additional IP whitelist egress
  #  crawlerAdditionalEgress:
  #      - name: postgres
  #        host: 192.168.1.1/32
  #        port: 5432
  #        protocol: TCP
  crawlerAdditionalEgress: []
```

## Containers

### Generic container privileges

All containers of the Soveren Sensors, except for the [Interceptors](#interceptors-privileges), have the following `securityContext` by default:

```yaml
securityContext:
  runAsUser: 1000 # 65534 for prometheusAgent
  runAsGroup: 1000 # 65534 for prometheusAgent
  allowPrivilegeEscalation: false
  runAsNonRoot: true
```

### Interceptors privileges

Interceptors capture traffic by monitoring the virtual interfaces of the host.

In each Interceptor pod, there are two containers: the `rpcapd`, which handles the actual traffic capturing, and the `interceptor` itself, which processes the captured data.

To allow Interceptors to read from the host, both the `interceptor` and `rpcapd` containers need to run in privileged mode. Hence, they are assigned the following `securityContext`:

```yaml
securityContext:
  privileged: true
```

Additionally, the `interceptor` container requires the following:

```yaml
dnsPolicy: ClusterFirstWithHostNet
hostNetwork: true
hostPID: true
```

Modifying these settings for `interceptor` and `rpcapd` containers will disrupt traffic interception.

### Verifying image signatures

Ensure the authenticity and integrity of downloaded images by validating their digital signatures.

We use [Cosign](https://docs.sigstore.dev/signing/quickstart/) for image signing. Below is the public key you should use when verifying the signatures:

```shell
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEF5frUnmoziugp0E1uOZJNTzQHJx3
zf93Qcg/kJO1RpV/2SkVK+u0NH+M1K4ja6nr0pIjIyFwP3L6rpKY9p0Kcg==
-----END PUBLIC KEY-----
```

### imagePullSecrets

If you store our images in your own private repository, you may want to use `imagePullSecrets` for each container:

```yaml
  imagePullSecrets: []
```

## Using secrets

To use Kubernetes secrets with Soveren, you need to pass their values via environment variables. There are several ways to do that.

First, you need to set the top-level `useExternalSecrets` to true:

```yaml
useExternalSecrets: true
```

By doing this, you are instructing Soveren to honor the environment variables set externally.

One way of setting the environment variables from secrets is via the containers' `env[]` sections of the chart, as described in the [Kubernetes documentation](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#define-container-environment-variables-using-secret-data):

```yaml
    env:
      - name: ENV_VARIABLE_NAME
        valueFrom:
          secretKeyRef:
            name: SECRET_NAME
            key: SECRET_VALUE_KEY
```

Another way is by executing a script and exporting the relevant variables before the container starts. This can be illustrated by the [example of getting the DIM sensor token from HashiCorp Vault](../configuring-sensor/#hashicorp-vault).

Good candidates for using secrets are the following environment variables:

* `SVRN_DIGGER_STATSCLIENT_TOKEN`: token for the DIM sensor;

* `SVRN_CRAWLER_STATSCLIENT_TOKEN`: token for the DAR sensor;

* `SVRN_CRAWLER_CRAWL_S3`: S3 connectivity configuration for DAR sensor (see the [configuration guide](../configuring-sensor/#s3-buckets))

* `SVRN_CRAWLER_CRAWL_KAFKA`: Kafka connectivity configuration for DAR sensor (see the [configuration guide](../configuring-sensor/#kafka_1))

* `SVRN_CRAWLER_CRAWL_DATABASE_POSTGRES`: database connectivity configuration for DAR sensor (see the [configuration guide](../configuring-sensor/#databases))
