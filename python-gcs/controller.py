#!/usr/bin/env python

import os
import requests
import json
import datetime

from google.cloud import pubsub_v1

from cloudevents.sdk import converters
from cloudevents.sdk import marshaller
from cloudevents.sdk.converters import structured
from cloudevents.sdk.event import v02

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
    print(message)
    print(sink_url)

    event = (
        v02.Event().
        SetContentType("application/json").
        SetData(message.data.decode()).
        SetEventID("xxx-yyy-zzz-www").
        SetSource("google cloud storage").
        SetEventTime(str(message.attributes['eventTime'])).
        SetEventType(str(message.attributes['eventType']))
    )
    m = marshaller.NewDefaultHTTPMarshaller()
    headers, body = m.ToRequest(event, converters.TypeStructured, json.dumps)

    requests.post(sink_url, data=body.getvalue(), headers=headers)
    message.ack()

write_credentials()
sub = pubsub_v1.SubscriberClient()
sub_name = 'projects/%s/subscriptions/%s' % (gcp_project, gcs_subscription)

future = sub.subscribe(sub_name, callback)
future.result()
