class Credentials:
    """
    Class that generates new instances of the credentials
    """
    def __init__(self, account_name,account_user_name, account_password):
        self.account_name = account_name
        self.account_user_name = account_user_name
        self.account_password = account_password

    credentials_list = []

    # saving credentials
    def save_credentials(self):
        """
        Method that saves credential objects into credentials_list
        """
        self.credentials_list.append(self)

    # deleting
    def delete_credential(self):
        """
        Method which deletes a particular credential
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a user that matches that name.

        Args:
            name: name to search for
        Returns :
            user that matches the name.
        '''   

        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exists(cls, name):
        """
        Method to check whether a credential exists
        Args:
        name: name of account to search whether it exists
        boolean: True or False depending if the user exists
        """

        for credential in cls.credentials_list:
            if credential.account_name == name:
                return True
        return False

    # @classmethod
    # def display_credentials(cls):
    #     """Method which displays all current credentials"""
    #     return cls.credentials_list



