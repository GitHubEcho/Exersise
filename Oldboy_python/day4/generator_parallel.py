#/usr/bin/env python2
#coding:utf-8

import time
''' 
另外一种说法：生成器就是一个返回迭代器的函数，与普通函数的区别是生成器包含yield语句，更简单点理解生成器就是一个迭代器。
生成器的好处就是无需一次性把所有元素加载到内存，只有迭代获取元素时才返回该元素，而列表是预先一次性把全部元素加载到了内存。此外用 yield 代码看起来更清晰。
'''

def consumer(name):
    print('%s准备开始吃包子了'%name)
    while True:
        baozi = yield
        print('%s把%s的包子吃了'%(name,baozi))

# c = consumer('heqian')
# c.__next__()
# c.send('hh')

def producer():
    A = consumer('xiaoxiao')
    B = consumer('heqian')
    A.__next__()
    B.__next__()
    # 因为生成器迭代器在生成器函数体的顶部开始执行，所以在生成器刚刚创建时，没有yield表达式来接收值。
    # 因此，当生成器迭代器刚刚启动时，禁止使用非无参数调用send（），如果发生这种情况，则会引发TypeError（可能是因为某种逻辑错误）。
    # 因此，在您可以与协程之前，您必须先调用next（）或send（None）将其执行提前到第一个yield表达式

    while True:
        print('已经做好一个包子'.center(50, '*'))
        A.send("猪肉大葱")
        B.send('猪肉白菜')
        print('\n')
        time.sleep(3)
producer()