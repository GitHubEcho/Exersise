#!/usr/bin/env python3
#coding:utf-8

from multiprocessing import Pipe,Process

def f(conn):
    conn.send('message is from child')
    message = conn.recv()
    print(message)

if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    P = Process(target=f,args=(child_conn,))
    P.start()
    print(parent_conn.recv())
    parent_conn.send('hello')
