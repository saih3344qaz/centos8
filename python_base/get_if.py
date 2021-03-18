#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from scapy_ping_one_new import test_ping
from paramiko_ssh import test_ssh
import re
import pprint


def get_if(*ips, username='admin', password='admin@123'):
    device_if_dict = {}
    for ip in ips:
        ping_result = test_ping(ip)
        if ping_result != None:
            port_dict = {}
            # print('\n', device, '可达')
            port_info = test_ssh(ip, username, password, cmd='show ip int bri')
            # print(port_info)
            for a in re.findall(r'(\w+\d/\d|\w+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*\w+\s*\w+\s+up\s+up',port_info):
                b = list(a)
                # print(b)
                port_dict[b[0]] = b[1]
            # print(port_dict)
            device_if_dict[ip] = port_dict
        else:
            print(ip, '不可达')
    return device_if_dict


if __name__ == '__main__':
    # print(get_if('192.168.128.131', '192.168.128.144'))
    pprint.pprint(get_if('192.168.128.131', '192.168.128.144'), indent=4)
