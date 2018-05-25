from client.view.user_view import Application
from client.communication.server_simulator import ServerSimulator
from client.controller.email_builder import MessageBuilder
options = {
	'1': 'send_message',
}

def show_menu():
	print('\n# Terminal #')
	while True:
		print('1 - Send Message')
		print('X - Exit')
		print('> ', end='')
		try:
			opc = input()
			if opc not in ['1',] and opc != 'X':
				print('Incorrect entry. Try again.')
			else:
				break
		except Exception:
			pass
	if opc == 'X':
		exit(0)
	return options[opc]


if __name__=='__main__':
	App = Application()
	user = App.getUser()
	server = ServerSimulator()

	while True:
		opc = show_menu()
		if opc == 'send_message':
			message = MessageBuilder()
			message.set_from_email(user.get_email())
			message.set_from_email(input('To: '))
			message.set_subject(input('Subject: '))
			message.set_msg(input('Message: '))
			message = message.build()



