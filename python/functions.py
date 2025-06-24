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
    print("8. Sort Items by Name (A-Z)")
    print("9. Sort Items by Price (₪ - ₪₪₪)")
    print("0. Calculate Stock by Categories\n")

def main_menu_add_new_items():
    pass

def main_menu_delete_item():
    pass

def main_menu_modify_item():
    pass

def main_menu_assign_item():
    pass

def main_menu_add_new_user():
    while True:
        user = str(input("Enter the Full Name: "))
        global user_id_counter
        user_id = str(user_id_counter)  # Convert to string in order to store all the user ID's in the same format
        users_db[user_id] = {"name": user, "items": []}
        print(f"✅ Success: The User `{user}` was successfully added to the system with the ID `{user_id}`.")
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

def main_menu_sort_items_by_name():
    pass

def main_menu_sort_items_by_price():
    pass

def main_menu_calculate_stock_by_categories():
    pass