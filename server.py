#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "49.38.251.110"
port = 4001
print(host)

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()

    print("recieved connection from %s " % str(address))
    message = "hello from the server\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
