# Integrating with Soveren

Soveren provides a number of integration options: creating tasks in Jira, sending alerts to Slack or webhooks, and Object API.

# Event based integrations 

Integrations with Jira, Slack and webhooks are all based on events produced by Soveren.

<div class="grid cards" markdown>

-   :material-code-json:{ .lg .middle } __Event objects__

    ---

    Events in Soveren are structured as JSON messages. You can process those messages in your systems, to create tasks or customized alerts.

    [:octicons-arrow-right-24: Event objects](event-objects/)

</div>

<div class="grid cards" markdown>

-   :material-jira:{ .lg .middle } __Jira__

    ---

    Integration with Jira allows you to open a ticket directly from e.g. the policy violation event and populate it with all relevant details.

    [:octicons-arrow-right-24: Integrating with Jira](jira/)

-   :material-slack:{ .lg .middle } __Slack__

    ---

    Integration with Slack comes in handy when you need to notify certain people right away if something requires immediate attention.

    [:octicons-arrow-right-24: Integrating with Slack](slack/)

</div>