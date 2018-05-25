from client.data.email_builder import EmailBuilder
from client.data.message import Message


class EmailController:
    def __init__(self, user, connection):
        self.user = user
        self.connection = connection

    def encrypt_email(self, email, e_from):
        """
        Encrypt email with key of receiver
        :param email: message
        :param e_from: email of receiver
        :return: Message encrypted
        """
        email_encrypted = None

        if e_from in self.user.known_users:
            self.request_user_key(e_from)
        else:
            pass

        return email_encrypted

    def request_user_key(self, e_from):
        msg_builder = Message()
        msg = msg_builder.msg_get_client_key(e_from, self.user.user_token)

    def set_email(self, e_from, cc, subject, message, priority = 1):
        email = EmailBuilder()
        email = email.set_from_email(e_from).set_cc_emails(cc).set_subject(subject).set_msg(message).\
            set_priority(priority).build()

        email_encrypted = self.encrypt_email(email, e_from)
        message = self.build_message(email_encrypted)
        self.send_message(message)

    def build_message(self, email_encrypted):
        msg_builder = Message()
        msg = msg_builder.msg_email(email_encrypted, self.user.user_token)
        return msg

    def send_message(self, message):
        self.connection.send_message(message)
