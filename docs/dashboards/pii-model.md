# PII model

## PII types

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

## PII sensitivity model

Soveren considers both individual PII fields and their combinations, because sensitivity of the combined data set can be significantly higher than that of any individual field.

The sensitivity model implements the following levels:

* Low — very low possibility of of identifying the person
* Medium — fair possibility of of identifying the person
* High — high possibility of of identifying the person

These sensitivity levels are applied both to individual PII types in the summary statistics and to combinations of PII types collected by services and available through APIs.















