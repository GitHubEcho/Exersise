#!/usr/bin/env python3
#coding:utf-8
import socket
import os

HOST = '127.0.0.1'
PORT = 6000


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))          #元组！
server.listen(5)

while True:
    conn,addr = server.accept()
    while True:
        data = conn.recv(2048)
        if not data :
            break
        res = os.popen(data.decode()).read()
        conn.send(res.encode('utf-8'))
