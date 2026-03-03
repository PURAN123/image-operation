import os
import json
import boto3
from botocore.exceptions import ClientError

def get_secret(secret_name, region_name="ap-south-1"):
    try:
        client = boto3.client("secretsmanager", region_name=region_name)
        response = client.get_secret_value(SecretId=secret_name)

        if "SecretString" in response:
            return json.loads(response["SecretString"])
        else:
            return None

    except ClientError as e:
        print("AWS Secret not found:", e)
        return None