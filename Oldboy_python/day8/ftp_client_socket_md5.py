#!/usr/bin/env python3
#coding:utf-8

import socket,hashlib

HOST = '127.0.0.1'
PORT = 6000

client = socket.socket()
client.connect((HOST, PORT))

while True:
    command = input('client >>').strip()
    if command == '':continue
    if command.startswith('get'):
        client.send(command.encode('utf-8'))
        server_respound = client.recv(1024)
        print('server >>',server_respound.decode())

        cmd, filename = command.split()
        file_size  = int(client.recv(1024).decode())
        print('file size is %s'%file_size)

        m = hashlib.md5()
        recevice_size = 0
        f = open(filename+'.new', 'wb')
        d = file_size - recevice_size

        while recevice_size < file_size:
            if d < 1024:
                size = d
            else :
                size = 1024
            data = client.recv(1024)
            recevice_size += len(data)
            m.update(data)
            f.write(data)
        else:
            print('recevice %s data'%recevice_size)
            print('file recevice success')
            new_flie_md5 = m.hexdigest()
            f.close()
            raw_flie_md5 = client.recv(1024).decode()
            print('raw file md5 is',raw_flie_md5)
            print('new file md5 is',new_flie_md5)
client.close()