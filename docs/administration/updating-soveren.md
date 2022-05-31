# Updating the Soveren Agent

Versions of the Soveren Agent components are explicitly stated in the manifest file, with no background auto-updates. In case of a major Soveren Cloud update pr anything else that requires the latest Agent version, we will inform you well ahead so you can plan for it.

To update your Soveren Agent, just re-apply the manifest:

```shell
kubectl apply -k https://github.com/soverenio/deployment.git/interceptor/base
```
