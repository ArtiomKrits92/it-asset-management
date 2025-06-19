### This is a Functions file which will contain functions for reusable logic of the Main file.
import getpass  # Importing Getpass module for password input data masking

db = {  # Database creation for the items, users, and items assignments
    "item": {}, # Keys:Values (item_id: item)
    "user": {}, # Keys:Values (user_id: user)
    "assignments": {}   # Keys:Values (item_id: user_id)
}
user_id_counter = 1 # Creation of User ID Counter value (will start from 1)

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

def main_menu_add_new_items():   # Add New Items
    print("Menu Option 1 has been choosen.\n")

def main_menu_delete_item():   # Delete Item
    print("Menu Option 2 has been choosen.\n")

def main_menu_modify_item():   # Modify Item
    print("Menu Option 3 has been choosen.\n")

def main_menu_assign_item():   # Assign User
    print("Menu Option 4 has been choosen.\n")

def main_menu_add_new_user():   # Add New User
    print("Menu Option 5 has been choosen.\n")
    user = input("Enter the Full Name: ")   # Prompt for user full name data entering
    global user_id_counter  # Call user_id_counter value
    user_id = user_id_counter   # Set the new user's ID the Counter ID current Value
    db["user"][user_id] = user  # Add the user based on the prompt name and automatically assigned ID using counter to the database
    user_id_counter += 1    # Update the counter by 1
    print (f"✅ Success: User {user} was successfully added to the system with the ID `{user_id}`") # Print the success message to the user

def main_menu_show_all_users():   # Show All Users
    print("Menu Option 6 has been choosen.\n")
    print("Users List:")
    for id, user in db["user"].items():
        print(f"ID: {id}, Full Name: {user}")

def main_menu_show_all_items_by_the_user():   # Show All Items by the User
    print("Menu Option 7 has been choosen.\n")

def main_menu_sort_items_by_name():   # Sort Items by Name (A-Z)
    print("Menu Option 8 has been choosen.\n")

def main_menu_sort_items_by_price():   # Sort Items by Price (₪ - ₪₪₪)
    print("Menu Option 9 has been choosen.\n")

def main_menu_calculate_stock_by_categories():   # Calculate Stock by Categories
    print("Menu Option 0 has been choosen.\n")

