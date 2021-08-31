Dashboards
==========

Soveren provides a number of dashboards that address the following questions:


* What personal data types are collected?
* Which data types are the most important?
* What data collections are the most risky/sensitive?
* Which systems collect the data?
* Where the personal data is in the API schema?
* Which services have access to personal data?
* Which APIs provide access to personal data?
* Which data is revealed in the calls?

To access the dashboards, `log in to your Soveren account <hhttps://app.soveren.io/pii-types>`_.

Addressed PII types
-------------------
Currently, Soveren dashboards show you the following PII types:

* Personal information
   * First Name
   * Last Name
   * Middle name (if any)
   * Date of birth
   * Gender
* National IDs
   * Driver license
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

Sensitivity model implements the following levels:

* Low — very low possibility of of identifying the person.
* Medium — fair possibility of of identifying the person.
* High — high possibility of of identifying the person.

These sensitivity levels are applied both to individual PII types in the summary statistics and to combinations of PII types collected by services and available through APIs.

















