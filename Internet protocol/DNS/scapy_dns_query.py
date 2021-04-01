#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
from kamene.all import *
import re


def dns_query(dns_name):
    # rd = 1 期望递归
    # qd 问题部分, DNSQR DNS请求记录
    # qname 询问的域名, qtype 请求类型为A
    query_pkt = IP(dst="114.114.114.114") / UDP() / DNS(rd=1, qd=DNSQR(qname=dns_name, qtype="A"))
    # query_pkt.show()
    dns_result = sr1(query_pkt, verbose=False)
    dns_result.show()
    layer = 1

    while True:  # 不太确定DNSRR到底有几组！！！
        try:
            # 如果an(DNS资源记录部分)的类型为1(A)
            # print(dns_result.getlayer(DNS).fields['an'][layer].fields)
            if dns_result.getlayer(DNS).fields['an'][layer].fields['type'] == 1:  # 找到A
                # 获取ip地址信息,an(DNS资源记录部分)的rdata字段
                dns_result_ip = dns_result.getlayer(DNS).fields['an'][layer].fields['rdata']
                print('域名: %-18s 对应的IP地址: %s' % (dns_name, dns_result_ip))  # 找到IP地址并打印
            layer += 1
        except Exception:  # 如果超出范围就跳出循环
            break


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    dns_query("adminmall.creditcard.cmbc.com.cn")

