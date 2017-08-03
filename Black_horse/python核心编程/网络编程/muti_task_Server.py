#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
from  threading import Thread

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',6546))
server.listen(5)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

def task(conn,addr):
    print('conected by ',addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('[%s]client is not connection'%str(addr))
            break
        else:
            conn.send(data)
    conn.close()

def main():
    try:
        while True:
            conn,addr = server.accept()
            t = Thread(target=task,args=(conn,addr))
            t.start()
            #conn.close()   #多进程和多多线程的区别之处
    finally:
        server.close()

if __name__ == '__main__':
    main()
