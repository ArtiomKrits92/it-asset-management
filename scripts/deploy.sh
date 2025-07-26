#!/bin/bash
# IT Asset Management AWS Deployment Script

echo "=== Getting AWS Account ID ==="
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
echo "Account ID: $ACCOUNT_ID"

echo "=== Creating ECR Repository ==="
aws ecr create-repository --repository-name it-asset-management --region us-east-1 || echo "Repository already exists"

echo "=== Building Docker Image ==="
docker build -f docker/Dockerfile -t it-asset-management .

echo "=== Logging into ECR ==="
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

echo "=== Tagging and Pushing Image ==="
IMAGE_URI="$ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/it-asset-management:latest"
docker tag it-asset-management:latest $IMAGE_URI
docker push $IMAGE_URI

echo "=== Deploying CloudFormation Stack ==="
aws cloudformation deploy \
  --template-file aws/cloudformation.yaml \
  --stack-name it-asset-management-stack \
  --parameter-overrides ImageURI=$IMAGE_URI \
  --capabilities CAPABILITY_IAM \
  --region us-east-1

echo "=== Getting Application URL ==="
LOAD_BALANCER_URL=$(aws cloudformation describe-stacks \
  --stack-name it-asset-management-stack \
  --query 'Stacks[0].Outputs[?OutputKey==`LoadBalancerURL`].OutputValue' \
  --output text \
  --region us-east-1)

echo "=== Deployment Complete ==="
echo "Image URI: $IMAGE_URI"
echo "Application URL: $LOAD_BALANCER_URL"
echo ""
echo "🎉 Your application will be available at: $LOAD_BALANCER_URL"
echo "⏰ Note: It may take 5-10 minutes for instances to become healthy"