#!/usr/bin/env python3
# -*- coding=utf-8 -*-



import ftplib


def listftpfile(hostname, username='anonymous', password='1@2.net', remote_dir='/', verbose=True):
    if verbose:
        print('罗列一个目录中的所有文件或者目录，并不递归罗列！')
    remote = ftplib.FTP(hostname)  # 连接站点
    remote.encoding = 'GB18030'  # 使用中文编码
    remote.login(username, password)  # 输入用户名和密码进行登录
    remote.cwd(remote_dir)  # 进入特定目录
    lst = remote.nlst()  # 罗列目录内容，并且产生清单
    remote.quit()  # 退出会话
    return lst  # 返回目录内容的清单


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    print(listftpfile('10.1.1.200'))
