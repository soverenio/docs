# AWS connections

You can configure Soveren to access your AWS account for automatic discovery of your data storages: managed Kafka clusters and databases.

## New AWS connection

You will need to create a new AWS connection [in the Soveren app](https://app.soveren.io/infrastructure-access/aws):

![AWS connections](../../img/administration/aws-connections.png "AWS connections")

There are several important parameters in the **New AWS connection** dialog that you will need to configure the AWS IAM role:

![New AWS connection](../../img/administration/new-aws-connection.png "New AWS connection")

* `AWS external ID`: a randomly generated identifier which should be associated with the role that you must configure in AWS IAM to provide Soveren with appropriate access rights.

* `Soveren AWS account ID`: the account ID of Soveren. You will need to configure the role in AWS IAM to provide this ID with the appropriate access rights.

* `Role ARN`: the role that you will need to configure in AWS IAM.

!!! info "`AWS external ID` and `Soveren AWS account ID` should be used and shared carefully, but they are not considered secret, sensitive, or confidential information."

## Role in AWS IAM

You will need to create a new role in AWS IAM. To do this, proceed with the following steps:

1. Open AWS IAM

2. Create a new role:

    2.1. **Trusted entity type**: AWS account

    2.2. **Another AWS account**: the `Soveren AWS account ID`, i.e. `579178354807`

    2.3. Check the **Require external ID** in Options and input the `AWS external ID` which you've generated in the **New AWS connection** dialog

    2.4. Pick a suitable policy that has minimum required permissions for Soveren to discover your data sources. You can skip this step if there's no appropriate policy: you will create the permissions later (see below).

    2.5. Check that the **Trust policy** looks like below. It’s essential that you see the `Soveren AWS account ID` is in the **Principal** block.

        ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": [
                            "arn:aws:iam::579178354807:root"
                        ]
                    },
                    "Action": "sts:AssumeRole",
                    "Condition": {
                        "StringEquals": {
                            "sts:ExternalId": "<your external id generated by Soveren>"
                        }
                    }
                }
            ]
        }
        ```

        !!! info "At the Preview phase, the Principal may look just like `"AWS": "579178354807"`. But it will be stored as `arn:aws:iam::579178354807:root`, so that's ok."

    2.6. Save the role.

    2.7. If you have not picked the existing policy on the step 4 above, then go to the Permissions tab and input our defaults:

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

    2.8. Now copy the ARN of the created role, go back to the [AWS connection setup in the Soveren app](https://app.soveren.io/infrastructure-access/aws) and paste it into the **Role ARN** field.

    2.9. Click Run test, it should display a positive result. (If it does not then send us the error message.)

    2.10. Save the connection.