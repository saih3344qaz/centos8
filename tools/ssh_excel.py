#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import read_excel_return_dict
from read_excel_return_dict import excel_parser_return_list
from write_excel_openpyxl import excel_write
from write_excel_openpyxl import excel_write_list
from ssh_client_netmiko import netmiko_show_cred, netmiko_config_cred
import re


def excel_user_to_ios(ip, username, password, excelfile):
    # 读取excel信息，返回字典！
    user_list = excel_parser_return_list(excelfile)
    # 产生配置命令
    cmds = []
    for user_dict in user_list:
        cmd = f"username {user_dict.get('username')} " \
              f"privilege {user_dict.get('privilege')} " \
              f"password {user_dict.get('password')}"
        cmds.append(cmd)
    # ssh登录路由器，配置用户信息
    netmiko_config_cred(ip, username, password, cmds, verbose=False)


def excel_ios_user_to_excel(ip, username, password, excelfile):
    # 执行'sh run | in username'并提取结果
    show_run = netmiko_show_cred(ip, username, password, 'sh run | in username')
    # 把结果通过'\r\n'分离，产生清单
    show_run_list = show_run.split('\n')
    user_list = []
    for x in show_run_list:
        # 如果格式为username admin privilege 15 password 0 cisco，提取用户名，密码和级别
        if re.match(r'username (\w+) privilege (\d+) password \w (\w+)', x):
            re_result = re.match(r'username (\w+) privilege (\d+) password \w (\w+)', x).groups()
            user_list.append({'username': re_result[0],
                              'privilege': int(re_result[1]),
                              'password': re_result[2],
                              })
        # 如果格式为username passuser password 0 12345，提取用户和密码，级别为1级
        elif re.match(r'username (\w+) password \w (\w+)', x):
            re_result = re.match(r'username (\w+) password \w (\w+)', x).groups()
            user_list.append({'username': re_result[0],
                              'privilege': 1,
                              'password': re_result[1],
                              })
    # 把字典的用户名，密码和级别信息，写入Excel
    # sheel_name为IP地址
    excel_write_list(file=excelfile, sheel_name=ip, write_list=user_list)


if __name__ == '__main__':
    excel_user_to_ios('10.1.1.253', 'admin', 'Cisc0123', './excel_file/read_accounts.xlsx')
    # excel_ios_user_to_excel('10.1.1.253', 'admin', 'Cisc0123', './excel_file/write_iosuser_new.xlsx')

