# Bash event source

This is a demo event source for knative written in bash.

* The bash script `event.sh` continuously sends `{"Hello":"World"}` to an HTTP endpoint.
* The script is Containerized via a `Dockerfile`
* The container is started via a Container Source described in the manifest `manifest.yaml`

## Build and Push Docker image manually

Use your own registry by replacing the `triggermesh` org below:

```
docker build -t gcr.io/triggermesh/bash .
docker push gcr.io/triggermesh/bash
```

## Deploy the source on your k8s cluster

This assumes a Channel named `default`

```
kubectl apply -f manifest.yaml
```

## Deploy a `message-dumper`

To verify that the source is working you can deploy a `message-dumper` which dumps the events it receives to stdout.

```
kubectl apply -f https://github.com/knative/eventing-sources/releases/download/v0.3.0/message-dumper.yaml
```

Then check the logs of the Pods corresponding to the `message-dumper` service and you should see the `Hello World` events, for example:

```
$ kubectl logs message-dumper-00001-deployment-6f84dcdcdf-zqrgm -c user-container -n sebgoa
2019/02/06 17:53:26 Message Dumper received a message: POST / HTTP/1.1
Host: message-dumper.sebgoa.svc.cluster.local
Accept-Encoding: gzip
Content-Length: 17
Content-Type: application/cloudevents+json
User-Agent: Go-http-client/1.1
X-B3-Parentspanid: 4531b08c90359d94
X-B3-Sampled: 1
X-B3-Spanid: e66bd5a73c805e5e
X-B3-Traceid: 4531b08c90359d94
X-Forwarded-For: 127.0.0.1
X-Forwarded-Proto: http
X-Request-Id: 4458f7a4-1274-9729-8146-bb975968cd30

{"Hello":"World"}
```


