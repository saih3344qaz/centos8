#!/usr/bin/python3
# -*- coding=utf-8 -*-

import re

port = '接口'
ip = 'IP地址'
status = '状态'

str1 = 'Ethernet0/0   192.168.128.131 YES DHCP   up  up'
msg = re.match(r'(\w+/\d+)\s+(\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s\w+\s\w+\s+[a-z]{2}\s+([a-z]{2})',str1).groups()
l1 = str1.split()
tup = tuple(l1)

print(tup)
print('-'*60)
print((f'{port:<8}: {msg[0]:<10}'))
print((f'{ip:<8}: {msg[1]:<10}'))
print((f'{status:<8}: {msg[2]:<10}'))



