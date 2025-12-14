#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新SQL文件中的图片路径为本地路径
"""
import re

# 读取SQL文件
with open('database/init_realistic_data.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义映射关系：数据库中的文字描述 -> 图片文件名
# 店铺图片映射
shop_mapping = {
    '老北京炸酱面馆': '老北京炸酱面馆.jpg',
    '川味小厨': '川味小厨.jpg',
    '粤式茶餐厅': '粤式茶餐厅.jpg',
    '日式料理屋': '日式料理屋.jpg',
    '韩式烤肉店': '韩式烤肉店.jpg',
    '意式西餐厅': '意式西餐厅.jpg',
    '重庆老火锅': '重庆老火锅.jpg',
    '东北烧烤王': '东北烧烤王.jpg',
    '甜蜜时光甜品屋': '甜蜜时光甜品屋.jpg',
    '快客快餐': '快客快餐.jpg',
    '湘味轩': '湘味轩.jpg',
    '鲁菜世家': '鲁菜世家.jpg',
    '街头小吃铺': '街头小吃铺.jpg',
    '海鲜大排档': '海鲜大排档.jpg',
    '新疆羊肉串': '新疆羊肉串.jpg',
    '手工饺子馆': '手工饺子馆.jpg',
    '麻辣香锅': '麻辣香锅.jpg',
    '黄焖鸡米饭': '黄焖鸡米饭.jpg',
    '兰州拉面': '兰州拉面.jpg',
    '小笼包专卖店': '小笼包专卖店.jpg',
    '炒饭专家': '炒饭专家.jpg',
    '汤圆甜品店': '汤圆甜品店.jpg',
    '煎饼果子摊': '煎饼果子摊.jpg',
    '臭豆腐摊': '臭豆腐摊.jpg',
    '冰淇淋工坊': '冰淇淋工坊.jpg',
}

# 美食图片映射（90道菜品）
food_mapping = {
    '麻婆豆腐': '麻婆豆腐.jpg',
    '宫保鸡丁': '宫保鸡丁.jpg',
    '水煮鱼': '水煮鱼.jpg',
    '回锅肉': '回锅肉.jpg',
    '夫妻肺片': '夫妻肺片.jpg',
    '鱼香肉丝': '鱼香肉丝.jpg',
    '口水鸡': '口水鸡.jpg',
    '辣子鸡': '辣子鸡.jpg',
    '蒜泥白肉': '蒜泥白肉.jpg',
    '干煸豆角': '干煸豆角.jpg',
    '毛血旺': '毛血旺.jpg',
    '干锅牛蛙': '干锅牛蛙.jpg',
    '干锅虾': '干锅虾.jpg',
    '干锅排骨': '干锅排骨.jpg',
    '麻辣香锅': '麻辣香锅.jpg',
    '叉烧包': '叉烧包.jpg',
    '虾饺': '虾饺.jpg',
    '烧鹅': '烧鹅.jpg',
    '白切鸡': '白切鸡.jpg',
    '煲仔饭': '煲仔饭.jpg',
    '肠粉': '肠粉.jpg',
    '蒸排骨': '蒸排骨.jpg',
    '凤爪': '凤爪.jpg',
    '流沙包': '流沙包.jpg',
    '叉烧': '叉烧.jpg',
    '三文鱼刺身': '三文鱼刺身.jpg',
    '寿司拼盘': '寿司拼盘.jpg',
    '天妇罗': '天妇罗.jpg',
    '日式拉面': '日式拉面.jpg',
    '日式烤肉': '日式烤肉.jpg',
    '鳗鱼饭': '鳗鱼饭.jpg',
    '章鱼小丸子': '章鱼小丸子.jpg',
    '日式炸鸡': '日式炸鸡.jpg',
    '味增汤': '味增汤.jpg',
    '日式茶碗蒸': '日式茶碗蒸.jpg',
    '意大利面': '意大利面.jpg',
    '披萨': '披萨.jpg',
    '牛排': '牛排.jpg',
    '提拉米苏': '提拉米苏.jpg',
    '意式咖啡': '意式咖啡.jpg',
    '奶油蘑菇汤': '奶油蘑菇汤.jpg',
    '意式沙拉': '意式沙拉.jpg',
    '意式烩饭': '意式烩饭.jpg',
    '毛肚': '毛肚.jpg',
    '鸭肠': '鸭肠.jpg',
    '牛肉片': '牛肉片.jpg',
    '虾滑': '虾滑.jpg',
    '豆皮': '豆皮.jpg',
    '金针菇': '金针菇.jpg',
    '土豆片': '土豆片.jpg',
    '宽粉': '宽粉.jpg',
    '宫保鸡丁饭': '宫保鸡丁饭.jpg',
    '鱼香肉丝饭': '鱼香肉丝饭.jpg',
    '红烧肉饭': '红烧肉饭.jpg',
    '麻婆豆腐饭': '麻婆豆腐饭.jpg',
    '黄焖鸡米饭': '黄焖鸡米饭.jpg',
    '黄焖排骨': '黄焖排骨.jpg',
    '黄焖牛肉': '黄焖牛肉.jpg',
    '炸酱面': '炸酱面.jpg',
    '京酱肉丝': '京酱肉丝.jpg',
    '糖醋里脊': '糖醋里脊.jpg',
    '芝士蛋糕': '芝士蛋糕.jpg',
    '马卡龙': '马卡龙.jpg',
    '布丁': '布丁.jpg',
    '奶茶': '奶茶.jpg',
    '冰淇淋': '冰淇淋.jpg',
    '香草冰淇淋': '香草冰淇淋.jpg',
    '巧克力冰淇淋': '巧克力冰淇淋.jpg',
    '羊肉串': '羊肉串.jpg',
    '烤鸡翅': '烤鸡翅.jpg',
    '烤茄子': '烤茄子.jpg',
    '烤韭菜': '烤韭菜.jpg',
    '烤生蚝': '烤生蚝.jpg',
    '烤羊排': '烤羊排.jpg',
    '肉夹馍': '肉夹馍.jpg',
    '凉皮': '凉皮.jpg',
    '羊肉泡馍': '羊肉泡馍.jpg',
    '小笼包': '小笼包.jpg',
    '煎饼果子': '煎饼果子.jpg',
    '臭豆腐': '臭豆腐.jpg',
    '饺子': '饺子.jpg',
    '汤圆': '汤圆.jpg',
    '炒饭': '炒饭.jpg',
    '剁椒鱼头': '剁椒鱼头.jpg',
    '口味虾': '口味虾.jpg',
    '湘式小炒肉': '湘式小炒肉.jpg',
    '糖油粑粑': '糖油粑粑.jpg',
    '湘式臭豆腐': '湘式臭豆腐.jpg',
    '糖醋鲤鱼': '糖醋鲤鱼.jpg',
    '九转大肠': '九转大肠.jpg',
    '德州扒鸡': '德州扒鸡.jpg',
    '葱烧海参': '葱烧海参.jpg',
    '爆炒腰花': '爆炒腰花.jpg',
}

# 用户头像映射（35个用户）
user_mapping = {
    '张三': '张三.jpg',
    '李四': '李四.jpg',
    '王五': '王五.jpg',
    '赵六': '赵六.jpg',
    '孙七': '孙七.jpg',
    '周八': '周八.jpg',
    '吴九': '吴九.jpg',
    '郑十': '郑十.jpg',
    '王十一': '王十一.jpg',
    '李十二': '李十二.jpg',
    '张十三': '张十三.jpg',
    '李十四': '李十四.jpg',
    '王十五': '王十五.jpg',
    '赵十六': '赵十六.jpg',
    '孙十七': '孙十七.jpg',
    '周十八': '周十八.jpg',
    '吴十九': '吴十九.jpg',
    '郑二十': '郑二十.jpg',
    '王二十一': '王二十一.jpg',
    '李二十二': '李二十二.jpg',
    '张二十三': '张二十三.jpg',
    '李二十四': '李二十四.jpg',
    '王二十五': '王二十五.jpg',
    '赵二十六': '赵二十六.jpg',
    '孙二十七': '孙二十七.jpg',
    '周二十八': '周二十八.jpg',
    '吴二十九': '吴二十九.jpg',
    '郑三十': '郑三十.jpg',
    '王三十一': '王三十一.jpg',
    '李三十二': '李三十二.jpg',
    '张三十三': '张三十三.jpg',
    '李三十四': '李三十四.jpg',
    '王三十五': '王三十五.jpg',
    '赵三十六': '赵三十六.jpg',
    '孙三十七': '孙三十七.jpg',
}

# 新闻图片映射
news_mapping = {
    '春季养生美食推荐': '春季养生美食推荐.jpg',
    '川菜文化历史': '川菜文化历史.jpg',
    '如何挑选新鲜食材': '如何挑选新鲜食材.jpg',
}

# 轮播图映射
banner_mapping = {
    'picture1': '美食轮播图1.jpg',
    'picture2': '美食轮播图2.jpg',
    'picture3': '美食轮播图3.jpg',
    'picture4': '美食轮播图4.jpg',
    'picture5': '美食轮播图5.jpg',
}

# 替换店铺图片路径
for shop_name, filename in shop_mapping.items():
    # 匹配店铺INSERT语句中的图片URL
    pattern = rf"('{re.escape(shop_name)}',\s*)'https://[^']+'"
    replacement = rf"\1'/upload/{filename}'"
    content = re.sub(pattern, replacement, content)

# 替换美食图片路径
for food_name, filename in food_mapping.items():
    # 匹配美食INSERT语句中的图片URL
    pattern = rf"('{re.escape(food_name)}',\s*'[^']+',\s*'[^']+',\s*'[^']+',\s*'[^']+',\s*'[^']+',\s*)'https://[^']+'"
    replacement = rf"\1'/upload/{filename}'"
    content = re.sub(pattern, replacement, content)

# 替换用户头像路径
for user_name, filename in user_mapping.items():
    # 匹配用户INSERT语句中的头像URL
    pattern = rf"('{re.escape(user_name)}',\s*'[^']+',\s*'[^']+',\s*)'https://[^']+'"
    replacement = rf"\1'/upload/{filename}'"
    content = re.sub(pattern, replacement, content)

# 替换新闻图片路径
for news_title, filename in news_mapping.items():
    # 匹配新闻INSERT语句中的图片URL
    pattern = rf"('{re.escape(news_title)}',\s*'[^']+',\s*)'https://[^']+'"
    replacement = rf"\1'/upload/{filename}'"
    content = re.sub(pattern, replacement, content)

# 替换轮播图路径
for banner_name, filename in banner_mapping.items():
    # 匹配config表中的轮播图URL
    pattern = rf"\({banner_name.replace('picture', '')},\s*'{banner_name}',\s*'https://[^']+'"
    replacement = rf"({banner_name.replace('picture', '')}, '{banner_name}', '/upload/{filename}'"
    content = re.sub(pattern, replacement, content)

# 替换评价图片路径（有图片的评价）
evaluation_mapping = {
    '宫保鸡丁': '宫保鸡丁.jpg',
    '虾饺': '虾饺.jpg',
    '毛肚': '毛肚.jpg',
}
for food_name, filename in evaluation_mapping.items():
    # 匹配评价INSERT语句中的图片URL
    pattern = rf"('{re.escape(food_name)}',\s*'[^']+',\s*'[^']+',\s*)'https://[^']+'"
    replacement = rf"\1'/upload/{filename}'"
    content = re.sub(pattern, replacement, content)

# 替换收藏图片路径
collection_mapping = {
    '麻婆豆腐': '麻婆豆腐.jpg',
    '叉烧包': '叉烧包.jpg',
    '三文鱼刺身': '三文鱼刺身.jpg',
    '牛排': '牛排.jpg',
    '毛肚': '毛肚.jpg',
}
for food_name, filename in collection_mapping.items():
    # 匹配收藏INSERT语句中的图片URL
    pattern = rf"('{re.escape(food_name)}',\s*)'https://[^']+'"
    replacement = rf"\1'/upload/{filename}'"
    content = re.sub(pattern, replacement, content)

# 写回文件
with open('database/init_realistic_data.sql', 'w', encoding='utf-8') as f:
    f.write(content)

print("图片路径更新完成！")
