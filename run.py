from user import User
from credentials import Credentials
import random

# creating credentials
def create_credentials(account_name, account_user_name, account_password):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(account_name, account_user_name, account_password)
    return new_credentials

 # Save credentials
def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials() 

# Finding a credentials
def find_credentials(account_name):
    '''
    Function that finds a credentials by account_name and returns the credentials
    '''
    return Credentials.find_by_name(account_name) 

# display all saved credentials
def display_credentials():
    """
    Function which displays all saved credentials
    """
    return Credentials.display_credentials() 

# delete credentials
def delete_credential(credentials):
    """
    Method that deletes credentials
    """
    return Credentials.delete_credentials(credentials)

