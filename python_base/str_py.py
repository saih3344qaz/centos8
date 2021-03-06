#!/usr/bin/python3
# -*- coding=utf-8 -*-

department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomp'
depart2_m = 'sunyanlong'
COURSE_FEES_SEC = 45678.123456
COURSE_FEES_Python = 1234.3456

line1 = (f'Department1 name:{department1:<12} Manager:{depart1_m:<12} COURSE_FEES:{COURSE_FEES_SEC:<12} The End!')
line2 = (f'Department2 name:{department2:<12} Manager:{depart2_m:<12} COURSE_FEES:{COURSE_FEES_Python:<12} The End!')

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
