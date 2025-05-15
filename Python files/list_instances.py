import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

print("Listing Running EC2 Instances...\n")

response = ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        public_ip = instance.get('PublicIpAddress', 'No Public IP')
        private_ip = instance.get('PrivateIpAddress', 'No Private IP')
        zone = instance['Placement']['AvailabilityZone']
        print(f"ID: {instance_id} | Public IP: {public_ip} | Private IP: {private_ip} | AZ: {zone}")
