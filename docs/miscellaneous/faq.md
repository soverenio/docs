# FAQ

We collected frequently asked questions about Soveren, its tech, and usage, and compiled a FAQ. If you have a question, the answer is probably on this page.

??? faq-question "What is Soveren gateway? What is a gateway instance?"
    
    **Soveren gateway** is a component of Soveren, which you install in your environment. We provide it as a pre-packaged Docker container. You tweak our configuration template and supply it when deploying the gateway so that the gateway transparently proxies the API calls between your web services (HTTP traffic with JSON payloads).
    
    Any actual deployment of Soveren gateway constitutes a **gateway instance**. We use terms "gateway" and "gateway instance" interchangeably depending on the context.
    
    The gateway creates a copy of each request and response, processes them asynchronously, and detects personal data inside the payloads. After that, it forms metadata packets describing which services/APIs and which data types were involved, and sends them to the Soveren cloud.
    You can deploy many instances of Soveren gateway, for example, for scalability reasons or to cover different places in your environment.
    
    You can find more details on Soveren gateway in the [introduction](https://docs.soveren.io/en/stable/). Deployment and configuration details are in the [quick start](https://docs.soveren.io/en/stable/getting-started/quick-start/).

??? faq-question "What is Soveren cloud?"
    
    Soveren cloud is a SaaS managed by Soveren. There is only one Soveren cloud out there. It provides you with dashboards and configuration means to work with the detected personal data (PII) and observed flows.
    
    To populate these dashboards, Soveren cloud receives metadata on the PII discovered by a particular instance of Soveren gateway deployed in your environment.
    
    If you deploy more than one instance of Soveren gateway, all of them contribute to the single unified user interface (Soveren dashboards).
    
    You can find more details on Soveren gateway in the [introduction](https://docs.soveren.io/en/stable/). Deployment and configuration details are in the [quick start](https://docs.soveren.io/en/stable/getting-started/quick-start/).
    
??? faq-question "Where is Soveren gateway deployed — in Soveren cloud or in my perimeter? Who manages the gateway — Soveren or me?"

    You deploy the gateway yourself, in your controlled environment of choice. The installation is managed fully by you. Soveren does not have or require any access to the gateway.
    
??? faq-question "What data does Soveren gateway send out of my perimeter?"
    
    The gateway only communicates with Soveren cloud and only sends the metadata about the communication it observed. 
    
    For example, service A sent a request to Service B. There were certain data types in the response, such as *name* and/or *email*. 
    None of your actual values are sent anywhere outside your perimeter, just the analysis — facts about what data types were observed and what services were engaged in communication.

??? faq-question "What is a Soveren token? Why do I need a Soveren token?"

    Soveren token is a token used in the communication between the gateway instance and the cloud. 
    You need a token for Soveren cloud to correctly identify the matching gateway instance. 

??? faq-question "Can I change the token for a gateway instance?"
    
    The token is unique for each gateway instance and cannot be changed. You can always look up the tokens  assigned to your gateway instances on the [gateways page](https://app.soveren.io/gateways).


??? faq-question "Can I deploy several instances of Soveren gateway?"

    You can deploy as many instances of Soveren gateway as you need, for example, for scalability reasons or to cover different places in the environment. 
    
    All those instances contribute to the single unified user interface in Soveren cloud. 
    You can log in to a single control plane in Soveren cloud and observe all the information collected by all Soveren gateways deployed in your environment.

??? faq-question "How do I debug Soveren gateway?"
    
    While running, a gateway instance produces logs as any other component that can be run with Docker or Kubernetes. 
    As a user, you should not be involved in any debugging of the instance, but you may want to check your logs and contact us for help if anything surprising happens.
    You can also leverage your Kubernetes or Docker monitoring tools.
    









