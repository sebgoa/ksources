#!/usr/bin/env python

import os
import json
import requests
import time

sink_url = os.environ['SINK']

headers = {}
headers['ce-specversion']='0.2'
headers['ce-time']='2018-04-05T03:56:24Z'
headers['ce-id']='XXX-YYY-ZZZ-WWW'
headers['ce-source']='https://github.com/sebgoa/ksources'
headers['ce-type']='io.triggermesh.event'
headers['Content-type']='application/json'

body={"Hello":"World"}

while True:
    requests.post(sink_url, data=json.dumps(body), headers=headers)
    time.sleep(60)
