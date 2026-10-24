"""Homework: say hello to AWS S3.

Run it (after `aws configure`, see the homework handout):

    python hello_aws.py <your-bucket-name>

It writes `hello.txt` into your bucket, reads it back and prints it.
"""
import sys

import boto3

AUTHOR = "your-github-username"  # TODO: replace with your GitHub username


def greeting(name: str) -> str:
    return f"Hello from {name}!"


def roundtrip(bucket: str, key: str = "hello.txt", s3=None) -> str:
    """Upload the greeting to s3://bucket/key, download it again, return the text."""
    s3 = s3 or boto3.client("s3")
    s3.put_object(Bucket=bucket, Key=key, Body=greeting(AUTHOR).encode("utf-8"))
    response = s3.get_object(Bucket=bucket, Key=key)
    return response["Body"].read().decode("utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python hello_aws.py <your-bucket-name>")
    print(roundtrip(sys.argv[1]))
