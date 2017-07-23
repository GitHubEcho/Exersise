#!/usr/bin/env python3
#coding:utf-8

import socket

server_address = ('127.0.0.1',8000)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(server_address)

while True:
    msg = input('>> ').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode())