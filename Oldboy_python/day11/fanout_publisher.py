#!/usr/bin/env python3
#coding:utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(
                        exchange='logs',
                        type= 'fanout'
                        )

message = 'info: hello world!'

channel.basic_publish(exchange='logs',
                      routing_key = '',
                      body = message
                        )
print('[x] sent %s message'%message)
connection.close()