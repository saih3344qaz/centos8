#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import logging

from kamene.layers.inet import ICMP, IP
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *


class Qytping:
    def __init__(self, ip):
        self.ip = ip
        self.srcip = None
        self.length = 100
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)

    def src(self, srcip):
        self.srcip = srcip
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)

    def size(self, length):
        self.length = length
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)

    def one(self):
        result = sr1(self.pkt, timeout=1, verbose=False)
        if result:
            print(self.ip, '可达！')
        else:
            print(self.ip, '不可达！')

    def ping(self):
        for i in range(100):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)
        print()

    def __str__(self):
        if not self.srcip:
            return '<dstip: {0}, size: {1}>'.format(self.ip, self.length)
        else:
            return '<srcip: {0}, dstip: {1}, size: {2}>'.format(self.srcip, self.ip, self.length)


class Newping(Qytping):
    def ping(self):
        for i in range(100):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('+', end='', flush=True)
            else:
                print('?', end='', flush=True)
        print()


if __name__ == '__main__':
    ping = Qytping('192.168.128.145')
    ping2 = Newping('www.baidu.com')
    # ping.size(200)
    # ping.src('192.168.128.160')
    # ping.ping()
    ping2.ping()

