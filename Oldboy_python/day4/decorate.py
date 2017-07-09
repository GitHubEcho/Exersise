#/usr/bin/env python2
#coding:utf-8

import  time

def timer(func):    #timer(test)==>func = test
    def deco(*args,**kwargs):  #*args是可变的positional arguments列表，**kwargs是可变的keyword arguments列表 非固定参数
        start_time = time.time()
        func(*args,**kwargs)  #run test()
        stop_time = time.time()
        print('func run time is %s'%(stop_time-start_time))
    return deco

@timer #test = timer(test)
def test():
    time.sleep(1)
    print('in the test')

@timer
def test1(name,age):
    print('%s is %s'%(name,age))

#test = timer(test)
test()
test1('heqian',20)

'''装饰器
- python中函数是对象: 可以赋值给一个变量，同时可以作为形参传递给函数（高阶函数）
- python中函数可以定义在函数中（嵌套函数）
'''
