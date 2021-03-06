#!/usr/bin/env python3
#coding:utf-8

import socket,select,queue

server_address = ('127.0.0.1',8000)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(False) #设置为非阻塞
server.bind(server_address)
server.listen(100)

inputs = [server]
outputs = []

message_queues = {} #创建字典{套接字对象:消息队列}

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
            conn.setblocking(0)
            inputs.append(conn)
            message_queues[conn] = queue.Queue()
        else:
            data = r.recv(1024)
            if  data:
                print('%s >> %s' % (r.getpeername(), data))
                message_queues[r].put(data)
                if r not in outputs:
                    outputs.append(r)
            else:
                print('%s client is disconnected'%r.getpeername())
                if r in outputs:
                    outputs.remove(r)
                inputs.remove(r)
                r.close()
                del message_queues[r]
    #处理writable
    for w in writable:
        try:
            data_to_client = message_queues[w].get_nowait()
        except queue.Empty:
            print("client [%s]" % w.getpeername()[0], "queue is empty..")
            outputs.remove(w)
        else:
            print("sending msg to [%s]" % w.getpeername()[0] )
            w.send(data_to_client)

    #处理exceptonal
    for e in exceptional:
        print("handling exception for ", e.getpeername())
        inputs.remove(e)
        if e in outputs:
            outputs.remove(e)

        e.close()
        del message_queues[e]

