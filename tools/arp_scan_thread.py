#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
import ipaddress
from multiprocessing.pool import ThreadPool
from arp_request import arp_request
from time_decorator import run_time


@run_time()
def scapy_arp_scan(network, ifname):
    net = ipaddress.ip_network(network)  # 产生网络对象
    ip_list = [str(ip_add) for ip_add in net]  # 把网络中的IP放入ip_list
    pool = ThreadPool(processes=100)  # 创建多进程的进程池（并发为100）
    result = [pool.apply_async(arp_request, args=(i, ifname)) for i in ip_list]  # 把线程放入result清单
    pool.close()  # 关闭pool，不再加入新的线程
    pool.join()  # 等待每一个线程结束
    scan_dict = {}  # ARP扫描结果的字典, 键为IP, 值为MAC
    for r in result:
        if r.get()[1]:  # 如果没有获得MAC，就continue进入下一次循环
            scan_dict[r.get()[0]] = r.get()[1]
    return scan_dict


if __name__ == '__main__':
    # Windows Linux均可使用
    for ip, mac in scapy_arp_scan("10.1.1.0/24", 'ens33').items():
        print('ip地址:'+ip+'是活动的,他的MAC地址是:'+mac)
