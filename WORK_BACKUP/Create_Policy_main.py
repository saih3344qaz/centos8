#!/usr/bin/python3.9
# -*- coding=utf-8 -*-
# 本脚由孙艳龙编写，用于Python学习及网络自动化脚本，如有问题或技术交流请与本人联系！
# mail:sunyanlong@bris.cn

from Read_Policy_File_FG import read_excel as readfile
from Read_Policy_File_FG import create_sadd as fg_src
from Read_Policy_File_FG import create_dadd as fg_dst
from Read_Policy_File_FG import create_service as fg_ser
from Read_Policy_File_FG import create_policy as fg_policy
from Read_Policy_File_Hillstone import create_sadd as ss_src
from Read_Policy_File_Hillstone import create_dadd as ss_dst
from Read_Policy_File_Hillstone import create_service as ss_ser
from Read_Policy_File_Hillstone import create_policy as ss_policy
import time
import os
from netmiko import ConnectHandler

now = time.strftime(
    '%Y-%m-%d_%H:%M:%S',
    time.localtime(
        time.time()))  # 定义时间格式，创建脚本具体时间用到
date = time.strftime('%Y-%m-%d', time.localtime(time.time()))


def policy_main(input_excel, output_file):  # 创建主程序策略模板
    inputexcel = readfile(input_excel)
    for device_type in inputexcel.values():
        try:
            if device_type[0] == 'FG':
                # policy_cmd = ['生成策略时间：' + str(now) + '\n' + '=' * 50]
                policy_cmd = []
                src = fg_src(input_excel)
                dst = fg_dst(input_excel)
                ser = fg_ser(input_excel)
                policy = fg_policy(input_excel)
                policy_cmd.extend((src, dst, ser, policy))
                policy_cmd.append('end')
                policy_cmds = '\n'.join(policy_cmd)
                # print('\n', '=' * 10, 'FG策略开始执行', '=' * 10)
                # policy_output = open(
                #     str(output_file) +
                #     '_' +
                #     now +
                #     '.txt',
                #     'w')
                policy_output = open(
                    str(output_file) +
                    '.txt',
                    'w')
                policy_output.write(policy_cmds)
                # print('\n执行完成，请到输出目录下查看脚本......\n')
                policy_output.close()
                return policy_cmds
                # print(policy_cmds)
            elif device_type[0] == 'hillstone':
                # policy_cmd = ['生成策略时间：' + str(now) + '\n' + '=' * 50]
                policy_cmd = []
                src = ss_src(input_excel)
                dst = ss_dst(input_excel)
                ser = ss_ser(input_excel)
                policy = ss_policy(input_excel)
                policy_cmd.extend((src, dst, ser, policy))
                policy_cmds = '\n'.join(policy_cmd)
                # print('\n', '=' * 10, 'Hillstone策略开始执行', '=' * 10)
                policy_output = open(
                    str(output_file) +
                    '_' +
                    now +
                    '.txt',
                    'w')
                policy_output.write(policy_cmds)
                # print('\n执行完成，请到输出目录下查看脚本......\n')
                policy_output.close()
                return policy_cmds
            else:
                print('未定义设备')
        except Exception as e:
            print('文件格式有误：', e)
            pass


def netmiko_connect(device, file):
    print('\n正在连接:{0}'.format(device['host']))
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    for i in open('/home/python/py_files/fw_policy/' + date + '/' + file + '.txt', 'r'):
        cmd = i.replace('\n', ' ')
        # result = exe_command(net_connect, cmd)
        result = net_connect.send_config_set(cmd)
        print(result)
    net_connect.disconnect()
    # return result


def main(input_name, output_filename):
    try:
        os.mkdir('/home/python/py_files/fw_policy/' + date)  # 创建脚本输出日期目录
    except Exception:
        pass
    input_dir = '/home/python/py_files/fw_policy/'
    input_excelfile = input_dir + '/' + input_name
    output_dir = '/home/python/py_files/fw_policy/' + str(date) + '/'
    output_file = output_dir + '/' + output_filename
    policy_main(input_excelfile, output_file)  # 调用创建策略主程序


if __name__ == "__main__":
    main('policy_tmp_FG.xlsx', 'ID-PORTOPEN-20210324-00001')
    fg = {
        'device_type': 'fortinet',
        'host': '192.168.128.137',
        'username': 'admin',
        'password': 'admin123',
    }

    netmiko_connect(fg, file='ID-PORTOPEN-20210324-00001')
