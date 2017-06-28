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
d = {x:randint(60,100) for x in "sfadfadfd"}
d.keys()   #获取键
d.values() #获取值

#方法一
#zip(d.values(),d.keys())         #zip函数构成元祖
zip(d.itervalues(),d.iterkeys())  #优化内存
print sorted(zip(d.itervalues(),d.iterkeys()))
#方法二
print sorted(d.items(),key=lambda x:x[1])
