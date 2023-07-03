# Interceptors: capturing the traffic

## Overview

The primary objective of Interceptors is to intercept and monitor the network traffic across the nodes within the cluster.

![Traffic interception](../../img/architecture/interception.png "Traffic interception")

Interceptors are deployed as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/), and by default, exist as `pod`s on all worker nodes in the cluster.

`Pod`s with Interceptors have `hostNetwork` set to `true` ([see more on this](#required-permissions)), granting them access to the host machine. Thus, Interceptors can read data from the host's network namespaces and virtual interfaces using the [PCAP library](https://www.tcpdump.org/).

Interceptors read data from the virtual interfaces in a non-blocking manner. If the host is engaged with higher priority tasks, the OS may limit resources for the Interceptor, possibly resulting in partial traffic coverage.

## How the Interceptors work

The simplified flow of how each Interceptor works is as follows:

![The main flow of the Interceptor](../../img/architecture/interceptor-flow.png "The main flow of the Interceptor")

Step by step:

1. The Interceptor looks into the processes running on the host. It identifies `pod`s and individual containers by matching IP addresses of their virtual network interfaces

2. By looking into the processes of individual containers, the Interceptor identifies which `pod`s are running service mesh (Istio or Linkerd). If the mesh is found then the Interceptor starts listening to the `loopback` interface of the container with mesh, to see the unencrypted traffic. If the mesh is not present then the Interceptor listens to the external network interface of the `pod`

3. The Interceptor listens to the `tcp` traffic of the virtual interface until it collects the whole request or response. At this moment the Interceptor understands whether this is HTTP or some other protocol. The non-HTTP information is dropped by the Interceptor

4. If the collected request or response is larger in size than some pre-defined limit (currently 1Mb), it is discarded and not accounted for in the further analysis

5. The Interceptor remembers the collected request and waits for the response. If the response is not collected for too long, the request is discarded

6. The collected request / response pair also must not exceed the pre-defined size limit (1Mb), otherwise it is discarded

7. While building the pair, the Interceptor checks the `content-type` from the header, it must be one of the following:

   7.1 `application/json`

   7.2 `application/x-www-form-urlencoded`

8. `content-type`s other than the above are discarded at this point. At least one half of the pair must have the manageable `content-type` set properly

9. The following information is considered apriori technical and is discarded from further analysis:

    9.1 Internal Kubernetes or Soveren requests: `UA: kube-probe` and `X-Soveren-Request` headers

    9.2 HTTP errors with codes `301`, `308`, `4xx`, `5xx`

    9.3 Requests to the following URLs: `/metrics`, `/healthz`, `/api/health`, `/api/v2/alive`, `/api/v2/detect`

10. The collected pairs are stored in a buffer. Eventually the Interceptor writes them to a dedicated Kafka topic (Kafka here is a separate component of the Soveren Agent, a part of the processing and messaging system). If for whatever reason Kafka is not available for too long, the Interceptor flushes the buffer, therefore losing some of the collected information

## Required permissions

To enable Interceptors to read from the host, their containers require the following permissions (modifying these might disrupt traffic interception):

```shell
securityContext:
  privileged: true
  dnsPolicy: ClusterFirstWithHostNet
  hostNetwork: true
  hostPID: true
```

## Important caveat

It is important to note that the Interceptors are optimized to consume as little resources as possible under all possible load conditions. Those can be really extreme, therefore there can be situations where the Interceptors are literally deprived of resources. This may occasionally lead to weird situations, like e.g. Interceptor not able to connect to the virtual interface because the pod or container is already gone by that time (results in Kubernetes errors in the log).

However extreme the conditions, the Interceptors are designed to cope with them. If they omit some portion of the captured traffic, or if they occasionally miss a container or a `pod`, then the map will just take longer to build. 