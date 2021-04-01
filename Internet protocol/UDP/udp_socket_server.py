#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from tools.get_ip_netifaces import get_ip_address
import socket
import sys

address = ("0.0.0.0", 6666)
# 创建UDP套接字Socket, AF_INET为IPv4, SOCK_DGRAM为Datagram就是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 套接字绑定到地址,元组(host, port)
s.bind(address)

print('UDP服务器就绪!等待客户数据!')
while True:
    try:
        # 接收UDP套接字的数据,2048为接收的最大数据量,多的直接丢弃!
        # 不推荐使用UDP传大量数据
        aa = s.recvfrom(2048)
        print(aa)
        data, addr = aa
        # 如果客户发来空数据,就退出循环
        if not data:
            print("客户端退出!")
            break
        # 如果客户发来的数据不为空,就显示数据,与源信息
    except KeyboardInterrupt:
        sys.exit()

s.close()

