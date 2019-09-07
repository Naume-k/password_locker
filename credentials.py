class Credentials:
    """
    Class that generates new instances of the credentials
    """
    def __init__(self, account_name,account_user_name, account_password):
        self.account_name = account_name
        self.account_user_name = account_user_name
        self.account_password = account_password

    credentials_list = []
    user_credentials_list = []

    # saving credentials
    def save_credentials(self):
        """
        Method that saves credential objects into credentials_list
        """
        self.credentials_list.append(self)

        # generating password
    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass

    # deleting
    def delete_credentials(self):
        """
        Method which deletes a particular credential
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls,account_name):
        '''
        Method that takes in a name and returns a user that matches that name.

        Args:
            name: name to search for
        Returns :
            user that matches the name.
        '''   

        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials

    @classmethod
    def credentials_exists(cls, account_name):
        """
        Method to check whether a credential exists
        Args:
        account_name: account_name of account to search whether it exists
        boolean: True or False depending if the user exists
        """

        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return True
        return False

    @classmethod
    def display_credentials(cls, account_name):
        """
        Method which displays all current credentials
        """
        user_credentials_list = []
		for credentials in cls.credentials_list:
			if credential.account_name == account_name:
				user_credentials_list.append(credentials)
		return user_credentials_list

if __name__ == '__main__':
    main()

