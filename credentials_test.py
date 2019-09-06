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

    def test_credentials_instance(self):
        """
        Method that tests whether the new_credentials have been instantiated correctly
        """
        self.assertEqual(self.new_credentials.account_name, "Istagram")
        self.assertEqual(self.new_credentials.account_user_name, "instauser")
        self.assertEqual(self.new_credentials.account_password, "12345678")