#!/usr/bin/python3
# -*- coding=utf-8 -*-

import random
ip_1 = random.randrange(1 , 256)
ip_2 = random.randrange(0 , 256)
ip_3 = random.randrange(0 , 256)
ip_4 = random.randrange(1 , 256)
ipv4 = (f'{ip_1}.{ip_2}.{ip_3}.{ip_4}')

print(ipv4)
