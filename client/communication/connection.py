from conf.configuration import Configuration
from encrypt import EncryptEmail
import socket


class Connection:
    def __init__(self):
        self.host = Configuration.get("CONNECTION", 'ip')
        self.port = Configuration.get_int("CONNECTION", 'port')
        self.class_encript = EncryptEmail()

    def send_message(self, message):
        '''
        Connect with sever and
        :param message: Message not encripted
        :return: None
        '''
        print('Sending Secure Message to sever')
        message_encrypted = self.class_encript.cryptography_msg(message)
        destination = (self.host, self.port)
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect(destination)
        connection.send(message_encrypted)
        connection.listen(1)
        connection.close()

    def receive_message(self, message):
        pass

    def send_key(self):
        '''
        Share public key to sever
        :param key: Key of cryptography
        :return: None
        '''
        public_key = self.class_encript.get_public_key()
        self.send_message(public_key)

