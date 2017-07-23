#!/usr/bin/env python3
#coding:utf-8

import socket,select,queue

server_address = ('127.0.0.1',8000)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(server_address)
server.listen(100)

server.setblocking(False)

inputs = [server]
outputs = []

message_queues = {}#套接字对象:消息队列

while inputs :
    readable,writable,exceptional = select.select(inputs,outputs,inputs)
    #select()系统调用来监视多个文件描述符的数组，当select()返回后，该数组中就绪的文件描述符便会被内核修改标志位，
    #使得进程可以获得这些文件描述符从而进行后续的读写操作。
    # readable:返回活动的文件描述符
    # writable:下一次监视时，返回上次放入的数据

    #print(readable,writable,exceptional)
    if not (readable or writable or exceptional):
        print ("Time out ! ")
        break

    #处理readable
    for r in readable:
        if r is server :
            conn,addr = server.accept()
            print('new connecton:',addr)
            inputs.append(conn)
            message_queues[conn] = queue.Queue()
        else:
            msg = r.recv(1024)
            if  not msg:continue
            print('%s >> %s'%(r.getpeername(),msg))
            message_queues[r].put(msg)
            # r.send(msg)
            # print('send done...')
            outputs.append(r)

    #处理writable
    for w in writable:
        data_to_client = message_queues[w].get()
        w.send(data_to_client)
        outputs.remove(w)

    #处理exceptonal
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        e.close()
        del message_queues[e]

