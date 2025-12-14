#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

# 读取SQL文件
with open('database/init_realistic_data.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复店铺名称编码问题
content = content.replace('鑰佸寳浜炸酱面馆', '老北京炸酱面馆')
content = content.replace('老北', '老北京')
content = re.sub(r'老北[^\']*炸酱面[^\']*', '老北京炸酱面馆', content)

# 确保所有URL格式正确
# 修复 ?random=数字/尺寸 格式为 ?random=数字
content = re.sub(r'\?random=(\d+)/\d+/\d+', r'?random=\1', content)

# 写回文件
with open('database/init_realistic_data.sql', 'w', encoding='utf-8') as f:
    f.write(content)

print("SQL文件修复完成！")


