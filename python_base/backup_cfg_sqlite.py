#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sqlite3
import pg8000
from ssh_client_netmiko import netmiko_show_cred
import hashlib
import re
import os


def create_configdb():
    conn = sqlite3.connect('configdb.sqlite')
    # conn = pg8000.connect(host='192.168.128.160', user='postgres', password='postgres@123', database='postgres')
    cursor = conn.cursor()
    cursor.execute("create table config_md5(ip varchar (40), config varchar (99999), md5 varchar (999))")
    conn.commit()
    conn.close()

device_list = ['192.168.128.145','192.168.128.131','192.168.128.144']
username = 'admin'
password = 'admin@123'

def get_md5_config(host, username, password):
    try:
        # 获取完整的running-configuration
        device_config_raw = netmiko_show_cred(host, username, password, 'show run')
        split_result = re.split(r'\nhostname \S+[\s\S]+\n', device_config_raw)
        run_config = device_config_raw.replace(split_result[0], '').strip()
        # 计算MD5值
        m = hashlib.md5()
        m.update(run_config.encode())
        md5_value = m.hexdigest()

        # 返回ip, 配置, md5值
        return host, run_config, md5_value
    except Exception as e:
        print('%stErrorn %s' % (host, e))

def wirte_config_md5_to_db():
    conn = sqlite3.connect('configdb.sqlite')
    # conn = pg8000.connect(host='192.168.128.160', user='postgres', password='postgres@123', database='postgres')
    cursor = conn.cursor()
    for device in device_list:
        config_and_md5 = get_md5_config(device, username, password)
        cursor.execute("select * from config_md5 where ip =?", (device,))
        md5_results = cursor.fetchall()
        # print(md5_results)
        if not md5_results:
            cursor.execute("insert into config_md5(ip,config,md5) values (?,?,?)",
                           (device, config_and_md5[1], config_and_md5[2]))

            conn.commit()
        else:
            if config_and_md5[2] != md5_results[0][2]:
                cursor.execute("update config_md5 set config=?,md5=? where ip = ?",
                               (config_and_md5[1], config_and_md5[2], device))

                conn.commit()
            else:
                pass
    cursor.execute("select * from config_md5")
    all_results = cursor.fetchall()
    for x in all_results:
        print(x[0],x[2])

    conn.commit()


if __name__ == '__main__':
    if os.path.exists('configdb.sqlite'):
        os.remove('configdb.sqlite')
    create_configdb()
    # print(get_md5_config('192.168.128.145','admin','admin@123'))
    wirte_config_md5_to_db()
