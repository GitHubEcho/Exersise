#!/usr/bin/env python3
#coding:utf-8

import socket

HOST = '127.0.0.1'
PORT = 6000

clint = socket.socket()
clint.connect((HOST,PORT))

while True:
    conmand = input('>>').strip()
    if conmand == '':continue
    clint.send(conmand.encode('utf-8'))
    data = clint.recv(2048)
    print(data.decode('utf-8'))
client.close()