# Interceptors: collecting the traffic

Listen to the virtual interfaces on the host
Collect tcp until it's clear it's http
Drop everything else, drop http larger than 1mb
Drop errors and pure technical stuff
Collect the request, then wait for response. Check content type. Build pairs with at least one half of correct content type. Drop pairs larger than 1mb
Write pairs to Kafka. Flush buffers if Kafka is not available for too long
Profile cpu/mem on demand from Digger
