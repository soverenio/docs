# AWS connections

You can configure Soveren to access your AWS account for automatic discovery of your data storages: managed Kafka clusters and databases.

## Create the new AWS connection

You will need to create a new AWS connection [in the Soveren app](https://app.soveren.io/infrastructure-access/aws):

![AWS connections](../../img/administration/aws-connections.png "AWS connections")

There are several important parameters in the **New AWS connection** dialog that you will need to configure the AWS IAM role:

![New AWS connection](../../img/administration/new-aws-connection.png "New AWS connection")

* `AWS external ID`: a randomly generated identifier which should be associated with the role that you must configure in AWS IAM to provide Soveren with appropriate access rights.

* `Soveren AWS account ID`: the account ID of Soveren. You will need to configure the role in AWS IAM to provide this ID with the appropriate access rights.

* `Role ARN`: the role that you will need to configure in AWS IAM.

## Configure the AWS IAM role

You will need to create a new role in AWS IAM. To do this, proceed with the following steps:

1. Open AWS IAM

2. Create a new Role:

    * **Trusted entity type**: AWS account

    * **Another AWS account** — enter the `Soveren AWS account ID`: `579178354807`

    * Check the **Require external ID** in Options and input the `AWS external ID` which you've generated in the **New AWS connection** dialog

    * Pick a suitable policy that has minimum required permissions for Soveren to discover your data sources, or use our defaults from below:

        ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "ec2:DescribeRegions",
                        "rds:DescribeDBInstances",
                        "rds:DescribeDBClusters",
                        "rds:DescribeDBClusterEndpoints",
                        "kafka:ListClustersV2",
                        "ec2:DescribeSecurityGroups",
                        "kafka:GetBootstrapBrokers"
                    ],
                    "Resource": [
                        "*"
                    ]
                }
            ]
        }
        ```