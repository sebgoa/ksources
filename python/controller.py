#!/usr/bin/env python

import os
import json
import requests
import time

sink_url = os.environ['SINK']

body = {"Hello":"World"}
headers = {'Content-Type': 'application/json'}

while True:
    requests.post(sink_url, data=json.dumps(body), headers=headers)
    time.sleep(60)
