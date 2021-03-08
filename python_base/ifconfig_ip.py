#!/usr/bin/python3
# -*- coding=utf-8 -*-

import re

ipconfig_result = 'ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\n        inet 192.168.128.143  netmask 255.255.255.0  broadcast 192.168.128.255\n        inet6 fe80::5717:f58c:c92:5c6e  prefixlen 64  scopeid 0x20<link>\n        ether 00:0c:29:d3:7a:1d  txqueuelen 1000  (Ethernet)\n        RX packets 42710  bytes 33149852 (31.6 MiB)\n        RX errors 0  dropped 0  overruns 0  frame 0\n        TX packets 28791  bytes 13834445 (13.1 MiB)\n        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n\n'
re_findall_result = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ipconfig_result)
# print(re_findall_result)
for ip in re_findall_result:
    if ip[-1] == '0':
        print('{:>13} : {:<15}'.format('Network Mask',ip))
    elif ip[-3:] == '255':
        print('{:>13} : {:<15}'.format('Broadcast',ip))
    else:
        print('{:>13} : {:<15}'.format('Ipv4_Addr',ip))



