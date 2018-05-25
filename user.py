#! -*- coding:utf-8 -*-
from Crypto.PublicKey import RSA

class User:
	def __init__(self, email, password):
		self.__email = email
		self.__password = password
		self.__generate_user_keys()

	def __generate_user_keys(self):
		new_key = RSA.generate(1024)
		exportedKey = new_key.exportKey('DER', self.__password, pkcs=1)
		key = RSA.importKey(exportedKey)
		self.public_key = key.publickey() # será armazenada apenas a chave publica
		del key # forçar exclusão

	def get_private_key(self):
		new_key = RSA.generate(1024)
		exportedKey = new_key.exportKey('DER', self.__password, pkcs=1)
		key = RSA.importKey(exportedKey)
		keyexportkey = key.exportKey()
		del key # forçar exclusão
		return keyexportkey # Binary String

	def get_public_key(self):
		new_key = RSA.generate(1024)
		exportedKey = new_key.exportKey('DER', self.__password, pkcs=1)
		key = RSA.importKey(exportedKey)
		keyexportkey = key.publickey().exportKey()
		del key  # forçar exclusão
		return keyexportkey # Binary String

	def get_email(self):
		return self.__email