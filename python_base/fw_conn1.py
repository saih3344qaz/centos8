#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re

session1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

sess1 = re.match(
    r'(\w+)\s\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})\s\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}),\s\w+\s(\d+):(\d+):(\d+),\s\w+\s(\d+),\s\w+\s([U|I|O]{1,3})',
    session1).groups()
protocol = 'protocol'
server = 'server'
localserver = 'localserver'
idle = 'idle'
bytes = 'bytes'
flags = 'flags'

# print(sess1)
print(f'{protocol:<15} : {sess1[0]:<20}')
print(f'{server:<15} : {sess1[1]:<20}')
print(f'{localserver:<15} : {sess1[2]:<20}')
print(f'{idle:<15} : {sess1[3]}小时{sess1[4]}分钟{sess1[5]}秒')
print(f'{bytes:<15} : {sess1[6]:<20}')
print(f'{flags:<15} : {sess1[7]:<20}')