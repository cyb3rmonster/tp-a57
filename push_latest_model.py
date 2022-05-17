import boto3
from botocore.client import Config
import os

s3 = boto3.resource('s3',
                    endpoint_url='https://minio.cyber.monster:9000',
                    aws_access_key_id='tp-hafed',
                    aws_secret_access_key='strong-password',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

# Upload a new file
data = open('model.dat', 'rb')
s3.Bucket('tp-a57').put_object(Key='latestmodel/model.dat', Body=data)