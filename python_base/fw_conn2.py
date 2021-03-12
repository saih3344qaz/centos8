#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re

session = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\nTCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}
for conn in session.split('\n'):
    re_result = re.match(
        r'\w+\s\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}),\s\w+\s\d:\d\d:\d\d,\s\w+\s(\d+),\s\w+\s([U|I|O]{1,3})',
        conn).groups()
    asa_dict[(re_result[0], re_result[1], re_result[2], re_result[3])] = (re_result[4], re_result[5])
print('\n打印分析以后的字典!\n')
print(asa_dict)

src = 'src'
src_p = 'src_p'
dst = 'dst'
dst_p = 'dst_p'
bytes = 'bytes'
flags = 'flags'
format_str1 = '{:>5} : {:<20} |{:>10} : {:<10} |{:>10} : {:<16}|{:>10} : {:<10}'
format_str2 = '{:>5} : {:<20} |{:>10} : {:<10}'
print('\n格式化打印输出:\n')

for key,value in asa_dict.items():
    # print(f'{src:>5} : {key[0]:<20}|{src_p:>10} : {key[1]:<10}|{dst:>10} : {key[2]:<16}|{dst_p:>10} : {key[3]:<10}')
    # print(f'{bytes:>5} : {value[0]:<20}|{flags:>10} : {value[1]:<10}')
    print(format_str1.format('src', key[0], 'src_p', key[1], 'dst', key[2], 'dst_p', key[3]))
    print(format_str2.format('bytes', value[0], 'flags', value[1]))
    print('=' * 105)
