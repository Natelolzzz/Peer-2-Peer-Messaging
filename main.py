import socket
import threading

class Server:
    def __init__(self, host, port):
        self.clients = []
        self.sock = socket.socket()
        self.sock.bind((host, port))
        self.sock.listen()

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024)
                if message:
                    self.broadcast(message)
                else:
                    remove(client)
            except:
                continue

    def receive(self):
        while True:
            client, address = self.sock.accept()
            client.send(b'Connected to the server')
            print(f'Connected to {address}')
            client.send(b'NICK')
            nickname = client.recv(1024).decode('utf-8')
            client.send(b'Connected')
            self.clients.append(client)
            client.send(b'Connected to the server')
            print(f'Nickname of client is {nickname}!')
            client.send(f'{nickname} joined the chat!'.encode('utf-8'))
            self.broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
            client.send(b'Type your message:')
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

    def remove(self, client):
        client.close()
        self.clients.remove(client)

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
    message = input()
    client.send(message.encode('utf-8'))
