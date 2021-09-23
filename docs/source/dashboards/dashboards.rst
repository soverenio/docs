.. raw:: html

    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-TCK46V7');</script>
    <!-- End Google Tag Manager -->

Dashboards
==========

Soveren provides a number of dashboards that address the following questions:


* What personal data types are collected?
* Which data types are the most important?
* What data collections are the most risky/sensitive?
* Which systems collect the data?
* Where is personal data in the API schema?
* Which services have access to personal data?
* Which APIs provide access to personal data?
* Which data is revealed in the calls?

To access the dashboards, `log in to your Soveren account <hhttps://app.soveren.io/pii-types>`_.

PII types
---------
Currently, Soveren dashboards show you the following PII types:

* Personal information
   * First name
   * Last name
   * Middle name (if any)
   * Date of birth
   * Gender
* National IDs
   * Driver's license
   * SSN
* Financial information
   * Card numbers
* Contact information
   * Email
   * Phone number
   * Home address

PII sensitivity model
---------------------

Soveren considers both individual PII fields and their combinations, because sensitivity of the combined data set can be significantly higher than that of any individual field.

The sensitivity model implements the following levels:

* Low — very low possibility of of identifying the person
* Medium — fair possibility of of identifying the person
* High — high possibility of of identifying the person

These sensitivity levels are applied both to individual PII types in the summary statistics and to combinations of PII types collected by services and available through APIs.

















