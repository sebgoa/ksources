# Bash event source

This is a demo event source for knative written in bash.

* The bash script `event.sh` continuously sends `{"Hello":"World"}` to an HTTP endpoint.
* The script is Containerized via a `Dockerfile`
* The container is started via a Container Source described in the manifest `source.yaml`

## Build and Push Docker image manually

Use your own registry by replacing the `triggermesh` org below:

```
docker build -t gcr.io/triggermesh/bashsource .
docker push gcr.io/triggermesh/bashsource
```

## Deploy the source on your k8s cluster

```
kubectl apply -f manifest.yaml
```
