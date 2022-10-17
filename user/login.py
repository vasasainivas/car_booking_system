

class Login:
    def __init__(self, login_user_name, login_password):
        self.login_user_name = login_user_name
        self.login_password = login_password


class LoginValidate:
    @staticmethod
    def validate_account(register_object, login_object):
        login_status = register_object.user_name == login_object.login_user_name and register_object.password\
                       == login_object.login_password
        return login_status
