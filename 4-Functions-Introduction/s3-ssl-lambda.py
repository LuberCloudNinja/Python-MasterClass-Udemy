import awspolicy
import boto3
import json
from awspolicy import *


def lambda_handler():
    authentication = boto3.session.Session(profile_name="lguilarte")
    s3_buckets = authentication.client('s3')
    all_buckets = []
    for buckets in s3_buckets.list_buckets()['Buckets']:
        all_buckets.append(buckets['Name'])
        bucket_name = buckets['Name']
        bucket_policy = {
            'Version': '2012-10-17',
            'Statement': [{
                'Sid': 'Deny non-HTTPS access',
                'Effect': 'Deny',
                'Principal': '*',
                'Action': ['s3:*'],
                'Resource': f'arn:aws:s3:::{bucket_name}/*',
                'Condition': {
                    'Bool': {
                        'aws:SecureTransport': 'false'
                    }
                }
            }]
        }
        bucket_policy = json.dumps(bucket_policy)

        for existing_buckets in all_buckets:
            existing_policies = s3_buckets.get_bucket_policy(
                Bucket=bucket_name)
            bkt_policy = existing_policies['Policy']
            bp_staging = bkt_policy[:-3]
            print(bp_staging)
            append_policy = bp_staging+bucket_policy
            response_2 = s3_buckets.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)



lambda_handler()
