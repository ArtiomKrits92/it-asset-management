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
- :eight: Sort Items by Name (A-Z)<br>
- :nine: Sort Items by Price (₪ - ₪₪₪)<br>
- :zero: Calculate Stock by Categories<br>

### 2.3 Project Files
- :file_folder: *python* directory contains pure Python code:
    - :memo: *main.py* is the main project file
    - :memo: *functions.py* contains functions for reusable logic of the main file
    - :memo: *demo.py* contains pre-created and loaded dummie data for demonstration purposes
- :file_folder: *website* directory contains website data like HTML pages etc.
- :file_folder: *docker* directory contains Dockerfile
- :file_folder: *aws* directory contains data relevant to AWS deployment

## 3. Deployment & Implementation
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

## Bonus: Tech Notes for Authors
Main Menu Structure:
Entry Data Keys:
1. Add New Item
2. Delete Item
3. Modify Item
4. Assign Item
5. Add New User
6. Show All Users
7. Show All Items by the User
8. Sort Items by Name (A-Z)
9. Sort Items by Price (₪ - ₪₪₪)
0. Calculate Stock by Categories

Entry Data Keys and Explainations:
1. Add New Item - Keys: Item Name, Main Category, Secondary Category, Manufacturer, Model, Price Per Unit, Quantity (maybe using ID as a key)
* Main Categories: Assets, Accessories, Licenses
* Secondary Categories: Assets (PC, Laptop), Accessories (Mouse, Keyboard, Docking Station, Monitor, Headset), Licenses (Serial Number, Subscription)
* By default after adding the item to the database the items status will be "In Stock". Option to assign the item to the user directly after adding to the database will be prompted.
* Item Status Types: In Stock (for the new items), Assigned (for assigned to the user items)

2. Delete Item - Delete Item from the database using item ID as a key
3. Modify Item - Change the Item's Name, Manufacturer, Model, Price Per Unit
4. Assign Item - Assign the Item to the User
5. Add New User - Add New User to the database using ID as a key
6. Show All Users - All users existing in the database will be shown
7. Show All Items by the User - All items will be displayed for the same user
8. Sort Items by Name (A-Z) - The items will be sorted by Name from A to Z including category, quantity and price
* Maybe need to calculate and display the available items and assigned items to the users (For example: Total, Assigned, In Stock)

9. Sort Items by Price (₪ - ₪₪₪) - The items will be sorted by Price from cheapest to expensive including name, category, quantity and price
0. Calculate Stock by Categories - All Stock will be calculated in ILS currency and displayed per Category.
