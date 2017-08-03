#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

def random_list(n):
    list =random.sample(range(1,n+1),n)
    return list

print(random_list(6))