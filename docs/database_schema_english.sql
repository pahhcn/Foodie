-- =============================================
-- 食客在线 - 数据库表结构 (英文版)
-- Database: foodie_online
-- Date: 2025-11-06
-- Description: 英文命名的数据库表结构
-- =============================================

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- =============================================
-- 1. 管理员表 (Admins)
-- =============================================
DROP TABLE IF EXISTS `admins`;
CREATE TABLE `admins` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `username` VARCHAR(100) NOT NULL COMMENT '管理员账号',
  `password` VARCHAR(100) NOT NULL COMMENT '密码',
  `role` VARCHAR(100) DEFAULT '管理员' COMMENT '角色',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='管理员表';

-- =============================================
-- 2. 用户表 (Users)
-- =============================================
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `username` VARCHAR(200) NOT NULL COMMENT '用户账号',
  `password` VARCHAR(200) NOT NULL COMMENT '密码',
  `full_name` VARCHAR(200) DEFAULT NULL COMMENT '用户姓名',
  `gender` VARCHAR(200) DEFAULT NULL COMMENT '性别',
  `age` INT DEFAULT NULL COMMENT '年龄',
  `avatar` VARCHAR(255) DEFAULT NULL COMMENT '头像URL',
  `phone` VARCHAR(200) DEFAULT NULL COMMENT '手机号',
  `delivery_address` VARCHAR(500) DEFAULT NULL COMMENT '配送地址',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_username` (`username`),
  KEY `idx_phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

-- =============================================
-- 3. 餐厅表 (Restaurants)
-- =============================================
DROP TABLE IF EXISTS `restaurants`;
CREATE TABLE `restaurants` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `account` VARCHAR(200) NOT NULL COMMENT '店铺账号',
  `password` VARCHAR(200) NOT NULL COMMENT '密码',
  `name` VARCHAR(200) DEFAULT NULL COMMENT '店铺名称',
  `photo` VARCHAR(255) DEFAULT NULL COMMENT '照片URL',
  `contact_phone` VARCHAR(200) DEFAULT NULL COMMENT '联系电话',
  `description` LONGTEXT DEFAULT NULL COMMENT '店铺介绍',
  `address` VARCHAR(500) DEFAULT NULL COMMENT '店铺地址',
  `signature_dishes` VARCHAR(500) DEFAULT NULL COMMENT '招牌美食',
  `contact_person` VARCHAR(200) DEFAULT NULL COMMENT '联系人',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_account` (`account`),
  KEY `idx_name` (`name`),
  KEY `idx_contact_phone` (`contact_phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='餐厅表';

-- =============================================
-- 4. 美食分类表 (Food Categories)
-- =============================================
DROP TABLE IF EXISTS `food_categories`;
CREATE TABLE `food_categories` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `category_name` VARCHAR(200) NOT NULL COMMENT '分类名称',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_category_name` (`category_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='美食分类表';

