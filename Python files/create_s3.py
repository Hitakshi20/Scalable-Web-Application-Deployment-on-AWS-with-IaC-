import boto3
import uuid
import os

bucket_suffix = uuid.uuid4().hex[:8]
bucket_name = f"courseproject-hitakshis3"
region = "us-east-1"  

s3 = boto3.client("s3", region_name=region)

# 1. Create the bucket (handle us-east-1 special case)
if region == "us-east-1":
    s3.create_bucket(Bucket=bucket_name)
else:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": region}
    )

print(f"Created bucket: {bucket_name}")

# 2. Upload file (make sure test.txt exists)
file_to_upload = "test-file.txt"
if not os.path.exists(file_to_upload):
    with open(file_to_upload, "w") as f:
        f.write("Hello from Python + Boto3!\n")

s3.upload_file(file_to_upload, bucket_name, file_to_upload)
print(f"Uploaded '{file_to_upload}' to '{bucket_name}'")
