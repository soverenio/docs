# Interceptors: capturing the traffic

## Overview

The primary objective of Interceptors is to intercept and monitor the network traffic across the nodes within the cluster.

![Traffic interception](../../img/architecture/interception.png "Traffic interception")

Interceptors are deployed as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/), and by default, exist as `pod`s on all worker nodes in the cluster.

`Pod`s with Interceptors have `hostNetwork` set to `true` ([see more on this](#required-permissions)), granting them access to the host machine. Thus, Interceptors can read data from the host's network namespaces and virtual interfaces using the [PCAP library](https://www.tcpdump.org/).

Interceptors read data from the virtual interfaces in a non-blocking manner. If the host is engaged with higher priority tasks, the OS may limit resources for the Interceptor, possibly resulting in partial traffic coverage.

## Interceptor operation

The simplified flow of each Interceptor's operation is outlined below:

![The main flow of the Interceptor](../../img/architecture/interceptor-flow.png "The main flow of the Interceptor")

Step by step:

1. The Interceptor examines the processes operating on the host. It identifies `pod`s and individual containers by associating the IP addresses of their virtual network interfaces.

2. Upon inspecting individual container processes, the Interceptor discerns which `pod`s are running service mesh (Istio or Linkerd). If a mesh is detected, the Interceptor initiates monitoring of the container's `loopback` interface to observe unencrypted traffic. If the mesh is absent, the Interceptor monitors the `pod`s external network interface.

3. The Interceptor observes the `tcp` traffic of the virtual interface until an entire request or response is compiled. At this juncture, the Interceptor discerns whether the traffic comprises HTTP or a different protocol. Non-HTTP data is disregarded by the Interceptor.

4. If the collected request or response exceeds a predefined size limit (currently 1Mb), it is dismissed and excluded from subsequent analysis.

5. The Interceptor retains the collected request and awaits the response. If the response is delayed, the request is abandoned.

6. The combined request/response pair must also not exceed the predefined size limit (1Mb); otherwise, it is discarded.

7. During the pair's assembly, the Interceptor verifies the `content-type` from the header, which must be one of the following:

    7.1 `application/json`

    7.2 `application/x-www-form-urlencoded`

8. `Content-type`s deviating from the above are discarded. At least one half of the pair must have a permissible `content-type` properly set.

9. The ensuing data is deemed technically a priori and is excluded from further analysis:

    9.1 Internal Kubernetes or Soveren requests: `UA: kube-probe` and `X-Soveren-Request` headers

    9.2 HTTP errors with codes `301`, `308`, `4xx`, `5xx`

    9.3 Requests to the following URLs: `/metrics`, `/healthz`, `/api/health`, `/api/v2/alive`, `/api/v2/detect`

10. The compiled pairs are stored in a buffer. Eventually, the Interceptor forwards them to a dedicated Kafka topic (In this context, Kafka is a standalone component of the Soveren Agent, forming part of the processing and messaging system). If Kafka is unavailable for a significant duration, the Interceptor clears the buffer, resulting in the loss of some collected information.

## Required permissions

To enable Interceptors to read from the host, their containers require the following permissions (modifying these might disrupt traffic interception):

```shell
securityContext:
  privileged: true
  dnsPolicy: ClusterFirstWithHostNet
  hostNetwork: true
  hostPID: true
```

## Important considerations

It's crucial to acknowledge that the Interceptors are designed to use as few resources as possible under all conceivable load conditions. In certain extreme scenarios, Interceptors might be completely starved of resources. This might sporadically result in unusual situations, such as an Interceptor failing to connect to the virtual interface because the pod or container has already been terminated (resulting in Kubernetes log errors).

Regardless of how severe the conditions, Interceptors are designed to manage them. If they omit a portion of the captured traffic, or if they occasionally overlook a container or a  `pod`, the map construction will merely be slightly delayed. 