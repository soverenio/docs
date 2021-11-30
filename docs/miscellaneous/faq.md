# FAQ

### 1. What is a Soveren gateway? What is a gateway instance?
    
Soveren gateway is a component of Soveren, which you install in your environment. The gateway proxies API calls between your web services. 
    
Any actual deployment of Soveren gateway constitutes a gateway instance. We use terms "gateway" and "gateway instance" interchangeably depending on the context.


### 2. What is Soveren cloud?
    
Soveren cloud is a SaaS managed by Soveren. There is only one Soveren cloud out there. 
It provides you with dashboards and configuration means to work with the detected personal data and observed flows.

    
### 3. Where is Soveren gateway deployed — in Soveren cloud or in my perimeter? Who manages the gateway — Soveren or me?

You deploy the gateway yourself, in your controlled environment of choice. 
The installation is managed fully by you. Soveren does not have or require any access to the gateway.
    
    
### 4. What data does the gateway send out of my perimeter? What exactly is "metadata"?
    
The gateway only communicates with Soveren cloud and only sends the metadata about the communication it observed.  
    
For example, service A sent a request to Service B. There were certain data types in the response, such as *name* and/or *email*. 
None of your actual values are sent anywhere outside your perimeter, just the *metadata* — facts about what data types were observed and what services were engaged in communication.


### 5. What is a Soveren token? What do I need a Soveren token for? 

Soveren token is a token used in the communication between the gateway instance and the cloud. 
You need a token for Soveren cloud to correctly identify the matching gateway instance. 


### 6. Can I deploy several instances of Soveren gateway?

You can deploy as many instances of Soveren gateway as you need, for example, for scalability reasons or to cover different places in the environment. 

All those instances contribute to the single unified user interface in Soveren cloud. 
You can log in to a single control plane in Soveren cloud and observe all the information collected by all Soveren gateways deployed in your environment.


### 7. How do I troubleshoot the gateway? What do I do if the gateway does not work?
    
While running, a gateway instance produces logs as any other component that can be run with Docker or Kubernetes. 
You may want to check your logs and contact us for help at [support@soveren.io](mailto:support@soveren.io) if anything surprising happens.
You can also leverage your Kubernetes or Docker monitoring tools.


### 8. What does asynchronous PII detection mean?

The gateway consists of a proxy (a Traefik fork), asynchronous messaging system (Apache Kafka), and custom detection component which discovers PII. 
The proxy extracts payloads from each request and response and sends those payloads to the detection component through the messaging system. 
Along with that, the proxy passes each request or response straight away to its proper destination, without any modification. 

The PII detection happens on the payloads, independently from proxying the traffic. 
Thus, the latency the gateway introduces is comparable to usual proxying and is negligible.

### 9. Can I deploy Soveren gateway in AWS / Azure / Google Cloud / any other cloud?

You can deploy Soveren gateway in any cloud of your choice, or in your own data center. 
What you need is either Docker or Kubernetes running in your environment, those are the deployment options Soveren supports right now.


###  10. If I deploy Soveren gateway in my K8s cluster, does it mean that all the services that the gateway monitors must be in the same K8s cluster?

You can monitor services that are located anywhere on the internet, provided that the Soveren gateway instance you deployed can reach them. 
More specifically, the URLs that you configure (see the [quick start](../../getting-started/quick-start)) must be reachable from where you placed the gateway.

For example, the gateway and services may be even on different cloud providers, if you can point the gateway in the services’ direction and the calls pass through.


### 11. If I deploy Soveren gateway in Cloud X (e.g. AWS), does it mean that all the services that the gateway monitors must also be in the same Cloud X? 

All that matters is you being able to point the gateway in the services’ direction and their calls passing through it. 
Can be any cloud provider both for services and the gateway, in any combination.

### 12. What is the performance penalty introduced by the gateway? I am conscious of any potential slowdowns.

The gateway does not introduce any noticeable latency or performance penalty, as the traffic goes straight through without any interruption. 
PII analysis is done asynchronously and doesn't impede the traffic going through.

### 13. What exactly is a data source?
You configure one or multiple upstreams for your gateway instance. 
That boils down to defining particular URLs with applications or services which live in the upstreams. 
Applications or services in turn provide one or several APIs that can be called and will be monitored by our gateway.

We refer to those applications and  services as "data sources", meaning that they provide actual data which Soveren gateway monitors.

For example, you might have `/some/client/service/get_basic_info?parameters` and `/some/client/service/get_contacts?parameters`, and also `/some/order/service/get_order?parameters`. 
Specific data sources in this case are `/some/client/service/` and `/some/order/service/`.


### 14. What exactly Soveren charges for?

We charge for the data sources that are involved in the actual data transmission. We monitor only those data sources which you actually use, not just configure, so only they contribute to the bill.

Moreover, we do not charge per API, but only per data source which provides that API.
For example, you might have `/some/client/service/get_basic_info?parameters`, `/some/client/service/get_contacts?parameters`, and `/some/order/service/get_order?parameters`.
We would charge for these two data sources: `/some/client/service/` and `/some/order/service/`; and only if they are actually receiving requests.

To expand, look at `/some/client/service/`: it might be called at `get_basic_info` or `get_contacts`, or at both. 
If none of these two endpoints is called, you will not be charged for `/some/client/service/`.

### 15. What personal data types does the gateway support? Can we configure our own data types?

The current version supports only a [limited set of data types](../../dashboards/overview/#pii-types), but the list is constantly updated. 

We intend to free our users of any manual configuration, so Soveren should detect any personal data automatically out of the box.
If it doesn't or you have some highly specific data types, please drop us a line at [support@soveren.io](mailto:support@soveren.io).


    









