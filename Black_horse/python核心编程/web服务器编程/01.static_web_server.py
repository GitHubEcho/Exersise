#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket
import re
import multiprocessing


def handle_client(client_socket):
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
        flie = open(HTML_ROOT_DIR + file_name, 'rb')
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


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 7788))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        print('[%s,%s] is conneted' % addr)
        t = multiprocessing.Process(target=handle_client, args=(conn,))
        t.start()
        conn.close()


HTML_ROOT_DIR = './html'

if __name__ == '__main__':
    main()
