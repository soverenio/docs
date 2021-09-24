.. raw:: html

    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-TCK46V7');</script>
    <!-- End Google Tag Manager -->
    
Failover
========

As a part of the fault tolerance policy, Soveren gateway launches several proxy instances running simultaneously.
On your part, you need a failover plan to reroute traffic back to your services in emergency cases, and generally to avoid making Soveren gateway a single point of failure in your perimeter.
Taking into account the variety of possible environment setups, we leave it up to you to make up the exact details of a failover plan.

To help you, here are some tips:
   * Soveren gateway is designed to run three copies of the proxy simultaneously for load balancing and availability purposes. These copies don't need different Soveren tokens, as they run within a within a single Soveren gateway setup.
   * Failure of the messaging system, Apache Kafka, does not make a proxy instance fail.
   * Kubernetes has a `built-in balancing system <https://kubernetes.io/docs/concepts/services-networking/>`_ and manages pods lifecycle, including rebalancing pods in emergency cases.

If you need more help understanding possible failover options, visit `Integration options <../getting-started/integration-options.html>`_ for reference architecture diagrams showing possible ways to integrate Soveren gateway.
















