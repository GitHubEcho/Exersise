#!/usr/bin/env python3
#coding:utf-8

import os
def Test3(rootDir, level=1):
    if level==1: print (rootDir )
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        print ('│  '*(level-1)+'│--'+lists )
        if os.path.isdir(path):
            Test3(path, level+1)
