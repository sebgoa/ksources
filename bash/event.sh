#!/bin/bash

set -ex

while true; do
    curl -XPOST -H 'Content-type: application/cloudevents+json' -d '{"Hello":"World"}' ${SINK}
    sleep 60
done

