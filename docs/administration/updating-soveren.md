# Updating Soveren

## Soveren gateway

Once you know the update is out, we recommend you update Soveren gateway to the latest version.
Otherwise, your old version may lose connection to Soveren cloud, as the Cloud supports only the latest Gateway version.

!!! tip
    At the early adopters stage, we personally let our adopters know when a new Soveren gateway version is out.


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

Soveren cloud is managed by the Soveren team and doesn't require updates from the user side.

!!! tip
    Soveren cloud supports only the latest Soveren gateway version. Learn how to update Soveren gateway above to avoid any incompatibility issues.





