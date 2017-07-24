#!/usr/bin/env python3
#coding:utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters( 'localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello',durable=True) #队列持久化


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=2)  #当队列中还有prefetch_count消息数量时发给其他接收端

channel.basic_consume(callback,
                      queue='hello1',
                      #no_ack=True  #不确认，处理结果不用不返回rabbitmq-server确认，
                      #如果不确认，在客户端断开时，把消息当成新的消息发送给下一个接收者
                     )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

