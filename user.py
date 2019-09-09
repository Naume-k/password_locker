class User:
    """
    Class that generates new instances of a user
    """

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
    user_list = []

    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        self.user_list.append(self)


if __name__ == '__main__':
    main()