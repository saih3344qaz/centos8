#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re

session1 = 'TCP Student 192.168.189.167:32806 Teacher 137.8.5.128:65247, idle 0:00:00, bytes 74, flags UIO'
session2 = 'TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO'

sess1_ip = re.match(
    r'\w+\s\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}),\s\w+\s\d:\d\d:\d\d,\s\w+\s\d+,\s\w+\s[U|I|O]{1,3}',
    session1).groups()
sess2_ip = re.match(
    r'\w+\s\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}),\s\w+\s\d:\d\d:\d\d,\s\w+\s\d+,\s\w+\s[U|I|O]{1,3}',
    session2).groups()
sess1_port = re.match(
    r'\w+\s\w+\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}\s\w+\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5},\s\w+\s\d:\d\d:\d\d,\s\w+\s(\d+),\s\w+\s([U|I|O]{1,3})',
    session1).groups()
sess2_port = re.match(
    r'\w+\s\w+\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}\s\w+\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5},\s\w+\s\d:\d\d:\d\d,\s\w+\s(\d+),\s\w+\s([U|I|O]{1,3})',
    session2).groups()
dict1 = {sess1_ip: sess1_port, sess2_ip: sess2_port}

src = 'src'
src_p = 'src_p'
dst = 'dst'
dst_p = 'dst_p'
bytes = 'bytes'
flags = 'flags'

print('打印字典')
print(dict1)
print('格式化打印输出')
print(
    f'{src:>5} : {sess1_ip[0]:<20}|{src_p:>10} : {sess1_ip[1]:<10}|{dst:>10} : {sess1_ip[2]:>12}|{dst_p:>10} : {sess1_ip[3]:<10}|')
print(f'{bytes:>5} : {sess1_port[0]:<20}|{flags:>10} : {sess1_port[1]:<10}')
print('=' * 105)
print(
    f'{src:>5} : {sess2_ip[0]:<20}|{src_p:>10} : {sess2_ip[1]:<10}|{dst:>10} : {sess2_ip[2]:>12}|{dst_p:>10} : {sess2_ip[3]:<10}|')
print(f'{bytes:>5} : {sess2_port[0]:<20}|{flags:>10} : {sess2_port[1]:<10}')
print('=' * 105)
