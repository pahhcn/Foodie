#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
替换SQL文件中所有picsum.photos URL为本地图片路径
"""
import re

# 读取SQL文件
with open('database/init_realistic_data.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义ID到文件名的映射
id_to_filename = {}

# 店铺ID映射 (1001-1025)
shop_names = ['老北京炸酱面馆', '川味小厨', '粤式茶餐厅', '日式料理屋', '韩式烤肉店', 
              '意式西餐厅', '重庆老火锅', '东北烧烤王', '甜蜜时光甜品屋', '快客快餐',
              '湘味轩', '鲁菜世家', '街头小吃铺', '海鲜大排档', '新疆羊肉串',
              '手工饺子馆', '麻辣香锅', '黄焖鸡米饭', '兰州拉面', '小笼包专卖店',
              '炒饭专家', '汤圆甜品店', '煎饼果子摊', '臭豆腐摊', '冰淇淋工坊']
for i, name in enumerate(shop_names, 1001):
    id_to_filename[i] = f"{name}.jpg"

# 用户ID映射 (2001-2035)
user_names = ['张三', '李四', '王五', '赵六', '孙七', '周八', '吴九', '郑十', '王十一', '李十二',
              '张十三', '李十四', '王十五', '赵十六', '孙十七', '周十八', '吴十九', '郑二十', 
              '王二十一', '李二十二', '张二十三', '李二十四', '王二十五', '赵二十六', '孙二十七',
              '周二十八', '吴二十九', '郑三十', '王三十一', '李三十二', '张三十三', '李三十四', 
              '王三十五', '赵三十六', '孙三十七']
for i, name in enumerate(user_names, 2001):
    id_to_filename[i] = f"{name}.jpg"

# 美食ID映射 (3001-3095)
food_names = ['麻婆豆腐', '宫保鸡丁', '水煮鱼', '回锅肉', '夫妻肺片', '鱼香肉丝', '口水鸡', 
              '辣子鸡', '蒜泥白肉', '干煸豆角', '毛血旺', '干锅牛蛙', '干锅虾', '干锅排骨', 
              '麻辣香锅', '叉烧包', '虾饺', '烧鹅', '白切鸡', '煲仔饭', '肠粉', '蒸排骨', 
              '凤爪', '流沙包', '叉烧', '三文鱼刺身', '寿司拼盘', '天妇罗', '日式拉面', 
              '日式烤肉', '鳗鱼饭', '章鱼小丸子', '日式炸鸡', '味增汤', '日式茶碗蒸', 
              '意大利面', '披萨', '牛排', '提拉米苏', '意式咖啡', '奶油蘑菇汤', '意式沙拉', 
              '意式烩饭', '毛肚', '鸭肠', '牛肉片', '虾滑', '豆皮', '金针菇', '土豆片', 
              '宽粉', '宫保鸡丁饭', '鱼香肉丝饭', '红烧肉饭', '麻婆豆腐饭', '黄焖鸡米饭', 
              '黄焖排骨', '黄焖牛肉', '炸酱面', '京酱肉丝', '糖醋里脊', '提拉米苏', '芝士蛋糕', 
              '马卡龙', '布丁', '奶茶', '冰淇淋', '香草冰淇淋', '巧克力冰淇淋', '羊肉串', 
              '烤鸡翅', '烤茄子', '烤韭菜', '烤生蚝', '烤羊排', '肉夹馍', '凉皮', '羊肉泡馍', 
              '小笼包', '煎饼果子', '臭豆腐', '兰州拉面', '饺子', '汤圆', '炒饭', '剁椒鱼头', 
              '口味虾', '湘式小炒肉', '糖油粑粑', '湘式臭豆腐', '糖醋鲤鱼', '九转大肠', 
              '德州扒鸡', '葱烧海参', '爆炒腰花']
for i, name in enumerate(food_names, 3001):
    id_to_filename[i] = f"{name}.jpg"

# 评价ID映射 (4002, 4005, 4008)
eval_foods = {4002: '宫保鸡丁', 4005: '虾饺', 4008: '毛肚'}
for eval_id, food_name in eval_foods.items():
    id_to_filename[eval_id] = f"{food_name}.jpg"

# 收藏ID映射 (7001-7005)
coll_foods = {7001: '麻婆豆腐', 7002: '叉烧包', 7003: '三文鱼刺身', 7004: '牛排', 7005: '毛肚'}
for coll_id, food_name in coll_foods.items():
    id_to_filename[coll_id] = f"{food_name}.jpg"

# 新闻ID映射 (6001-6003)
news_titles = {6001: '春季养生美食推荐', 6002: '川菜文化历史', 6003: '如何挑选新鲜食材'}
for news_id, title in news_titles.items():
    id_to_filename[news_id] = f"{title}.jpg"

# 轮播图ID映射 (1-5)
banner_files = {1: '美食轮播图1.jpg', 2: '美食轮播图2.jpg', 3: '美食轮播图3.jpg', 
                4: '美食轮播图4.jpg', 5: '美食轮播图5.jpg'}
for banner_id, filename in banner_files.items():
    id_to_filename[banner_id] = filename

# 替换所有 picsum.photos URL
def replace_url(match):
    url = match.group(0)
    # 提取ID
    id_match = re.search(r'/seed/(\d+)/', url)
    if id_match:
        img_id = int(id_match.group(1))
        if img_id in id_to_filename:
            return f"'/upload/{id_to_filename[img_id]}'"
    return url

# 替换所有匹配的URL
content = re.sub(r"'https://picsum\.photos/seed/\d+/100/100'", replace_url, content)

# 写回文件
with open('database/init_realistic_data.sql', 'w', encoding='utf-8') as f:
    f.write(content)

print("所有图片路径更新完成！")

