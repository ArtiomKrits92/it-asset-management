# IT Asset Management
Make your IT Asset Management process simple and controlled. This web-based, runs on Apache complete application for tracking computer equipment, software licenses, and accessories in the organization, will make it happen.

![Logo](https://cdn3d.iconscout.com/3d/premium/thumb/asset-allocation-3d-icon-download-in-png-blend-fbx-gltf-file-formats--money-management-portfolio-diversification-risk-classes-capital-preservation-investment-pack-business-icons-7863809.png?f=webp)

## Table Of Contents
1. Introduction<br>
2. Code Explaination and Data Structure<br>
    2.1 Python Application Review<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.1 Data Structure Design<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.2 Main Menu Functions<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.3 Input Validations<br>
    2.2 Web Development Using Flask<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.2.1 Application Structure<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.2.2 HTML Template System<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.2.3 Other Features<br>
    2.3 Containerization with Docker<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.1 Dockerfile<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.2 Operating With Docker<br>
    2.4 AWS Cloud Architecture<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.4.1 CloudFormation Template Structure<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.4.2 EC2 Launch Template<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.4.3 Automated Deployment Script<br>
    2.5 Project Files<br>
3. Deployment and Implementation<br>
    3.1 Getting Started<br>
    3.2 Cloning Github Repository<br>
    3.3 Testing Python Application in Local Environment<br>
    3.4 Code Migration to Webserver Using Flask and Docker Container<br>
    3.5 AWS Setup and Cloud Deployment<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.5.1 Setting AWS Lab Credentials<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.5.2 Running Automated Deployment Script<br>
4. License<br>
5. Authors<br>
6. Feedback<br>

## 1. Introduction
Why we decided to made this application? The answer is pretty simple - every IT department needs asset tracking.<br>
It prevents equipment loss, tracks costs, manages assignments in every organization.

## 2. Code Explaination and Data Structure
Architecture Evolution of the Project:
- Python Application Pure Code Developing
- Code Integration to Webserver Using Flask
- Containerization With Docker
- Migration The Environment to AWS With High Availability

### 2.1 Python Application Review
#### 2.1.1 Data Structure Design
Python Pure Code contains *`main.py`* with main menu UI, *`functions.py`* for all core logic and *`demo.py`* for dummy data pre-loading.
There are two different dabatases (Python dictionaries) exists in *`functions.py`* with relationships by *`assigned_to`* links items to users. There is fast lookup by users/items ID's.
```python
# Users Database
users_db["1"] = {"name": "Brandon Guidelines", "items": []}
users_db["2"] = {"name": "Carnegie Mondover", "items": []}
users_db["3"] = {"name": "John Doe", "items": []}

# Items Database
items_db["1"] = {
    "id": "1", "main_category": "Assets", "sub_category": "Laptop", "manufacturer": "Dell", "model": "XPS", "price": 5000, "quantity": 1, "status": "In Stock", "assigned_to": None
}
items_db["2"] = {
    "id": "2", "main_category": "Assets", "sub_category": "Laptop", "manufacturer": "Lenovo", "model": "X1 Carbon", "price": 8300, "quantity": 1, "status": "In Stock", "assigned_to": None
}
items_db["3"] = {
    "id": "3", "main_category": "Assets", "sub_category": "PC", "manufacturer": "Asus", "model": "Desktop Intel Core i9 14900KS", "price": 14900, "quantity": 1, "status": "In Stock", "assigned_to": "1"
}
```

#### 2.1.2 Main Menu Functions
- *`Add New Item`* - Validates category selection, generates unique item ID, creates item record and updates global item ID counter<br>
- *`Delete Item`* - Searches item by ID, removes from user's item list in case it assigned to him and deletes from items database<br>
- *`Modify Item`* - Loads existing item data by item ID, allows editing manufacturer, model and price data<br>
- *`Assign Item`* - Validates items and user exist, checks if item not already assigned, updates item status to "Assigned" and adds item ID to user's items list<br>
- *`Add New User`* - Generates unique user ID, creates user record and updates global user ID counter<br>
- *`Show All Users`* - Shows all existing users list<br>
- *`Show All Items by the User`* - Shows all assigned items to specific user by user ID<br>
- *`Show All Stock Items`* - Shows all existing stock items list<br>
- *`Calculate Stock by Categories`* - Calculates all stock items price by categories<br>

#### 2.1.3 Input Validations
There are multiple input validation patterns:
- Numeric Validation
```python
if not price.isdigit(): # Checking if the user entered numeric value into the input line above
    print("❌ Error: Entered value for the price must be numeric.")   # Printing Error Message
    return  # Exit the function in this phase (return to main menu)
```
- Category Validation
```python
if sub_category.lower() not in ["pc", "laptop"]:    # In case the User's choise is not equal the sub category prompt
    print("❌ Error: Error: Invalid Item has been chosen.")  # Error Message Printing
    return  # Exit the function in this phase (return to main menu)
```
- Existence Validation
```python
    if not users_db:    # In case there are no users exists in the Users Database
        print("❌ Error: There are no users existing in the database.") ## Printing Error Message 
```
- Item Assignment Status Validation
```python
if items_db[item_id]["status"] == "Assigned":   # Checking if the Item's Status is "Assigned"
    print(f"❌ Error: The item `{items_db[item_id]["sub_category"]} {items_db[item_id]["manufacturer"]} {items_db[item_id]["model"]}` with the ID `{item_id}` is already assigned to another user.")    # Printing Error Message because the item is already assigned to another user
    return  # Exit the function in this phase (return to main menu)
```
### 2.2 Web Development Using Flask
Migration phase to web-server using Flask module has been choosen because Flask is a great solution for small or medium applications, it doesn't force specific structure and it's easy to convert existing Python login.

#### 2.2.1 Application Structure
*```app.py```* - Main Flask Application
```python
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # For flash messages
```
Route Pattern Example:
```python
@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    global item_id_counter
    if request.method == "POST":
        # Process form submission
        return redirect(url_for("add_item"))
    # Show form
    return render_template("add_item.html", menu_links=get_menu_links())
```

#### 2.2.2 HTML Template System
HTML template pages were pre-created for each menu item function. *```base.html```* page uses as a template for all pages and *```index.html```* page for the home page with users and items databases calculated statistics. Python code via Flask module is integrated and running on them based on menu function has chosen.

#### 2.2.3 Other Features
- Flash Messages System
```python
flash(f"Item with ID {item_id} deleted.", "success")
flash(f"No item found with ID {item_id}.", "danger")
```
- Required Fields Validation
```html
<form method="POST">
  <div class="mb-3">
    <label for="sub_category" class="form-label">Sub Category</label>
    <select class="form-select" id="sub_category" name="sub_category" required>
      <option value="">Select a main category</option>
    </select>
  </div>
  <button type="submit" class="btn btn-primary">Add Item</button>
</form>
```
- Main and Sub-Categories Validation
```html
  <div class="mb-3">
    <label for="main_category" class="form-label">Main Category</label>
    <select class="form-select" id="main_category" name="main_category" required onchange="updateSubcategories()">
      <option value="">Choose category</option>
      <option value="Assets">Assets</option>
      <option value="Accessories">Accessories</option>
      <option value="Licenses">Licenses</option>
    </select>
  </div>

  <div class="mb-3">
    <label for="sub_category" class="form-label">Sub Category</label>
    <select class="form-select" id="sub_category" name="sub_category" required>
      <option value="">Select a main category</option>
    </select>
  </div>
```
- Numeric Validation
```html
  <div class="mb-3">
    <label for="price" class="form-label">Price per Unit (₪)</label>
    <input type="number" class="form-control" id="price" name="price" min="0" step="0.01" required />
  </div>
```

### 2.3 Containerization with Docker
Containerization using Docker provides same environment everywhere, the application runs independently of host system, it works on any Docker-enabled system and it's easy to run multiple instances with it.

#### 2.3.1 Dockerfile
*```Dockerfile```* was created with all relevant commands for "one-click" environment creation. Port 31415 is used for web application.
```python
# Use Ubuntu as base image
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-flask \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /var/www/it-asset-management

# Copy website files from the correct path
COPY website/ ./

# Install Flask using pip (backup)
RUN pip3 install flask

# Expose port 31415 web access
EXPOSE 31415

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run when container starts
CMD ["python3", "-m", "flask", "run", "--port=31415"]
```
#### 2.3.2 Operating With Docker
Follow the commands below in order to build image using Dockerfile, run container based on the image and verify running afterward:
- *`docker build -f docker/Dockerfile -t it-asset-management .`* to build image based on Dockerfile
- *`docker run -d -p 31415:31415 --name my-app it-asset-management`* to run container based on the image
- *`docker ps`* and *`curl http://localhost:31415`* to verify running

### 2.4 AWS Cloud Architecture
Amazon Web Services platform has been chosen for cloud hosting of the web-server including HA (High Availability) feature using AWS tools:
- Load Balancer
- Auto Scaling Group
- Multiple EC2 Instances
- Multiple Availability Zones

#### 2.4.1 CloudFormation Template Structure
*```cloudformation.yaml```* file contains all relevant configuration for the above mentioned features to deploy:
- *`Network Infrastructure`* - Isolated network environment with multiple subnets located in different avialability zones with direct internet access for web servers
```yaml
VPC: 10.0.0.0/16
PublicSubnet1: 10.0.1.0/24 (AZ-1)
PublicSubnet2: 10.0.2.0/24 (AZ-2)
InternetGateway: Internet access
```
- *`Security Groups`* - Least privilege access
```yaml
LoadBalancerSG: Port 80 from anywhere
WebServerSG: Port 31415 from LoadBalancer only
```
- *`Auto Scaling Group`* - Always 2 or more instances properly running for HA including health check for replacing failed instances
```yaml
MinSize: 2
MaxSize: 4
DesiredCapacity: 2
HealthCheckType: ELB
```
- *`Application Load Balancer`* - Splits users requests sends to web servers across instances via sending traffic to healthy instances only
```yaml
Scheme: internet-facing
HealthCheckPath: /
HealthCheckInterval: 30s
```

#### 2.4.2 EC2 Launch Template
Launch Template for EC2 instances is used for creating new instances in order to automatically replace failed instances, which can increase capacity automatically as well.

```shell
#!/bin/bash
# AWS Academy compatible startup script

# Update system and install requirements
yum update -y
yum install -y docker git

# Start Docker
service docker start
chkconfig docker on
usermod -a -G docker ec2-user

# Clone repository and build app (no ECR dependency)
cd /home/ec2-user
git clone https://github.com/dcoacher/it-asset-management.git
cd it-asset-management

# Build Docker image from source
docker build -f docker/Dockerfile -t it-asset-management .

# Run the application
docker run -d -p 31415:31415 --restart unless-stopped --name it-asset-app it-asset-management
```

### 2.4.3 Automated Deployment Script
Automated AWS Deployment Script has been used as a part of DevOps flow in order to automate the deployment process to cloud environment. As a result we have the same infrastructure available, which can be deployed to test environments every time it needs.

```bash
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
```

### 2.5 Project Files
- :file_folder: *`aws`* directory contains data relevant to AWS deployment
    - :memo: *`cloudformation.yaml`* configuration file for CloudFormation in AWS environment
- :file_folder: *`docker`* directory contains Dockerfile
    - :memo: *`Dockerfile`* configuration file for Docker environment deployment
- :file_folder: *`python`* directory contains pure Python code:
    - :memo: *`main.py`* is the main project file
    - :memo: *`functions.py`* contains functions for reusable logic of the main file
    - :memo: *`demo.py`* contains pre-created and loaded dummy data for demonstration purposes
- :file_folder: *`scripts`* directory contains script files
    - :memo: *`deploy.sh`* AWS deployment automation script
- :file_folder: *`website`* directory contains website data like HTML pages etc.
    - :file_folder: *`templates`* pre-rendered .html webpages
        - :memo: *`add_item.html`*
        - :memo: *`add_user.html`*
        - :memo: *`assign_item.html`*
        - :memo: *`base.html`*
        - :memo: *`delete_item.html`*
        - :memo: *`index.html`*
        - :memo: *`modify_item_form.html`* 
        - :memo: *`modify_item_select.html`*
        - :memo: *`show_stock_items.html`* 
        - :memo: *`show_user_items_select.html`*
        - :memo: *`show_user_items.html`*
        - :memo: *`show_users.html`*
        - :memo: *`stock_by_categoeirs.html`*
    - :memo: *`app.py`* main webserver file
    - :memo: *`data.py`* database data webserver file
    - :memo: *`demo.py`* dummy pre-loaded data webserver file
    - :memo: *`it-asset-management.conf`* website configuration file for Apache
    - :memo: *`wsgi.py`* routing file for WSGI in order to work with Flask

## 3. Deployment and Implementation
### 3.1 Getting Started
Before starting, ensure to check your environment is ready to go:
- AWS CLI Installed - *[AWS CLI install and update instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)*
- Docker Installed and Running - *[Install Docker Engine](https://docs.docker.com/engine/install/)*
- Git Installed - *[Git Downloads](https://git-scm.com/downloads)*
- AWS Sandbox Lab is Running - *[AWS Academy Login](https://awsacademy.instructure.com/)*

### 3.2 Cloning Github Repository
*`Git Bash`* application or *`Visual Studio Code terminal`* will be used for the deployment in the next steps:
- *`mkdir Documents/technion-midterm-project`* to create a clean workspace for demonstration
- *`cd Documents/technion-midterm-project`* to change work directory
- *`git clone https://github.com/dcoacher/it-asset-management.git`* to clone git repository
- *`cd it-asset-management`* to change work directory
- *`ls -la`* to display project structure

### 3.3 Testing Python Application in Local Environment
Test Python application in local environment in order to check it's workability:
- Open the project directory folder in Visual Studio Code
- Run the *`main.py`* application file from *`python`* folder

### 3.4 Code Migration to Webserver Using Flask and Docker Container
Migrate the Python application to Apache webserver using Flask module and Docker Containerization and perform test in local environment:
- *`docker build -f docker/Dockerfile -t it-asset-management .`* to build image based on Dockerfile
- *`docker run -d -p 31415:31415 --name my-app it-asset-management`* to run container based on the image
- *`curl http://localhost:31415`* to verify running
- *`docker stop my-app && docker rm my-app`* for cleanup performing

### 3.5 AWS Setup and Cloud Deployment
#### 3.5.1 Setting AWS Lab Credentials
TBA

#### 3.5.2 Running Automated Deployment Script
TBA

## 4. License
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://github.com/dcoacher/it-asset-management/blob/main/LICENSE)

## 5. Authors
This project is a result of the great collaboration of the two developers:
- Desmond Coacher - [@dcoacher](https://github.com/dcoacher)
- Artiom Krits - [@ArtiomKrits92](https://github.com/ArtiomKrits92)

## 6. Feedback
If you have any feedback, feel free to contact us via email: 
- [Desmond Coacher](mailto:dcoacher@outlook.com)
- [Artiom Krits](mailto:artiomkrits92@gmail.com)
