#!/usr/bin/env python

import os
import requests

from google.cloud import pubsub_v1

from cloudevents.sdk import converters
from cloudevents.sdk import marshaller
from cloudevents.sdk.converters import structured
from cloudevents.sdk.event import v01

gcp_project = os.environ['PROJECT']
gcs_subscription = os.environ['SUBSCRIPTION']
google_credentials = os.environ['CREDENTIALS']
google_credentials_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
sink_url = os.environ['SINK']

def write_credentials():
  fh=open(google_credentials_path, 'w')
  fh.write(str(google_credentials))
  fh.close() 

def callback(message):
    print(message.data.decode())
    print(sink_url)

    event = (
        v01.Event().
        SetContentType("application/json").
        SetData(message.data.decode()).
        SetEventID("my-id").
        SetSource("from-galaxy-far-far-away").
        SetEventTime("tomorrow").
        SetEventType("cloudevent.greet.you")
    )
    m = marshaller.NewHTTPMarshaller(
        [
            structured.NewJSONHTTPCloudEventConverter()
        ]
    )

    headers, body = m.ToRequest(event, converters.TypeStructured, lambda x: x)

    requests.post(sink_url, data=body, headers=headers)
    message.ack()

write_credentials()
sub = pubsub_v1.SubscriberClient()
sub_name = 'projects/%s/subscriptions/%s' % (gcp_project, gcs_subscription)

future = sub.subscribe(sub_name, callback)
future.result()
