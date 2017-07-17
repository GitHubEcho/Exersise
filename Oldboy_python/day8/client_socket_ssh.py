#!/usr/bin/env python3
#coding:utf-8

import socket

HOST = '127.0.0.1'
PORT = 6000

client = socket.socket()
client.connect((HOST, PORT))

while True:
    conmand = input('>>').strip()
    if conmand == '':continue
    client.send(conmand.encode('utf-8'))

    res_size = client.recv(1024)  # 接收结果大小
    print('接收结果大小',res_size)
    client.send('client准备好接收了'.encode())
    recevice_size = 0
    com_res = b''
    while recevice_size < int(res_size.decode()):
        data = client.recv(1024)  # 接收结果
        recevice_size += len(data)
        com_res += data
    else:
        print('接收大小',recevice_size)
    print(com_res.decode('utf-8'))

client.close()