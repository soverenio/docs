# Sample testing environment for Soveren

You can give Soveren a try in an artificial setup before deploying it in your production or development environment. There are several ways of doing that.

## Try Soveren Data-in-motion (DIM) Sensor

The [Soveren Data-in-motion (DIM) Sensor sample testing environment](https://github.com/soverenio/helm-charts-testing/) Helm chart provides a way of generating artificial traffic resembling personal data. You will need to deploy a Soveren DIM Sensor in an empty cluster and then follow the instructions from the testing repository.

As a result, several services are deployed, which communicate with each other by sending different testing payloads described in the repository. You will see a lifelike data map, service catalog, and sample detections as described in the [User guide](../../user-guide/overview/).

## Try Soveren Data-at-rest (DAR) Sensor

The simplest way to test the Soveren Data-at-rest (DAR) Sensor is to [deploy it and point it to your existing S3 bucket](../quick-start/). Then you can add some JSON or CSV files containing data that resembles personal information to that bucket.

You will see a lifelike data map, S3 bucket, and sample detections as described in the [User guide](../../user-guide/overview/).

## Sandbox

Soveren can provide you with access to a sandbox environment populated with synthetic data resembling an actual configuration. That configuration includes web services in Kubernetes clusters, S3 buckets, Kafka clusters, and databases in different locations.

This sandbox, while artificial, provides the best view into what you might be able to see in your actual environment.

Please contact us at [support@soveren.io](mailto:support@soveren.io?Subject=Sandbox) if you are willing to try the sandbox.