#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import paramiko
import time


def paramiko_ssh_multi_cmd(ip, username, password, cmd_list, enable='',wait_time=2, verbose=True):
    ssh = paramiko.SSHClient()  # 创建SSH Client
    ssh.load_system_host_keys()  # 加载系统SSH密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)  # SSH连接
    chan = ssh.invoke_shell()  # 激活交互式shell
    time.sleep(1)
    x = chan.recv(2048).decode()
    if enable and '>' in x:
        chan.send('enable'.encode())     #发送命令
        chan.send(b'\n')     #回车
        time.sleep(wait_time)
        chan.send(enable.encode())      # 发送命令
        chan.send(b'\n')  # 回车
        time.sleep(wait_time)
    elif not enable and '>' in x:
        print('需要配置enable密码')
        return
    elif enable and '#' in x:
        chan.send('configure'.encode())     #发送命令
        chan.send(b'\n')

    for cmd in cmd_list:  # 读取命令
        chan.send(cmd.encode())  # 执行命令，注意字串都需要编码为二进制字串
        chan.send(b'\n')  # 一定要注意输入回车
        time.sleep(2)  # 由于有些回显可能过长，所以可以考虑等待更长一些时间
        x = chan.recv(40960).decode()  # 读取回显，有些回想可能过长，请把接收缓存调大
        if verbose:
            print(x)  # 打印回显
    chan.send(b'save\n')
    chan.send(b'y')
    chan.send(b'y')
    x = chan.recv(40960).decode()  # 读取回显，有些回想可能过长，请把接收缓存调大
    print(x)  # 打印回显

    chan.close()  # 退出交互式shell
    ssh.close()  # 退出ssh会话


if __name__ == '__main__':
    # paramiko_ssh_multi_cmd('192.168.128.145', 'admin', 'admin@123',
    #                        ['terminal length 0', 'show ver', 'config ter', 'router ospf 1','network 0.0.0.0 0.0.0.0 a 0'],
    #                        enable='admin@123',wait_time=2, verbose=True)
    paramiko_ssh_multi_cmd('192.168.128.129', 'hillstone', 'hillstone',
                           ['address 10.1.1.1/32', 'ip 10.1.1.1/32', 'exit'],
                           enable='admin@123',wait_time=2, verbose=True)