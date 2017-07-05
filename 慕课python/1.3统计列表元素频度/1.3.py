#!/usr/bin/env python2
#coding:utf-8
from random import randint
from collections import Counter
import re

#案例一：随机列表中[5,6,5,4,...,5,6]中出现次数最高的三个元素
data = [randint(0,20) for _ in xrange(30)]
c = dict.fromkeys(data,0)
for x in data:
    c[x] += 1
print c

c2 = Counter(data)
print c2.most_common(3)


#案例二：对文章的单词进行词频统计
txt = open('/home/heqian/Exersise/snake.py').read()
s = re.split('\W+',txt) #正则非单词分割
c3 = Counter(s)
print c3.most_common(10)