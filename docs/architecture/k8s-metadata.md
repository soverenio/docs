# Retrieving metadata from the Kubernetes API

Digger utilizes the Kubernetes (K8s) API to gather metadata on these entities: `pod`s, `endpoint`s, and `service`s. This process employs the method depicted as [Efficient detection of changes](https://kubernetes.io/docs/reference/using-api/api-concepts/#efficient-detection-of-changes) in the official K8s documentation.

Here's how the communication between Digger and the Kubernetes API is structured:

![How Digger interacts with the Kubernetes API](../../img/architecture/k8s-metadata-watching.png "How Digger interacts with the Kubernetes API")

During the initiation phase of the Agent, Digger conducts three `list` calls to collect initial data on [collections](https://kubernetes.io/docs/reference/using-api/api-concepts/#collections) of `pod`s, `endpoint`s, and `service`s. Subsequently, Digger initiates three `watch` calls, essentially subscribing to notifications about configuration modifications in entities of these three types.

In scenarios where the K8s API is unavailable due to any reason, Digger attempts to re-subscribe, with the waiting duration between attempts incrementing exponentially.

For the subscription process, Digger employs the `resourceVersion` so that Kubernetes will only transmit new events to it.

Upon receiving a new entity in the notifications from Kubernetes, Digger processes the metadata, such as the name, namespace, labels, and annotations, storing these in the cache. Digger also identifies the higher-level Kubernetes construct that created this entity, in other words, the workload resource (such as `DaemonSet`, `ReplicaSet`, or `Deployment`, among others) that serves as the actual owner of this entity. This method gives a broader context, for instance, to the pod name (which could be quite cryptic in isolation) of the discovered asset.
