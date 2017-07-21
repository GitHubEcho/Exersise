#!/usr/bin/env python3
#coding:utf-8

from multiprocessing import Process,Pool
import os,time

# def bar():
#     print('exec-->',os.getpid())
#     return

def bar(i):
    print(i,'exec-->',os.getpid())

def Foo(i):
    print('process is ',i)
    time.sleep(1)
    return i + 100             #需要返回i的值，不然后面的bar不知道


if __name__ == '__main__':
    pool = Pool(processes=3)
    print('main process ',os.getpid())
    for i in range(10):
        #p = Process(target=pool,args=(i,))
        #pool.apply(func=Foo,args=(i,))                   #串行
        #pool.apply_async(func=Foo,args=(i,))             #并行
        pool.apply_async(func=Foo,args=(i,),callback=bar) #共享一个参数需要添加参数

    pool.close()
    pool.join()

'''
进程池：限制进程的数量
callback函数由主程序进程执行
假设一种情形：
    在每个子进程在数据库操作后，向数据库加入一条日志
    因为启动的每个进程，去访问数据库时，要建立新的连接，但是回调函数，只需要主进程持久连接
'''