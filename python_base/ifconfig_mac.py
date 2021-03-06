#!/usr/bin/python3
# -*- coding=utf-8 -*-

import re

ipconfig_result = 'ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\n        inet 192.168.128.143  netmask 255.255.255.0  broadcast 192.168.128.255\n        inet6 fe80::5717:f58c:c92:5c6e  prefixlen 64  scopeid 0x20<link>\n        ether 00:0c:29:d3:7a:1d  txqueuelen 1000  (Ethernet)\n        RX packets 42710  bytes 33149852 (31.6 MiB)\n        RX errors 0  dropped 0  overruns 0  frame 0\n        TX packets 28791  bytes 13834445 (13.1 MiB)\n        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n\n'
re_findall_result = re.findall(r'[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}',ipconfig_result)

mac = ''.join(re_findall_result)
print('MAC地址为:{:>18}'.format(mac))
