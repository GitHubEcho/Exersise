#!/usr/bin/env python2
#coding:utf-8

import json
import pickle

def seahi():
    print('hello')

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23,
    #'func' :seahi,
    'sex' :True
}

#data = pickle.dump(f.read())
with open('data.json','w') as f:
    json.dump(data,f)
    #pickle.dump(data,f)

"""
把变量从内存中变成可存储或传输的过程称之为序列化，注意：序列化对象，不是内存地址
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
"""
