#!/usr/bin/python3
# -*- coding=utf-8 -*-

import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
# logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from kamene.layers.inet import ICMP, IP
from kamene.all import *
# from scapy.layers.inet import ICMP, IP
# from scapy.all import *

def test_ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt,timeout=1,verbose=False)
    if ping_result:
        return (ip)
    else:
        return

if __name__ == '__main__':
    result = test_ping('1.1.1.1')
    if result != None:
        print(result,'通!')
    else:
        print('不通!')
