from oauth2client import client
from client.controller.autenticate_messages import Authentication
from user import User
import getpass

welcome = "                __                             __                                             __                        _ __\n\
 _      _____  / _________  ____ ___  ___     / /_____     ____  __  ______________  ______  / /_____  ____ ___  ____ _(_/ /\n\
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __/ __ \   / __ \/ / / / ___/ ___/ / / / __ \/ __/ __ \/ __ `__ \/ __ `/ / / \n\
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ /  / /_/ / /_/ / /__/ /  / /_/ / /_/ / /_/ /_/ / / / / / / /_/ / / /  \n\
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/   \__/\____/  / .___/\__, /\___/_/   \__, / .___/\__/\____/_/ /_/ /_/\__,_/_/_/   \n\
                                                       /_/    /____/          /____/_/                                      "


class Application:
    def __init__(self):
        self.start_connection()
        self.print_welcome_msg()
        self.print_menu_login()

    def start_connection(self):
        '''
        Establish connection with server
        :return:None
        '''
        pass

    def print_menu_login(self):
        '''
        Print Menu containing login form
        :return: None
        '''
        print('EnTEr wlTh Y0uR Credencials:\n')
        email = input('Email:')
        password = getpass.getpass('Password: ')
        self.__user = User(email=email, password=password)


    def print_get_token(self):
        '''
        Print messsage to token required:
        :return: None
        '''

    def print_emails(self):
        '''
        Print emails requested from server
        :return: None
        '''
        pass

    def send_email(self):
        '''
        Send emails
        :return: None
        '''
        pass

    def print_welcome_msg(self):
        '''
        Print
        :return:
        '''
        print(welcome)
        print("######### Send email with security ##########")

    def getUser(self):
        return self.__user

if __name__ == "__main__":
    Application()
