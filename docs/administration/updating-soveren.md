# Updating Soveren

## Soveren gateway

Soveren cloud supports older versions of the gateway, so you can update the gateway at your own pace.

Versions of Soveren gateway components are explicitly stated in the manifest file, with no background auto-updates.

In case of a major cloud update that requires the latest gateway version, we will inform you well ahead so you can plan for it.

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




