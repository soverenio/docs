Deployment and fallback
========================

Deployment scheme
-----------------
Nobody knows your infrastructure like you. Decide where to deploy Soveren Gateway against your system services and edge router/proxy if you have one.

Take the example deployment scheme below as a reference and remember this is only one of the various options and doesn't include your service layout.

.. image:: ../images/architecture/deployment-scheme.png
   :width: 800


Fallback
--------
You need to have a fallback plan for emergency cases to automatically reroute your traffic back to your services.

Decide what it's going to be and use the deployment scheme example above for reference.