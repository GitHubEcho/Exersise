#!/usr/bin/env python2
#coding:utf-8
from random import randint
"""
解决办法：
 内置sorted函数
  - 算法千锤百炼足够
  - 在内部以c的速度运行

"""
#1.使用sorted函数
d = {x:randint(60,100) for x in "sfadfadfd"}#生成随机列表
d.keys()   #获取键
d.values() #获取值

#方法一
print zip(d.values(),d.keys())         #zip函数构成元祖
zip(d.itervalues(),d.iterkeys())  #优化内存
print sorted(zip(d.itervalues(),d.iterkeys()))
#方法二
print d.items()             #返回字典可遍历的(键, 值) 元组数组。
print sorted(d.items(),key=lambda x:x[1])  #key的意思就是把列表的每一个元素去执行key里面的方法并返回，构成一个新的列表

"""
通过值去求得键
分析
    1.字典迭代的是键而不是值
    2.字典具有唯一键，值不是唯一的

"""
a = {'a':"haha",'b':"dfka",'c':"haha",'d':"sdf"}
search = "haha"
key_list = []
for x,y in a.items():   #使字典items()以列表返回可遍历的(键, 值) 元组数组。
    if search in y:
        key_list.append(x)
print key_list