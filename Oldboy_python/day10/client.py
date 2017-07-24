#!/usr/bin/env python3
#coding:utf-8

import socket

server_address = ('192.168.1.141',9000)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(server_address)

while True:
    msg = str(input('>> ')).strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode())