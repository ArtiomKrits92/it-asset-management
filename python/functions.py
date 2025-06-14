### This is a Functions file which will contain functions for reusable logic of the Main file.
import getpass  # Importing Getpass module for password input data masking
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

def menu_handler(): # Menu Handler function
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

def m1():   # Add New Items
    print("Menu Option 1 has been choosen.\n")

def m2():   # Delete Item
    print("Menu Option 2 has been choosen.\n")

def m3():   # Modify Item
    print("Menu Option 3 has been choosen.\n")

def m4():   # Assign User
    print("Menu Option 4 has been choosen.\n")

def m5():   # Add New User
    print("Menu Option 5 has been choosen.\n")

def m6():   # Show All Users
    print("Menu Option 6 has been choosen.\n")

def m7():   # Show All Items by the User
    print("Menu Option 7 has been choosen.\n")

def m8():   # Sort Items by Name (A-Z)
    print("Menu Option 8 has been choosen.\n")

def m9():   # Sort Items by Price (₪ - ₪₪₪)
    print("Menu Option 9 has been choosen.\n")

def m0():   # Calculate Stock by Categories
    print("Menu Option 0 has been choosen.\n")

