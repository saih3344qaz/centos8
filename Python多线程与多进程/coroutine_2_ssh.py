#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from ssh_client import ssh_client_no_async

import gevent
from gevent import monkey

monkey.patch_all()


def get_ssh_result(i):
    print("start", i)
    result = ssh_client_no_async('localhost', 'root', 'centos@123', 'ls / -an', asy_id=i)
    print("end", i)
    return result


tasks = [gevent.spawn(get_ssh_result, i) for i in range(3)]
all_result = gevent.joinall(tasks)
for x in all_result:
    print(x.get())

    # print(x.get().text)

