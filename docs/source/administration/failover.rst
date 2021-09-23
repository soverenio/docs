Failover
========

As a part of the fault tolerance policy, Soveren gateway launches several proxy instances running simultaneously.
On your part, you need a failover plan to reroute traffic back to your services in emergency cases, and generally to avoid making Soveren gateway a single point of failure in your perimeter.
Taking into account the variety of possible environment setups, we leave it up to you to make up the exact details of the failover plan.

To help you, here are some caveats you should know:
   * Soveren gateway is designed to run three copies of the proxy simultaneously for load balancing and availability purposes.
   * Failure of the messaging system, Apache Kafka, does not make a proxy instance fail.
   * Kubernetes has a built-in balancing system and manages pods lifecycle, including rebalancing pods in emergency cases.

If you need more help understanding possible failover options, visit `Integration options <../getting-started/integration-options.html>`_ for reference architecture diagrams showing possible ways to integrate Soveren gateway.
















