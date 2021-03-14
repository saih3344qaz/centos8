#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from netmiko import ConnectHandler
from tools.read_excel_todict import read_excel
from tools.test_decorator import write_to_file
import time
import os


@write_to_file('final_test.txt')
def netmiko_connect(device, ty, newpwd):
    print('\n正在连接:{0}'.format(device['host']))
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    if ty == 'fortinet':
        cmds = ['config system admin',
                'edit admin',
                'set password ' + newpwd,
                'end']
        for command in cmds:
            result = exe_command(net_connect, command)
            print(result)
        net_connect.disconnect()
    elif ty == 'h3c':
        cmds = ['config system admin',
                'edit admin',
                'set password ' + newpwd]
        for command in cmds:
            result = exe_command(net_connect, command)
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
        ip = device_list[device_name][0]
        print('=' * 60 + '\n开始PING: ' + ip)
        response = os.system('ping -c 5 ' + ip)
        time.sleep(2)
        if response == 0:
            try:
                if device_list[device_name][1] == 'fortinet':
                    device = FG(device_list[device_name][0], device_list[device_name][3])
                    netmiko_connect(device, ty='fortinet', newpwd=device_list[device_name][4])
                elif device_list[device_name][1] == 'h3c':
                    device = H3C(device_list[device_name][0], device_list[device_name][3])
                    netmiko_connect(device, ty='h3c', newpwd=device_list[device_name][4])
                    """
                    根据需求增加elif添加其它设备类型
                    """
                else:
                    print('未定义设备！')
                    pass
            except Exception as e:
                print('连接超时：', e)
                pass
        else:
            print(ip, 'Ping不通')
    print('配置任务已完成...\n')


if __name__ == '__main__':
    ssh_config_main('/home/sunyanlong/py_files/device_list.xlsx')
