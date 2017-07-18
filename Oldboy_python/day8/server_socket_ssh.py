#!/usr/bin/env python3
#coding:utf-8
import socket,os
HOST = '127.0.0.1'
PORT = 6000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))          #元组！
server.listen(5)

while True:
    conn,addr = server.accept()
    print('new connection :',addr)
    while True:
        data = conn.recv(1024)
        if not data :
            break
        res = os.popen(data.decode()).read()
        print(res)
        res_size = str(len(res.encode())).encode()  #len()得到的是一个int型，encode方法只有str有
        print(res_size)
        conn.send(res_size)            #发送数据大小
        #time.sleep(0.5)
        client_ack = conn.recv(1024)
        conn.send(res.encode('utf-8')) #发送数据

'''
网络开发中的粘包问题，缓冲区包两次发送的数据连成一条发送
time.sleep()
'''

