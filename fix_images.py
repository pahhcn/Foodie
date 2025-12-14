#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

# 读取SQL文件
with open('database/init_realistic_data.sql', 'r', encoding='utf-8') as f:
    lines = f.readlines()

result = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # 修复店铺图片URL - 查找 (1001, ... 'https://picsum.photos/seed/1002/400/300'
    if re.search(r'\((\d+),.*?picsum\.photos/seed/1002', line):
        id_match = re.search(r'\((\d+),', line)
        if id_match:
            shop_id = id_match.group(1)
            line = line.replace('seed/1002', f'seed/{shop_id}')
    
    # 修复包含 CAST 的URL
    if "'https://picsum.photos/seed/' + CAST(id AS CHAR)" in line:
        # 查找这一行的ID
        id_match = re.search(r'\((\d+),', line)
        if id_match:
            item_id = id_match.group(1)
            # 确定尺寸
            if '/400/300' in line:
                line = re.sub(r"'https://picsum\.photos/seed/' \+ CAST\(id AS CHAR\) \+ '/400/300'", f"'https://picsum.photos/seed/{item_id}/400/300'", line)
            elif '/100/100' in line:
                line = re.sub(r"'https://picsum\.photos/seed/' \+ CAST\(id AS CHAR\) \+ '/100/100'", f"'https://picsum.photos/seed/{item_id}/100/100'", line)
            elif '/200/200' in line:
                line = re.sub(r"'https://picsum\.photos/seed/' \+ CAST\(id AS CHAR\) \+ '/200/200'", f"'https://picsum.photos/seed/{item_id}/200/200'", line)
            elif '/800/400' in line:
                line = re.sub(r"'https://picsum\.photos/seed/' \+ CAST\(id AS CHAR\) \+ '/800/400'", f"'https://picsum.photos/seed/{item_id}/800/400'", line)
            elif '/1200/400' in line:
                line = re.sub(r"'https://picsum\.photos/seed/' \+ CAST\(id AS CHAR\) \+ '/1200/400'", f"'https://picsum.photos/seed/{item_id}/1200/400'", line)
    
    # 修复 Unsplash URL
    if 'source.unsplash.com' in line:
        id_match = re.search(r'\((\d+),', line)
        if id_match:
            item_id = id_match.group(1)
            # 替换不同尺寸的URL
            line = re.sub(r"'https://source\.unsplash\.com/(\d+)x(\d+)/\?food(\d+)?'", f"'https://picsum.photos/seed/{item_id}/\\1/\\2'", line)
            line = re.sub(r"'https://source\.unsplash\.com/(\d+)x(\d+)/\?portrait(\d+)?'", f"'https://picsum.photos/seed/{item_id}/\\1/\\2'", line)
    
    # 修复店铺名称编码问题
    line = line.replace('鑰佸寳浜炸酱面馆', '老北京炸酱面馆')
    
    result.append(line)
    i += 1

# 写回文件
with open('database/init_realistic_data.sql', 'w', encoding='utf-8') as f:
    f.writelines(result)

print("图片URL修复完成！")
