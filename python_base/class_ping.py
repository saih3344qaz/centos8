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
        for i in range(5):
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
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('+', end='', flush=True)
            else:
                print('?', end='', flush=True)
        print()


if __name__ == '__main__':
    ping = Qytping('192.168.128.1')
    total_len = 70


    def print_new(word, s='_'):
        print('{0}{1}{2}'.format(s * int((70 - len(word)) / 2), word, s * int((70 - len(word)) / 2)))


    print_new('print class')
    print(ping)
    print_new('ping one for sure reachable')
    ping.one()
    print_new('ping five')
    ping.ping()
    print_new('set payload lenth')
    ping.length = 200
    print(ping)
    ping.ping()
    print_new('set ping src ip address')
    ping.srcip = '192.168.128.20'
    print(ping)
    ping.ping()
    print_new('new class NewPing', '=')
    newping = Newping('172.16.200.99')
    newping.length = 300
    print(newping)
    newping.ping()
