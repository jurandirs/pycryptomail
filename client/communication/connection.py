from client.controller.encrypt import Encrypt
import socket


class Connection:
    def __init__(self):
        self.host = 'localhost'
        self.port = 6655
        self.section_encryption = Encrypt()
        self.section_encryption.generate_key()

    def send_message(self, message):
        destination = (self.host, self.port)
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect(destination)
        connection.send(message)
        connection.listen(1)
        connection.close()

    def receive_message(self, message):
        pass

    def send_key(self):
        public_key = self.section_encryption.get_serialized_public_key()
        self.send_message(public_key)


if __name__ == "__main__":
    # con = Connection
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_socket.connect(('localhost', 6565))

    print cli_socket.recv(255)

    cli_socket.close()
