import requests

# AWS EC2 Metadata base URL
base_url = "http://169.254.169.254/latest/meta-data/"

# Optional: Get specific metadata items
fields = ["instance-id", "ami-id", "public-ipv4", "local-ipv4", "placement/availability-zone"]

print("Retrieving EC2 Metadata...\n")
for field in fields:
    response = requests.get(base_url + field)
    if response.status_code == 200:
        print(f"{field}: {response.text}")
    else:
        print(f"{field}: Not available")
