#!/usr/bin/env python3
#coding:utf-8

import os
from multiprocessing import Process,Queue

def acesse_queue(queue):
    print('\n### current process is ', __name__)
    print('parent process PID:', os.getppid())
    print('current process PID:', os.getpid())
    queue.put(['xiao','he','zhang'])
    print(queue.get())

if __name__ == '__main__':
    q = Queue()
    #q.put('li')
    P = Process(target=acesse_queue,args=(q,))
    P.start()
    P.join()
    print('\n### current process is ', __name__)
    print('parent process PID:', os.getppid())
    print('current process PID:', os.getpid())
    print(q.get())

'''
把进程中的数据pickle了一份
'''