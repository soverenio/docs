Dashboards
==========

Soveren provides a number of dashboards that address the following questions:

* What PII data types are collected?
* Which ones are the most important?
* Which systems collect the PII data?
* What data collections are the most risky / sensitive?
* How exactly is the PII data exposed?
* Which systems access the PII data?
* Which PII data are revealed in the calls?


To access the dashboards, `log in to your Soveren account <https://app.soveren.io/>`_.

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

* Low — very low possibility of person identification.
* Medium — fair possibility of person identification.
* High — high possibility of person identification.

These sensitivity levels are applied both to individual PII types in the summary statistics and to combinations of PII types collected by services and available through APIs.

















