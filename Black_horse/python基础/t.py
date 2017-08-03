#!/usr/bin/env python3
# -*- coding:utf-8 -*-

a = "aAsmr3idd4bgs7Dlsf9eAF"
a_list = sorted(list(a))
a_lower_list = []
a_upper_list = []
for x in a :
    if x.islower():
        a_lower_list.append(x)
    if x.isupper():
        a_upper_list.append(x)
for y in a_upper_list:
    y_lower = y.lower()
    if y_lower in a_lower_list:
        a_lower_list.insert(a_lower_list.index(y_lower),y)
print(a_lower_list)

for y in a_lower_list:
    if y.upper() in a_upper_list:
        #a_upper = a_upper_list.pop(y.upper())
        a_upper_list.insert(a_upper_list.index(y.upper()),y)
print(a_lower_list)


