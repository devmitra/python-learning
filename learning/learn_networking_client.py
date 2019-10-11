# File Name learn_network_client.py
# Demo of python based network client
# link : https://www.tutorialspoint.com/python3/python_networking.htm
#!usr/bin/python3

from utility import *
printDes("Networking-Server", """ A simple python client""")

import socket
import sys

#print("ARGV: ", sys.argv)

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
msg = s.recv(1024)
print (msg.decode('ascii'))

# Getting messag from command prompt
#text = input("\n Enter a message: ")
#print("client will send message: ", text)
#msgSend = text + "\r\n"

# Getting input from argv
option = sys.argv[1]
if len(sys.argv) >= 2:
    if option == '-c':
        text = input("\n Enter a message: ")
        print("client will send message: ", text)
        msgSend = text + "\r\n"
        s.send(msgSend.encode('ascii'))
    elif option == '-a':
        if len(sys.argv) >= 3:
            msgSend = sys.argv[2] + "\r\n"
            print("client will send message: ", sys.argv[2])
            s.send(msgSend.encode('ascii'))
        else:
            print("No message word, will end connection")
    else:
        print("Invalid input, will end connection")
else:
    print("No Option: will close connection")

s.close()
