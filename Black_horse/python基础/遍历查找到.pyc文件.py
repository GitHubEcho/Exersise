#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 1. for-in dir/subdir to get the filesname
# 2. splitext filename to filter

import os

def getFiles(dir, suffix):
    res = []
    for root, directory, files in os.walk(dir):  # =>当前根,根下目录,目录下的文件
        print(root)
        print(directory)
        print(files)
        for filename in files:
            name, suf = os.path.splitext(filename) # =>文件名,文件后缀
            if suf == suffix:
                res.append(os.path.join(root, filename)) # =>吧一串字符串组合成路径
    return res

for file in getFiles("./", '.py'):
    print(file)