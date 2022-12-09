# Updating the Soveren Agent

Versions of the Soveren Agent components are explicitly stated in the Helm chart, with no background auto-updates.

In case of a major Soveren Cloud update or anything else that requires the latest Agent version, we will inform you well ahead so you can plan for it.

To update your Soveren Agent, just update the Help repo and upgrade the release:

```shell
helm repo update soveren
helm -n soverenio upgrade soveren-agent soveren/soveren-agent
```
