#!/bin/bash

set -ex

cat <<EOF >> event.json
{
  "Hello":"World"
}
EOF

while true; do
    curl -XPOST -H 'Content-type: application/json' \
                -H 'ce-specversion: 0.2' \
                -H 'ce-type: io.triggermesh.sebgoa' \
                -H 'ce-source: https://github.com/sebgoa/sources' \
                -H 'ce-id: XXX-YYY-ZZZ-WWW' \
                -d @event.json ${SINK}
    sleep 60
done

