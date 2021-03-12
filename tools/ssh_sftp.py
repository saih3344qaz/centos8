#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import paramiko
import os
import sys
import time


def ssh_sftp_put(ip, user, password, local_file, remote_file, port=22):
    ssh = paramiko.SSHClient()  # 创建SSH Client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
    ssh.connect(ip, port, user, password)  # 连接服务器
    sftp = ssh.open_sftp()  # 打开sftp
    sftp.put(local_file, remote_file)  # 上传本地文件到服务器


def ssh_sftp_get(ip, user, password, remote_file, local_file, port=22):
    ssh = paramiko.SSHClient()  # 创建SSH Client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
    ssh.connect(ip, port, user, password)  # 连接服务器
    sftp = ssh.open_sftp()  # 打开sftp
    sftp.get(remote_file, local_file)  # 下载服务器文件到本地


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    # ssh_sftp_put('10.1.1.80', 'root', 'Cisc0123', './file_dir/upload_file.txt', 'upload_file.txt', port=22)
    ssh_sftp_get('10.1.1.80', 'root', 'Cisc0123', 'upload_file.txt', './file_dir/download_file.txt', port=22)
