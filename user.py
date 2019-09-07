class User:
    """
    Class that generates new instances of a user
    """

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    user_list = []    #empty user list

    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        self.user_list.append(self)

        # check user
    @classmethod
	def check_user(cls,user_name,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.user_name == user_name and user.password == password):
				current_user = user.user_name
		return current_user

if __name__ == '__main__':
    main()