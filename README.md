# AWS-Course-Project
# Cloud Infrastructure for Web App Deployment

This repository contains the complete infrastructure setup and automation for deploying a scalable, resilient web application on AWS using Terraform, AWS CloudFormation, and Python Boto3 scripts.

---

## 📌 Project Overview

This project demonstrates:
- Infrastructure as Code using Terraform and CloudFormation
- Deployment of a PHP-based web application on EC2
- Integration with RDS MySQL database
- Autoscaling EC2 instances based on load
- Logging file uploads to S3 using AWS Lambda and CloudWatch
- Manual resource management using Python and Boto3

---

## 📁 Repository Structure

```
cloud-infra-webapp-deployment/
│
├── terraform/                  # Terraform scripts for VPC, subnets, ALB, EC2 autoscaling
│   └── main.tf
│
├── cloudformation/            # CloudFormation YAML templates for EC2, RDS, Lambda
│   └── webapp_stack.yaml
│
├── boto3-scripts/             # Python files to interact with EC2, S3, Lambda
│   ├── create_s3_upload.py
│   ├── ec2_metadata.py
│   ├── list_instances.py
│   └── invoke_lambda.py
│
├── architecture-diagram/     # Architecture diagram image
│   └── final-diagram.png
│
├── README.md                  # Project documentation and setup instructions
└── .gitignore
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/cloud-infra-webapp-deployment.git
cd cloud-infra-webapp-deployment
```

### 2. Deploy with Terraform
```bash
cd terraform
terraform init
terraform apply
```

### 3. Deploy with CloudFormation
Upload your `webapp_stack.yaml` via AWS Console or:
```bash
aws cloudformation deploy --template-file webapp_stack.yaml --stack-name my-webapp-stack
```

### 4. Upload Files to S3
```bash
aws s3 cp test-file.txt s3://your-bucket-name/
```

### 5. Invoke Lambda via CLI
```bash
aws lambda invoke --function-name S3UploadLogger --payload '{}' response.json
```

---

## 🔍 Python Scripts (Boto3)

- `create_s3_upload.py`: Creates an S3 bucket and uploads a file
- `ec2_metadata.py`: Retrieves metadata of the running EC2 instance
- `list_instances.py`: Lists all running EC2 instances
- `invoke_lambda.py`: Invokes the logging Lambda function manually

---

## 🖼️ Architecture Diagram

A high-level architecture showing:
- Public & Private Subnets
- EC2 Web Server behind ALB
- RDS Database in Private Subnet
- S3 Bucket + Lambda for Logging
- IAM Roles and Security Groups

---


