# Introduction

## Problem that we are solving

Sensitive data is painstakingly hard to control and protect. Businesses process an ever-expanding set of data, subject to complex security, privacy, and compliance requirements, and spread across diverse application environments. All the while, cyberattacks are on the rise.

Even the best manual controls and security tools routinely overlook critical risks, leading to costly data breaches and regulatory fines.

## What Soveren offers

Soveren makes it easy for modern security teams to regain control over sensitive data:

* Gain complete data intelligence across your application environments
* Automate policy enforcement and find critical changes and anomalies in data flows
* Mitigate data risks early on to prevent them from becoming costly incidents

Soveren’s proprietary technology scans Kubernetes clusters in real time to autopilot critical (but tedious) data protection tasks, such as:

* Discovery and classification of [sensitive data](user-guide/data-model/)
* Detection of sensitive data in non-production environments
* Detection of PCI data outside of the PCI DSS perimeter
* Control of sensitive data sharing with 3rd parties

The resulting benefits include automated data discovery and classification, continuously enforced security and compliance policies, and reduced probability of data breaches and fines.

## Why Soveren

Soveren takes 15 minutes to deploy and provides value immediately (not in days or weeks!), with a set of out-of-the-box policies and baseline rules. It automatically routes issues to the right teams in Jira and Slack without slowing down your operations.

Soveren replaces costly and unreliable manual controls. It automates monitoring of application environments to control sensitive data flows (including 3rd-party data transfers) and detect security, privacy, and compliance risks in real time.

Unlike other security tools, Soveren requires zero configuration, has low total cost of ownership, and covers all critical security, privacy, and compliance needs at once. 


## How Soveren works

Soveren offers a native Kubernetes integration with zero impact on latency and reliability. Our Helm-based deployment is typically done in 15 minutes and supports cloud, on-prem, and hybrid infrastructures. Sensitive data always stays inside your environment.

Once deployed, Soveren’s technology works autonomously in the background. It handles all the critical aspects of sensitive data protection, so you don’t have to. Soveren:

* Classifies [45+ country-specific data types in 20+ languages](user-guide/data-model/) with 95% detection accuracy, out-of-the-box (powered by proprietary ML algorithms)
* Visualizes Kubernetes environments so security teams can monitor and analyze data flows in real time (without relying on “opinions”)
* Maintains automated control of security guidelines, privacy regulations, and compliance standards (e.g., PCI DSS, GDPR, CPRA, NIST)

Take a look at the [architecture section](getting-started/architecture/) for more details on how Soveren works under the hood.
