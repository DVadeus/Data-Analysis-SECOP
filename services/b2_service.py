import boto3
import os

def get_b2_client():
    return boto3.client(
        's3',
        endpoint_url = "s3.us-east-005.backblazeb2.com",
        aws_access_key_id=os.getenv("B2_KEY_ID"),
        aws_secret_access_key=os.getenv("B2_APP_KEY")
    )

def partition_exists(client, bucket, prefix):
    response = client.list_objects_v2(
        Bucket=bucket,
        Prefix=prefix,
        MaxKeys=1
    )
    return "Contents" in response
