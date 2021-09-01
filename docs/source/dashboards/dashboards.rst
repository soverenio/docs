.. raw:: html

    <!-- Hotjar Tracking Code for https://docs.soveren.io/ -->
    <script>
        (function(h,o,t,j,a,r){
            h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
            h._hjSettings={hjid:2580378,hjsv:6};
            a=o.getElementsByTagName('head')[0];
            r=o.createElement('script');r.async=1;
            r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
            a.appendChild(r);
        })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
    </script>

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
-------------------
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

* Low — low possibility of of identifying the person
* Medium — fair possibility of of identifying the person
* High — high possibility of of identifying the person

These sensitivity levels are applied both to individual PII types in the summary statistics and to combinations of PII types collected by services and available through APIs.

















