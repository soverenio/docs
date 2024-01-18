# Event objects

## What are event objects in Soveren?

Besides the [UI]((../overview/#events)), Soveren provides you with representations of events as structured JSON messages. You can use those messages in your own [SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management) or process management software, as well as create customized alerts in the messaging apps.

<details>
  <summary>Example of an event JSON object</summary>

```{.json .copy .annotate linenums="1"} 
{
  "title": "Internal asset Asset 3 is sharing Person with third parties",
  "sensitivity": "Medium",
  "time": "2013-10-21T13:28:06.419Z",
  "event_link": "https://app.soveren.io/events?id=123",
  "category": "New data type",
  "event_type": "policy_violation",
  "data_types": [
    "Person",
    "Email"
  ],

  "sending": {
    "link": "https://app.soveren.io/data-inventory/internal-assets/1",
    "name": "service 1",
    "namespace": "namespace 1",
    "groups": [
      {
        "link": "https://app.soveren.io/asset-groups/1/info",
        "name": "group 1"
      },
      {
        "link": "https://app.soveren.io/asset-groups/2/info",
        "name": "group 2"
      }
    ]
  },
  "receiving": {
    "link": "https://app.soveren.io/data-inventory/internal-assets/2",
    "name": "service 2",
    "namespace": "namespace 2",
    "groups": []
  },
  "endpoint": {
    "link": "https://app.soveren.io/data-inventory/sample?id=432&direction=response",
    "url": "api/v1/path-1",
    "hostname": "soveren.io",
    "method": "POST"
  },

  "policy": {
    "link": "https://app.soveren.io/policies/234",
    "name": "Policy 234"
  },

  "conflicting_assets":[
    {
      "name":"Asset 1",
      "link": "https://app.soveren.io/data-inventory/external-assets/1"
    },
    {
      "name":"Asset 2",
      "link": "https://app.soveren.io/data-inventory/external-assets/2"
    }
  ],
  "third_party_ip": "123.1.1.1",
  "user_agent": "some user agent"
}
```
</details>

Each JSON message carries significant information about an event and is composed of the following attributes:

1. `title`: A human-readable title for the event, such as a brief summary or description.

2. `sensitivity`: A string that indicates the sensitivity level of the event. It can be 'High', 'Medium', or 'Low', according to the event policy.

3. `time`: The timestamp when the event was created, formatted according to the JavaScript ISO string format.

4. `event_link`: A URL linking to the event details in the Soveren app. Users can follow this link directly into the product.

5. `category`: The [category](#event-categories) of the event. Helps in broadly classifying the event.

6. `event_type`: The [specific type](#event-types) of the event. Helps in identifying the concrete nature of the event.

7. `data_types`: An array of strings that specify the [types of data](../data-model/) involved in the event.

8. `sending` and `receiving`: The assets involved in the event. They each contain the following sub-attributes:

   * `link`: A URL linking to the asset details.

   * `name`: The name of the asset.

   * `namespace`: The Kubernetes namespace that the asset belongs to.

   * `groups`: A group that the asset belongs to. Each group has a `link` and `name` fields.

9. `endpoint`: An object that represents the endpoint involved in the event, defined by the following attributes: `link`, `URL`, `hostname`, and `method`.

10. `policy`: An object that represents the policy related to the event. It includes a `link` to the policy details and the policy `name`.

11. `conflicting_assets`: An array of objects where each object represents an asset that is conflicting with the event policy.

12. `third_party_ip`: The IP address of a third party involved in the event, if relevant.

13. `user_agent`: The user agent information for the event, if relevant.

## Event categories

The events that Soveren detects belong to one of following four categories:

1. **New Data Type**: events of this type are recorded whenever Soveren observes a data type for the first time in your infrastructure.

2. **Data Flow Change**: this category encapsulates all changes related to both internal and external senders and receivers: introduction of new assets (senders or receivers), detection of previously unobserved data types in them.

3. **Policy Violation**: cover all events triggered by violations of policies configured in the Soveren app.

4. **Other**: this category encompasses a plethora of things not related to detected data types, flow changes or policy violatoins. For example, data map is built and ready for review, misconfiguration of the rules either in Soveren or in your infrastructure.

## Event types

Besides being broadly categorized, the events in Soveren are also fine-grained into specific types describing concrete situations that require your pointed attention.

Here's the list of the event types by category. Your can use `event_type` and event `category` to build automation around specific cases when getting event messages through integrations with Soveren.

| Event category (`category`) | Event type (`event_type`) | Triggered when  |
|-------------------  |----------------------------------- |----------------|
| `new_data_types`    | `new_data_type`                    | A new data type is observed for the first time.|
| `data_flow_changes` | `new_internal_receiver`            | An internal asset is newly registered to receive data. |
|                     | `new_internal_sender`              | An internal asset is newly registered to send data. |
|                     | `updated_internal_receiver`        | An existing internal asset (data receiver) starts receiving new data type. |
|                     | `updated_internal_sender`          | An existing internal asset (data sender) starts sending new data type. |
|                     | `new_external_receiver`            | A new external asset is registered to receive data. |
|                     | `updated_external_receiver`        | An existing external asset (data receiver) starts receiving new data type. |
|                     | `updated_enduser_receiver`         | An existing end-user (external data receiver) starts receiving new data type. |
|                     | `updated_robot_receiver`           | An existing robot (external data receiver) starts receiving new data type. |
| `policy_violations` | `policy_violation`                 | A violation of policy configured within the Soveren app is detected. |
|                     | `3rd_party_policy_violation`       | A violation of a third-party policy (sending data to 3rd party) is detected. |
| `others`            | `discovery_complete`               | A discovery process concludes, all assets are present on the data map. |
|                     | `custom_asset_rule_conflict`       | A rule conflict related to a custom asset arises. |
|                     | `email_clustered`                  | There are actual emails used in your URLs, Soveren detected & masked them in those URLs in Soveren app. |
