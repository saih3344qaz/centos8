#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re
from jinja2 import Template
tem_path = '/home/python/.virtualenvs/py_env_lab1/jinja2_template/'


def netconf_if_ip(interface, address, mask):
    interface_name, interface_no = re.match('([a-zA-Z]*)([0-9].*)', interface).groups()
    with open(tem_path + 'interface_ip.xml') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(if_type=interface_name,
                                              if_no=interface_no,
                                              ip_address=address,
                                              net_mask=mask)
    return netconf_payload


def netconf_if_no_shutdown(interface, status=True):
    with open(tem_path + 'interface_no_shutdown.xml') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(interface_name=interface, interface_status='true' if status else 'false')
    return netconf_payload


def netconf_ospf_router_id(process_id, router_id):
    with open(tem_path + 'ospf_router_id.xml') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(process_id=process_id, router_id=router_id)
    return netconf_payload


def netconf_ospf_network(process_id, ip, mask, area):
    with open(tem_path + 'ospf_network.xml') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(process_id=process_id, network=ip, wild_mask=mask, area=area)
    return netconf_payload


def netconf_monitor_cpu(monitor_type):
    with open(tem_path + 'monitor_cpu.xml') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(monitor_type_use=monitor_type)
    return netconf_payload


if __name__ == '__main__':
    import lxml.etree as ET
    if_ip_str = netconf_if_ip('Loopback0', '61.128.1.1', '255.255.255.0')
    print(if_ip_str)
    # 模板替换结果就是一个字符串
    print(type(if_ip_str))
    parser = ET.XMLParser(recover=True)
    # 从字符串fromstring, 转换为XML
    tree = ET.ElementTree(ET.fromstring(if_ip_str, parser=parser))
    # 已经转换XML对象
    print(type(tree))
    # 写入文件
    with open("./jinja2_xml/if_ip_xml.xml", "wb") as f:
        f.write(ET.tostring(tree))

