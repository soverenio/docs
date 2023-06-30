# Getting metadata from Kubernetes API

Digger uses the Kubernetes (K8s) API to get metadata on Kubernetes entities: `pod`s, `endpoint`s and `service`s. We leverage the techique described as the [Efficient detection of changes](https://kubernetes.io/docs/reference/using-api/api-concepts/#efficient-detection-of-changes) in the official K8s documentation.

When the Agent is starting, the Digger makes several `list` calls and receives initial information on [collections](https://kubernetes.io/docs/reference/using-api/api-concepts/#collections) of `pod`s, `endpoint`s and `service`s. It then makes the `watch` calls, effectively subscribing to notifications about the configuration changes of the entities of those three kinds.

When subscribing, Digger uses the `resourceVersion`, so that Kubernetes would send only the new events to it.


Owners (DaemonSets etc)



Caching
