#!/usr/bin/python2
#coding:utf-8
"""迭代方式输出"""
data = [1,5,-3,-2,6,0,9]
res = []
for n in data:
    if n < 0:
        res.append(n)

print(res)

"""列表筛选数据 """
from random import randint
data = [randint(-10,10)for _ in xrange(10)]
print(data)

#fliter函数筛选
print filter(lambda x:x >= 0,data)


#列表过滤
print [x for x in data if x >= 0]


"""note:
# 1.lambda 会创建一个函数对象，，但是不会把函数的对对象赋值给标识符，而def则会把函数对象赋值给一个变量。
# 2.lambda 是一个表达式，而def是一个语句。
"""

"""字典筛选数据"""
from random import randint
dic = {x: randint(60,100) for x in xrange(1,21)}
print dic
print {k: v for k,v in dic.iteritems() if v >= 80}


"""集合筛选数据"""
from random import randint
data = [randint(-10,10) for _ in xrange(10)]
s = set(data)
print {x for x in s if x%3==0}
