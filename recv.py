#!/usr/bin/python3

import socket

ip='0.0.0.0'
port=9999

#generate protocol type of socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#to bind ip and port

s.bind((ip,port))

#now we can receive data from sender

while True:
        web=s.recvfrom(100)
        print(web)
        # reply to send
        s.sendto("niceeeeee".encode('ascii'),web[1])
