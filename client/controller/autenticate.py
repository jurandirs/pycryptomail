from client.data.message import Message

class Authentication:
    def __init__(self):
        self.user_token = None
        self.user_name = None

    def request_authentication(self, email, password):
        msg = Message.msg_autentication(email, password)

    def connect(self):
        pass
