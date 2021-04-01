#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import logging
import ipaddress
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from multiprocessing.pool import ThreadPool
from ping_one import scapy_ping_one
from kamene.all import *
from tools.sort_ip import sort_ip
from tools.time_decorator import run_time


@run_time()
def scapy_ping_scan(network):
    net = ipaddress.ip_network(network)
    ip_list = [str(ip_add) for ip_add in net]  # 把网络(net)中的IP放入ip_list

    pool = ThreadPool(processes=100)  # 创建多进程的进程池（并发为10）

    # 方案一
    # result = []
    # for i in ip_list:
    #         result.append(pool.apply_async(scapy_ping_one,args=i))

    # 方案二
    result = pool.map(scapy_ping_one, ip_list)  # 关联函数与参数，并且提取结果到result

    pool.close()  # 关闭pool，不在加入新的进程
    pool.join()  # 等待每一个进程结束

    scan_list = []  # 扫描结果IP地址的清单
    # print(result)
    for ip_address, ok in result:
        if ok:  # 如果ok为True
            scan_list.append(ip_address)  # 把IP地址放入scan_list清单里边
    return sort_ip(scan_list)  # 排序并且打印清单


if __name__ == '__main__':
    # Windows Linux均可使用
    for ip in scapy_ping_scan("172.16.66.0/24"):
        print(str(ip))


