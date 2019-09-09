#!/usr/bin/python
import random
from user import User
from credentials import Credentials

def create_new_credential(account_name, site_name, account_password):
    """
    Function to create a new account and its credentials
    """
    new_credential = Credentials(account_name, site_name, account_password)
    return new_credential


def save_new_credential(credentials):
    """
    Function to save the newly created account and password
    """
    credentials.save_credentials()


def find_credential(account_name):
    """
    Function that finds credentials based on account_name given
    """
    return Credentials.find_by_name(account_name)


def check_existing_credentials(name):
    """
    Method that checks whether a particular account and its credentials exist based on searched account_name
    """
    return Credentials.find_by_name(name)


def display_credentials():
    """
    Function which displays all saved credentials
    """
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    Method that deletes credentials
    """
    return Credentials.delete_credential(credentials)


def main():
    print("Hello Welcome to Password locker, What is your name?")
        user_name = input()

        print(f"Hello {user_name}, what would you like to do?")
        print('\n')
        while True:
            print("Use these short codes to select an option: Create New account use 'ca': Login to your account use 'li' or 'ex' to exit password locker")
            short_code = input().lower()
            print('\n')
            if short_code == 'ca':
                print("Enter your UserName")
                created_user_name = input()

                print("Enter user Password")
                created_user_password = input()

                print("Confirm Your Password")
                confirm_password = input()

                while confirm_password != created_user_password:
                    print("Sorry your passwords dont't match!")
                    print("Enter user password")
                    created_user_password = input()
                    print("Confirm Your Password")
                    confirm_password = input()

                else:
                    print(f"Congratulations {created_user_name}! You have created a new account.")
                    print('\n')
                    print("Proceed to Log In to your Account")
                    print("Username")
                    entered_userName = input()
                    print("Your Password")
                    entered_password = input()

                    while entered_userName != created_user_name or entered_password != created_user_password:
                        print("You entered a wrong username or password")
                        print("Username")
                        entered_userName = input()
                        print("Your Password")
                        entered_password = input() 

                    else:
                    print(f"Welcome: {entered_userName} to your Account")
                    print('\n')

                    print("Select an option below to continue: Enter a, b, c, d or e")
                    print('\n')

                while True:
                    print("a: View Your saved credentials")
                    print("b: Add new credentials")
                    print("c: Remove credentials")
                    print("d: Search credentials")
                    print("e: Log Out")
                    option = input() 

                    if option == 'b':
                        while True:
                            print("Enter The Account Name")
                            account_name = input()
                            print("Enter The site Name")
                            site_name = input()
                            print("Enter a password")
                            print("To generate a random password, enter keyword 'gp' or 'cp' to create your own password")
                            keyword = input().lower()

                            if keyword == 'gp':
                                account_password = random.randint(111111, 1111111, 1111111)
                                print(f"Account: {account_name}")
                                print(f"Account: {site_name}")
                                print(f"Password: {account_password}")
                                print('\n')

                            elif keyword == 'cp':
                                print("Create your password")
                                account_password = input()
                                print(f"Account: {account_name}")
                                print(f"Account: {site_name}")
                                print(f"Password: {account_password}")
                                print('\n')  

                            else:
                                print("Please enter a valid Code")

                            save_new_credential(create_new_credential(account_name, site_name, account_password))

                        else choice == 'cp':
                            break

                elif option == 'a':
                    while True:
                        print("Below is a list of all your credentials")
                        if display_credentials():

                            for credential in display_credentials():
                                print(f"ACCOUNT NAME:{credential.account_name}")
                                print(f"SITE NAME:{credential.site_name}")
                                print(f"PASSWORD:{credential.account_password}")

                        else:
                            print('\n')
                            print("You don't seem to have any credentials yet") 
                            print('\n')   
                            break

                      
                elif option == 'e':
                    print("WARNING! You will loose all your credentials if you log out. Are you sure? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print("You have Successfully logged out")
                        break
                    elif logout == 'n':
                        continue

                elif option == 'c':
                    while True:
                        print("Search for credential to delete")

                        search_name = input()

                        if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password} \n SITE NAME: {search_credential.site_name}")
                            print("Delete? y/n")
                            sure = input().lower()
                            if sure == 'y':
                                delete_credential(search_credential)
                                print("Account SUCCESSFULLY deleted")
                                break
                            elif sure == 'n':
                                continue

                        else:
                            print("That credential does not exist")
                            break

                elif option == 'd':
                    while True:
                        print("Enter an account name to find credentials")
                        search_name = input()
                        if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password} \n SITE NAME: {search_credential.site_name}")
                        else:
                                print("That credential does not exist")
                       

                else:
                    print("Please enter a valid code")
                    continue

            elif short_code == 'li':
                print("WELCOME")
                print("Enter UserName")
                default_user_name = input()

                print("Enter Your password")
                default_user_password = input()
                print('\n')


                while default_user_name != 'NewUser' or default_user_password != '12345678':
                print("Wrong userName or password. Username 'NewUser' and password '12345678'")
                print("Enter UserName")
                default_user_name = input()

                print("Enter Your password")
                default_user_password = input()

                print('\n')

            if default_user_name == 'NewUser' and default_user_password == '12345678':
                print("YOU HAVE SUCCESSFULLY LOGGED IN!")
                print('\n')
                print("Select an option below to continue: Enter a, b, c, d or e")
                print('\n')

                ##############################################
            while True:
                print("a: View Your saved credentials")
                print("b: Add new credentials")
                print("c: Remove credentials")
                print("d: Search credentials")
                print("e: Log Out")
                option = input()

                if option == 'b':
                    while True:
                        # print("Continue to add? y/n")

                        # choice = input().lower()
                        # if choice == 'y':
                            print("Enter The Account Name")
                            account_name = input()
                            print("Enter The site Name")
                            site_name = input()
                            print("Enter a password")
                            print("To generate random password enter keyword 'gp' or 'cp' to create your own password")
                            keyword = input().lower()
                            if keyword == 'gp':
                                account_password = random.randint(111111, 1111111, 1111111)
                                print(f"Account: {account_name}")
                                print(f"SITE: {site_name}")
                                print(f"Password: {account_password}")
                                print('\n')

                            elif keyword == 'cp':
                                print("Create your password")
                                account_password = input()
                                print(f"Account: {account_name}")
                                print(f"Site: {site_name}")
                                print(f"Password: {account_password}")
                                print('\n')

                            else:
                                print("Please enter a valid Code")

                            save_new_credential(create_new_credential(
                                account_name, site_name, account_password))
                        elif choice == 'cp':
                            break
                        # else:
                            # print("Please use 'y' for yes or 'n' for no!")
                elif option == 'a':
                    while True:
                        print("Below is a list of all your credentials")
                        if display_credentials():

                            for credential in display_credentials():
                                print(f"ACCOUNT NAME:{credential.account_name}")
                                print(f"SITE NAME:{credential.site_name}")
                                print(f"PASSWORD:{credential.account_password}")

                        else:
                            print('\n')
                            print("You don't seem to have any credentials yet")
                            print('\n')

                        # print("Back to Menu? y/n")

                        # back = input().lower()
                        # if back == 'y':
                            # break
                        elif back == 'cp':
                            continue
                        # else:
                            # print("Please Enter a valid code")
                        # elif choice1 == 'n':
                        #     break
                        # else:
                        #     print("Please use y or n")
                elif option == 'e':
                    print("WARNING! You will loose all your credentials if you log out. Are you sure? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print("You have Successfully logged out")
                        break
                    elif logout == 'n':
                        continue

                elif option == 'c':
                    while True:
                        print("Search for credential to delete")

                        search_name = input()

                        if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password} \n SITE NAME: {search_credential.site_name}")
                            print("Delete? y/n")
                            sure = input().lower()
                            if sure == 'y':
                                delete_credential(search_credential)
                                print("Account successfully deleted")
                                break
                            elif sure == 'n':
                                continue

                        else:
                            print("That credential Does not exist")
                            break

                elif option == 'd':
                    while True:
                        # print("Continue? y/n")
                        # option2 = input().lower()
                        # if option2 == 'y':
                            print("Enter an account name to find credentials")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password} \n SITE NAME: {search_credential.site_name}")
                            else:
                                print("That credential Does not exist")
                        # elif option2 == 'n':
                            # break
                        # else:
                            # print("Please enter a valid code")
                else:
                    print("Please enter a valid code")
        elif short_code == 'ex':
            break
        else:
            print("Please Enter a valid code to continue")        



if __name__ == '__main__':
    main()