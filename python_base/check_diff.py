#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from tools.ssh_client_netmiko import netmiko_show_cred
from tools.compare_diff_conf import diff_txt
import re
import hashlib
import time


def get_config(host, username, password):
    try:
        # 获取完整的running-configuration
        device_config_raw = netmiko_show_cred(host, username, password, 'show run')
        # print(device_config_raw)
        split_result = re.split(r'\nhostname \S+[\s\S]+\n', device_config_raw)
        run_config = device_config_raw.replace(split_result[0], '').strip()
        # 获取配置的MD5值
        m = hashlib.md5()
        m.update(run_config.encode())
        md5_value = m.hexdigest()

        # 获取配置的MD5值
        # md5 = re.findall(r'=\s(\w+)',netmiko_show_cred(host, username, password, 'verify /md5 system:running-config'))
        # md5_value = ''.join(md5)
        # 返回ip, 配置, md5值
        return host, run_config, md5_value
    except Exception:
        return

def check_diff(host, username, password):
    beforce_md5 = get_config(host,username,password)[2]
    beforce_config = get_config(host,username,password)[1]
    while True:
        time.sleep(3)
        new_md5 = get_config(host,username,password)[2]
        if beforce_md5 == new_md5:
            print(new_md5)
            continue
        else:
            print(new_md5)
            print('MD5 value changed')
            new_config = get_config(host,username,password)[1]
            print(diff_txt(beforce_config,new_config))
            break


if __name__ == '__main__':
    # print(check_diff('192.168.128.145', 'admin', 'admin@123'))
    print(get_config('192.168.128.145', 'admin', 'admin@123'))