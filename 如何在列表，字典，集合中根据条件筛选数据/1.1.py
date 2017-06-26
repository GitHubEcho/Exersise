#!/bin/python
#coding:utf-8
"""迭代方式输出"""
data = [1,5,-3,-2,6,0,9]
res = []
for n in data:
    if n < 0:
        res.append(n)

print(res)
