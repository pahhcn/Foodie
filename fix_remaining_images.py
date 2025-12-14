#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
修复SQL文件中剩余的图片路径
"""
import os
import re

sql_file = 'database/init_realistic_data.sql'
image_dir = 'foodie-backend/src/main/resources/static/upload'

# 读取SQL文件
with open(sql_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 获取所有图片文件映射（文件名不含扩展名 -> 完整文件名）
image_files = {}
if os.path.exists(image_dir):
    for f in os.listdir(image_dir):
        if f.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')):
            name_without_ext = os.path.splitext(f)[0]
            image_files[name_without_ext] = f

print(f"找到 {len(image_files)} 个图片文件")

# 读取SQL文件，逐行处理
lines = content.split('\n')
updated_lines = []
updated_count = 0

for line in lines:
    # 查找包含 picsum.photos 的行
    if 'picsum.photos' in line:
        # 尝试匹配各种模式并替换
        
        # 模式1: 美食信息 (meishixinxi) - 格式: (id, ..., '美食名称', ..., 'https://picsum.photos/...')
        # 提取美食名称
        food_match = re.search(r"\((\d+),\s*[^,]+,\s*'([^']+)',\s*'[^']+',\s*'[^']+',\s*'[^']+',\s*'[^']+',\s*'[^']+',\s*)'https://picsum\.photos/seed/\d+/\d+/\d+'", line)
        if food_match:
            food_name = food_match.group(2)
            if food_name in image_files:
                img_file = image_files[food_name]
                line = re.sub(r"'https://picsum\.photos/seed/\d+/\d+/\d+'", f"'/foodie/upload/{img_file}'", line)
                updated_count += 1
                print(f"替换美食: {food_name} -> {img_file}")
        
        # 模式2: 店铺信息 (meishidian) - 格式: (id, ..., '店铺名称', 'https://picsum.photos/...')
        shop_match = re.search(r"\((\d+),\s*[^,]+,\s*'[^']+',\s*'[^']+',\s*'([^']+)',\s*)'https://picsum\.photos/seed/\d+/\d+/\d+'", line)
        if shop_match:
            shop_name = shop_match.group(2)
            # 处理"老北京炸酱面馆" -> "老北京杂酱面馆"
            if shop_name == '老北京炸酱面馆':
                shop_name = '老北京杂酱面馆'
            if shop_name in image_files:
                img_file = image_files[shop_name]
                line = re.sub(r"'https://picsum\.photos/seed/\d+/\d+/\d+'", f"'/foodie/upload/{img_file}'", line)
                updated_count += 1
                print(f"替换店铺: {shop_name} -> {img_file}")
        
        # 模式3: 用户信息 (yonghu) - 格式: (id, ..., '用户名称', ..., 'https://picsum.photos/...')
        user_match = re.search(r"\((\d+),\s*[^,]+,\s*'[^']+',\s*'[^']+',\s*'([^']+)',\s*'[^']+',\s*'[^']+',\s*)'https://picsum\.photos/seed/\d+/\d+/\d+'", line)
        if user_match:
            user_name = user_match.group(2)
            if user_name in image_files:
                img_file = image_files[user_name]
                line = re.sub(r"'https://picsum\.photos/seed/\d+/\d+/\d+'", f"'/foodie/upload/{img_file}'", line)
                updated_count += 1
                print(f"替换用户: {user_name} -> {img_file}")
        
        # 模式4: 新闻信息 (news) - 格式: (id, ..., '标题', '简介', 'https://picsum.photos/...')
        news_match = re.search(r"\((\d+),\s*[^,]+,\s*'([^']+)',\s*'[^']+',\s*)'https://picsum\.photos/seed/\d+/\d+/\d+'", line)
        if news_match:
            news_title = news_match.group(2)
            if news_title in image_files:
                img_file = image_files[news_title]
                line = re.sub(r"'https://picsum\.photos/seed/\d+/\d+/\d+'", f"'/foodie/upload/{img_file}'", line)
                updated_count += 1
                print(f"替换新闻: {news_title} -> {img_file}")
        
        # 模式5: 收藏信息 (storeup) - 格式: (id, ..., '名称', 'https://picsum.photos/...')
        storeup_match = re.search(r"\((\d+),\s*[^,]+,\s*'[^']+',\s*'[^']+',\s*'[^']+',\s*'([^']+)',\s*)'https://picsum\.photos/seed/\d+/\d+/\d+'", line)
        if storeup_match:
            storeup_name = storeup_match.group(2)
            if storeup_name in image_files:
                img_file = image_files[storeup_name]
                line = re.sub(r"'https://picsum\.photos/seed/\d+/\d+/\d+'", f"'/foodie/upload/{img_file}'", line)
                updated_count += 1
                print(f"替换收藏: {storeup_name} -> {img_file}")
        
        # 模式6: 配置信息 (config) - 格式: (id, 'picture1', 'https://picsum.photos/...')
        config_match = re.search(r"\((\d+),\s*'picture(\d+)',\s*)'https://picsum\.photos/seed/\d+/\d+/\d+'", line)
        if config_match:
            pic_num = config_match.group(2)
            img_name = f'美食轮播图{pic_num}'
            if img_name in image_files:
                img_file = image_files[img_name]
                line = re.sub(r"'https://picsum\.photos/seed/\d+/\d+/\d+'", f"'/foodie/upload/{img_file}'", line)
                updated_count += 1
                print(f"替换轮播图: {img_name} -> {img_file}")
        
        # 模式7: 评价信息 (meishipingjia) - 格式: (id, ..., '美食名称', ..., 'https://picsum.photos/...')
        review_match = re.search(r"\((\d+),\s*[^,]+,\s*'[^']+',\s*'[^']+',\s*'([^']+)',\s*'[^']+',\s*'[^']+',\s*)'https://picsum\.photos/seed/\d+/\d+/\d+'", line)
        if review_match:
            review_food = review_match.group(2)
            if review_food in image_files:
                img_file = image_files[review_food]
                line = re.sub(r"'https://picsum\.photos/seed/\d+/\d+/\d+'", f"'/foodie/upload/{img_file}'", line)
                updated_count += 1
                print(f"替换评价: {review_food} -> {img_file}")
    
    updated_lines.append(line)

# 写回文件
with open(sql_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(updated_lines))

print(f"\n完成！共替换 {updated_count} 个图片URL")

