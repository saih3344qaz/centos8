#!/usr/bin/python3
# -*- coding=utf-8 -*-

import re

vlan = 'VLAN ID'
mac = 'MAC'
type = 'Type'
int = 'Interface'

str1 = '100  0050.56c0.0008  DYNAMIC  Et0/0'
m = re.match(r'(\d+)\s+([A-Fa-f0-9]{4}\.[A-Fa-f0-9]{4}.[A-Fa-f0-9]{4})\s+(\w+)\s+(\w+/\d*)',str1).groups()
print('-'*60)
print((f'{vlan:<10}: {m[0]:<10}'))
print((f'{mac:<10}: {m[1]:<10}'))
print((f'{type:<10}: {m[2]:<10}'))
print((f'{int:<10}: {m[3]:<10}'))




