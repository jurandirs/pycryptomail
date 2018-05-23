import hashlib
from Crypto.PublicKey import RSA
from Crypto.Util.randpool import RandomPool


class EncryptEmail:

    def __init__(self):
        self.key, self.public_key = self.generate_key()
        self.server_public_key = None

    def generate_key(self):
        '''
        Generate public and private key
        '''
        pool = RandomPool(384)
        pool.stir()
        randfunc = pool.get_bytes
        key_size = 1024
        key = RSA.generate(key_size, randfunc)
        public_key = key.publickey()
        return key, public_key

    def get_public_key(self):
        '''
        Return public key
        '''
        return self.key.publickey().exportKey(format='PEM', passphrase=None, pkcs=1)

    def set_server_public_key(self, server_public_key):
        '''
        Store public key received from server
        :param server_public_key: key
        '''
        self.server_public_key = RSA.importKey(server_public_key, passphrase=None)

    def hash_md5(self, message):
        '''
        Apply hash in msg
        :param message: mesage to hash
        '''
        return hashlib.sha256(message.encode('utf-8'))

    def check_msg_received(self, ):
        '''
        Use hash to checking msg received integrity
        :return:
        '''
        pass

    def encrypt_msg(self, message):
        '''
        Encrypt messages using key of server
        :param message: Message to cryptography
        :return: Message encrypted
        '''

        encrypted_msg = self.server_public_key.encrypt(message, "")

        return encrypted_msg

    def decrypt_msg(self, message):
        '''
        Encrypt messages using RSA
        :param message: Message to cryptography
        :return: Message encrypted
        '''
        msg_decrypted = self.key.decrypt(message)

        return msg_decrypted


# Testes:

if __name__ == '__main__':
    e = EncryptEmail()

    # ----------Client -----------------
    key_pv_client, key_pub_client = e.generate_key()
    client_key = key_pv_client.publickey().exportKey(format='PEM', passphrase=None, pkcs=1)

    # ----------Server -----------------
    key_pv_server, key_pub_server = e.generate_key()
    server_key = key_pv_server.publickey().exportKey(format='PEM', passphrase=None, pkcs=1)


    key_rcv_server = RSA.importKey(server_key, passphrase=None)

    key_rcv_client = RSA.importKey(client_key, passphrase=None)

    # Server encrypt msg with key of client
    msg = key_rcv_client.encrypt("Hello", '')

    # Client decrypt msg with private key
    msg = key_pv_client.decrypt(msg)
    print(msg)
