#!/usr/bin/env python3
#coding:utf-8
import json
import pickle
# with open('data.json','r') as  f:
#     s = f.read()
# print(type(s))
# print(s[2])

def seahi(name):
    print("hello2,",name)
    pass

#data = pickle.loads(f.read())
with open('data.json','rb') as  f:
    # data = json.load(f)
    data = pickle.load(f)

print(data['func']('heqian'))
# print(data['name'])




"""
结尾带s就是在字符串层面上操作，如果不带s就是在文件层级操作。

官方文档中对于这2者也有一段比较的话，我就直接拿来用了

 - JSON是文本形式的存储，Pickle则是二进制形式（读取时以二进制打开）
 - JSON是人可读的，Pickle不可读
 - JSON广泛应用于除Python外的其他领域，Pickle是Python独有的。
 - JSON只能dump一些python的内置对象，Pickle可以存储几乎所有对象。

在我看来，如果偏向应用特别是web应用方面，可以常用JSON格式。如果偏向算法方面，尤其是机器学习，
则应该使用cPickle，pylearn2库中保存model就是使用这项技术的;)
"""
