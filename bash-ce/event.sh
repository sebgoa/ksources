#!/bin/bash

set -ex

cat <<EOF >> event.json
{
    "specversion" : "0.2",
    "type" : "io.triggermesh.sebgoa",
    "source" : "https://github.com/sebgoa/sources",
    "id" : "XXX-YYY-ZZZ-WWW",
    "time" : "2018-04-05T17:31:00Z",
    "datacontenttype" : "application/json",
    "data" : "{"Hello":"World"}"
}
EOF

while true; do
    curl -XPOST -H 'Content-type: application/cloudevents+json' -d @event.json ${SINK}
    sleep 60
done

