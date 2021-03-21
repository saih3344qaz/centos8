#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sqlite3
conn = sqlite3.connect('qytangdb.sqlite')
cursor = conn.cursor()
cursor.execute("create table test1(t1 int, t2 varchar(40))")
cursor.execute("insert into test1 (t1,t2) values (11, 'welcome to qytang')")
cursor.execute("insert into test1 (t1,t2) values (12, 'welcome to python')")
cursor.execute("select * from test1")
yourresults = cursor.fetchall()
for i in yourresults:
    print(i)

conn.commit()

