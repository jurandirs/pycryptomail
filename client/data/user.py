class User:
    def __init__(self):
        self.user_token = None
        self.user_name = None
        self.user_email = None
        self.connection = None
        self.known_users = {}

    def set_token(self, token):
        self.user_token = token

    def set_user_name(self, user):
        self.user_name = user

    def set_connection(self, connection):
        self.connection = connection
