#!/usr/bin/env python3
#coding:utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello',durable=True) #队列持久化

channel.basic_publish(exchange ='',               #其实rabbitmq这个主要的中间人就是xchange=''是特殊的，可以通过route_key 直接指向queue
                      routing_key = 'hello',
                      body = 'hello world!',
                      properties = pika.BasicProperties(
                          delivery_mode=2      #消息持久化
                      ))
print("[x] sent 'hello world'")
connection.close()