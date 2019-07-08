#!/usr/local/bin/python

import boto3
import json
import watchtower
import logging
import datetime

# commandargs = ''
#
# cmd = "none"
#
# if len(sys.argv) > 2:
#     commandargs = sys.argv[2]
#
# if len(sys.argv) > 1:
#     cmd = sys.argv[1]
#
#
# params = json.loads(commandargs)
#
#
# profile = params.get("profile", "none")
#
# if profile == "none":
#     session = boto3.Session()
# else:
#     session = boto3.Session(profile_name=profile)

session = boto3.Session()
region = session.region_name
s3 = session.client('s3')


today = datetime.datetime.now()
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('Multipart-Upload-List-' +str((today-datetime.datetime(1970,1,1)).total_seconds(-)))
logGroup = '/Multipart_Uploads/'
logger.addHandler(watchtower.CloudWatchLogHandler(log_group=logGroup, boto3_session=session))


msg = 'Beginning Process'
logger.info(msg)

response = s3.list_multipart_uploads(Bucket="vtpanda-backup-mac")
logger.info("Before Delete: ", response)

for uploaditem in response["Uploads"]:
    logger.info("Deleting: Key=" + uploaditem["Key"] + ", UploadId=" + uploaditem["UploadId"])
    response = s3.abort_multipart_upload(
        Bucket='vtpanda-backup-mac',
        Key=uploaditem["Key"],
        UploadId=uploaditem["UploadId"]
    )

response = s3.list_multipart_uploads(Bucket="vtpanda-backup-mac")
logger.info("After Delete: ", response)


msg = 'Ending Process'
logger.info(msg)
