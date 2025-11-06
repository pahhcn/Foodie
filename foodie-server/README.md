# Foodie 后端服务

基于 Spring Boot 的餐饮管理系统后端服务

## 技术栈

- **框架**: Spring Boot 2.x
- **数据库**: MySQL 8.0
- **ORM**: MyBatis Plus
- **认证**: JWT
- **文档**: Swagger/Apifox
- **构建工具**: Maven

## 项目结构

```
foodie-server/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/foodie/
│   │   │       ├── controller/     # 控制器层
│   │   │       ├── service/        # 服务层
│   │   │       ├── mapper/         # 数据访问层
│   │   │       ├── entity/         # 实体类
│   │   │       ├── dto/            # 数据传输对象
│   │   │       ├── config/         # 配置类
│   │   │       └── utils/          # 工具类
│   │   └── resources/
│   │       ├── mapper/             # MyBatis 映射文件
│   │       ├── application.yml     # 配置文件
│   │       └── static/             # 静态资源
│   └── test/                       # 测试代码
├── pom.xml                         # Maven 配置
└── README.md
```

## 主要模块

### 用户模块
- 用户注册/登录
- 用户信息管理
- 权限控制

### 商家模块
- 商家入驻
- 店铺管理
- 营业状态控制

### 菜品模块
- 菜品信息管理
- 分类管理
- 库存管理

### 订单模块
- 订单创建
- 订单状态管理
- 支付处理

### 评价模块
- 用户评价
- 评分统计

## 开发规范

### API 接口规范
- 统一返回格式
- RESTful 风格
- 完整的接口文档

### 代码规范
- 遵循阿里巴巴 Java 开发手册
- 单元测试覆盖率 > 80%
- 代码注释完整

## 快速开始

1. 克隆项目
```bash
git clone https://github.com/pahhcn/Foodie.git
cd Foodie/foodie-server
```

2. 配置数据库
```bash
# 修改 application.yml 中的数据库配置
```

3. 启动项目
```bash
mvn spring-boot:run
```

4. 访问接口文档
```
http://localhost:8080/swagger-ui.html
```

## 团队分工

- **成员A**: 系统架构设计、数据库设计、核心接口实现
- **成员B**: 商家模块、评价模块、接口测试与联调

## 注意事项

- 所有开发在 `backend` 分支进行
- 提交前确保代码通过测试
- 遵循团队协作指南中的 Git 规范