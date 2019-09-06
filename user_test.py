import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.
    """
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("App_User", "12345678")

    def test_init(self):
        """
        Testing to ensure that the object is initialized properly
        """
        self.assertEqual(self.new_user.user_name, "App_User")
        self.assertEqual(self.new_user.password, "12345678")

    def test_save_user(self):
        """
        Method that tests whether user credentials have been successfully saved
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

if __name__ == '__main__':
    unittest.main()
    