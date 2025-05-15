import boto3
import json

# Initialize Lambda client
lambda_client = boto3.client('lambda', region_name='us-east-1')

# Define payload
# Define payload (simulate S3 upload event)
payload = {
    "Records": [
        {
            "s3": {
                "bucket": { "name": "myapp-log-bucket-hitakshi" },
                "object": { "key": "test-file.txt" }
            }
        }
    ]
}

# Invoke Lambda function
response = lambda_client.invoke(
    FunctionName='S3UploadLogger',
    InvocationType='RequestResponse',
    Payload=json.dumps(payload)
)

# Read and print response
response_payload = response['Payload'].read().decode('utf-8')
print("Response from Lambda:")
print(response_payload)
