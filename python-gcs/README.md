## NOTES

- Use ENTRYPOINT and not CMD otherwise the `--sink` will be parsed as an executable and not an argument
- env var SINK gives you the address of the sink defined in the manifest
- GOOGLE_APPLICATION_CREDENTIALS needs to be a file so load string as secret and write string to file
- referencing a bucket is three hops: bucket -> topic -> subscription (which you set in pubsub menu)
- casting cloudevent is a pain
- need to change ImagePullPolicy of deployment created by container source controller

## IAM service account.
 
* Create a service account in GCP console with a PubSub subscriber role.
* Generate the key file and store it in `json`
* Create a k8s secret that contains the service account key

```
kubectl create secret generic pubsub --from-file=/path/to/key.json
```

## Create a topic and a subscription

```
gsutil notification create -t foobar -f json gs://sebgoa
gsutil notification list gs://sebgoa
gcloud pubsub subscriptions create foobarsub --topic foobar
Created subscription [projects/skippbox/subscriptions/foobarsub].
```

## Build and Push Docker image

Use your own registry

```
docker build -t gcr.io/triggermesh/gcssource
docker push gcr.io/triggermesh/gcsource
```

## Deploy the source on your k8s cluster

```
kubectl apply -f gcssource.yaml
```
