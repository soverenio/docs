# Sensitive data model

We recognize a number of data types that can potentially identify a person, like name or email. We also take into account the context within which this particular data was used, like a combination of the first and last names with the street address, or whether the name was actually a company name and not person's name. Based on that, we reason whether that usage posed a risk of actually identifying a person, and how high was that risk.

We developed our own machine learning model that does data detection and classification.

You can think of the Soveren model as a two-stage classifier. First, for each observed field the classifier determines a data type, for example email. Then, depending on the context, the classifier decides if this was actually sensitive data or not, for example if the person's identity could actually be revealed if the observed value was disclosed.

On top of that, the model assigns different weights or _sensitivities_ to different data types and their combinations. Those sensitivities define how likely it is to get the actual person's identity when this data is disclosed.

## Recognised sensitive data types

Right noew Soveren works with the following data types:

  * **`Person`**. This is a person's name which can be any combination of the first and last names.
  * **`Birth date`**: date of birth of a person. This can be any conceivable representation of a date, in the form of any combination of day / month / year, or even a Unix timestamp.
  * **`Gender`**, or more precisely sex of a person (male or female).
  * **US `Driver license`** number (or code).
  * **`Passport` data**, including the number.
  * **`Tax number`**, or Taxpayer Identification Number. Depends on the country. Special case is the US Social Security Number (`SSN`)
  * **`Pension number`**, depends on the country.
  * **Credit or debit `Card`**, including the number (checked for validity according to standards) and expiration date.
  * **`Phone`** number.
  * **`Email`** address.
  * **`Location`** where the person may reside, i.e. to be present physically, or live or receive a postage. This includes coordinates like latitude / longitude and all details of physical address (country code / city / street / building etc).
  * **`IBAN`**: international bank account number.
  * **`IP address`**.

 The list of supported data types is ever-growing. [Drop us a line](mailto:support@soveren.io) if you think that we should support some particular data type which you'd use as PII or consider otherwise sensitive. 

## The sensitivity model

We consider both individual data types and their combinations, because sensitivity of the combined data set can be significantly higher than that of any individual value. For example, the name itself does not reveal much in terms of identification when used alone. But the name combined with the postal address can reveal the identity with much higher certainty.

There are three levels of sensitivity: **Low**, **Medium** and **High**.

All sensitive data types that we recognize are individually assigned the following levels:

* **Low**: `Birth date`, `Gender`
* **Medium**: `Person`, `Phone`, `Email`, `IP address`
* **High**: `Location`, `Card`, `Driver license`, `Passport`, `Tax number`, `SSN`, `Pension number`, `IBAN`

These sensitivity levels are described by different numerical weights. Thus, different data type combinations result in different combined sensitivities. For example, `Birth date` combined with `Gender` still result in **Low** sensitivity. Similarly, `Person` + `Phone` + `Email` are of **Medium** sensitivity, whereas `Person` + `Phone` + `Email` + `Gender` is of **High** sensitivity from the potential person's identification point of view.