-- =============================================
-- 5. 美食信息表 (Foods)
-- =============================================
DROP TABLE IF EXISTS `foods`;
CREATE TABLE `foods` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `food_name` VARCHAR(200) NOT NULL COMMENT '美食名称',
  `category_id` BIGINT DEFAULT NULL COMMENT '分类ID',
  `category_name` VARCHAR(200) DEFAULT NULL COMMENT '分类名称',
  `restaurant_id` BIGINT DEFAULT NULL COMMENT '餐厅ID',
  `restaurant_account` VARCHAR(200) DEFAULT NULL COMMENT '店铺账号',
  `restaurant_name` VARCHAR(200) DEFAULT NULL COMMENT '店铺名称',
  `contact_phone` VARCHAR(200) DEFAULT NULL COMMENT '联系电话',
  `image` VARCHAR(255) DEFAULT NULL COMMENT '图片URL',
  `flavor` VARCHAR(200) DEFAULT NULL COMMENT '口味',
  `features` VARCHAR(500) DEFAULT NULL COMMENT '特色',
  `price` DECIMAL(10,2) NOT NULL DEFAULT 0.00 COMMENT '价格',
  `details` LONGTEXT DEFAULT NULL COMMENT '详情',
  `last_click_time` DATETIME DEFAULT NULL COMMENT '最近点击时间',
  `click_count` INT DEFAULT 0 COMMENT '点击次数',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `idx_food_name` (`food_name`),
  KEY `idx_category_id` (`category_id`),
  KEY `idx_restaurant_id` (`restaurant_id`),
  KEY `idx_click_count` (`click_count`),
  CONSTRAINT `fk_foods_category` FOREIGN KEY (`category_id`) REFERENCES `food_categories` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_foods_restaurant` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='美食信息表';

-- =============================================
-- 6. 订单表 (Orders)
-- =============================================
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `order_number` VARCHAR(200) NOT NULL COMMENT '订单编号',
  `food_id` BIGINT DEFAULT NULL COMMENT '美食ID',
  `food_name` VARCHAR(200) DEFAULT NULL COMMENT '美食名称',
  `restaurant_id` BIGINT DEFAULT NULL COMMENT '餐厅ID',
  `restaurant_account` VARCHAR(200) DEFAULT NULL COMMENT '店铺账号',
  `restaurant_name` VARCHAR(200) DEFAULT NULL COMMENT '店铺名称',
  `contact_phone` VARCHAR(200) DEFAULT NULL COMMENT '联系电话',
  `price` DECIMAL(10,2) NOT NULL COMMENT '单价',
  `quantity` INT NOT NULL DEFAULT 1 COMMENT '购买数量',
  `total_price` DECIMAL(10,2) NOT NULL COMMENT '总价格',
  `user_id` BIGINT DEFAULT NULL COMMENT '用户ID',
  `user_account` VARCHAR(200) DEFAULT NULL COMMENT '用户账号',
  `user_name` VARCHAR(200) DEFAULT NULL COMMENT '用户姓名',
  `user_phone` VARCHAR(200) DEFAULT NULL COMMENT '用户手机',
  `delivery_address` VARCHAR(500) DEFAULT NULL COMMENT '配送地址',
  `order_time` DATETIME DEFAULT NULL COMMENT '下单时间',
  `is_reviewed` TINYINT(1) DEFAULT 0 COMMENT '是否审核(0:否,1:是)',
  `review_reply` LONGTEXT DEFAULT NULL COMMENT '审核回复',
  `payment_status` VARCHAR(20) DEFAULT 'unpaid' COMMENT '支付状态(paid:已支付,unpaid:未支付)',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_order_number` (`order_number`),
  KEY `idx_user_id` (`user_id`),
  KEY `idx_restaurant_id` (`restaurant_id`),
  KEY `idx_order_time` (`order_time`),
  KEY `idx_payment_status` (`payment_status`),
  CONSTRAINT `fk_orders_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_orders_restaurant` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_orders_food` FOREIGN KEY (`food_id`) REFERENCES `foods` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='订单表';

-- =============================================
-- 7. 评价表 (Reviews)
-- =============================================
DROP TABLE IF EXISTS `reviews`;
CREATE TABLE `reviews` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `restaurant_id` BIGINT DEFAULT NULL COMMENT '餐厅ID',
  `restaurant_account` VARCHAR(200) DEFAULT NULL COMMENT '店铺账号',
  `restaurant_name` VARCHAR(200) DEFAULT NULL COMMENT '店铺名称',
  `food_id` BIGINT DEFAULT NULL COMMENT '美食ID',
  `food_name` VARCHAR(200) DEFAULT NULL COMMENT '美食名称',
  `user_id` BIGINT DEFAULT NULL COMMENT '用户ID',
  `user_account` VARCHAR(200) DEFAULT NULL COMMENT '用户账号',
  `user_name` VARCHAR(200) DEFAULT NULL COMMENT '用户姓名',
  `image` VARCHAR(255) DEFAULT NULL COMMENT '图片URL',
  `rating` TINYINT NOT NULL DEFAULT 5 COMMENT '评分(1-5)',
  `content` LONGTEXT DEFAULT NULL COMMENT '评价内容',
  `review_time` DATETIME DEFAULT NULL COMMENT '评价时间',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `idx_restaurant_id` (`restaurant_id`),
  KEY `idx_food_id` (`food_id`),
  KEY `idx_user_id` (`user_id`),
  KEY `idx_rating` (`rating`),
  CONSTRAINT `fk_reviews_restaurant` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_reviews_food` FOREIGN KEY (`food_id`) REFERENCES `foods` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_reviews_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='评价表';

