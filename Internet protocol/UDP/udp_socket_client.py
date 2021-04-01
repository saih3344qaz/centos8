#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import socket

address = ("192.168.128.1", 6666)
# 创建UDP套接字Socket, AF_INET为IPv4, SOCK_DGRAM为Datagram就是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 收集客户输入数据
    msg = input('请输入数据:')
    # 如果客户输入为空,发送空数据,并且退出
    if not msg:
        s.sendto(msg.encode(), address)
        break
    # 如果客户输入不为空,发送数据
    s.sendto(msg.encode(), address)

s.close()


