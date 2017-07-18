#!/usr/bin/env python3
#coding:utf-8

import time,threading

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n
    def run(self):
        print('task',self.n)
        time.sleep(1)

t1 = MyThread('t1')
t2 = MyThread('t2')

t1.start()
t2.start()
