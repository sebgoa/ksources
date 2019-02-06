## How To Write Knative Container Sources

[Container Sources](https://github.com/knative/docs/tree/master/eventing#containersource) as mentioned in the official documentation:

> ... instantiate a container image which can generate events until the ContainerSource is deleted. This may be used (for example) to poll an FTP server for new files or generate events at a set time interval.

These types of event sources are described in so-called `ContainerSource` object manifest (e.g [`manifest.yaml`](./bash/manifest.yaml)) and can be deployed to your Knative cluster with the single command `kubectl apply -f manifest.yaml`.

This repository contains a collection of Container sources for knative eventing. They are meant to be an introduction to writing event sources.

In this repository will use the term _Container Source_ to describe a Knative event source of the kind `ContainerSource`.

## Collection Samples

Each directory showcases the use of a different language as well as different ways to send events.

Each directory contains a `Dockerfile` to build the event source container image

Each directory contains a `manifest.yaml` manifest to deploy the event source

* [bash](./bash)
* [bash with cloudevents](./bash-ce)
* [python](./python)

## Concepts

A container source generates events and forwards those events to an event receiver called a _sink_.

There are two types of container sources depicted in the diagram below.

a) Container sources that generate events in an autonomous manner (e.g Task that runs at a regular interval)
b) Container sources that pull events from a third-party event provider (e.g Google PubSub, Weather service)

![ContainerSource types](./images/containersource.png)

Event sources that need a publicy accessible endpoint (i.e WebHook) tend to be written using a Kubernetes controller (see this [tutorial](https://github.com/knative/docs/blob/master/eventing/samples/writing-a-source/README.md))

A _sink_ receives the events send by the container source. In the context of Function as a Service, you can think of a _sink_ as a function, but it could be something else.

## Specification

Container Sources are custom Kubernetes objects. A well configured Knative cluster will have the `ContainerSource` Custom Resource Definition pre-defined and you will be able to create custom objects of the `Kind` `ContainerSource`.

A sample manifest is shown below. Like most Kubernetes objects it has an `apiVersion`, a `kind`, some `metadata` with a mandatory name and a spec. The specification of a Container Source is fully described in the [API](https://github.com/knative/eventing-sources/blob/master/pkg/apis/sources/v1alpha1/containersource_types.go
) but in its simplest form contains a container _image_ (which once running will generate or pull the events) and a _sink_ which is the event receiver.

```yaml
apiVersion: sources.eventing.knative.dev/v1alpha1
kind: ContainerSource
metadata:
  name: bashsample
spec:
  image: gcr.io/triggermesh/bash
  sink:
    apiVersion: eventing.knative.dev/v1alpha1
    kind: Channel
    name: default
```

### Version

The specification is still `v1alpha1` and may change. In addition to the image name and the sink, you can also define a set of environment variables, some arguments to the container and a service account name.

## Technical Tips

The Knative event controller which handles Container Sources handles the destination for events using the `sink` object referenced in the manifest. This sink is automatically discovered and referenced as an argument to the container *and* as an environment variable.

This leads to two technical details

- Use ENTRYPOINT and not CMD in your Dockerfile, otherwise the `--sink` will be parsed as an executable and not an argument
- You can use the environment variable SINK which gives you the address of the sink defined in the manifest

## Support

We would love your feedback on this tool so don't hesitate to let us know what is wrong and how we could improve it, just file an [issue](https://github.com/sebgoa/ksources/issues/new)

## Code of Conduct

This plugin is by no means part of [CNCF](https://www.cncf.io/) but we abide by its [code of conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md)
