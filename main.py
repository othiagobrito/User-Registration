from userActions import *
from getpass import getpass

def action(option):
    if option == 1:
        user = input("User: ")
        password = getpass("Password: ")

        Login(user, password)

    elif option == 2:
        user = input("Choose a user name (must have at least 3 characters): ")
        password = getpass("Choose a Password (must have from 8 to 15 characters): ")

        Register(user, password)
    
    else:
        print("ERROR: Invalid option!")


option = int(input("What do you wish to do, Login (1) or Register(2)?\n> "))
action(option)
