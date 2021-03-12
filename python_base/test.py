#!/usr/bin/python3
# -*- coding=utf-8 -*-

import re


str1 = """TCP Student  192.168.189.167:32806 Teacher  137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO 
TCP Student  192.168.189.167:80 Teacher  137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO """


list1 = str1.split('\n')

dict1 = {}
for x in list1:
    result = re.match(".*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*bytes\s+(\d+).*flags\s+(\w*)\s*", x).groups()
    qyt_key = result[0], result[1], result[2], result[3]
    qyt_value = result[4], result[5]
    dict1[qyt_key] = qyt_value

print("\n\n打印字典\n")
print(dict1)

print("\n\n格式化打印输出\n")
for key, value in dict1.items():
    print('%10s : %-20s |%10s : %-10s |%10s : %-10s|%10s : %-10s|' % (
        "src", key[0], "src_p", key[1], "dst", key[2], "dst_p", key[3]))
    print('%10s : %-20s |%10s : %-10s' % ('bytes', value[0], 'flags', value[1]))
    print('=' * 110)

