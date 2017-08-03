#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def fun(a,b):
    def fun_in(x):
        print(a * x + b)
    return fun_in

line  = fun(4,5)
line(5)