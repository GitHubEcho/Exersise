#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

res = os.fork()
if res == 0:
    while True:
        print('---child process----')
else:
    while True:
        print('-----parent process----')