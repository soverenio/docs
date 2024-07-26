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

### Secrets basics 

To use secrets with Soveren, you need to set the top-level `useExternalSecrets` to true:

```yaml
useExternalSecrets: true
```

By doing this, you are instructing Soveren to prioritize the environment variables set externally over those set by Soveren components themselves.

You can pass secrets to Soveren via environment variables. There are several ways to do this.

One way of setting the environment variables from secrets is via the containers' `env[]` sections of the chart, as described in the [Kubernetes documentation](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#define-container-environment-variables-using-secret-data):

```yaml
    env:
      - name: ENV_VARIABLE_NAME
        valueFrom:
          secretKeyRef:
            name: SECRET_NAME
            key: SECRET_VALUE_KEY
```

Another way is by executing a script and exporting the relevant variables before the container starts. 

### DIM and DAR tokens

Good candidates for using secrets are the tokens of the sensors.

If you decide to store the token in a secret, keep in mind that you need to set both `digger`/`crawler` token and `detectionTool` token. They use the same token value for accessing the Soveren Cloud.

!!! danger "When using secrets for tokens, define both the `digger`/`crawler` token and the `detectionTool` token" 

By default Soveren takes care of both, but when you want to use secrets, there is no good way to sync the `detectionTool` token with the `digger` or `crawler` token, so you must define them both manually:

* For the DIM sensor:

    * `SVRN_DIGGER_STATSCLIENT_TOKEN`: token for the `digger`

* For the DAR sensor:

    * `SVRN_CRAWLER_STATSCLIENT_TOKEN`: token for the `crawler`

* For the `detectionTool`, both for DIM and DAR sensors:

    * `SVRN_DETECTION_TOOL_OTAREGISTRY_AUTH_TOKEN`: token for the `detectionTool`

### DAR data sources

Soveren Data-at-rest (DAR) sensor requires you to set up connections to data sources for monitoring. These connections usually include access credentials, so it is a good idea to store them in secrets.

The relevant environment variables to manage the DAR sensor connections are:

* `SVRN_CRAWLER_CRAWL_S3`: S3 connectivity configuration for the DAR sensor (see the [configuration guide](../configuring-sensor/#s3-buckets))

* `SVRN_CRAWLER_CRAWL_KAFKA`: Kafka connectivity configuration for the DAR sensor (see the [configuration guide](../configuring-sensor/#kafka_1))

* `SVRN_CRAWLER_CRAWL_DATABASE_POSTGRES`: database connectivity configuration for the DAR sensor (see the [configuration guide](../configuring-sensor/#databases))

### Secrets management systems

You can store the secrets in a secrets management system like HashiCorp Vault and retrieve their values at runtime using various techniques. To do this, establish communication with the Vault and export the necessary environment variables:

<details>
    <summary>An example of how you could retrieve the tokens from Vault</summary>

```yaml
useExternalSecrets: true

digger:
  podAnnotations:
    vault.hashicorp.com/agent-inject: 'true'
    vault.hashicorp.com/role: soveren-app
    vault.hashicorp.com/log-level: info
    vault.hashicorp.com/agent-inject-secret-soverentokens: secret/data/digger/token
    vault.hashicorp.com/agent-run-as-same-user: 'true'
    # -- Environment variable export template
    vault.hashicorp.com/agent-inject-template-soverentokens: |
      {{ with secret "secret/data/digger/token" -}}
        export SVRN_DIGGER_STATSCLIENT_TOKEN="{{ .Data.data.SVRN_DIGGER_STATSCLIENT_TOKEN }}"
      {{- end }}
  image:
    # -- Default entrypoint for digger: '/usr/local/bin/digger --config /etc/config.yaml'
    # -- Example for hashcorp/vault:
    command: [ '/bin/bash', '-c' ]
    args: [ 'source /vault/secrets/soverentokens && /usr/local/bin/digger --config /etc/config.yaml' ]


detectionTool:
  podAnnotations:
    vault.hashicorp.com/agent-inject: 'true'
    vault.hashicorp.com/role: soveren-app
    vault.hashicorp.com/log-level: debug
    vault.hashicorp.com/agent-inject-secret-soverentokens: secret/data/digger/token
    vault.hashicorp.com/agent-run-as-same-user: 'true'
    # -- Environment variable export template
    vault.hashicorp.com/agent-inject-template-soverentokens: |
      {{ with secret "secret/data/digger/token" -}}
        export SVRN_DETECTION_TOOL_OTAREGISTRY_AUTH_TOKEN="{{ .Data.data.SVRN_DIGGER_STATSCLIENT_TOKEN }}"
      {{- end }}
  image:
    # -- Default entrypoint for detection-tool: './entrypoint.sh'
    # -- Example for hashcorp/vault:
    command: [ '/bin/bash', '-c' ]
    args: [ 'source /vault/secrets/soverentokens && ./entrypoint.sh' ]
```

</details>
