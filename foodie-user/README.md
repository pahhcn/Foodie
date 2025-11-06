# Foodie 用户端前台

基于 Vue3 的餐饮平台用户端前台应用

## 技术栈

- **框架**: Vue 3 + Composition API
- **状态管理**: Pinia
- **UI 组件库**: Element Plus
- **路由**: Vue Router 4
- **HTTP 客户端**: Axios
- **构建工具**: Vite
- **包管理器**: npm/pnpm

## 项目结构

```
foodie-user/
├── public/                    # 静态资源
├── src/
│   ├── assets/               # 资源文件
│   ├── components/           # 公共组件
│   │   ├── common/           # 通用组件
│   │   ├── layout/           # 布局组件
│   │   └── business/         # 业务组件
│   ├── views/                # 页面视图
│   │   ├── home/             # 首页
│   │   ├── restaurant/       # 餐厅页面
│   │   ├── menu/             # 菜单页面
│   │   ├── cart/             # 购物车
│   │   ├── order/            # 订单页面
│   │   ├── user/             # 用户中心
│   │   └── auth/             # 登录注册
│   ├── router/               # 路由配置
│   ├── stores/               # Pinia 状态管理
│   ├── api/                  # API 接口
│   ├── utils/                # 工具函数
│   ├── styles/               # 样式文件
│   ├── hooks/                # 组合式函数
│   ├── App.vue               # 根组件
│   └── main.js               # 入口文件
├── package.json              # 项目配置
├── vite.config.js            # Vite 配置
└── README.md
```

## 主要功能模块

### 用户认证
- 用户注册
- 用户登录
- 第三方登录（微信/支付宝）
- 忘记密码

### 首页
- 热门推荐
- 商家列表
- 搜索功能
- 分类筛选

### 餐厅详情
- 餐厅信息展示
- 菜品浏览
- 菜品搜索
- 营业时间

### 点餐功能
- 菜品详情
- 购物车管理
- 规格选择
- 数量调整

### 订单管理
- 下单流程
- 订单支付
- 订单状态跟踪
- 订单历史

### 用户中心
- 个人信息管理
- 收货地址管理
- 优惠券
- 积分系统

### 评价系统
- 订单评价
- 查看评价
- 图片上传

## 设计规范

### UI/UX 设计
- 响应式设计，支持移动端
- 统一的设计风格
- 良好的用户体验

### 代码规范
- ESLint + Prettier 代码格式化
- 组件化开发
- TypeScript 类型检查（可选）

## 快速开始

1. 克隆项目
```bash
git clone https://github.com/pahhcn/Foodie.git
cd Foodie/foodie-user
```

2. 安装依赖
```bash
npm install
# 或者
pnpm install
```

3. 启动开发服务器
```bash
npm run dev
# 或者
pnpm dev
```

4. 访问应用
```
http://localhost:3000
```

## 构建部署

```bash
# 构建生产版本
npm run build

# 预览构建结果
npm run preview
```

## 团队分工

- **成员C**: 前端用户端负责人，负责用户前台页面（点餐、下单、支付、评价）

## 开发流程

1. 在 `frontend-user` 分支进行开发
2. 遵循组件化开发原则
3. 确保代码通过 ESLint 检查
4. 提交前进行功能测试
5. 通过 Pull Request 合并到 `dev` 分支

## API 接口

后端接口文档地址：`http://localhost:8080/swagger-ui.html`

## 注意事项

- 确保与后端接口字段一致
- 注意移动端适配
- 优化页面加载性能
- 做好错误处理和用户提示