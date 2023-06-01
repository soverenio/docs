# Webhook

## Why use webhooks

Soveren provides you with the [nice UI](../overview/#events) to respond to all sorts of events happening in your infrastructure. However sometimes it is more convenient to use the knowledge about the events in other automation tools like process management or risk management systems. A common example of such system is [Security information and event management (SIEM)](https://en.wikipedia.org/wiki/Security_information_and_event_management).

A webhook between Soveren and your application tells your application whenever something important happens, so that you don't even need to open the UI and your regular workflow is directly enriched and is up to date.

## Configuring the webhook

Creating a webhook is simple and straightforward.

First, open the [Integrations in the Soveren app](https://app.soveren.io/integrations/), and press **Connect** on the Webhook configuration there:

![Webhook in Integration](../../img/integration/integrations-list-webhook.png "Webhook in Integration")

The following [configuration panel](https://app.soveren.io/integrations/webhook/) will open:

![Webhook configuration](../../img/integration/webhook-config-emtpy.png "Webhook configuration")

Here you need to provide a couple of parameters:

* **Webhook URL**: en endpoint that will be receiving the events.

* **Token (optional)**: an optional secret that we should use for signing the request body, if provided. The resulting signature ([HMAC-SHA-256](https://en.wikipedia.org/wiki/HMAC)) will be present in the `x-soveren-signature` request header, e.g.: `x-soveren-signature:sha256=46f45c56b2accfdeb492584db9c809a204005a1ad922279f88da429f7f0a7b47`

We do recommend that you provide the token and check the signature (this protects the webhook from unauthorised use), but if you don't want to then just put in some dummy value.

Now you need to specify what [event categories](../event-objects/#event-categories) you want to get from the webhook. You can go for all of them or only for some of them.

After pressing the **Save** button, make sure you test the connection. If successful, the `200 OK` message should appear right next to the **Sent test event** button:

![Successful webhook test](../../img/integration/webhook-config-full.png "Successful webhook test")

## Using the webhook

Webhook will be sending `POST` requests to the enpoint that you've provided. The [Event object](../event-objects/) page describes the structure of messages that you will get. You can filter and aggregate on `category` or `event_type` or on [other attributes](../event-objects/#what-are-event-objects-in-soveren) of the message.

## Checking the webhook status

If the webhook is working properly, the [Integrations in the Soveren app](https://app.soveren.io/integrations/) will show the successful connected status:

![Properly working webhook](../../img/integration/webhook-connected.png "Properly working webhook")

If Soveren cannot send succesful messages to the webhook endpoint for some time (longer than 15 minutes), then the status will turn into disconnected:

![Disconnected webhook](../../img/integration/webhook-disconnected.png "Disconnected webhook")
