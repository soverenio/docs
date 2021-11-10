# FAQ

### What is a Soveren gateway? What is a gateway instance?
    
Soveren gateway is a component of Soveren, which you install in your environment. The gateway proxies API calls between your web services. 
    
Any actual deployment of Soveren gateway constitutes a gateway instance. We use terms "gateway" and "gateway instance" interchangeably depending on the context.


### What is Soveren cloud?
    
Soveren cloud is a SaaS managed by Soveren. There is only one Soveren cloud out there. 
It provides you with dashboards and configuration means to work with the detected personal data and observed flows.

    
### Where is Soveren gateway deployed — in Soveren cloud or in my perimeter? Who manages the gateway — Soveren or me?

You deploy the gateway yourself, in your controlled environment of choice. 
The installation is managed fully by you. Soveren does not have or require any access to the gateway.
    
    
### What data does the gateway send out of my perimeter? What exactly is "metadata"?
    
The gateway only communicates with Soveren cloud and only sends the metadata about the communication it observed.  
    
For example, service A sent a request to Service B. There were certain data types in the response, such as *name* and/or *email*. 
None of your actual values are sent anywhere outside your perimeter, just the *metadata* — facts about what data types were observed and what services were engaged in communication.


### What is a Soveren token? What do I need a Soveren token for? 

Soveren token is a token used in the communication between the gateway instance and the cloud. 
You need a token for Soveren cloud to correctly identify the matching gateway instance. 


### Can I deploy several instances of Soveren gateway?

You can deploy as many instances of Soveren gateway as you need, for example, for scalability reasons or to cover different places in the environment. 

All those instances contribute to the single unified user interface in Soveren cloud. 
You can log in to a single control plane in Soveren cloud and observe all the information collected by all Soveren gateways deployed in your environment.


### How do I troubleshoot the gateway? What do I do if the gateway does not work?
    
While running, a gateway instance produces logs as any other component that can be run with Docker or Kubernetes. 
You may want to check your logs and contact us for help if anything surprising happens.
You can also leverage your Kubernetes or Docker monitoring tools.
    









