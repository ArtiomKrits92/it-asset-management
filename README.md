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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.2.3 Operating With Docker<br>
    2.4 AWS Cloud Architecture<br>
    2.5 Project Files<br>
3. Deployment and Implementation<br>
    3.1 Python Application Testing in Local Environment
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
Python Pure Code contains `main.py` with main menu UI, `functions.py` for all core logic and `demo.py` for dummy data pre-loading.
There are two different dabatases (Python dictionaries) exists in `functions.py` with relationships by `assigned_to` links items to users. There is fast lookup by users/items ID's.
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
- `Add New Item` - Validates category selection, generates unique item ID, creates item record and updates global item ID counter<br>
- `Delete Item` - Searches item by ID, removes from user's item list in case it assigned to him and deletes from items database<br>
- `Modify Item` - Loads existing item data by item ID, allows editing manufacturer, model and price data<br>
- `Assign Item` - Validates items and user exist, checks if item not already assigned, updates item status to "Assigned" and adds item ID to user's items list<br>
- `Add New User` - Generates unique user ID, creates user record and updates global user ID counter<br>
- `Show All Users` - Shows all existing users list<br>
- `Show All Items by the User` - Shows all assigned items to specific user by user ID<br>
- `Show All Stock Items` - Shows all existing stock items list<br>
- `Calculate Stock by Categories` - Calculates all stock items price by categories<br>

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
    print("❌ Error: Error: Invalid Item has been choosen.")  # Error Message Printing
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
```app.py``` - Main Flask Application
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
HTML template pages were pre-created for each menu item function. ```base.html``` page uses as a template for all pages and ```index.html``` page for the home page with users and items databases calculated statistics. Python code via Flask module is integrated and running on them based on menu function has choosen.

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
```Dockerfile``` was created with all relevant commands for "one-click" environment creation. Port 31415 is used for web application.
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
- `docker build -f docker/Dockerfile -t it-asset-management .` to build image based on Dockerfile
- `docker run -d -p 31415:31415 --name my-app it-asset-management` to run container based on the image
- `docker ps` and `curl http://localhost:31415` to verify running

### 2.4 AWS Cloud Architecture
TBA

### 2.5 Project Files
- :file_folder: *`aws`* directory contains data relevant to AWS deployment
    - :memo: *cloudformation.yaml* configuration file for CloudFormation in AWS environment
- :file_folder: *docker* directory contains Dockerfile
    - :memo: *Dockerfile* configuration file for Docker environment deployment
- :file_folder: *python* directory contains pure Python code:
    - :memo: *main.py* is the main project file
    - :memo: *functions.py* contains functions for reusable logic of the main file
    - :memo: *demo.py* contains pre-created and loaded dummy data for demonstration purposes
- :file_folder: *scripts* directory contains script files
    - :memo: *deploy.sh* AWS deployment automation script
- :file_folder: *website* directory contains website data like HTML pages etc.
    - :file_folder: *templates* pre-rendered .html webpages
        - :memo: *add_item.html*
        - :memo: *add_user.html*
        - :memo: *assign_item.html*
        - :memo: *base.html*
        - :memo: *delete_item.html*
        - :memo: *index.html*
        - :memo: *modify_item_form.html* 
        - :memo: *modify_item_select.html*
        - :memo: *show_stock_items.html* 
        - :memo: *show_user_items_select.html*
        - :memo: *show_user_items.html*
        - :memo: *show_users.html*
        - :memo: *stock_by_categoeirs.html*
    - :memo: *app.py* main webserver file
    - :memo: *data.py* database data webserver file
    - :memo: *demo.py* dummy pre-loaded data webserver file
    - :memo: *it-asset-management.conf* website configuration file for Apache
    - :memo: *wsgi.py* routing file for WSGI in order to work with Flask

## 3. Deployment and Implementation
### 3.1 Python Application Testing in Local Environment
Before proceed to the next steps, you can test pure python code in local environment in case to check its workability.

### 3.2 Migrating Python Code to Webserver Running on Apache Using Flask
Testing Deployment:
- docker run -it -p 500:80 ubuntu
- apt update
- apt install git -y && apt install apache2 -y
- git clone https://github.com/dcoacher/it-asset-management.git
- mkdir /var/www/it-asset-management
- cp -r it-asset-management/website/templates/ it-asset-management/website/app.py it-asset-management/website/wsgi.py it-asset-management/website/demo.py it-asset-management/website/data.py /var/www/it-asset-management/
- cp -r it-asset-management/website/it-asset-management.conf /etc/apache2/sites-available/
- apt-get install libapache2-mod-wsgi-py3 -y
- apt install python3-flask -y
- a2ensite it-asset-management.conf && a2dissite 000-default.conf
- service apache2 reload && service apache2 restart

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
