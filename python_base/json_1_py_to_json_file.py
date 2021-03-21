#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import json
from source_db import qyt_teachers, qyt_courses  # 导入字典


print('把Python对象转换为JSON格式，并且写入文件')
with open('./json_dir/json_0_qyt_teachers.json', 'w', encoding='utf-8') as f:
    json.dump(qyt_teachers, f, ensure_ascii=False)  # 不要确认所有的字符都能够被ASCII表示, 因为有中文

with open('./json_dir/json_0_qyt_courses.json', 'w', encoding='utf-8') as f:
    json.dump(qyt_courses, f, ensure_ascii=False)

with open('./json_dir/json_0_true.json', 'w', encoding='utf-8') as f:
    json.dump({"qytang": True}, f, ensure_ascii=False)


qyt_f = open('./json_dir/json_0_qyt_teachers.json', 'r', encoding='utf-8')
new_dict = json.load(qyt_f)
print(new_dict)

