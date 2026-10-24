"""Tests for hello_aws.py. They run on GitHub Actions for every pull request.

Note that they need no AWS login: FakeS3 stands in for the real S3 service.
"""
import io

import hello_aws


class FakeS3:
    """A tiny in-memory stand-in for boto3's S3 client."""

    def __init__(self):
        self.store = {}

    def put_object(self, Bucket, Key, Body):
        self.store[(Bucket, Key)] = Body

    def get_object(self, Bucket, Key):
        return {"Body": io.BytesIO(self.store[(Bucket, Key)])}


def test_greeting_names_the_author():
    assert hello_aws.greeting("alice") == "Hello from alice!"


def test_author_was_changed():
    assert hello_aws.AUTHOR != "your-github-username", "set AUTHOR to your GitHub username"


def test_roundtrip_returns_what_was_uploaded():
    fake = FakeS3()
    text = hello_aws.roundtrip("some-bucket", s3=fake)
    assert text == hello_aws.greeting(hello_aws.AUTHOR)
    assert ("some-bucket", "hello.txt") in fake.store
