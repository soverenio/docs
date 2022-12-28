# Architecture

Soveren consists of two major parts: Soveren Agent which you [install](../quick-start/) in your Kubernetes cluster, and [Soveren Cloud](https://app.soveren.io/) which is hosted by Soveren and provides all the functionality actually visible to you in the form of [dashboards](../../user-guide/overview/).

Since Soveren Agent probably requires a lot more attention from your part than Soveren Cloud, here we outline in more detail how the whole thing works with the focus on Agent.

## Soveren Agent: the overview

Soveren Agent consists of several parts:

* **Interceptors** which are distributed to all worker nodes of the cluster through the [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/). They capture the traffic from virtual interfaces of the pods with the help of a [packet capturing](https://www.tcpdump.org/) mechanism;
* **Messaging system** which receives data from the Interceptors. Consists of a [Kafka](https://kafka.apache.org/) instance which stores request/response data, and Digger which passes data to the detection and further to the Soveren Cloud;
* **Sensitive Data Detector** (or simply Detector) which discovers data types and their sensitivity with the help of proprietary machine learning algorithms.

In Kubernetes terms, all components of the Soveren Agent are pods which are deployed to the worker nodes.

In general, Interceptors are present on each node of the cluster. Kafka, Digger and Detector are deployed onto a separate node.

So speaking in Kubernetes terms, there are the following pods:

* _Interceptors_: many of them, one per each worker node;
* _Kafka_ as part of the Messaging system, one per deployment;
* _Digger_ as another part of the Messaging system, one per deployment;
* _Detection-tool_ as Detector, one per deployment.

Let’s look into what those components do and how they talk to each other in more detail.

## Traffic interception

## The end-to-end flow
