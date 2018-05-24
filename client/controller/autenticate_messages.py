class Authentication:
    def __init__(self):
        self.user_token = None
        self.user_name = None

    def request_authentication(self, email, password):
        pass

    def set_token(self, token):
        self.user_token = token

    def get_token(self):
        return self.user_token

    def connect(self):
        pass