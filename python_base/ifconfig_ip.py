#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re
import os
ipconfig_result = os.popen('ifconfig ' + 'ens33').read()

ipv4_add = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ipconfig_result)[0]
netmask = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.[0]',ipconfig_result)[0]
broadcast = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.[2][5][5]',ipconfig_result)[0]
mac_add = re.findall(r'[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}',ipconfig_result)[0]

#格式化字符串
format_string = 'ipv4_add   :{0:<10}\nnetmask    :{1:<10}\nbroadcast  :{2:<10}\nmac_add    :{3:<10}'
#打印结果
print(format_string.format(ipv4_add,netmask,broadcast,mac_add))

#产生网关地址
ipv4_gw = '192.168.128.1'

#打印网关的IP地址：
print('\n我们假设网关IP地址为第一位为1，因此网关IP地址为：'+ ipv4_gw + '\n')

#ping网关
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()

re_ping_result = re.findall(r'\s[0][%]\s\w+\s[l][o][s][s]',ping_result)
if re_ping_result:
    print('网关可达')
else:
    print('网关不可达')



# print()

# for ip in re_findall_result:
#     if ip[-1] == '0':
#         print('{:>13} : {:<15}'.format('Network Mask',ip))
#     elif ip[-3:] == '255':
#         print('{:>13} : {:<15}'.format('Broadcast',ip))
#     else:
#         print('{:>13} : {:<15}'.format('Ipv4_Addr',ip))



