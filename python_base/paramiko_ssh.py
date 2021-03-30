#!/usr/bin/python3
# -*- coding=utf-8 -*-

import paramiko
import re
from tools.test_decorator import write_to_file

@write_to_file('test.txt')
def test_ssh(ip, username, password,port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

def ssh_get_route(ip, username, password,port=22, cmd='route -n'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d.\d.\d.\d\s+[U][G]',stdout.read().decode())[0]
    return x

if __name__ == '__main__':
    # print(test_ssh('192.168.128.160','root','centos@123'))
    print(test_ssh('192.168.128.145', 'admin', 'admin@123',cmd='show run'))
    # print('网关为：')
    # print(ssh_get_route('192.168.128.160', 'root', 'centos@123'))