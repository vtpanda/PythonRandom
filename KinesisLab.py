#!/usr/local/bin/python

import requests
import boto3
import json
import time
import random


client = boto3.client('firehose')
max = 10000
i = 0

while i < max:
    i += 1
    response = requests.get("https://randomuser.me/api/?format=json")
    # statusCode = response.status_code
    new_person = json.dumps(response.json()).encode('utf-8')
    client.put_record(DeliveryStreamName='PersonLoad',
        Record={
            'Data': new_person
        })
    time.sleep(random.uniform(0, 1))
