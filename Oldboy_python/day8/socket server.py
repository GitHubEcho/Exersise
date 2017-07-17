#!/usr/bin/env python3
#coding:utf-8

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strp()
                print('{} say'.format(self.client_address[1]))
                print(self.data)
                self.request.send(self.data)
            except ConnectionResetError as e :
                print('error',e)
                break
if __name__ == '__main__':
    HOST,PORT = '127.0.0.1',6000
    servcer = socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    servcer.serve_forever()

