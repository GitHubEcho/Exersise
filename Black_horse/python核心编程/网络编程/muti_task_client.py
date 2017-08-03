#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',7788))

while True:
    data = input('>>')
    client.send(data.encode('utf-8'))
    #msg = client.recv(1024)
    #print(msg.decode())
client.close()