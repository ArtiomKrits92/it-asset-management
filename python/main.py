### This is a Main file which will contain Welcome Screen and Main Menu features. 
import functions # Importing functions module from functions.py file
functions.welcome_screen() # Welcome Screen (will be displayed once and not included to the menu loop)
# functions.login_screen()    # Adding Login Screen feature using admin username and password credentials (Temporarily Disabled)

while True: # Start of Loop Menu
    functions.menu_handler()
    user_choise = input("\nPlease choose menu option (q for exit): ")

    match user_choise:  # Start of Menu Options, based on match cases
        case "1":
            functions.m1()

        case "2":
            functions.m2()

        case "3":
            functions.m3()

        case "4":
            functions.m4()

        case "5":
            functions.m5()

        case "6":
            functions.m6()

        case "7":
            functions.m7()

        case "8":
            functions.m8()

        case "9":
            functions.m9()

        case "0":
            functions.m0()
        
        case "q":   # Exit
            print("Thank you for using our service. See you later!\n")   # Print goodbye message to the user before quit the loop
            break   # Breaking the loop

        case _:
            print("❌ Error: Incorrect menu option has been choosen. Please try again.") # In case the user's chosen option does not exist
    # End of Menu Options, based on match cases

#    input("Press Enter key in order to return to the Main Menu.") # Prompt the input message as a part of the loop for returning to the Main Menu (Temporarily Disabled)
# End of Loop Menu
