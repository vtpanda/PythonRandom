#!/usr/local/bin/python

import requests
import boto3
import json
import time
import random


client = boto3.client('firehose')
url = "https://randomuser.me/api/?format=json"

response = requests.get(url)


# statusCode = response.status_code

new_person = json.dumps(response.json()).encode('utf-8')
# testjson = response.json()
#
# testjson['results'][0]['name']['first']
# testjson['results'][0]['name']['last']
# testjson['results'][0]['dob']['age']
# testjson['results'][0]['gender']
# testjson['results'][0]['location']['coordinates']['latitude']
# testjson['results'][0]['location']['coordinates']['longitude']


# print(response.content)
client.put_record(DeliveryStreamName='PersonLoad',
    Record={
        'Data': new_person
    })

# count = 0
#
# while (count < 10000):
#     count = count + 1
#
#     time.sleep(random.uniform(0, 1))
