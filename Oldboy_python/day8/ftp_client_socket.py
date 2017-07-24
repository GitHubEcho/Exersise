#!/usr/bin/env python3
#coding:utf-8

import socket,sys

HOST = '127.0.0.1'
PORT = 6000

client = socket.socket()
client.connect((HOST, PORT))

def progress_bar(proportion):
    s = '#'
    for _ in range(40):
        sys.stdout.write(s*int(40*proportion))
        sys.stdout.flush()

progress_bar(0.4)

while True:
    command = input('client >>').strip()
    if command == '':continue
    if command.startswith('get'):
        client.send(command.encode('utf-8'))        #send command
        server_respound = client.recv(1024)
        print('server >>',server_respound.decode())

        cmd, filename = command.split()
        file_size  = int(client.recv(1024).decode()) #receive data_size
        print('file size is %s'%file_size)

        recevice_size = 0
        f = open(filename+'.new', 'wb')
        d = file_size - recevice_size
        while recevice_size < file_size:              #loop receive data
            #proportion = float(recevice_size/file_size)
            if d < 1024:
                size = d
            else :
                size = 1024
            data = client.recv(1024)
            recevice_size += len(data)
            f.write(data)                              #write data in the file
        else:
            print('recevice %s data'%recevice_size)
            print('file recevice success')
            f.close()

client.close()