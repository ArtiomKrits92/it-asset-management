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
Why we choose to made this application? The answer is pretty simple - every IT department needs asset tracking.<br>
It prevents equipment loss, tracks costs, manages assignments in every organization.

## 2. Code Explaination and Data Structure

### 2.1 Python Application Review

#### 2.1.1 Data Structure Design
TBA

#### 2.1.2 Main Menu Functions
- :one: Add New Item<br>
- :two: Delete Item<br>
- :three: Modify Item<br>
- :four: Assign Item<br>
- :five: Add New User<br>
- :six: Show All Users<br>
- :seven: Show All Items by the User<br>
- :eight: Show All Stock Items<br>
- :nine: Calculate Stock by Categories<br>

#### 2.1.3 Input Validations
TBA

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
    - :memo: *deploy.sh* script for deploying EC2 machine in AWS environment
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
