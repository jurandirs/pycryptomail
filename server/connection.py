import hashlib
import socket
from Crypto.PublicKey import RSA
from Crypto.Util.randpool import RandomPool

list_of_users = {'jura': 'bla'}
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


class Connection:
    def __init__(self):
        self.encryption = Encrypt()
        self.encryption.generate_key()

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
