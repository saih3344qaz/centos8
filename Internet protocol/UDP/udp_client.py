#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import socket
import pickle
import struct

def udp_send_date(ip, port, data_list):
    address = (ip, port)
    s =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    version = 1
    pkt_type = 1
    seq_id = 1
    length = 4
    for x in data_list:
        # ---header设计---
        # 2 字节 版本 1
        # 2 字节 类型 1 为请求 2 为响应(由于是UDP单向流量!所有此次试验只有请求)
        # 4 字节 ID号
        # 4 字节 长度

        # ---变长数据部分---
        # 使用pickle转换数据

        # ---HASH校验---
        # 16 字节 MD5值
        send_data = pickle.dumps(x)

        udp_header = struct.pack('>hhii', version, pkt_type, seq_id, length + len(send_data))
        msg = udp_header + send_data
        # print(type(msg))
        # 如果客户输入为空,发送空数据,并且退出
        if not msg:
            s.sendto(msg,address)
            break
        # 如果客户输入不为空,发送数据
        s.sendto(msg, address)
        seq_id += 1

    s.close()


if __name__ == "__main__":
    user_date = ['乾颐堂', [1,'qytang', 3],{'qytang':1, 'test':3}]
    udp_send_date('192.168.128.1', 6666, user_date)