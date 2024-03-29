import socket
import threading

class Client:
    def __init__(self, host, port, nickname):
        self.sock = socket.socket()
        self.sock.connect((host, port))
        self.sock.send(nickname.encode('utf-8'))
        print(self.sock.recv(1024).decode('utf-8'))
        self.sock.send(b'Connected')

    def send(self, message):
        self.sock.send(message)

    def receive(self):
        while True:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if message:
                    print(message)
            except:
                continue

nickname = input('Choose a nickname > ')
SA = input('Server adress > ')
client = Client('127.0.0.1', int(SA), nickname)
client_thread = threading.Thread(target=client.receive)
client_thread.start()

while True:
    message = input('> ')
    client.send(message.encode('utf-8'))
