#!/usr/bin/env python3
#coding:utf-8

import redis

pool = redis.ConnectionPool(host = '192.168.1.141',port = 6379)

r = redis.Redis(connection_pool=pool)
r.set('fool','bar')
print(r.get('fool'))