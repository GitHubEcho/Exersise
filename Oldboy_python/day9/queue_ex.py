#!/usr/bin/env python3
#coding:utf-8

import threading,time,queue
'''
队列提高双方效率

程序的解耦

有队列以后解决了程序之间解耦问题
①解耦
②提高交互双方效率
'''
#consumer_and_producer model

q = queue.Queue(10)

def consumer(name):
    while True:
        q.get()
        time.sleep(1)
        print('\033[42;0m%s eatd bone\033[0m'%name)

def producuer():
    sum = 1
    while True:
        q.put(sum)
        time.sleep(3)
        print('%s is done'%sum)
        sum += 1

producuer = threading.Thread(target=producuer)
producuer.start()

dog1 = threading.Thread(target=consumer,args=('dog1',))
dog2 = threading.Thread(target=consumer,args=('dog2',))
dog3 = threading.Thread(target=consumer,args=('dog3',))
dog1.start()
dog2.start()
dog3.start()

