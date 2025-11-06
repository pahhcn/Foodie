# Foodie 后台管理系统

基于 Vue3 的餐饮平台后台管理系统

## 技术栈

- **框架**: Vue 3 + Composition API
- **状态管理**: Pinia
- **UI 组件库**: Element Plus
- **图表库**: ECharts
- **路由**: Vue Router 4
- **HTTP 客户端**: Axios
- **构建工具**: Vite
- **包管理器**: npm/pnpm

## 项目结构

```
foodie-admin/
├── public/                   # 静态资源
├── src/
│   ├── assets/              # 资源文件
│   ├── components/          # 公共组件
│   │   ├── common/          # 通用组件
│   │   ├── layout/          # 布局组件
│   │   ├── charts/          # 图表组件
│   │   └── form/            # 表单组件
│   ├── views/               # 页面视图
│   │   ├── dashboard/       # 仪表盘
│   │   ├── restaurant/      # 餐厅管理
│   │   ├── menu/            # 菜品管理
│   │   ├── order/           # 订单管理
│   │   ├── user/            # 用户管理
│   │   ├── review/          # 评价管理
│   │   ├── finance/         # 财务统计
│   │   ├── system/          # 系统设置
│   │   └── auth/            # 登录页面
│   ├── router/              # 路由配置
│   ├── stores/              # Pinia 状态管理
│   ├── api/                 # API 接口
│   ├── utils/               # 工具函数
│   ├── styles/              # 样式文件
│   ├── hooks/               # 组合式函数
│   ├── directives/          # 自定义指令
│   ├── App.vue              # 根组件
│   └── main.js              # 入口文件
├── package.json             # 项目配置
├── vite.config.js           # Vite 配置
└── README.md
```

## 主要功能模块

### 仪表盘
- 数据概览
- 销售统计图表
- 实时订单状态
- 关键指标监控

### 餐厅管理
- 餐厅信息编辑
- 营业时间设置
- 配送范围管理
- 餐厅状态控制

### 菜品管理
- 菜品信息维护
- 分类管理
- 库存管理
- 价格设置
- 图片上传

### 订单管理
- 订单列表查看
- 订单状态更新
- 退款处理
- 订单统计分析

### 用户管理
- 用户信息查看
- 用户状态管理
- 积分管理
- 优惠券发放

### 评价管理
- 评价查看
- 回复管理
- 评价统计
- 问题评价处理

### 财务统计
- 收入统计
- 成本分析
- 利润报表
- 对账管理

### 系统设置
- 管理员账号管理
- 权限配置
- 系统参数设置
- 操作日志

## 设计特色

### 管理界面
- 清晰的数据展示
- 直观的操作流程
- 响应式设计
- 数据可视化

### 权限管理
- 基于角色的权限控制
- 细粒度权限设置
- 安全的操作验证

## 快速开始

1. 克隆项目
```bash
git clone https://github.com/pahhcn/Foodie.git
cd Foodie/foodie-admin
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

4. 访问管理系统
```
http://localhost:3001
```

## 构建部署

```bash
# 构建生产版本
npm run build

# 预览构建结果
npm run preview
```

## 默认管理员账号

```
用户名: admin
密码: admin123
```

## 团队分工

- **成员D**: 前端管理端负责人，负责后台管理系统（菜品、订单、用户管理）

## 开发流程

1. 在 `frontend-admin` 分支进行开发
2. 遵循 Element Plus 设计规范
3. 确保数据可视化效果
4. 做好权限控制
5. 通过 Pull Request 合并到 `dev` 分支

## API 接口

后端接口文档地址：`http://localhost:8080/swagger-ui.html`

## 技术要点

### 数据可视化
- 使用 ECharts 制作各种统计图表
- 实时数据更新
- 多维度数据分析

### 表格管理
- 分页查询
- 排序筛选
- 批量操作
- 导出功能

### 表单处理
- 表单验证
- 文件上传
- 富文本编辑

## 注意事项

- 注意数据安全和权限控制
- 优化大数据量的处理性能
- 确保图表数据的准确性
- 做好错误处理和用户反馈