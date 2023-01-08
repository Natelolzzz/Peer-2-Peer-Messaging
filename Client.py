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

server = Server('127.0.0.1', 12345)
server_thread = threading.Thread(target=server.receive)
server_thread.start()

nickname = input('Choose a nickname: ')
client = Client('127.0.0.1', 12345, nickname)
client_thread = threading.Thread(target=client.receive)
client_thread.start()

while True:
    message = input(>)
    client.send(message.encode('utf-8'))
