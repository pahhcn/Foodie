# 食客在线 - 在线点餐平台


## 项目简介

食客在线是一个功能完善的在线点餐平台，为用户提供便捷的美食浏览、在线下单、评价等服务。本系统采用前后端分离架构，后端使用Spring Boot框架，前端包含Vue.js管理后台和Layui用户前台。

### ✨ 核心功能

#### 用户端功能
- 🔐 用户注册、登录、个人中心
- 🍽️ 美食分类浏览、搜索、详情查看
- 🛒 在线下单、购物车管理
- 📝 订单查询、状态跟踪
- ⭐ 美食评价、评分系统
- ❤️ 收藏功能

#### 商家端功能
- 🏪 店铺信息管理
- 📦 美食信息发布、编辑
- 📋 订单管理、状态更新
- 📊 销售数据统计

#### 管理端功能
- 👥 用户管理、商家审核
- 🍴 美食分类管理
- 📰 资讯发布管理
- ⚙️ 系统配置管理

### 快速开始

```bash
# 1. 克隆项目
git clone <repository-url>

# 2. 导入数据库
mysql -u root -p < db.sql

# 3. 配置数据库连接
编辑 src/main/resources/application.yml

# 4. 启动项目
mvn spring-boot:run

# 5. 访问应用
前台: http://localhost:8080/foodie/front/index.html
后台: http://localhost:8080/foodie/admin/dist/index.html (abo/abo)
```

## 技术栈

### 后端技术
- **核心框架**: Spring Boot 2.7.18 (LTS)
- **持久层**: MyBatis Plus 2.3 / MyBatis Spring Boot Starter 2.3.1
- **数据库**: MySQL 8.0.28
- **权限管理**: Apache Shiro 1.13.0
- **连接池**: HikariCP (Spring Boot 自动配置)
- **Java版本**: JDK 11
- **JSON处理**: Fastjson2 2.0.43
- **工具库**: Hutool 5.8.25, Commons Lang3 3.14.0

### 前端技术
- **管理后台**: Vue.js 2.x + Element UI + Vue Router + Vuex
- **用户前台**: Layui + jQuery + HTML5 + CSS3
- **构建工具**: Vue CLI (管理后台)

## 项目结构

```
foodie/
├── src/main/java/com/              # Java 后端代码
│   ├── controller/                 # 控制器层
│   ├── service/                    # 服务层
│   │   └── impl/                   # 服务实现
│   ├── dao/                        # 数据访问层
│   ├── entity/                     # 实体类
│   ├── utils/                      # 工具类
│   └── SpringbootSchemaApplication.java  # 启动类
│
├── src/main/resources/             # 资源文件
│   ├── mapper/                     # MyBatis XML映射文件
│   ├── static/upload/              # 文件上传目录
│   ├── application.yml             # 应用配置文件
│   │
│   ├── admin/admin/                # 管理后台前端 (Vue.js)
│   │   ├── src/                    # Vue 源代码
│   │   │   ├── assets/             # 静态资源
│   │   │   │   ├── css/            # 样式文件
│   │   │   │   └── img/            # 图片资源
│   │   │   ├── components/         # 公共组件
│   │   │   ├── views/              # 页面组件
│   │   │   ├── router/             # 路由配置
│   │   │   ├── store/              # Vuex 状态管理
│   │   │   └── App.vue             # 根组件
│   │   ├── dist/                   # 编译后的生产代码
│   │   │   └── index.html          # 后台入口 (编译生成)
│   │   ├── package.json            # npm 依赖配置
│   │   └── vue.config.js           # Vue 配置文件
│   │
│   └── front/front/                # 用户前台 (Layui)
│       ├── index.html              # 前台首页
│       ├── css/                    # 样式文件
│       │   ├── style.css           # 主样式
│       │   └── theme.css           # 主题样式
│       ├── js/                     # JavaScript 文件
│       ├── layui/                  # Layui 框架
│       ├── pages/                  # 各功能页面
│       │   ├── home/               # 首页
│       │   ├── login/              # 登录
│       │   ├── meishixinxi/        # 美食信息
│       │   ├── meishidingdan/      # 订单管理
│       │   └── ...                 # 其他页面
│       └── modules/                # 功能模块
│
├── pom.xml                         # Maven 配置 (JAR包)
├── pom-war.xml                     # Maven 配置 (WAR包)
└── db.sql                          # 数据库脚本
```

---

## 前后端代码位置详解

### 一、后端代码

#### 位置
```
src/main/java/com/
src/main/resources/mapper/
src/main/resources/application.yml
```

#### 主要目录说明
- **controller**: 接口控制器，处理HTTP请求
- **service**: 业务逻辑层
- **dao**: 数据访问接口
- **entity**: 数据库实体类
- **mapper**: MyBatis SQL映射文件

#### 配置文件
- `application.yml`: 数据库连接、端口、上下文路径等配置

---

### 二、管理后台前端 (Vue.js)

#### 位置
```
src/main/resources/admin/admin/
```

#### 开发目录
```
src/
├── assets/              # 静态资源
│   ├── css/            # 样式文件 (修改这里调整样式)
│   │   ├── style.scss           # 全局样式
│   │   └── element-variables.scss  # Element UI 主题变量
│   └── img/            # 图片资源 (Logo、背景等)
├── components/         # 可复用组件
├── views/              # 页面组件 (各功能模块页面)
├── router/             # 路由配置
├── store/              # Vuex 状态管理
└── App.vue             # 根组件
```

#### 编译输出
```
dist/                   # 生产环境代码 (不要直接修改)
└── index.html          # 后台访问入口
```

