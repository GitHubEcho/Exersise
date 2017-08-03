#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('',9000))
server.listen(10)
server.setblocking(False)

connection_list = []

while True:
    try:
        conn,addr = server.accept()
    except :
        pass
    else:
        print('connected by ',str(addr))
        conn.setblocking(False)         #先设为阻塞，再加入表中
        connection_list.append((conn,addr))

        for conn,addr in connection_list:
            try:
                recvData = conn.recv(1024)
            except  :
                pass
            else:
                if len(recvData) > 0:
                    print('%s recv data:%s'%(str(addr),recvData))
                else:
                    conn.close()
                    connection_list.remove((conn,addr))
                    print('%s is not connected' % str(addr))



