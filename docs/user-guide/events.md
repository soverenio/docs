# Events

## What are events?

Events are something interesting or new happening in your infrasructure. For example, you may start sharing a sensitive data type in the flow which was not allowed to do that. Or there can be a new external party that your serivces are talking to, previously unobserved. Whenever something like that happens, Soveren shows you an event that you can deal with, e.g. decide whether this new data type sharing should be allowed or blocked.

## Example of an event

```json
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

## Event categories and types
