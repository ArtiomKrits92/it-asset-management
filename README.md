# it-asset-management
Description: IT Asset Management system based on Apache webserver

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