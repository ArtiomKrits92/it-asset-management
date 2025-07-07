# IT Asset Management
Make your IT-related asset process simple and controlled. This Web-based system runs on Apache will make it happen.
* Note: Work in Progress. The final version may differ.

![Logo](https://cdn3d.iconscout.com/3d/premium/thumb/asset-allocation-3d-icon-download-in-png-blend-fbx-gltf-file-formats--money-management-portfolio-diversification-risk-classes-capital-preservation-investment-pack-business-icons-7863809.png?f=webp)

## Table Of Contents
1. Introduction<br>
2. Code Explaination<br>
    2.1 Data Structure<br>
    2.2 Main Menu<br>
    2.3 Project Files<br>
3. Deployment & Implementation<br>
4. License<br>
5. Authors<br>
6. Feedback<br>

## 1. Introduction
TBA

## 2. Code Explaination
### 2.1 Data Structure
TBA

### 2.2 Main Menu
- :one: Add New Item<br>
- :two: Delete Item<br>
- :three: Modify Item<br>
- :four: Assign Item<br>
- :five: Add New User<br>
- :six: Show All Users<br>
- :seven: Show All Items by the User<br>
- :eight: Show All Stock Items<br>
- :nine: Calculate Stock by Categories<br>

### 2.3 Project Files
- :file_folder: *python* directory contains pure Python code:
    - :memo: *main.py* is the main project file
    - :memo: *functions.py* contains functions for reusable logic of the main file
    - :memo: *demo.py* contains pre-created and loaded dummie data for demonstration purposes
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
    - :memo: *demo.py* dummie pre-loaded data webserver file
    - :memo: *wsgi.py* routing file for WSGI in order to work with Flask
    - :memo: *it-asset-management.conf* website configuration file for Apache
- :file_folder: *docker* directory contains Dockerfile
- :file_folder: *aws* directory contains data relevant to AWS deployment

## 3. Deployment & Implementation
### 3.1 Python Core Code Local Testing (Optional)
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

## Bonus: Tech Notes and Tracking Status for Authors
### Main Menu Structure (Entry Data Keys per Status):
1. Add New Item (Done)
2. Delete Item (Done)
3. Modify Item (Done)
4. Assign Item (Done)
5. Add New User (Done)
6. Show All Users (Done)
7. Show All Items by the User (Done)
8. Show All Stock Items (Done)
9. Calculate Stock by Categories (Done)

### Code Fine-Tuning:
1. Testing All Functions (Done)
2. Adding Typo Data Input by The User Checking (for non-numeric values) and Proper Error Messages Printing (Done)
3. Code Comments Adding (Done)
4. Code Checking for All Errors Scenarios (Done)

### General Project Implementation Steps Status:
1. Python Core Code Writing and Testing (Done) - Desmond
2. Python Core Code Migration to Webserver Support using Flask (Done) - Desmond
3. Adding Docker Containers Support (TBD) - Artiom
4. Project Migration to AWS Including Redundancy Support (TBD) - Artiom
5. Readme File Fine-Tuning and Proper Documentation Adding (TBD) - Desmond

