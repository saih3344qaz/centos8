#!/usr/bin/env python3
# -*- coding=utf-8 -*-

list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

print('方案一：')
for x in list1:
    for y in list2:
        if x == y:
            print(str(x) + ' in List1 and List2')
            break
    else:
        print(str(x) + ' only in List1')

print('方案二：')

def test_for():
    for x in list1:
        for y in list2:
            if x == y:
                print(str(x) + ' in List1 and List2')
                break
        else:
            print(str(x) + ' only in List1')
test_for()