#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import datetime
now = datetime.datetime.now()

def save_time():
    fiveDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 5))
    otherStyleTime = now.strftime("%Y-%m-%d_%H-%M-%S")
    time_file_name = 'save_fivedayago_time_' + otherStyleTime + '.txt'
    time_file = open(time_file_name,'w')
    time_file.write(str(fiveDayAgo))
    time_file.close()

if __name__ == '__main__':
    save_time()