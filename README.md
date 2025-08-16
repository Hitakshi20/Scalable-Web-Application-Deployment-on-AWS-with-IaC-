# Scalable Web Application Deployment on AWS with IaC


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
AWS-Course-Project/
│
├── terraform files/                  # Terraform scripts for VPC, subnets, ALB, EC2 autoscaling
│   └── main.tf
│   └── variables.tf
│   └── outputs.tf
│
├── cloudformation templates/            # CloudFormation YAML templates for EC2, RDS, Lambda
│   └── ec2-stack.yaml
│   └── lambda-stack.yaml
│   └── rds-stack.yaml
│
├── Python files/             # Python files to interact with EC2, S3, Lambda
│   ├── create_s3.py
│   ├── ec2.py
│   ├── list_instances.py
│   └── invoke_lambda.py
│
├── Arhitecture Diagram.jpg  # Architecture diagram image
│   
├── README.md                  # Project documentation and setup instructions
```

---
## 🖼️ Architecture Diagram

A high-level architecture showing:
- Public & Private Subnets
- EC2 Web Server behind ALB
- RDS Database in Private Subnet
- S3 Bucket + Lambda for Logging
- IAM Roles and Security Groups

---
## 🔍 How It Works

1. Terraform provisions a VPC, subnets, route tables, and security groups.
2. CloudFormation deploys an EC2 instance (PHP web app) and RDS DB.
3. Files uploaded to S3 trigger Lambda, which logs metadata to CloudWatch.
4. Python scripts list EC2 instances, retrieve metadata, and manually invoke Lambda.

---
## 🧪 Testing the Setup

- Access your EC2 app via public IP.
- Upload a file to the S3 bucket.
- View logs in CloudWatch.
- Run `invoke_lambda.py` and observe results.

---
## ⚙️ Technologies Used

- AWS EC2, RDS, S3, Lambda, CloudWatch, IAM
- Terraform
- AWS CloudFormation
- Boto3 (Python SDK for AWS)
- AWS CLI
- GitHub

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Hitakshi20/AWS-Course-Project.git
cd AWS-Course-Project
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
aws s3 cp test-file.txt s3://myapp-log-bucket-hitakshi/
```

### 5. Invoke Lambda via CLI
```bash
aws lambda invoke --function-name S3UploadLogger --payload '{}' response.json
```


