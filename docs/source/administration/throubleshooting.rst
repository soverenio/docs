Troubleshooting
==================

**Problem: Kafka fails and PII detection stops**

Technical details: If a Kafka instance is on, messages will accumulate till the topic capacity is reached. When the topic's capacity is reached, new messages will cause the oldest messages to be deleted. Also, if the message TTL max value is reached, the message is deleted.

Solution: `Restart the Kafka instance <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/>`_ in the Kubernetes cluster where you deployed Soveren.















