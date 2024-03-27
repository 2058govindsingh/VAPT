import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.1.104'
host = socket.gethostname()

port = 4000
clientsocket.connect((host, port))
while True:
    serversocket, address = clientsocket.accept()
    serversocket.send("hello server")
    message = clientsocket.recv(1024)
    clientsocket.close()
    print(message.decode('ascii'))