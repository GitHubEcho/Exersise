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
    print('new connection :',addr)
    while True:
        cmd = conn.recv(1024)
        if not cmd :
            print('client is not connection')
            break
        cmd,filename = cmd.decode().split()
        file_size = os.stat(filename).st_size
        conn.send(b'I will send data')
        conn.send(str(file_size).encode())

        with open(filename,'rb') as f:
            for line in f :
                conn.send(line)




