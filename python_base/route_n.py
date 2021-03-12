#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import os
import re

route_n_result = os.popen('route -n').read()
route_n_result_re = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d.\d.\d.\d\s+[U][G]',route_n_result)[0]
print('网关为：',route_n_result_re)
