.. raw:: html

    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-TCK46V7');</script>
    <!-- End Google Tag Manager -->

Deployment
==========

Here’s the reference architecture of Soveren deployment:

.. image:: ../images/architecture/deployment-scheme.jpg
   :width: 900

.. admonition:: Note
   :class: note

   Currently, only Kubernetes deployments are supported. You can implement different approaches, including accounting for fallback scenarios if something happens to Soveren gateway.




