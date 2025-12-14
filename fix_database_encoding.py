#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
修复数据库中的中文编码问题
通过直接UPDATE语句修复所有数据
"""
import pymysql

# 数据库连接配置
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'www111222azq',
    'database': 'foodie',
    'charset': 'utf8mb4'
}

# 美食名称映射
food_names = {
    3001: ('麻婆豆腐', '川菜', '/upload/麻婆豆腐.jpg'),
    3002: ('宫保鸡丁', '川菜', '/upload/宫保鸡丁.jpg'),
    3003: ('水煮鱼', '川菜', '/upload/水煮鱼.jpg'),
    3004: ('回锅肉', '川菜', '/upload/回锅肉.jpg'),
    3005: ('夫妻肺片', '川菜', '/upload/夫妻肺片.jpg'),
    3006: ('鱼香肉丝', '川菜', '/upload/鱼香肉丝.jpg'),
    3007: ('口水鸡', '川菜', '/upload/口水鸡.jpg'),
    3008: ('辣子鸡', '川菜', '/upload/辣子鸡.jpg'),
    3009: ('蒜泥白肉', '川菜', '/upload/蒜泥白肉.jpg'),
    3010: ('干煸豆角', '川菜', '/upload/干煸豆角.jpg'),
    3011: ('毛血旺', '川菜', '/upload/毛血旺.jpg'),
    3012: ('干锅牛蛙', '川菜', '/upload/干锅牛蛙.jpg'),
    3013: ('干锅虾', '川菜', '/upload/干锅虾.jpg'),
    3014: ('干锅排骨', '川菜', '/upload/干锅排骨.jpg'),
    3015: ('麻辣香锅', '川菜', '/upload/麻辣香锅.jpg'),
    3016: ('叉烧包', '粤菜', '/upload/叉烧包.jpg'),
    3017: ('虾饺', '粤菜', '/upload/虾饺.jpg'),
    3018: ('烧鹅', '粤菜', '/upload/烧鹅.jpg'),
    3019: ('白切鸡', '粤菜', '/upload/白切鸡.jpg'),
    3020: ('煲仔饭', '粤菜', '/upload/煲仔饭.jpg'),
    3021: ('肠粉', '粤菜', '/upload/肠粉.jpg'),
    3022: ('蒸排骨', '粤菜', '/upload/蒸排骨.jpg'),
    3023: ('凤爪', '粤菜', '/upload/凤爪.jpg'),
    3024: ('流沙包', '粤菜', '/upload/流沙包.jpg'),
    3025: ('叉烧', '粤菜', '/upload/叉烧.jpg'),
    3026: ('三文鱼刺身', '日料', '/upload/三文鱼刺身.jpg'),
    3027: ('寿司拼盘', '日料', '/upload/寿司拼盘.jpg'),
    3028: ('天妇罗', '日料', '/upload/天妇罗.jpg'),
    3029: ('日式拉面', '日料', '/upload/日式拉面.jpg'),
    3030: ('日式烤肉', '日料', '/upload/日式烤肉.jpg'),
    3031: ('鳗鱼饭', '日料', '/upload/鳗鱼饭.jpg'),
    3032: ('章鱼小丸子', '日料', '/upload/章鱼小丸子.jpg'),
    3033: ('日式炸鸡', '日料', '/upload/日式炸鸡.jpg'),
    3034: ('味增汤', '日料', '/upload/味增汤.jpg'),
    3035: ('日式茶碗蒸', '日料', '/upload/日式茶碗蒸.jpg'),
    3036: ('意大利面', '西餐', '/upload/意大利面.jpg'),
    3037: ('披萨', '西餐', '/upload/披萨.jpg'),
    3038: ('牛排', '西餐', '/upload/牛排.jpg'),
    3039: ('提拉米苏', '西餐', '/upload/提拉米苏.jpg'),
    3040: ('意式咖啡', '西餐', '/upload/意式咖啡.jpg'),
    3041: ('奶油蘑菇汤', '西餐', '/upload/奶油蘑菇汤.jpg'),
    3042: ('意式沙拉', '西餐', '/upload/意式沙拉.jpg'),
    3043: ('意式烩饭', '西餐', '/upload/意式烩饭.jpg'),
    3044: ('毛肚', '火锅', '/upload/毛肚.jpg'),
    3045: ('鸭肠', '火锅', '/upload/鸭肠.jpg'),
    3046: ('牛肉片', '火锅', '/upload/牛肉片.jpg'),
    3047: ('虾滑', '火锅', '/upload/虾滑.jpg'),
    3048: ('豆皮', '火锅', '/upload/豆皮.jpg'),
    3049: ('金针菇', '火锅', '/upload/金针菇.jpg'),
    3050: ('土豆片', '火锅', '/upload/土豆片.jpg'),
    3051: ('宽粉', '火锅', '/upload/宽粉.jpg'),
    3052: ('宫保鸡丁饭', '快餐', '/upload/宫保鸡丁饭.jpg'),
    3053: ('鱼香肉丝饭', '快餐', '/upload/鱼香肉丝饭.jpg'),
    3054: ('红烧肉饭', '快餐', '/upload/红烧肉饭.jpg'),
    3055: ('麻婆豆腐饭', '快餐', '/upload/麻婆豆腐饭.jpg'),
    3056: ('黄焖鸡米饭', '快餐', '/upload/黄焖鸡米饭.jpg'),
    3057: ('黄焖排骨', '快餐', '/upload/黄焖排骨.jpg'),
    3058: ('黄焖牛肉', '快餐', '/upload/黄焖牛肉.jpg'),
    3059: ('炸酱面', '小吃', '/upload/炸酱面.jpg'),
    3060: ('京酱肉丝', '小吃', '/upload/京酱肉丝.jpg'),
    3061: ('糖醋里脊', '小吃', '/upload/糖醋里脊.jpg'),
    3062: ('提拉米苏', '甜品', '/upload/提拉米苏.jpg'),
    3063: ('芝士蛋糕', '甜品', '/upload/芝士蛋糕.jpg'),
    3064: ('马卡龙', '甜品', '/upload/马卡龙.jpg'),
    3065: ('布丁', '甜品', '/upload/布丁.jpg'),
    3066: ('奶茶', '甜品', '/upload/奶茶.jpg'),
    3067: ('冰淇淋', '甜品', '/upload/冰淇淋.jpg'),
    3068: ('香草冰淇淋', '甜品', '/upload/香草冰淇淋.jpg'),
    3069: ('巧克力冰淇淋', '甜品', '/upload/巧克力冰淇淋.jpg'),
    3070: ('羊肉串', '烧烤', '/upload/羊肉串.jpg'),
    3071: ('烤鸡翅', '烧烤', '/upload/烤鸡翅.jpg'),
    3072: ('烤茄子', '烧烤', '/upload/烤茄子.jpg'),
    3073: ('烤韭菜', '烧烤', '/upload/烤韭菜.jpg'),
    3074: ('烤生蚝', '烧烤', '/upload/烤生蚝.jpg'),
    3075: ('烤羊排', '烧烤', '/upload/烤羊排.jpg'),
    3076: ('肉夹馍', '小吃', '/upload/肉夹馍.jpg'),
    3077: ('凉皮', '小吃', '/upload/凉皮.jpg'),
    3078: ('羊肉泡馍', '小吃', '/upload/羊肉泡馍.jpg'),
    3079: ('小笼包', '小吃', '/upload/小笼包.jpg'),
    3080: ('煎饼果子', '小吃', '/upload/煎饼果子.jpg'),
    3081: ('臭豆腐', '小吃', '/upload/臭豆腐.jpg'),
    3082: ('兰州拉面', '小吃', '/upload/兰州拉面.jpg'),
    3083: ('饺子', '小吃', '/upload/饺子.jpg'),
    3084: ('汤圆', '小吃', '/upload/汤圆.jpg'),
    3085: ('炒饭', '小吃', '/upload/炒饭.jpg'),
    3086: ('剁椒鱼头', '湘菜', '/upload/剁椒鱼头.jpg'),
    3087: ('口味虾', '湘菜', '/upload/口味虾.jpg'),
    3088: ('湘式小炒肉', '湘菜', '/upload/湘式小炒肉.jpg'),
    3089: ('糖油粑粑', '湘菜', '/upload/糖油粑粑.jpg'),
    3090: ('湘式臭豆腐', '湘菜', '/upload/湘式臭豆腐.jpg'),
    3091: ('糖醋鲤鱼', '鲁菜', '/upload/糖醋鲤鱼.jpg'),
    3092: ('九转大肠', '鲁菜', '/upload/九转大肠.jpg'),
    3093: ('德州扒鸡', '鲁菜', '/upload/德州扒鸡.jpg'),
    3094: ('葱烧海参', '鲁菜', '/upload/葱烧海参.jpg'),
    3095: ('爆炒腰花', '鲁菜', '/upload/爆炒腰花.jpg'),
}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    
    # 更新美食信息
    for food_id, (name, category, image) in food_names.items():
        sql = "UPDATE meishixinxi SET meishimingcheng=%s, meishifenlei=%s, tupian=%s WHERE id=%s"
        cursor.execute(sql, (name, category, image, food_id))
    
    conn.commit()
    print(f"成功更新 {len(food_names)} 条美食数据")
    
    # 验证
    cursor.execute("SELECT id, meishimingcheng, meishifenlei FROM meishixinxi WHERE id IN (3001, 3002, 3066)")
    results = cursor.fetchall()
    print("\n验证结果:")
    for row in results:
        print(f"ID: {row[0]}, 名称: {row[1]}, 分类: {row[2]}")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"错误: {e}")

