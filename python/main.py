### This is a Main file which will contain Welcome Screen and Main Menu features. 
import functions # Importing functions module from functions.py file
functions.welcome_screen() # Welcome Screen (will be displayed once and not included to the menu loop)
functions.login_screen()    # Adding Login Screen feature using admin username and password credentials

while True: # Start of Loop Menu
    functions.menu_handler()
    user_choise = input("\nPlease choose menu option (q for exit):\n")

    match user_choise:  # Start of Menu Options, based on match cases
        case "1":
            pass

        case "2":
            pass

        case "3":
            pass

        case "4":
            pass

        case "5":
            pass

        case "6":
            pass

        case "7":
            pass

        case "8":
            pass

        case "9":
            pass

        case "0":
            pass
        
        case "q":   # Exit
            print("Thank you for using our service. See you later!\n")   # Print goodbye message to the user before quit the loop
            break   # Breaking the loop

        case _:
            print("❌ Error: Incorrect menu option has been choosen. Please try again.") # In case the user's chosen option does not exist
    # End of Menu Options, based on match cases
    input("Press Enter key in order to return to the Main Menu.") # Prompt the input message as a part of the loop for returning to the Main Menu
# End of Loop Menu
