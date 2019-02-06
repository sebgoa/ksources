## Python basic sample

This basic Python event source sends `Hello World` every 60 seconds.

It uses the Python `requests` module and gets the sink URL from the environment variable SINK

```
#!/usr/bin/env python

import os
import json
import requests
import time

sink_url = os.environ['SINK']

body = {"Hello":"World"}
headers = {'Content-Type': 'application/cloudevents+json'}

while True:
    requests.post(sink_url, data=json.dumps(body), headers=headers)
    time.sleep(60)
```

## Build and Push Docker image

Use your own registry

```
docker build -t gcr.io/triggermesh/pythonsample
docker push gcr.io/triggermesh/pythonsample
```

## Deploy the source on your k8s cluster

```
kubectl apply -f manifest.yaml
```
