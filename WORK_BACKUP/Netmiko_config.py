#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from netmiko import ConnectHandler
from tools.read_excel_todict import read_excel
import paramiko
import time
# import threading
# from queue import Queue


def paramiko_connect(ip, username, password, verbose=True):
    # def paramiko_connect(device):
    ssh = paramiko.SSHClient()  # 创建SSH Client
    ssh.load_system_host_keys()  # 加载系统SSH密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)  # SSH连接
    # ssh.connect(**device)  # SSH连接
    chan = ssh.invoke_shell()  # 激活交互式shell
    time.sleep(1)
    for cmd in open('/home/sunyanlong/py_files/hs_commend.txt', 'r').readlines():  # 读取命令
        chan.send(cmd.encode())  # 执行命令，注意字串都需要编码为二进制字串
        time.sleep(2)  #
        chan.send(b'\n')
        x = chan.recv(1024).decode()  # 读取回显，有些回想可能过长，请把接收缓存调大
        if verbose:
            print(x)  # 打印回显
    chan.send(b'save\n')
    chan.send(b'y')
    chan.send(b'y')
    y = chan.recv(1024).decode()
    if verbose:
        print(y)
    print('\n配置完成......')
    chan.close()  # 退出交互式shell
    ssh.close()  # 退出ssh会话


def netmiko_connect(device, ty):
    print('\n正在连接:{0}'.format(device['host']))
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    if ty == 'fortinet':
        for i in open('/home/sunyanlong/py_files/fg_commend.txt', 'r'):
            cmd = i.replace('\n', ' ')
            result = exe_command(net_connect, cmd)
            print(result)
        net_connect.disconnect()
    elif ty == 'h3c':
        for i in open('/home/sunyanlong/py_files/h3c_commend.txt', 'r'):
            cmd = i.replace('\n', ' ')
            result = exe_command(net_connect, cmd)
            print(result)
        net_connect.disconnect()
        """
        根据需求增加elif添加其它设备命令
        """
    else:
        pass


def exe_command(net_connect, cmd):
    print('正在执行命令：', cmd)
    # send_command_timing 沿通道发送命令，返回输出（基于时序）。就是紧接着回显后边执行。
    result = net_connect.send_command_timing(cmd)
    # send_command 向下发送命令，返回输出（基于模式）。就是在回显的下一行刷入命令。
    # result = net_connect.send_command(cmd)
    return result


def FG(ip, password):
    fg = {
        'device_type': 'fortinet',
        'host': ip,
        'username': 'admin',
        'password': password,
    }
    return fg


def HS(ip, password):
    hs = {
        'host': ip,
        'port': '22',
        'username': 'hillstone',
        'password': password,
        'timeout': '5',
        'compress': 'True',
    }
    return hs


def H3C(ip, password):
    h3c = {
        'device_type': 'hp_comware',
        'host': ip,
        'username': 'root',
        'password': password,
    }
    return h3c


def ssh_config_main(ip_file):
    device_list = read_excel(ip_file)
    for device_name in device_list.keys():
        try:
            if device_list[device_name][1] == 'fortinet':
                device = FG(device_list[device_name][0], device_list[device_name][3])
                netmiko_connect(device, ty='fortinet')
            elif device_list[device_name][1] == 'h3c':
                device = H3C(device_list[device_name][0], device_list[device_name][3])
                netmiko_connect(device, ty='h3c')
            elif device_list[device_name][1] == 'hillstone':
                # device = HS(device_list[device_name][0], device_list[device_name][3])
                host = device_list[device_name][0]
                username = 'hillstone'
                password = device_list[device_name][3]
                print('\n正在连接:{0}'.format(device_list[device_name][0]))
                paramiko_connect(host, username, password)
                # paramiko_connect(device)
                """
                根据需求增加elif添加其它设备类型
                """
            else:
                print('未定义设备！')
                pass
        except Exception as e:
            print('连接超时：', e)
            pass
        time.sleep(1)
    print('配置任务已完成...\n')


if __name__ == '__main__':
    ssh_config_main('/home/sunyanlong/py_files/device_list.xlsx')
