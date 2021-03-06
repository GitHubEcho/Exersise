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

'''
generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''