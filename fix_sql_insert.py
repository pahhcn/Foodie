#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
修复SQL文件中的INSERT语句，添加IGNORE避免重复键错误
"""
import re

# 读取SQL文件
with open('database/init_realistic_data.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换INSERT INTO为INSERT IGNORE INTO（仅对meishifenlei表）
content = re.sub(
    r"INSERT INTO `meishifenlei`",
    r"INSERT IGNORE INTO `meishifenlei`",
    content
)

# 写回文件
with open('database/init_realistic_data.sql', 'w', encoding='utf-8') as f:
    f.write(content)

print("SQL文件修复完成！")

