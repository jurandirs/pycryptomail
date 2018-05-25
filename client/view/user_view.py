from client.communication.connection import Connection
from client.controller.autenticate import Authentication
from client.controller.email_controller import EmailController
import getpass

welcome = "                __                             __                                             __                        _ __\n\
 _      _____  / _________  ____ ___  ___     / /_____     ____  __  ______________  ______  / /_____  ____ ___  ____ _(_/ /\n\
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __/ __ \   / __ \/ / / / ___/ ___/ / / / __ \/ __/ __ \/ __ `__ \/ __ `/ / / \n\
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ /  / /_/ / /_/ / /__/ /  / /_/ / /_/ / /_/ /_/ / / / / / / /_/ / / /  \n\
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/   \__/\____/  / .___/\__, /\___/_/   \__, / .___/\__/\____/_/ /_/ /_/\__,_/_/_/   \n\
                                                       /_/    /____/          /____/_/                                      "


class Application:
    def __init__(self):
        self.user = None
        self.connection = self.start_connection

        self.print_login()

    @property
    def start_connection(self):
        connection = Connection()
        return connection

    def print_login(self):
        print(welcome)
        print("######### Send email with security ##########")

        auth = Authentication()
        print('EnTEr wlTh Y0uR Credencials:\n')
        email = input('Email:')
        password = getpass.getpass('Password: ')
        auth.request_authentication(email, password)

    def print_emails(self, list_of_emails):
        for email in list_of_emails:
            pass

    def print_write_email(self):
        email_from = input('From: ')
        email_cc = input('CC: -- None for nothing')
        email_subject = input('Subject: ')
        email_msg = input('Message: ')
        ec = EmailController(self.user, self.connection)
        ec.set_email(email_from, email_cc, email_subject, email_msg)


if __name__ == "__main__":
    Application()
