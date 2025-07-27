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
    2.2 Migration to Webserver Using Flask<br>
    2.3 Containerization with Docker<br>
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
### 2.2 Migration to Webserver Using Flask
TBA

### 2.3 Containerization with Docker
TBA

### 2.4 AWS Cloud Architecture
TBA

### 2.5 Project Files
- :file_folder: *aws* directory contains data relevant to AWS deployment
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
