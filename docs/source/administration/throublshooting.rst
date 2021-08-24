Troubleshooting
==================

Work in progress...

When Kafka fails, PII detection stops.

If a Kafka instance is on, messages will accumulate till the topic capacity is reached. When the topic's capacity is reached, new messages will cause the oldest messages to be deleted.
Also, if TTL max value is reached, the message is deleted.

















