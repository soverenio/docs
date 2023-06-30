# Interceptors: capturing the traffic

## Overview

The primary objective of Interceptors is to intercept and monitor the network traffic across the nodes within the cluster.

![Traffic interception](../../img/architecture/interception.png "Traffic interception")

Interceptors are deployed as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/), and by default, exist as pods on all worker nodes in the cluster.

Pods with Interceptors have `hostNetwork` set to `true` ([see more on this](#required-permissions)), granting them access to the host machine. Thus, Interceptors can read data from the host's network namespaces and virtual interfaces using the [PCAP library](https://www.tcpdump.org/).

Interceptors read data from the virtual interfaces in a non-blocking manner. If the host is engaged with higher priority tasks, the OS may limit resources for the Interceptor, possibly resulting in partial traffic coverage.

## Required permissions

To enable Interceptors to read from the host, their containers require the following permissions (modifying these might disrupt traffic interception):

```shell
securityContext:
  privileged: true
  dnsPolicy: ClusterFirstWithHostNet
  hostNetwork: true
  hostPID: true
```

Listen to the virtual interfaces on the host

Collect tcp until it's clear it's http

Drop everything else, drop http larger than 1mb

Drop errors and pure technical stuff

Collect the request, then wait for response. Check content type. Build pairs with at least one half of correct content type. Drop pairs larger than 1mb

Write pairs to Kafka. Flush buffers if Kafka is not available for too long

Profile cpu/mem on demand from Digger
