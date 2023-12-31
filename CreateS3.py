"""
As part of the AWS Free Tier, you can get started with Amazon S3 for free. 
Upon sign-up, new AWS customers receive 5GB of Amazon S3 storage in the 
S3 Standard storage class; 20,000 GET Requests; 
2,000 PUT, COPY, POST, or LIST Requests; 
and 100 GB of Data Transfer Out each month.
"""
import boto3
import logging
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

print("Preload bucket list")
for bucket in s3.buckets.all():
    print(bucket.name)

bucket_name = "test-bucket-tb-us-west-1"
region = "us-west-1"
location = {'LocationConstraint': region}
response = s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

with open('test.jpg', 'rb') as data:
    s3.Bucket('test-bucket-tb-us-west-1').put_object(Key='test.jpg', Body=data)


# Output the bucket names
print('Postload bucket list and contents:')
response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(f"Finding item in bucket: {bucket["Name"]}")
    response = s3_client.list_objects_v2(Bucket=bucket["Name"])
    for content in response.get('Contents', []):
        print(f"items in bucket: {content['Key']}")
