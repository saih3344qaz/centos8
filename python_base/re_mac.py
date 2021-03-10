#!/usr/bin/python3
# -*- coding=utf-8 -*-

import re

vlan = 'VLAN ID'
mac = 'MAC'
type = 'Type'
int = 'Interface'

str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
m = re.match(r'(\d+)\s+([A-Fa-f0-9]{4}\.[A-Fa-f0-9]{4}.[A-Fa-f0-9]{4})\s+(\w+)\s+(\w+/\d+/\d+)',str1).groups()
print('-'*60)
print((f'{vlan:<10}: {m[0]:<10}'))
print((f'{mac:<10}: {m[1]:<10}'))
print((f'{type:<10}: {m[2]:<10}'))
print((f'{int:<10}: {m[3]:<10}'))




