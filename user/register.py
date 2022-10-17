
class Register:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def print_status(self):
        registration_status = "You are Successfully registered with Username " + str(self.user_name)\
                              + " and Password " + str(self.password)
        return registration_status
