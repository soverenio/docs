# Events

## What are events in Soveren?

Events are something interesting or new happening in your infrasructure. For example, you may start sharing a sensitive data type in the flow which was not allowed to do that. Or there can be a new external party that your serivces are talking to, previously unobserved. Whenever something like that happens, Soveren shows you an event that you can deal with, e.g. decide whether this new data type sharing should be allowed or blocked.

Soveren provides you with a nice UI to manage the events. Here's an example of the events view:

![Events](../../img/user-guide/events-01.png "Events")

## Event objects

Besides in the UI, Soveren provides you with representations of events as structured JSON messages. You can use those messages in your own SIEM or process management software, as well as create customized alerts in the messaging apps.

<details>
  <summary>Example of an event JSON object</summary>

```{.json .copy .annotate} 
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

  "conflicting_assets":[ # (1)!
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

1.  `conflicting_assets`: An array of objects where each object represents an asset that is conflicting with the event policy.

</details>

### Event object structure

Each such JSON message carries significant information about an event and is composed of the following attributes:

1. `title`: A human-readable title for the event, such as a brief summary or description.

2. `sensitivity`: A string that indicates the sensitivity level of the event. It can be 'High', 'Medium', or 'Low', according to the event policy.

3. `time`: The timestamp when the event was created, formatted according to the JavaScript ISO string format.

4. `event_link`: A URL linking to the event details in the Soveren app. Users can follow this link directly into the product.

5. `category`: The category of the event. Helps in broadly classifying the event.

6. `event_type`: The specific type of the event. Helps in identifying the concrete nature of the event.

7. `data_types`: An array of strings that specify the types of data involved in the event.

8. `sending` and `receiving`: The assets involved in the event. They each contain the following sub-attributes:
   - `link`: A URL linking to the asset details.
   - `name`: The name of the asset.
   - `namespace`: The Kubernetes namespace that the asset belongs to.
   - `groups`: A group that the asset belongs to. Each group has a `link` and `name` fields.

9. `endpoint`: An object that represents the endpoint involved in the event, defined by the following attributes: `link`, `URL`, `hostname`, and `method`.

10. `policy`: An object that represents the policy related to the event. It includes a `link` to the policy details and the policy `name`.

11. `conflicting_assets`: An array of objects where each object represents an asset that is conflicting with the event policy.

12. `third_party_ip`: The IP address of a third party involved in the event, if relevant.

13. `user_agent`: The user agent information for the event, if relevant.


 
## Event categories and types
