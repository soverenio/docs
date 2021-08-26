Troubleshooting
==================

Work in progress...

**Problem: Kafka fails and PII detection stops.**

Technical details: If a Kafka instance is on, messages will accumulate till the topic capacity is reached. When the topic's capacity is reached, new messages will cause the oldest messages to be deleted. Also, if TTL max value is reached, the message is deleted.

Solution: `Restart the Kafka instance: <https://support.websoft9.com/docs/kafka/admin-services.html>`_.
















