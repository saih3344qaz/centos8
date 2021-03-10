#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import pg8000
conn  = pg8000.connect(host='192.168.128.161', user='sunyanlongdbuser', password='sunyanlongdbuser',database='sunyanlongdb') #创建数据库
cursor = conn.cursor()  #执行数据库操作
cursor.execute("create table test1(t1 int, t2 varchar(40))")  #创建表
cursor.execute("insert into test1 (t1,t2) values (11,'welcome to beijing')") #插入条目
cursor.execute("insert into test1 (t1,t2) values (12,'welcome to beijing')") #插入条目
cursor.execute("select * from test1")
yourresults = cursor.fetchall()  #获取执行结果
print(yourresults)
# for i in yourresults:
#     print(i)
#
# cursor.execute("dorp table test1")  #删除数据库表

conn.commit()

