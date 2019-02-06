## NOTES

- Use ENTRYPOINT and not CMD otherwise the `--sink` will be parsed as an executable and not an argument
- env var SINK gives you the address of the sink defined in the manifest

## Build and Push Docker image

Use your own registry

```
docker build -t gcr.io/triggermesh/bashsource .
docker push gcr.io/triggermesh/bashsource
```

## Deploy the source on your k8s cluster

```
kubectl apply -f manifest.yaml
```
