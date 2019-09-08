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

    def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('App_User','12345678')
		self.new_user.save_user()
		user2 = User('Nana','12345678')
		user2.save_user()

		for user in User.users_list:
			if user.user_name == user2.user_name and user.password == user2.password:
				current_user = user.user_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

if __name__ == '__main__':
    unittest.main()
    