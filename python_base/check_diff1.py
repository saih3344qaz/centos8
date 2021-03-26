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
        return run_config
    except Exception:
        return

def check_diff(host, username, password):
    beforce_md5 = ''
    while True:
        device_cfg = get_config(host,username,password)
        # 获取配置的MD5值
        m = hashlib.md5()
        m.update(device_cfg.encode())
        md5_value = m.hexdigest()
        print(md5_value)
        if not beforce_md5:
            beforce_md5 = md5_value
        elif beforce_md5 != md5_value:
            print('MD5 value changed!')
            break
        time.sleep(5)

if __name__ == '__main__':
    check_diff('192.168.128.145', 'admin', 'admin@123')
    # print(get_config('192.168.128.145', 'admin', 'admin@123'))