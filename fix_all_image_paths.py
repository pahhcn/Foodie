#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新SQL文件中所有图片路径为本地路径
"""
import re

# 读取SQL文件
with open('database/init_realistic_data.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换所有 picsum.photos URL 为本地路径
# 根据ID和名称映射

# 1. 替换店铺图片 (meishidian) - ID 1001-1025
shop_names = {
    1001: '老北京炸酱面馆',
    1002: '川味小厨',
    1003: '粤式茶餐厅',
    1004: '日式料理屋',
    1005: '韩式烤肉店',
    1006: '意式西餐厅',
    1007: '重庆老火锅',
    1008: '东北烧烤王',
    1009: '甜蜜时光甜品屋',
    1010: '快客快餐',
    1011: '湘味轩',
    1012: '鲁菜世家',
    1013: '街头小吃铺',
    1014: '海鲜大排档',
    1015: '新疆羊肉串',
    1016: '手工饺子馆',
    1017: '麻辣香锅',
    1018: '黄焖鸡米饭',
    1019: '兰州拉面',
    1020: '小笼包专卖店',
    1021: '炒饭专家',
    1022: '汤圆甜品店',
    1023: '煎饼果子摊',
    1024: '臭豆腐摊',
    1025: '冰淇淋工坊',
}

# 2. 替换美食图片 (meishixinxi) - ID 3001-3095
food_names = {
    3001: '麻婆豆腐', 3002: '宫保鸡丁', 3003: '水煮鱼', 3004: '回锅肉', 3005: '夫妻肺片',
    3006: '鱼香肉丝', 3007: '口水鸡', 3008: '辣子鸡', 3009: '蒜泥白肉', 3010: '干煸豆角',
    3011: '毛血旺', 3012: '干锅牛蛙', 3013: '干锅虾', 3014: '干锅排骨', 3015: '麻辣香锅',
    3016: '叉烧包', 3017: '虾饺', 3018: '烧鹅', 3019: '白切鸡', 3020: '煲仔饭',
    3021: '肠粉', 3022: '蒸排骨', 3023: '凤爪', 3024: '流沙包', 3025: '叉烧',
    3026: '三文鱼刺身', 3027: '寿司拼盘', 3028: '天妇罗', 3029: '日式拉面', 3030: '日式烤肉',
    3031: '鳗鱼饭', 3032: '章鱼小丸子', 3033: '日式炸鸡', 3034: '味增汤', 3035: '日式茶碗蒸',
    3036: '意大利面', 3037: '披萨', 3038: '牛排', 3039: '提拉米苏', 3040: '意式咖啡',
    3041: '奶油蘑菇汤', 3042: '意式沙拉', 3043: '意式烩饭',
    3044: '毛肚', 3045: '鸭肠', 3046: '牛肉片', 3047: '虾滑', 3048: '豆皮',
    3049: '金针菇', 3050: '土豆片', 3051: '宽粉',
    3052: '宫保鸡丁饭', 3053: '鱼香肉丝饭', 3054: '红烧肉饭', 3055: '麻婆豆腐饭',
    3056: '黄焖鸡米饭', 3057: '黄焖排骨', 3058: '黄焖牛肉',
    3059: '炸酱面', 3060: '京酱肉丝', 3061: '糖醋里脊',
    3062: '提拉米苏', 3063: '芝士蛋糕', 3064: '马卡龙', 3065: '布丁',
    3066: '奶茶', 3067: '冰淇淋', 3068: '香草冰淇淋', 3069: '巧克力冰淇淋',
    3070: '羊肉串', 3071: '烤鸡翅', 3072: '烤茄子', 3073: '烤韭菜', 3074: '烤生蚝', 3075: '烤羊排',
    3076: '肉夹馍', 3077: '凉皮', 3078: '羊肉泡馍', 3079: '小笼包', 3080: '煎饼果子',
    3081: '臭豆腐', 3082: '兰州拉面', 3083: '饺子', 3084: '汤圆', 3085: '炒饭',
    3086: '剁椒鱼头', 3087: '口味虾', 3088: '湘式小炒肉', 3089: '糖油粑粑', 3090: '湘式臭豆腐',
    3091: '糖醋鲤鱼', 3092: '九转大肠', 3093: '德州扒鸡', 3094: '葱烧海参', 3095: '爆炒腰花',
}

# 3. 替换用户头像 (yonghu) - ID 2001-2035
user_names = {
    2001: '张三', 2002: '李四', 2003: '王五', 2004: '赵六', 2005: '孙七',
    2006: '周八', 2007: '吴九', 2008: '郑十', 2009: '王十一', 2010: '李十二',
    2011: '张十三', 2012: '李十四', 2013: '王十五', 2014: '赵十六', 2015: '孙十七',
    2016: '周十八', 2017: '吴十九', 2018: '郑二十', 2019: '王二十一', 2020: '李二十二',
    2021: '张二十三', 2022: '李二十四', 2023: '王二十五', 2024: '赵二十六', 2025: '孙二十七',
    2026: '周二十八', 2027: '吴二十九', 2028: '郑三十', 2029: '王三十一', 2030: '李三十二',
    2031: '张三十三', 2032: '李三十四', 2033: '王三十五', 2034: '赵三十六', 2035: '孙三十七',
}

# 4. 替换新闻图片 (news) - ID 6001-6003
news_titles = {
    6001: '春季养生美食推荐',
    6002: '川菜文化历史',
    6003: '如何挑选新鲜食材',
}

# 5. 替换轮播图 (config) - ID 1-5
banner_files = {
    1: '美食轮播图1.jpg',
    2: '美食轮播图2.jpg',
    3: '美食轮播图3.jpg',
    4: '美食轮播图4.jpg',
    5: '美食轮播图5.jpg',
}

# 替换店铺图片
for shop_id, shop_name in shop_names.items():
    pattern = rf"\({shop_id},[^)]+'https://picsum\.photos[^']+'"
    replacement = rf"({shop_id}, DATE_SUB(NOW(), INTERVAL 180 DAY), 'laobeijing', '123456', '{shop_name}', '/upload/{shop_name}.jpg'"
    # 更精确的匹配
    pattern = rf"\({shop_id},[^)]+'{shop_name}',\s*'https://picsum\.photos[^']+'"
    replacement = rf"({shop_id}, DATE_SUB(NOW(), INTERVAL 180 DAY), 'laobeijing', '123456', '{shop_name}', '/upload/{shop_name}.jpg'"
    content = re.sub(pattern, lambda m: m.group(0).replace(f"https://picsum.photos/seed/{shop_id}/100/100", f"/upload/{shop_name}.jpg"), content)

# 替换美食图片
for food_id, food_name in food_names.items():
    pattern = rf"\({food_id},[^)]+'{food_name}'[^)]+'https://picsum\.photos[^']+'"
    content = re.sub(pattern, lambda m: m.group(0).replace(f"https://picsum.photos/seed/{food_id}/100/100", f"/upload/{food_name}.jpg"), content)

# 替换用户头像
for user_id, user_name in user_names.items():
    pattern = rf"\({user_id},[^)]+'{user_name}'[^)]+'https://picsum\.photos[^']+'"
    content = re.sub(pattern, lambda m: m.group(0).replace(f"https://picsum.photos/seed/{user_id}/100/100", f"/upload/{user_name}.jpg"), content)

# 替换新闻图片
for news_id, news_title in news_titles.items():
    pattern = rf"\({news_id},[^)]+'{news_title}'[^)]+'https://picsum\.photos[^']+'"
    content = re.sub(pattern, lambda m: m.group(0).replace(f"https://picsum.photos/seed/{news_id}/100/100", f"/upload/{news_title}.jpg"), content)

# 替换轮播图
for banner_id, banner_file in banner_files.items():
    pattern = rf"\({banner_id},\s*'picture{banner_id}',\s*'https://picsum\.photos[^']+'"
    content = re.sub(pattern, lambda m: m.group(0).replace(f"https://picsum.photos/seed/{banner_id}/100/100", f"/upload/{banner_file}"), content)

# 替换评价图片（有图片的评价）
eval_foods = {
    4002: '宫保鸡丁',
    4005: '虾饺',
    4008: '毛肚',
}
for eval_id, food_name in eval_foods.items():
    pattern = rf"\({eval_id},[^)]+'{food_name}'[^)]+'https://picsum\.photos[^']+'"
    content = re.sub(pattern, lambda m: m.group(0).replace(f"https://picsum.photos/seed/{eval_id}/100/100", f"/upload/{food_name}.jpg"), content)

# 替换收藏图片
collection_foods = {
    7001: '麻婆豆腐',
    7002: '叉烧包',
    7003: '三文鱼刺身',
    7004: '牛排',
    7005: '毛肚',
}
for coll_id, food_name in collection_foods.items():
    pattern = rf"\({coll_id},[^)]+'{food_name}',\s*'https://picsum\.photos[^']+'"
    content = re.sub(pattern, lambda m: m.group(0).replace(f"https://picsum.photos/seed/{coll_id}/100/100", f"/upload/{food_name}.jpg"), content)

# 通用替换：替换所有剩余的 picsum.photos URL
content = re.sub(r"'https://picsum\.photos[^']+'", "'/upload/default.jpg'", content)

# 写回文件
with open('database/init_realistic_data.sql', 'w', encoding='utf-8') as f:
    f.write(content)

print("所有图片路径更新完成！")

