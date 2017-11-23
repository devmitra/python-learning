# File Name learn_network_server.py
# Demo of python based network server
# link : https://www.tutorialspoint.com/python3/python_networking.htm
#!usr/bin/python3

from utility import *
printDes("Networking-Server", """ A simple python server""")

import socket

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999


# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)
print("Server is ready with host: ", host, ", Port: ", port)

while True:
   # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))

    msg = 'Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    while True:
        text = clientsocket.recv(1024)
        print('Receive text from client : ' , text.decode('ascii'))
        break

    clientsocket.close()
    print("Closing client connection")