-- =============================================
-- 8. 收藏表 (Favorites)
-- =============================================
DROP TABLE IF EXISTS `favorites`;
CREATE TABLE `favorites` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `user_id` BIGINT NOT NULL COMMENT '用户ID',
  `reference_id` BIGINT NOT NULL COMMENT '收藏对象ID',
  `table_name` VARCHAR(100) NOT NULL COMMENT '表名',
  `name` VARCHAR(200) DEFAULT NULL COMMENT '收藏名称',
  `picture` VARCHAR(255) DEFAULT NULL COMMENT '图片URL',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `idx_user_id` (`user_id`),
  KEY `idx_reference` (`reference_id`, `table_name`),
  CONSTRAINT `fk_favorites_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='收藏表';

-- =============================================
-- 9. 资讯表 (News)
-- =============================================
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `title` VARCHAR(200) NOT NULL COMMENT '标题',
  `introduction` LONGTEXT DEFAULT NULL COMMENT '简介',
  `picture` VARCHAR(255) DEFAULT NULL COMMENT '图片URL',
  `content` LONGTEXT NOT NULL COMMENT '内容',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `idx_title` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='资讯表';

-- =============================================
-- 10. 系统配置表 (System Config)
-- =============================================
DROP TABLE IF EXISTS `system_config`;
CREATE TABLE `system_config` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` VARCHAR(100) NOT NULL COMMENT '配置名称',
  `value` VARCHAR(500) DEFAULT NULL COMMENT '配置值',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='系统配置表';

-- =============================================
-- 11. Token表 (Tokens)
-- =============================================
DROP TABLE IF EXISTS `tokens`;
CREATE TABLE `tokens` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `user_id` BIGINT NOT NULL COMMENT '用户ID',
  `username` VARCHAR(100) NOT NULL COMMENT '用户名',
  `table_name` VARCHAR(100) NOT NULL COMMENT '表名',
  `role` VARCHAR(100) DEFAULT NULL COMMENT '角色',
  `token` VARCHAR(500) NOT NULL COMMENT 'token值',
  `expire_time` DATETIME DEFAULT NULL COMMENT '过期时间',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_token` (`token`(255)),
  KEY `idx_user` (`user_id`, `table_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Token表';

-- =============================================
-- 初始化数据
-- =============================================

-- 管理员数据
INSERT INTO `admins` (`username`, `password`, `role`) VALUES
('admin', '123456', '管理员');

-- 美食分类数据
INSERT INTO `food_categories` (`category_name`) VALUES
('川菜'),
('粤菜'),
('湘菜'),
('鲁菜'),
('苏菜'),
('浙菜'),
('闽菜'),
('徽菜'),
('快餐'),
('西餐'),
('日韩料理'),
('烧烤'),
('火锅'),
('小吃');

-- 系统配置数据
INSERT INTO `system_config` (`name`, `value`) VALUES
('systemName', '食客在线'),
('uploadPath', 'upload/'),
('maxFileSize', '10485760');

SET FOREIGN_KEY_CHECKS = 1;

-- =============================================
-- 索引说明
-- =============================================
-- 1. 主键索引：所有表的id字段
-- 2. 唯一索引：账号、用户名、订单编号等唯一字段
-- 3. 外键索引：关联关系字段
-- 4. 普通索引：常用查询字段（名称、分类、时间、状态等）
-- 5. 复合索引：多字段联合查询

-- =============================================
-- 性能优化建议
-- =============================================
-- 1. 对于大数据量表(orders, reviews, foods)考虑分表分库
-- 2. 热点数据使用Redis缓存
-- 3. 图片等静态资源使用CDN
-- 4. 定期归档历史订单数据
-- 5. 监控慢查询并优化索引

-- END

