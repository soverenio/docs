# Integration with Jira

## Why use Jira integration

While Soveren provides you with the [nice UI](../overview/) to respond to events which are happening in your infrastructure, sometimes you need to assign actions depending on what you've found. Integration with Jira provides you with this opportunity: you will be able to open a ticket directly from e.g. the policy violation event and populate it with all relevant details.

## Configuring the integration with Jira

Creating a Jira integration is simple and straightforward.

First, open the [Integrations in the Soveren app](https://app.soveren.io/integrations/), and press **Connect** on the Jira configuration there:

![Jira in Integration](../../img/integration/integrations-list-jira.png "Jira in Integration")

The following [connection settings](https://app.soveren.io/integrations/jira/) will open:

![Jira connection settings](../../img/integration/jira-config-empty.png "Jira connection settings")

Here you need to provide the following:

* **Jira username**: in most cases this would be your work email.

* **Jira base URL**: the URL via which users access your Jira. [Here's how to get it](https://confluence.atlassian.com/adminjiraserver/configuring-the-base-url-938847830.html) if you don't have it handy.

* **API token**: a token to authenticate your Soveren app with an Atlassian cloud product. Usually you will need to generate a new one, [here's how to do it](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

Here's how these settings should look like:

![Jira credentials](../../img/integration/jira-config-creds.png "Jira credentials")

After you press the **Next** button, Soveren will try to establish and authenticate the connection with your Jira. If successful, you will get the following additional configuration options:

![Jira issue settings](../../img/integration/jira-config-issue.png "Jira issue settings")

Fill in the **Project**, **Issue type**, **Priority** and **Components** according to your needs, and press the **Save and enable** button.

The result should look like the following:

![Jira integration final settings](../../img/integration/jira-config-final.png "Jira integration final settings")

You are all set with Jira config now. On to creating some tickets!
