import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the Credentials class behavior
    """

    def setUp(self):
        """
        Set up method to run befor before each test case
        """
        self.new_credentials = Credentials("Istagram","instauser", "12345678")

    def test_init(self):
        """
        Method that tests whether the new_credentials have been instantiated correctly
        """
        self.assertEqual(self.new_credentials.account_name, "Istagram")
        self.assertEqual(self.new_credentials.account_user_name, "instauser")
        self.assertEqual(self.new_credentials.account_password, "12345678")

    def test_save_credentials(self):
        """
        Method that tests whether the new credential created has been saved
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credential
        objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","user","#0782386439?") # new contact
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []
                
    def test_find_credentials_by_name(self):
        '''
        test to check if we can find credentials by name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","user","#0782386439?") # new contact
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_name("Test")

        self.assertEqual(found_credentials.account_name,test_credentials.account_name)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()        