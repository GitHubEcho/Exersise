#!/usr/bin/env python3
#coding:utf-8
"""简单sed文件修改"""
import sys
import os

file = sys.argv[1]
old = sys.argv[2]
new = sys.argv[3]


with open(file,'r') as f,open('a','w') as f_new:
    for line in f:
        if old in line:
            line = line.replace(old,new)
        f_new.write(line)
os.system('cat a > hello')
print('fix success')
