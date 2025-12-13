#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

# 读取SQL文件
with open('database/init_realistic_data.sql', 'r', encoding='utf-8') as f:
    lines = f.readlines()

result = []
for i, line in enumerate(lines):
    # 修复店铺名称编码问题 - 查找并替换乱码
    if '鑰佸寳浜' in line or '老北' in line:
        # 使用正则表达式匹配并替换
        line = re.sub(r"'[^']*老北[^']*炸酱面[^']*'", "'老北京炸酱面馆'", line)
        line = re.sub(r"'鑰佸寳浜[^']*'", "'老北京炸酱面馆'", line)
    
    # 确保图片URL格式正确
    # picsum.photos/400/300?random=数字 格式
    if 'picsum.photos' in line:
        # 修复 ?random=数字/尺寸 格式
        line = re.sub(r'picsum\.photos/(\d+)/(\d+)\?random=(\d+)/\d+/\d+', r'picsum.photos/\1/\2?random=\3', line)
        # 确保格式为 picsum.photos/400/300?random=数字
        line = re.sub(r'picsum\.photos/id/(\d+)/(\d+)/(\d+)', r'picsum.photos/\2/\3?random=\1', line)
    
    result.append(line)

# 写回文件
with open('database/init_realistic_data.sql', 'w', encoding='utf-8') as f:
    f.writelines(result)

print("SQL文件编码和URL格式修复完成！")

