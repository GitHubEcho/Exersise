#/usr/bin/env python2
#coding:utf-8


def fib(max = 10):
    n,a,b, = 0,0,1
    while n < max:
        yield (b)  #yield保存了函数的中断状态
        a,b = b,a+b
        n +=1
    return 'done'
f = fib(9)
while True:
    try:
        print(f.__next__())
    except StopIteration as a:
       print(a.value)
       break