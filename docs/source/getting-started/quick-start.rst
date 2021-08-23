Quick start
===========

...Work in progress


Deployment
----------

Soveren gateway supports Kubernetes and Docker Compose for deployment.

.. tab:: Docker Compose

   **Prerequisites**

   1. `Docker <https://docs.docker.com/get-docker/>`_ and `Docker Compose <https://docs.docker.com/compose/install/>`_.
   2. Soveren API key. If you don't have a Soveren account, `visit and register <https://soveren.io/sign-up>`_.

   **Configure and deploy**

   1. Download the manifest file to the machine you want to deploy Soveren at and switch to the directory with it: ``wget  -O /path_to_folder_to_download_manifest "path_to_manifest_file&cd path_to_folder_to_download_manifest"``
   2. Add your API key from #2 in **Prerequisites** either via the .env file in the or via the local environment at the server where you want to deploy Soveren.
   3. `Configure Soveren proxy <https://doc.traefik.io/traefik/>`_ to make it ready to receive requests and proxy them to the backend services.
   4. Run ``docker-compose up -d``.

   **Livecheck**

   Log in to your Soveren account and check tha Soveren proxy is on.


Redirect your traffic
^^^^^^^^^^^^^^^^^^^^^

To redirect your traffic:

1. Configure the frontend to address the proxy.
2. If you have an edge proxy, configure it to address the Soveren proxy instance.

Refer to `Deployment options <deployment-options.html>`_ to understand the best way to integrate Soveren gateway into your perimeter.










