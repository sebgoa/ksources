## Python sample with CloudEvents

This Python event source sends `Hello World` every 60 seconds using the [CloudEvents](https://github.com/cloudevents/spec) event specification.

It uses the Python `requests` module and gets the sink URL from the environment variable SINK


## CloudEvents

CloudEvents have two modes: structure and binary. You can test the two modes by switching between `controller.py` and `controller-binary.py` in the `Dockerfile`.

Looking at the logs of the `message-dumper` you will see two different types of events:

```
2019-02-07T12:58:34.926865898Z 2019/02/07 12:58:34 Message Dumper received a message: POST / HTTP/1.1
2019-02-07T12:58:34.926911506Z Host: message-dumper.sebgoa.svc.cluster.local
2019-02-07T12:58:34.926915347Z Accept-Encoding: gzip
2019-02-07T12:58:34.926920592Z Content-Length: 160
2019-02-07T12:58:34.926923374Z Content-Type: application/cloudevents+json
2019-02-07T12:58:34.92692632Z User-Agent: Go-http-client/1.1
2019-02-07T12:58:34.926929155Z X-B3-Parentspanid: 8bddc8d9d1b2761d
2019-02-07T12:58:34.926932047Z X-B3-Sampled: 1
2019-02-07T12:58:34.926934765Z X-B3-Spanid: a95181ddbef799fc
2019-02-07T12:58:34.92693773Z X-B3-Traceid: 8bddc8d9d1b2761d
2019-02-07T12:58:34.926940391Z X-Forwarded-For: 127.0.0.1
2019-02-07T12:58:34.92694315Z X-Forwarded-Proto: http
2019-02-07T12:58:34.926945752Z X-Request-Id: fc0e515f-ee18-91a9-8275-609c247453c8
2019-02-07T12:58:34.92694856Z 
2019-02-07T12:58:34.92695118Z {"specversion": "0.2", "time": "2018-04-05T03:56:24Z", "id": "XXX-YYY-ZZZ-WWW", "datacontenttype": "Content-type: application/json", "data": {"Hello": "World"}}
2019-02-07T13:00:17.486042813Z 2019/02/07 13:00:17 Message Dumper received a message: POST / HTTP/1.1
2019-02-07T13:00:17.48608723Z Host: message-dumper.sebgoa.svc.cluster.local
2019-02-07T13:00:17.486092535Z Accept-Encoding: gzip
2019-02-07T13:00:17.486096171Z Ce-Id: XXX-YYY-ZZZ-WWW
2019-02-07T13:00:17.48614099Z Ce-Source: https://github.com/sebgoa/ksources
2019-02-07T13:00:17.486146125Z Ce-Specversion: 0.2
2019-02-07T13:00:17.486149447Z Ce-Time: 2018-04-05T03:56:24Z
2019-02-07T13:00:17.486153196Z Ce-Type: io.triggermesh.event
2019-02-07T13:00:17.486156602Z Content-Length: 18
2019-02-07T13:00:17.486160654Z Content-Type: application/json
2019-02-07T13:00:17.486164505Z User-Agent: Go-http-client/1.1
2019-02-07T13:00:17.486168521Z X-B3-Parentspanid: 006c38b41c72ef0f
2019-02-07T13:00:17.486172211Z X-B3-Sampled: 1
2019-02-07T13:00:17.486176058Z X-B3-Spanid: 500af3edd5e75f37
2019-02-07T13:00:17.486180199Z X-B3-Traceid: 034de36831dc3585
2019-02-07T13:00:17.486184176Z X-Envoy-Expected-Rq-Timeout-Ms: 600000
2019-02-07T13:00:17.486188081Z X-Envoy-Internal: true
2019-02-07T13:00:17.486191655Z X-Forwarded-For: 127.0.0.1, 127.0.0.1
2019-02-07T13:00:17.48621002Z X-Forwarded-Proto: http
2019-02-07T13:00:17.486213879Z X-Request-Id: 122b3d1a-00e7-9b86-be9b-eaed38333252
2019-02-07T13:00:17.486217437Z 
2019-02-07T13:00:17.486221159Z {"Hello": "World"}
```

## Build the Docker Image

Use your own registry

```
docker build -t gcr.io/triggermesh/python-ce
docker push gcr.io/triggermesh/python-ce
```

## Deploy the source on your k8s cluster

```
kubectl apply -f manifest.yaml
```
