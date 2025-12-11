# 下单功能测试指南

## 前置条件

### 1. 数据库配置
确保在 MySQL 中执行以下 SQL：
```sql
USE foodie;
ALTER TABLE meishidingdan MODIFY COLUMN goumaishuliang int(11) NOT NULL DEFAULT 1 COMMENT '购买数量';
```

### 2. 启动后端
```bash
cd Foodie-main/foodie-backend
mvn clean package -DskipTests
java -jar target/foodie-0.0.1-SNAPSHOT.jar
```
或者在 IDE 中运行 `SpringbootSchemaApplication`

后端应该运行在：http://localhost:8080

### 3. 启动前端
```bash
cd Foodie-main/foodie-user
npm install
npm run dev
```
前端应该运行在：http://localhost:3000

## 测试步骤

### 步骤 1：注册/登录
1. 访问 http://localhost:3000/
2. 点击右上角"登录"按钮
3. 如果没有账号，先注册：
   - 用户账号：test01
   - 密码：123456
   - 用户姓名：测试用户
   - 手机号：13800138000
   - 配送地址：测试地址123号
4. 使用账号登录

### 步骤 2：浏览美食
1. 在首页或美食列表页面浏览美食
2. 点击任意美食卡片进入详情页

### 步骤 3：下单
1. 在美食详情页面，选择购买数量
2. 点击"立即点餐"按钮
3. 在弹出的对话框中：
   - 确认美食信息
   - 填写/确认配送地址
   - 填写/确认联系方式
4. 点击"确认下单"按钮

### 步骤 4：验证
1. 看到"下单成功"提示
2. 选择"查看订单"或"继续浏览"
3. 如果选择"查看订单"，会跳转到订单列表页面
4. 在订单列表中应该能看到刚才创建的订单

## 调试方法

### 浏览器控制台
打开浏览器开发者工具（F12），切换到 Console 标签页，应该看到：
```
=== 美食详情页面已加载 ===
美食信息：{...}
点击立即点餐按钮
打开订单对话框
点击确认下单按钮
开始提交订单
提交订单数据：{...}
订单创建成功：{...}
```

### Network 标签页
在 Network 标签页中，应该看到：
- GET /foodie/meishixinxi/info/{id} - 获取美食详情
- POST /foodie/meishidingdan/add - 创建订单

### 后端日志
后端控制台应该显示：
- 接收到 POST /foodie/meishidingdan/add 请求
- 订单插入成功

## 常见问题

### 1. 提示"请先登录"
- 确保已经登录
- 检查 localStorage 中是否有 Token

### 2. 提示"请求参数错误"
- 检查美食信息是否完整（dianpuzhanghao, lianxidianhua 等字段）
- 查看浏览器控制台的详细错误信息

### 3. 提示"下单失败"
- 检查后端是否正常运行
- 查看后端控制台的错误日志
- 确认数据库连接正常

### 4. 页面没有反应
- 确认访问的是 http://localhost:3000（不是 8081）
- 刷新页面（Ctrl + Shift + R）
- 检查浏览器控制台是否有 JavaScript 错误

## 修改内容总结

### 前端修改
1. `foodie-user/src/views/Food/Detail.vue` - 重写下单逻辑
2. `foodie-user/src/router/index.js` - 修改路由基础路径为 `/`

### 后端修改
1. `foodie-backend/src/main/java/com/controller/MeishidingdanController.java` - 添加默认值处理
2. `foodie-backend/src/main/java/com/config/CorsConfig.java` - 添加跨域配置

### 数据库修改
1. `meishidingdan` 表的 `goumaishuliang` 字段添加默认值
