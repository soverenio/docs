# Sensitive data model

We recognize a number of data types that can potentially identify a person, like name or email. We also take into account the context within which this particular data was used, like a combination of the first and last names with the street address, or whether the name was actually a company name and not person's name. Based on that, we reason whether that usage posed a risk of actually identifying a person, and how high was that risk.

We developed our own machine learning model that does data detection and classification.

You can think of the Soveren model as a two-stage classifier. First, for each observed field the classifier determines the data type, for example email. And then depending on the context the classifier decides if this was actually sensitive data or not. For example if the person's identity could actually be revealed if the observed value was disclosed.

On top of that, the model assigns different weights or _sensitivities_ to different data types and their combinations. Those sensitivities define how likely it is to get the actual person's identity when this data is disclosed.

## Recognised sensitive data types

Right now Soveren detects the following [data types](https://app.soveren.io/data-types):

| Name                 | Kind              | Sensitivity   | Comment                                                                                                                                                                                                                                   |
|:---------------------|:------------------|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Person`             | PII data          | Medium        | This is a person's name which can be any combination of the first and last names.                                                                                                                                                         |
| `Gender`             | PII data          | Low           | Gender, or more precisely sex of a person (male or female).                                                                                                                                                                               |
| `Birth date`         | PII data          | Low           | Date of birth of a person. This can be any conceivable representation of a date, in the form of any combination of day / month / year, or even a Unix timestamp.                                                                          |
| `Location`           | PII data          | High          | Location where the person may reside, i.e. to be present physically, or live or receive a postage. This includes coordinates like latitude / longitude and all details of physical address (country code / city / street / building etc). |
| `Phone`              | PII data          | Medium        | Phone number.                                                                                                                                                                                                                             |
| `Email`              | PII data          | Medium        | Email address.                                                                                                                                                                                                                            |
| `Username`           | PII data          | Medium        | User name.                                                                                                                                                                                                                                |
| `IP address`         | PII data          | Medium        | IP Address.                                                                                                                                                                                                                               |
| `Passport`           | PII data          | High          | Passport data, including the number.                                                                                                                                                                                                      |
| `Pension number`     | PII data          | High          | Pension number.                                                                                                                                                                                                                           |
| `Tax number`         | PII data          | High          | Taxpayer identification number.                                                                                                                                                                                                           |
| `SSN`                | PII data          | High          | US Social Security Number.                                                                                                                                                                                                                |
| `Driver license`     | PII data          | High          | Driver license number or code.                                                                                                                                                                                                            |
| `IBAN`               | PII data          | High          | International Bank Account Number.                                                                                                                                                                                                        |
| `Identity document`  | PII data          | High          | Identity document.                                                                                                                                                                                                                        |
| `PII data`           | PII data          | High          | Generic personally identifiable information (PII).                                                                                                                                                                                        |
| `Card`               | PCI data          | High          | Credit or debit card number, checked for validity according to standards.                                                                                                                                                                 |
| `Expiration date`    | PCI data          | High          | Expiration date of a credit or debit card.                                                                                                                                                                                                |
| `CAV2/CVC2/CVV2/CID` | PCI data          | High          | Security code of a credit or debit card.                                                                                                                                                                                                  |
| `Cardholder name`    | PCI data          | High          | Person's name as it appears of the credit or debit card.                                                                                                                                                                                  |
| `Full track data`    | PCI data          | High          | Data stored on the magnetic strip of a credit or debit card.                                                                                                                                                                              |
| `Masked card number` | PCI data          | Medium        | Partially masked number of a credit or debit card (last 4 digits, first 4/last 4 etc.).                                                                                                                                                   |
| `PCI data`           | PCI data          | High          | Generic Payment Card Industry (PCI) information.                                                                                                                                                                                          |
| `Security token`     | Developer secrets | High          | Security token.                                                                                                                                                                                                                           |
| `Private key`        | Developer secrets | High          | Private key.                                                                                                                                                                                                                              |
| `MAC address`        | Developer secrets | Medium        | Medium access control (MAC) address.                                                                                                                                                                                                      |
| `IMEI`               | Developer secrets | Medium        | International Mobile Equipment Identity.                                                                                                                                                                                                  |
| `Password`           | Developer secrets | High          | Password.                                                                                                                                                                                                                                 |
| `Authorization code` | Developer secrets | High          | Authorization code.                                                                                                                                                                                                                       |
| `User ID`            | Developer secrets | Medium        | Identifier of a user.                                                                                                                                                                                                                     |
| `Developer secrets`  | Developer secrets | High          | Generic developer secrets.                                                                                                                                                                                                                |

 The list of supported data types is ever-growing. [Drop us a line](mailto:support@soveren.io) if you think that we should support some particular data type which you'd use as PII or consider otherwise sensitive. 

## Custom data types

You can [add your own custom data types](https://app.soveren.io/data-types/new) using regular expressions to match the field (key) name and it's value:

![Creating custom data type](../../img/user-guide/data-types-custom.png "Creating custom data type")


## The sensitivity model

We consider both individual data types and their combinations, because sensitivity of the combined data set can be significantly higher than that of any individual data field. For example, the name itself does not reveal much in terms of identification when used alone. But the name combined with the postal address can reveal the identity with much higher certainty.

There are three levels of sensitivity: **Low**, **Medium** and **High**.

All sensitive data types that we recognize are individually assigned the following levels:

* **Low**: `Birth date`, `Gender`
* **Medium**: `Person`, `Phone`, `Email`, `IP address`
* **High**: `Location`, `Card`, `Driver license`, `Passport`, `Tax number`, `SSN`, `Pension number`, `IBAN`

These sensitivity levels are described by different numerical weights. Thus, different data type combinations result in different combined sensitivities. For example, `Birth date` combined with `Gender` still result in **Low** sensitivity. Similarly, `Person` + `Phone` + `Email` are of **Medium** sensitivity, whereas `Person` + `Phone` + `Email` + `Gender` is of **High** sensitivity from the potential person's identification point of view.
