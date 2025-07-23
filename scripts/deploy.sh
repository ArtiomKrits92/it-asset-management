#!/bin/bash
# IT Asset Management AWS Deployment Script

echo "=== Getting AWS Account ID ==="
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
echo "Account ID: $ACCOUNT_ID"

echo "=== Creating ECR Repository ==="
aws ecr create-repository --repository-name it-asset-management --region us-east-1

echo "=== Building Docker Image ==="
docker build -f docker/Dockerfile -t it-asset-management .

echo "=== Logging into ECR ==="
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

echo "=== Tagging and Pushing Image ==="
docker tag it-asset-management:latest $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/it-asset-management:latest
docker push $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/it-asset-management:latest

echo "=== Deployment Complete ==="
echo "Image URI: $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/it-asset-management:latest"