from user import User


class ServerSimulator:
	def __init__(self):
		pass

	def get_public_key(self, email):
		if email == 'dheisosnowden@inf.ufg.br':
			U = User(email = 'dheisosnowden@inf.ufg.br', password='snowden123')
			return U.get_public_key()
		elif email == 'marcosbond@inf.ufg.br':
			U = User(email = 'marcosbond@inf.ufg.br', password='bond123')
			return U.get_public_key()