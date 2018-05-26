import hashlib
import socket
import pickle
from Crypto.PublicKey import RSA
from Crypto.Util.randpool import RandomPool

Host = 'localhost'
port = 6655


class Encrypt:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.outside_public_key = None

    def generate_key(self):
        pool = RandomPool(384)
        pool.stir()
        randfunc = pool.get_bytes
        key_size = 1024
        self.private_key = RSA.generate(key_size, randfunc)
        self.public_key = self.private_key.publickey()

    def get_serialized_public_key(self):
        return self.private_key.publickey().exportKey(format='PEM', passphrase=None, pkcs=1)

    def set_outside_public_key(self, server_public_key):
        """
        Receive a serialized public key, generate object and store
        :param server_public_key: serizalized public key received from server
        :return: None
        """
        self.outside_public_key = RSA.importKey(server_public_key, passphrase=None)

    def hash_md5(self, message):
        return hashlib.sha256(message.encode('utf-8'))

    def check_msg_received(self, message):
        pass

    def encrypt_msg(self, message):
        encrypted_msg = self.outside_public_key.encrypt(message, '')
        return encrypted_msg

    def decrypt_msg(self, message):
        msg_decrypted = self.private_key.decrypt(message)
        return msg_decrypted

    def generate_token_for_client(self, email_client):
        pass

    def verify_user_token(self, token_received):
        pass


class Message:
    def __init__(self):
        pass

    def msg_send_key(self, key, token):
        msg                 = {}
        msg['header']       = "get_client_key"
        body                = {}
        body['key']         = key
        body['token']       = token
        msg['body']         = body

        return self.serialize(msg)

    def serialize(self, message):
        return pickle.dumps(message)

    def deserialize(self, message_serialized):
        return pickle.loads(message_serialized)

class Connection:
    def __init__(self):
        self.encryption = Encrypt()
        self.encryption.generate_key()

        self.list_of_users = []

    def send_key(self):
        pass

    def set_session_key_received(self, key):
        self.encryption.set_outside_public_key(key)

    def set_new_user(self, user_name, user_email, password, key):
        user = {}
        user['user_name'] = user_name
        user['email'] = user_email
        user['password'] = password
        user['key'] = key
        self.list_of_users.append(user)

    def run(self):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.bind(('0.0.0.0', 6565))
        server_sock.listen(100)
        while True:
            (cli_socket, address) = server_sock.accept()
            if cli_socket.send('ok' + '\n') == 0:
                print "Client connection is broken"

                cli_socket.close()



if __name__ == "__main__":
    con = Connection()
    con.run()
