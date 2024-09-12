# Data processing

## Overview

Depending on the data source, Soveren can work with various object types and employ different approaches to data sampling.

Soveren DAR Sensor receives all processing tasks from the Soveren Cloud. While the enumeration of data source contents and the detection of data in selected samples are performed within the customer's perimeter, the Soveren Cloud handles the logic of object clustering and the selection of relevant samples for further analysis.

## Data sources

### S3 buckets

Soveren discovers and periodically rescans the list of available buckets. The contents of each bucket are scanned regularly for changes and clustered based on patterns in key names.

For each cluster, a number of examples are randomly selected in logarithmic proportion to the total number of objects in the cluster, assuming that their structures are similar. The resulting key names are sent to the Crawler along with tasks for sensitive data detection in those objects.

For row-based data formats like CSV or NDJSON, samples are taken from different parts of the object if its size exceeds a certain threshold.

Currently, Soveren DAR Sensor supports integration with AWS.

Sensitive data detection is available for the following formats:

* JSON

* NDJSON

* CSV

* YAML

* Text-based logs

GZipped JSON and logs are also supported.

### Kafka

Soveren discovers and periodically rescans the list of available topics. From each topic, a random number of messages is periodically selected from different offsets. Messages with similar schemas are grouped into clusters, and from each cluster, randomly chosen messages are sent for sensitive data detection. The Soveren Cloud is responsible for forming the analysis tasks based on the topics and schema information obtained from the Crawler.

Currently, sensitive data detection is available for JSON messages.

### Databases

Soveren discovers and periodically rescans the list of available databases and their tables. From the tables, a random number of rows is periodically selected from different parts of the table and sent for sensitive data detection. The Soveren Cloud is responsible for forming the analysis tasks based on the database and schema information obtained from the Crawler.