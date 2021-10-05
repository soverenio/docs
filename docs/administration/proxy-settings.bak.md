<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TCK46V7');</script>
<!-- End Google Tag Manager --> 

# Proxy settings

The proxy is part of Soveren gateway and serves as an edge router for client's traffic.
Technically, it is a a [Traefik](https://doc.traefik.io/traefik/) fork with an added middleware.

Here's what you need to know to customize the proxy within the gateway.

## SSL termination

The proxy supports HTTPS protocol over an encrypted SSL/TLS connection.
You  can enable SSL termination by adding a TLS certificate, even when the proxy is already running, to the dynamic configuration in the ``tls {}`` section.

For example:

       http:
         routers:
           defaults:
             entryPoints:
               - web
             rule: PathPrefix(`/`)
             middlewares:
               - soveren
             service: upstream
             tls: {}

!!! tip
   
    To learn about specific `tls{}` parameters specific to your setup, and other encryption options, refer to [TLS](https://doc.traefik.io/traefik/https/tls/) in Traefik documentation.
    
    To learn more about routing options in the context of SSL termination, refer to [Routers](https://doc.traefik.io/traefik/routing/routers/#tls) in Traefik documentation.

=== "Kubernetes"

    To add a TLS certificate, edit the `replicator` configmap:
   
        kubectl edit cm replicator

=== "Docker Compose"

    1. Clone the repo containing the configuration files:
           
           ```
           git clone https://github.com/soverenio/deployment
           ```
           
    2. Edit the `configs/traefik_configs/conf.d/30-routers.yaml` configmap.





