# AWS Deployment Guide

## Prerequisites
- AWS CLI installed (Chocolatey: `choco install awscli`)
- Docker installed and running
- AWS Lab credentials from course platform

## Quick Deployment Steps

### 1. Set AWS Credentials
```bash
# Get from AWS Lab "Cloud Access" section
export AWS_ACCESS_KEY_ID="[from lab]"
export AWS_SECRET_ACCESS_KEY="[from lab]"  
export AWS_SESSION_TOKEN="[from lab]"
export AWS_DEFAULT_REGION="us-east-1"
2. Run Deployment Script
bash# Make script executable (Linux/Mac)
chmod +x scripts/deploy.sh

# On Windows, run directly:
bash scripts/deploy.sh
Commands Reference
All AWS ECR commands are automated in deploy.sh script
Notes

AWS Lab credentials expire every few hours
Script automatically detects new AWS account ID
Safe to run multiple times


## 📝 Key Points:
1. **After `export AWS_DEFAULT_REGION="us-east-1"`** you MUST have **```** on the next line
2. **Then** start the new section with **### 2. Run Deployment Script**
3. **Then** start a new code block with **```bash**

**The ``` symbols close and open code blocks - that's what's missing!**

Try this shorter version first, then save it (`Ctrl + S`). Let me know if it looks right!