class Credentials:
    """
    Class that generates new instances of the credentials
    """
    def __init__(self, account_name,account_user_name, account_password):
        self.account_name = account_name
        self.account_user_name = account_user_name
        self.account_password = account_password

    credentials_list = []

    def save_credentials(self):
        """
        Method that saves credential objects into credentials_list
        """
        self.credentials_list.append(self)
