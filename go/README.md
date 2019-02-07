## Go sample

This Go event source sends `Hello World` every 60 seconds.

## Build and Push Docker image

Use your own registry

```
docker build -t gcr.io/triggermesh/gosample
docker push gcr.io/triggermesh/gosample
```

## Deploy the source on your k8s cluster

```
kubectl apply -f manifest.yaml
```
