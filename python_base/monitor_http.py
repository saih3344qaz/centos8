#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import os
import time
while True:
    result = os.popen("netstat -tulnp").read()
    result_list = result.split('\n')
    result_list = result_list[2:-1]
    # print(result_list)
    for x in result_list:
        if x.split()[3].split(':')[-1] == '80':
            print('HTTP（TCP/80）服务已经被打开')
            break
    else:
        print('等待一秒重新开始监控！')
        time.sleep(1)
        continue
    break