#### 开发步骤
1. 进入目录: `cd src/main/resources/admin/admin/`
2. 安装依赖: `npm install` (首次运行)
3. 开发模式: `npm run serve` (本地预览)
4. 编译打包: `npm run build` (生成dist目录)

#### 修改样式
- **全局样式**: 编辑 `src/assets/css/style.scss`
- **主题颜色**: 编辑 `src/assets/css/element-variables.scss`
- **Logo/图片**: 替换 `src/assets/img/` 下的文件
- **页面布局**: 编辑 `src/views/` 下的 `.vue` 文件

---

### 三、用户前台 (Layui)

#### 位置
```
src/main/resources/front/front/
```

#### 目录结构
```
├── index.html          # 前台首页入口
├── css/                # 样式文件
│   ├── style.css      # 主样式 (修改这里调整样式)
│   ├── theme.css      # 主题配置
│   └── common.css     # 公共样式
├── js/                 # JavaScript 文件
├── layui/              # Layui 框架文件
├── pages/              # 各功能页面
│   ├── home/          # 首页
│   ├── login/         # 登录/注册
│   ├── meishixinxi/   # 美食列表、详情
│   ├── meishidingdan/ # 订单管理
│   ├── meishipingjia/ # 评价管理
│   └── yonghu/        # 用户中心
└── img/                # 图片资源
```

#### 开发特点
- **无需编译**: 基于传统HTML+CSS+JS，修改后直接生效
- **直接修改**: 编辑 `.html`、`.css` 文件后刷新浏览器即可
- **静态资源**: 图片、样式等直接放在对应目录

#### 修改样式
- **全局样式**: 编辑 `css/style.css`
- **主题颜色**: 编辑 `css/theme.css`
- **页面布局**: 编辑 `pages/` 下的 `.html` 文件
- **功能逻辑**: 编辑对应页面的 `.js` 文件

---

## 开发环境要求

### 后端开发
- JDK 11 或更高版本
- Maven 3.6+
- MySQL 8.0+
- IntelliJ IDEA

### 前端开发 (管理后台)
- Node.js 14.x 或 16.x
- npm 6.x+
- 代码编辑器: VS Code

### 前端开发 (用户前台)
- 无特殊要求，任何文本编辑器即可
- 推荐: VS Code

---

## 部署说明

### 1. 数据库初始化

```bash
# 连接MySQL
mysql -u root -p

# 导入数据库脚本
source /path/to/db.sql

# 或使用客户端工具导入 db.sql
```

### 2. 配置文件修改

编辑 `src/main/resources/application.yml`:

```yaml
spring:
  datasource:
    url: jdbc:mysql://127.0.0.1:3306/foodie?...
    username: root
    password: 你的密码
```

### 3. 后端编译运行

#### 开发模式
```bash
# IDEA: 直接运行 SpringbootSchemaApplication.java

# 命令行
mvn spring-boot:run
```

#### 生产部署 (JAR包)
```bash
mvn clean package
java -jar target/foodie-0.0.1-SNAPSHOT.jar
```

#### 生产部署 (WAR包)
```bash
mvn clean package -f pom-war.xml
# 将生成的 foodie.war 部署到 Tomcat
```

### 4. 管理后台编译

```bash
cd src/main/resources/admin/admin/

# 首次运行安装依赖
npm install

# 编译生产代码
npm run build

# dist 目录会自动生成，包含在后端项目中
```

### 5. 用户前台

用户前台无需编译，已包含在项目中，后端启动后自动可访问。

---

## 访问地址

启动后端服务后，控制台会自动输出访问地址：

```
========================================
应用启动成功！
========================================
前台地址: http://localhost:8080/foodie/front/index.html
后台地址: http://localhost:8080/foodie/admin/dist/index.html
========================================
管理员账号: abo
管理员密码: abo
========================================
```

### 默认配置
- **服务端口**: 8080
- **上下文路径**: /foodie
- **管理后台**: http://localhost:8080/foodie/admin/dist/index.html
- **用户前台**: http://localhost:8080/foodie/front/index.html

---

## 常见问题

### Q1: 管理后台修改后不生效？
**A**: 管理后台是 Vue 项目，需要重新编译：
```bash
cd src/main/resources/admin/admin/
npm run build
```
然后重启后端服务。

### Q2: 用户前台修改后不生效？
**A**: 清除浏览器缓存或使用 Ctrl+F5 强制刷新。

### Q3: 如何修改端口？
**A**: 编辑 `application.yml` 中的 `server.port`。

### Q4: 数据库连接失败？
**A**: 检查：
1. MySQL 服务是否启动
2. 数据库名称是否为 `foodie`
3. 用户名密码是否正确
4. MySQL 驱动版本是否匹配

### Q5: 前端 npm install 失败？
**A**: 尝试：
```bash
# 使用国内镜像
npm config set registry https://registry.npmmirror.com
npm install
```

---

## 开发建议

### 前后端分离开发流程

1. **后端开发**: 
   - 修改 Java 代码
   - 重启 Spring Boot 应用
   - 使用 Postman 测试接口

2. **管理后台开发**:
   - 修改 Vue 源代码
   - 运行 `npm run serve` 本地预览
   - 开发完成后运行 `npm run build`
   - 重启后端服务查看效果

3. **用户前台开发**:
   - 直接修改 HTML/CSS/JS
   - 刷新浏览器即可查看效果
   - 无需编译步骤

### 推荐开发工具

- **后端**: IntelliJ IDEA Ultimate
- **前端**: Visual Studio Code + Volar/Vetur 插件
- **数据库**: Navicat / MySQL Workbench
- **接口测试**: Postman / Apifox
- **版本控制**: Git
