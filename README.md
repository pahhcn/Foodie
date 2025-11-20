# 食客在线 - 在线点餐平台

## 项目简介

食客在线是一个功能完善的在线点餐平台，为用户提供便捷的美食浏览、在线下单、评价等服务。本系统采用**前后端完全分离**架构，后端使用 Spring Boot 2.7 提供 REST API，前端包含 Vue3 用户端和 Vue2 管理后台。

## 技术栈

### 后端技术
- **Spring Boot 2.7.18** - 核心框架
- **MyBatis-Plus** - ORM 框架
- **MySQL 8.0** - 数据库
- **Shiro** - 权限控制
- **SpringDoc OpenAPI 1.7.0** - API 文档
- **FastJson2** - JSON 处理
- **Hutool** - 工具类库

### 前端技术

**用户端 (foodie-user)**
- Vue 3.4
- Vite 5.1
- Element Plus 2.6
- Vue Router 4.3
- Pinia 2.1
- Axios

**管理后台 (foodie-admin)**
- Vue 2.6
- Element UI 2.15
- Vue Router 3.6
- Axios
- ECharts 4.9


## 快速开始

### 1. 环境要求

- JDK 11+
- Maven 3.6+
- MySQL 8.0+
- Node.js 16+
- npm 或 yarn

### 2. 数据库配置

```bash
# 导入数据库
mysql -u root -p < docs/sql.sql

# 修改数据库连接配置
# 编辑 foodie-backend/src/main/resources/application.yml
spring:
  datasource:
    url: jdbc:mysql://127.0.0.1:3306/foodie
    username: root
    password: 你的密码
```

### 3. 启动后端

```bash
cd foodie-backend
mvn clean install
mvn spring-boot:run

# 后端服务运行在: http://localhost:8080/foodie
```

### 4. 启动用户端前端

```bash
cd foodie-user
npm install
npm run dev

# 用户端运行在: http://localhost:3000
```

### 5. 启动管理后台

```bash
cd foodie-admin
npm install
npm run serve

# 管理后台运行在: http://localhost:8081
```

## 访问地址

| 服务 | 地址 | 说明 |
|------|------|------|
| 后端 API | http://localhost:8080/foodie | REST API 接口 |
| API 文档 | http://localhost:8080/foodie/v3/api-docs | OpenAPI JSON |
| 用户端 | http://localhost:3000 | Vue3 用户前台 |
| 管理后台 | http://localhost:8081 | Vue2 管理后台 |


