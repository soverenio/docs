# Introduction

## We are solving the problem of sensitive data observability

Modern application environments are constantly changing as engineers continuously modify or create new data stores, microservices, virtual machines, and APIs. Businesses that don’t know what to protect face an order of magnitude higher probability of data breaches and privacy violations. This impacts revenue, market capitalization, and customer confidence.

Against this backdrop, security teams face the critical — yet seemingly impossible — quest for a reliable, up-to-date understanding of their infrastructure down to every asset and the data they process.

With the lack of a perfect solution, most businesses have defaulted to some combination of manual processes, plus data discovery and security tools in an attempt to solve the data observability problem.

## What Soveren offers

Soveren helps modern tech-focused businesses with Kubernetes-based environments fulfill critical production data observability and security goals:

1. **Automate data and asset observability:** Enrich your data inventory and improve the quality of manual reviews

2. **Discover and prioritize crown jewels:** Gain near real-time visibility into sensitive assets and data flows

3. **Detect and fix misconfigurations:** Protect sensitive data and assets in the cloud from common security risks

4. **Audit and ensure data compliance:** Maintain ongoing compliance with data regulations (PCI DSS, GDPR, CPRA, etc.)

5. **Minimize third-party data exposure:** Reduce supply-chain attack risks and control sensitive data sharing

## How Soveren works

**Soveren seamlessly maps assets and data in Kubernetes**

* [Native Kubernetes deployment (via Helm)](getting-started/quick-start/) that takes 15 mins or less

* Automatically discovers all services deployed in Kubernetes

* Has zero impact on application performance (by mirroring the traffic)

* No sensitive data is transmitted outside of your environment

**Soveren uses powerful ML models to detect and classify sensitive data**

* Detects [sensitive data](user-guide/data-model/) with a 95% success rate, including unknown data

* Optimized to minimize the number of false-positive alerts

* Works out of the box with no configuration or manual setup

* Automated learning cycle to continuously improve detection quality

* Supports detection of 45+ data types and 20+ languages

## Hybrid architecture
Soveren’s product has a hybrid architecture:

* **Soveren Agent** provides traffic interceptors and data-classification engine installed in the your Kubernetes clusters

* **Soveren Cloud** offers data and asset map, policy engine, and various statistics and metrics dashboards

Take a look at the [architecture section](architecture/overview/) for more details on how Soveren works under the hood.
