#!/usr/bin/env python

import os
import json
import requests
import time

sink_url = os.environ['SINK']

body = {}
body['specversion']='0.2'
body['time']='2018-04-05T03:56:24Z'
body['id']='XXX-YYY-ZZZ-WWW'
body['datacontenttype']='Content-type: application/json'
body['data']={"Hello":"World"}

headers = {'Content-Type': 'application/cloudevents+json'}

while True:
    requests.post(sink_url, data=json.dumps(body), headers=headers)
    time.sleep(60)
