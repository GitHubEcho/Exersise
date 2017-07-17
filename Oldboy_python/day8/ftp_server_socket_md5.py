#!/usr/bin/env python3
#coding:utf-8
import socket ,os,hashlib

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

        m = hashlib.md5()
        with open(filename,'rb')as f:
            for line in f :
                m.update(line)
                conn.send(line)

        raw_file_md5 = m.hexdigest()
        conn.send(raw_file_md5.encode())


