#Requeriment: Crypto library

import hashlib

class EncryptEmail():
	def __init__(self):
		pass

	def generate_key(self):
		pass

	def encrypt_RSA(self):
		pass

	def encrypt_AES(self):
		pass

	def hash_md5(self, mensage):
		return hashlib.sha256(mensage.encode('utf-8'))

	def alg(self, mensage):
		pass