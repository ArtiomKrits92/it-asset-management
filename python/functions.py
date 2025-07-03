### This is a Functions file which will contain functions for reusable logic of the Main file.
import getpass  # Importing Getpass module for password input data masking

items_db = {}   # Creation of items database empty list
users_db = {}   # Creation of users database empty list

user_id_counter = 7 # Creation of User ID Counter value (will start from 7)
item_id_counter = 7 # Creation of Item ID Counter value (will start from 7)

def welcome_screen():   # Welcome Screen function
    print("\nWelcome to IT Asset Management System!")
    print("Credits to Desmond Coacher and Artiom Krits.")

def login_screen(): # Login Screen function
    while True: # Loop for user input prompt for username and password credentials
        username = input("Enter the username: ")
        password = getpass.getpass("Enter the password: ")
        if username == "root" and password == "123456": # Validation for the entered by the user credentials
            print(f"✅ Success: You has been successfully logged in as `{username}`.")    # Success case - break the loop and login
            break
        else:
            print("❌ Error: Incorrect username/password data has been entered. Please try again.\n")   # Incorrect data provided case, return to the loop start

def main_menu_handler(): # Menu Handler function
    print("\n1. Add New Item")
    print("2. Delete Item")
    print("3. Modify Item")
    print("4. Assign Item")
    print("5. Add New User")
    print("6. Show All Users")
    print("7. Show All Items by the User")
    print("8. Show All Stock Items")
    print("9. Calculate Stock by Categories\n")

def main_menu_add_new_items():
    global item_id_counter
    item_id = str(item_id_counter)
    main_category = input("Choose Category (Assets/Accessories/Licenses): ")
    if main_category == "Assets":
        sub_category = input("Choose Item (PC/Laptop): ")
        if sub_category.lower() not in ["pc", "laptop"]:
            print("❌ Error: Error: Invalid option has been choosen.")

    elif main_category == "Accessories":
        sub_category = input("Choose Item (Mouse/Keyboard/Docking Station/Monitor/Headset): ")
        if sub_category.lower() not in ["mouse", "keyboard", "docking station", "monitor", "headset"]:
            print("❌ Error: Error: Invalid option has been choosen.")

    elif main_category == "Licenses":
        sub_category = input("Choose Item (Serial Number/Subscription): ")
        if sub_category.lower() not in ["serial number", "subscription"]:
            print("❌ Error: Error: Invalid option has been choosen.")

    else:
        print("❌ Error: Invalid option has been choosen.")

    manufacturer = input("Enter the Manufacturer: ")
    model = input("Enter the Model: ")
    price = int(input("Enter the Price per Unit: "))

    item = {
        "id": item_id,  # Convert to string in order to store all the item ID's in the same format
        "main_category": main_category,
        "sub_category": sub_category,
        "manufacturer":manufacturer,
        "model": model,
        "price": price,
        "quantity": 1,
        "status": "In Stock",
        "assigned_to": None
    }

    item_id_counter += 1
    items_db[item["id"]] = item
    print(f"✅ Success: The Item `{sub_category} {manufacturer} {model}` with the ID `{item_id}` was successfully added to the database.")

def main_menu_delete_item():
    item_id = input("Enther Item ID to delete: ")
    if item_id in items_db:
        item_sub_category_ram = items_db[item_id]["sub_category"]
        item = items_db[item_id]
        assigned_user_id = item.get("assigned_to")
        if assigned_user_id in users_db:
            if item_id in users_db[assigned_user_id]["items"]:
                users_db[assigned_user_id]["items"].remove(item_id)
        
        del items_db[item_id]
        print(f"✅ Success: The item `{item_sub_category_ram}` with the ID `{item_id}` has been revomed from the database.")
    else:
        print(f"❌ Error: There are no item with the ID `{item_id}` existing in the database.")
              
def main_menu_modify_item():
    item_id = input("Enter Item ID to modify: ")
    if item_id in items_db:
        item = items_db[item_id]
        print("")
        print("-" * 50)
        print(f"Item            : {item["sub_category"]}")
        print("-" * 50)
        print(f"Manufacturer    : {item["manufacturer"]}")
        print("-" * 50)
        print(f"Model           : {item["model"]}")
        print("-" * 50)
        print(f"Price per Unit  : {item["price"]} ₪")
        print("-" * 50)
        change_type = input("\nWhich data do you want to modify?\nManufacturer (mfg), Model (m), Price per Unit (p) \nEnther your choise: ")
        if change_type.lower() == "mfg":
            current_manufacturer = item["manufacturer"]
            changed_manufacturer = input(f"Current Manufacturer is `{item["manufacturer"]}`. Enther new Manufacturer: ")
            item["manufacturer"] = changed_manufacturer
            print(f"✅ Success: Manufacturer for the Item `{item["sub_category"]}` with the ID `{item["id"]}` has been changed from `{current_manufacturer}` to `{changed_manufacturer}`.")

        elif change_type.lower() == "m":
            current_model = item["model"]
            changed_model = input(f"Current Model is `{item["model"]}`. Enther new Model: ")
            item["model"] = changed_model
            print(f"✅ Success: Model for the Item `{item["sub_category"]}` with the ID `{item["id"]}` has been changed from `{current_model}` to `{changed_model}`.")

        elif change_type.lower() == "p":
            current_price = item["price"]
            changed_price = input(f"Current Price is `{item["price"]} ₪`. Enther new Price: ")
            try:
                item["price"] = int(changed_price)
                print(f"✅ Success: Price for the Item `{item["sub_category"]}` with the ID `{item["id"]}` has been changed from `{current_price}` to `{changed_price}`.")
            except ValueError:
                print("❌ Error: Entered value must be numeric.")
        
        else:
           print("❌ Error: Invalid option has been choosen.") 

    else:
        print(f"❌ Error: There are no item with the ID `{item_id}` existing in the database.")

