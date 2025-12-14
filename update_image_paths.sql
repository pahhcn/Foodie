-- 更新数据库中的图片路径
-- 使用UTF-8编码执行此脚本

USE foodie;
SET NAMES utf8mb4;

-- 更新美食信息表中的图片路径
UPDATE meishixinxi SET tupian = CONCAT('/upload/', meishimingcheng, '.jpg') WHERE id BETWEEN 3001 AND 3095;

-- 更新店铺表中的图片路径
UPDATE meishidian SET zhaopian = CONCAT('/upload/', dianpumingcheng, '.jpg') WHERE id BETWEEN 1001 AND 1025;

-- 更新用户表中的头像路径（如果有）
UPDATE yonghu SET touxiang = CONCAT('/upload/', yonghuxingming, '.jpg') WHERE id > 2000 AND id <= 2035;

-- 更新新闻表中的图片路径
UPDATE news SET picture = CONCAT('/upload/', title, '.jpg') WHERE id BETWEEN 2001 AND 2003;

-- 更新配置表中的轮播图路径
UPDATE config SET value = CONCAT('/upload/picture', SUBSTRING(name, -1), '.jpg') WHERE name LIKE 'picture%';

