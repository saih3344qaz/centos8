#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import os

os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1', 'w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2', 'w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3', 'w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')

qytang_file_list = []
print('文件中包含"qytang"关键字的文件为:')
print('方案一：')
for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
        for file_line in open(file):
            if 'qytang' in file_line:
                qytang_file_list.append(file)
                print('\t', end='')
                print(file)
print('方案二：')
for root, dirs, files in os.walk(os.getcwd(),topdown=False):
    for file in files:
        for file_line in open(file):
            if 'qytang' in file_line:
                print('\t', end='')
                print(os.path.join(file))
os.chdir('..')
for root, dirs, files in os.walk('test',topdown=False):
    for name in files:
        os.remove(os.path.join(root,name))
    for name in dirs:
        os.rmdir(os.path.join(root,name))
os.removedirs('test')

