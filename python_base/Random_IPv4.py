#!/usr/bin/python3
# -*- coding=utf-8 -*-

import random
ip_1 = random.randint(1 , 255)
ip_2 = random.randint(1 , 255)
ip_3 = random.randint(1 , 255)
ip_4 = random.randint(1 , 255)
random_ip = (f'{ip_1}.{ip_2}.{ip_3}.{ip_4}')

print(random_ip)
