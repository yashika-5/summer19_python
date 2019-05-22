#!/usr/bin/python3

import socket

#creating udp socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#where to send data

rec_ip='0.0.0.0'
rec_port=9999

while True:
        data=input("enter your message...")
        #converting data to ascii
        new=data.encode('ascii')
        #finally sending the data
        s.sendto(new,(rec_ip,rec_port))
        # now recv data
        print(s.recvfrom(100))