def main_menu_assign_item():
    item_id = input("Enter Item ID to assign: ")
    user_id = input("Enter User ID to assign to: ")

    if not item_id in items_db and not user_id in users_db:
        print(f"❌ Error: There are no item with the ID `{item_id}` or/and user with the ID `{user_id}` existing in the database.")
    else:
        if items_db[item_id]["status"] == "Assigned":
            print(f"❌ Error: The item `{items_db[item_id]["sub_category"]} {items_db[item_id]["manufacturer"]} {items_db[item_id]["model"]}` with the ID `{item_id}` is already assigned to another user.") 
        else:
            items_db[item_id]["status"] = "Assigned"
            items_db[item_id]["assigned_to"] = user_id
            users_db[user_id]["items"].append(item_id)
            print(f"✅ Success: The item `{items_db[item_id]["sub_category"]} {items_db[item_id]["manufacturer"]} {items_db[item_id]["model"]}` with the ID `{item_id}` was successfully assigned to the user {users_db[user_id]["name"]}.")

def main_menu_add_new_user():
    while True:
        user = str(input("Enter the Full Name: "))
        global user_id_counter
        user_id = str(user_id_counter)  # Convert to string in order to store all the user ID's in the same format
        users_db[user_id] = {"name": user, "items": []}
        print(f"✅ Success: The User `{user}` with the ID `{user_id}` was successfully added to the database.")
        user_id_counter += 1
        add_additional_one = input("Do you want to add additional user? (y/n): ")
        if add_additional_one == "y":
            True
        else:
            break

def main_menu_show_all_users():
    if not users_db:
        print("❌ Error: There are no users existing in the database.")
    else:
        print("Users List:\n")
        for id, name, in users_db.items():
            print(f"ID: {id}, Full Name: {name["name"]}")

def main_menu_show_all_items_by_the_user():
    prompt_user_id = input("Enter the User ID: ")
    if prompt_user_id in users_db:
        user_id = users_db[prompt_user_id]
        items = user_id["items"]

        if not items:
            print(f"ℹ️  Info: The User `{user_id["name"]}` has no assigned items.")
        else:
            print(f"\nID: {prompt_user_id}, Full Name: {user_id["name"]}")
            print("Items List:")
            print("-" * 50)
            for item_id in items:
                item = items_db.get(item_id)
                if item:
                    print(f"Item ID         : {item["id"]}")
                    print(f"Item            : {item["sub_category"]}")
                    print(f"Category        : {item["main_category"]}")
                    print(f"Manufacturer    : {item["manufacturer"]}")
                    print(f"Model           : {item["model"]}")
                    print(f"Price per Unit  : {item["price"]} ₪")
                    print(f"Quantity        : {item["quantity"]}")
                    print(f"Status          : {item["status"]}")
                    print("-" * 50)
    else:
        print(f"❌ Error: There are no user with the ID `{prompt_user_id}` existing in the database.")

def main_menu_show_all_stock_items():
    if not items_db:
        print("❌ Error: There are no items existing in the database.")

    print("\nAll Stock Items List:")
    print("-" * 50)

    for item in items_db.values():
        print(f"Item ID         : {item["id"]}")
        print(f"Item            : {item["sub_category"]}")
        print(f"Category        : {item["main_category"]}")
        print(f"Manufacturer    : {item["manufacturer"]}")
        print(f"Model           : {item["model"]}")
        print(f"Price per Unit  : {item["price"]} ₪")
        print(f"Quantity        : {item["quantity"]}")
        print(f"Status          : {item["status"]}")
        print("-" * 50)   

def main_menu_calculate_stock_by_categories():
    print("")
    print("-" * 50)
    stock = {"Assets": 0, "Accessories": 0, "Licenses": 0}
    for item in items_db.values():
        main_category = item["main_category"]
        stock[main_category] += item["price"] * item["quantity"]
    for category, sum in stock.items():
        print(f"Category: {category}, Total Value: {sum}₪")
        print("-" * 50)