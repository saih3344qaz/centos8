#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import socket
import sys
import pickle
import struct

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
        recv_source_data = s.recvfrom(2048)
        data, addr = recv_source_data
        # print(len(data),len(addr))
        udp_header = struct.unpack('>hhii',data[:12])
        data_load = pickle.loads(data[12:])

        if not data:
            print("客户端退出!")
            break
        print('=' * 80)
        print('{0:<30}:{1:<30}'.format('数据来自于:',str(addr)))
        print('{0:<30}:{1:<30}'.format('数据序号为:', udp_header[2]))
        print('{0:<30}:{1:<30}'.format('数据长度为:', udp_header[-1]))
        print('{0:<30}:{1:<30}'.format('数据内容为:', str(data_load)))
    except KeyboardInterrupt:
        sys.exit()

s.close()
