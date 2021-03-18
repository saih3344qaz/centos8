#!/usr/bin/python3
# -*- coding=utf-8 -*-

from scapy_ping_one_new import test_ping
from paramiko_ssh import test_ssh
import re
import pprint


def get_if(*ips, username='admin', password='admin@123'):
    device_if_dict = {}
    for ip in ips:
        host = ip
        device = test_ping(host)
        if device != None:
            port_dict = {}
            # print('\n', device, '可达')
            port_info = test_ssh(device, username, password, cmd='show ip int bri')
            port_info_re = re.search(r'(\w+\d/\d|\w+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*\w+\s*\w+\s+up\s+up',port_info).groups()
            port_dict[port_info_re[0]] = port_info_re[1]
            device_if_dict[device] = port_dict
        else:
            print(host, '不可达')
    return device_if_dict


if __name__ == '__main__':
    # print(get_if('192.168.128.131', '192.168.128.144'))
    pprint.pprint(get_if('192.168.128.131', '192.168.128.144'), indent=4)

