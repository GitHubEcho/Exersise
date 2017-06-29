#/usr/bin/env python2
#coding:utf-8
"""统计某个字符"""
with open('test.txt') as f:
     print f.read().count('o')

res={}
with open('test.txt') as a:
    for s in a.read():
        res[s] = res.get(s,0)+1
        # if s in res:
        #     res[s] += 1
        # else:
        #     res[s] = 1
print res

