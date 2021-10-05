# Updating Soveren

## Soveren gateway

Once you know there is an update available, we recommend you update Soveren gateway to the latest version without delay.
Otherwise, your old version may lose connection to Soveren cloud, as the cloud supports only the latest version of the gateway.

!!! tip
    At the early adopters stage of Soveren, we personally let our adopters know when a new version of Soveren gateway is available.


=== "Kubernetes"

    To update Soveren gateway, apply the Soveren gateway manifest:   

        kubectl apply -f https://raw.githubusercontent.com/soverenio/deployment/master/gateway/kubernetes/install.yaml

=== "Docker Compose"

    To update Soveren gateway:

    1. Clone the repo containing the configuration files:
          
          ```
          git clone https://github.com/soverenio/deployment
          ```
          
    2. Apply the Soveren gateway manifest running the command below in the ``compose`` repo folder:
           
           ```
           docker-compose up -d
           ```
## Soveren cloud

Soveren cloud is managed by the Soveren team and doesn't require updates from the user.

!!! tip
    Soveren cloud supports only the latest Soveren gateway version. Update Soveren gateway with the latest version to avoid any incompatibility issues.





