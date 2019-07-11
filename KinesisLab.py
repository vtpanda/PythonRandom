#!/usr/local/bin/python

import requests
import boto3
import json

client = boto3.client('firehose')
url = "https://randomuser.me/api/?format=json"

response = requests.get(url)


statusCode = response.status_code

new_person = json.dumps(response.json())+"\n"
# print(response.content)


client.put_record(DeliveryStreamName='TestPerson',
    Record={
        'Data': new_person
    })
