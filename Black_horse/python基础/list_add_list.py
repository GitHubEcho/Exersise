#!/usr/bin/env python3
# -*- coding:utf-8 -*-
list = []
list_temp =[]
for l in (x for x in range(1,101)):
    list_temp.append(l)
    if len(list_temp)==3:
        list.append(list_temp)
        del list_temp
        list_temp = []
print(list)


