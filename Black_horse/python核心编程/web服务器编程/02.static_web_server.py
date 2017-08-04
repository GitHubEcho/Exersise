#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import socket
import multiprocessing


class Httpserver(object):
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def start(self):
        self.server.listen(5)
        while True:
            conn, addr = self.server.accept()
            print('[%s,%s] is conneted' % addr)
            t = multiprocessing.Process(target=self.handle_client, args=(conn,))
            t.start()
            conn.close()

    def handle_client(self, client_socket):
        '''处理客户端请求'''
        # 获取客户端请求
        request_data = client_socket.recv(1024)
        request_lines = request_data.splitlines()
        for line in request_lines:
            print(line)

        # 请求报文格式
        '''
        GET / HTTP/1.1
        Host: 127.0.0.1:7788
        '''
        # 解析请求报文
        request_start_line = request_lines[0]
        file_name = re.match(r'\w+ +(/[^ ]*)', request_start_line.decode('utf-8')).group(1)

        if '/' == file_name:
            file_name = '/index.html'
        try:
            flie = open(self.HTML_ROOT_DIR + file_name, 'rb')
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_headers = "Server: My server\r\n"
            response_body = "The file is not found!"
        else:
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server: My server\r\n"
            data = flie.read()
            response_body = data.decode('utf-8')

        # 构建响应报文
        response_messages = response_start_line + response_headers + "\r\n" + response_body
        print(response_messages)

        # 返回响应数据
        client_socket.send(response_messages.encode())

        # 关闭客户端连接
        client_socket.close()

    def set(self,dir,port):
        self.HTML_ROOT_DIR = dir
        self.server.bind(('',port))

if __name__ == '__main__':
    server = Httpserver()
    server.set('./html',7788) # 设置服务器根目录和端口
    server.start()
