#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import gevent
from gevent import monkey
monkey.patch_all()
import requests


def get_body(i):
    print("start", i)
    result = requests.get("http://www.baidu.com")
    print("end", i)
    return result


tasks = []

for i in range(3):
    tasks.append(gevent.spawn(get_body, i))

# ip_list = []
# for ip in ip_list:
#     tasks.append(gevent.spawn(qyt_ssh, (ip, 'show run')))
# tasks = [gevent.spawn(get_body, i) for i in range(3)]

all_result = gevent.joinall(tasks)
for x in all_result:
    print(x.get())
    # print(x.get().text)

