# Foodie 团队协作指南

基于 GitHub 的多人协作开发流程

---



## 一、团队组成

| 成员 | 角色                 | 主要职责                                    | 技术栈                              |
| ---- | -------------------- | ------------------------------------------- | ----------------------------------- |
| A    | **后端负责人**       | 系统架构设计、数据库设计、核心接口实现      | Spring Boot + MyBatis + MySQL + JWT |
| B    | **后端开发**         | 商家模块、评价模块、接口测试与联调          | Spring Boot + Swagger + Postman     |
| C    | **前端用户端负责人** | 用户前台页面（点餐、下单、支付、评价）      | Vue3 + Pinia + Element Plus         |
| D    | **前端管理端负责人** | 后台管理系统（菜品、订单、用户管理）        | Vue3 + Element Plus + ECharts       |
| E    | **测试与部署**       | 接口联调测试、Bug收集、前后端部署与文档编写 | Postman + Nginx                     |

---

## 二、GitHub 团队协作流程

### 1. 仓库管理

- 所有成员加入同一个 GitHub 仓库（由项目负责人邀请）。  
- 后端、前端共用一个仓库，统一代码管理。  
- 仓库结构如下：

```
/foodie-server       # 后端项目（Spring Boot）
/foodie-user         # 前端用户端（Vue3）
/foodie-admin        # 前端管理端（Vue3）
/docs                # 项目文档
Foodie团队协作指南.md  # 现在正在看的这个文件
```

---

### 2. 分支管理规范

采用 **主干 + 开发 + 功能分支** 模式。

> 所有开发在 `dev` 或子分支上进行，`main` 永远保持可部署版本。

```bash
main             # 主分支，稳定版
dev              # 开发分支，集成功能测试
backend          # 后端功能分支
frontend-user    # 用户端功能分支
frontend-admin   # 管理端功能分支
```

#### 使用规范

1. 不允许直接在 `main` 上开发。  
2. 每位开发者在对应分支编写代码并提交。  
3. 完成功能后通过 Pull Request 合并到 `dev`。  
4. `dev` 测试稳定后，由负责人合并到 `main`。  

---

### 3. 提交规范

#### Commit 信息格式

```bash
<type>(<scope>): <subject>
```

示例：

```bash
feat(order): add order cancel function
fix(user): correct token expiration bug
docs: update project introduction
```

常见 type 类型：

| 类型     | 含义                           |
| -------- | ------------------------------ |
| feat     | 新功能                         |
| fix      | 修复 bug                       |
| docs     | 文档更新                       |
| style    | 代码格式调整（不影响逻辑）     |
| refactor | 重构（这个我们这个项目用不到） |
| test     | 增加测试代码                   |
| chore    | 构建过程或辅助工具修改         |

---

### 4. 协作步骤

#### （1）项目克隆

```bash
git clone https://github.com/pahhcn/Foodie.git
cd Foodie
```

#### （2）创建并切换分支

```bash
git checkout -b frontend-user
```

#### （3）开发与提交

```bash
git add .
git commit -m "feat: add login page"
git push origin frontend-user
```

#### （4）发起合并请求（Pull Request）

1. 在 GitHub 网页端选择 “Compare & Pull Request”。  
2. 选择目标分支为 `dev`。  
3. 填写修改说明。  
4. 由其他成员或负责人审核后合并。  

---

### 5. 更新同步

多人开发时，定期拉取最新代码避免冲突：

```bash
git pull origin dev
```

如果有冲突：

- 先手动解决；
- 测试确认正常；
- 再执行 `git add . && git commit` 提交。  

---

## 三、接口与文档协作

- 后端使用 **Apifox** 生成接口文档。  
- 所有接口需说明：
    - URL 路径  
    - 请求方法（GET/POST/PUT/DELETE）  
    - 请求参数及类型  
    - 返回值格式与示例  

前端在文档确认后再对接，避免字段混乱。  

---

## 四、协作沟通建议

| 内容     | 工具            | 说明             |
| -------- | --------------- | ---------------- |
| 日常沟通 | QQ群            | 及时交流开发进度 |
| 接口对接 | Apifox          | 确认字段一致     |
| 任务管理 | GitHub Projects | 跟踪进度         |
| 文档协作 | `/docs` 目录    | 保存设计草图等   |

---

## 五、协作节奏建议

| 周次  | 后端任务           | 前端任务                |
| ----- | ------------------ | ----------------------- |
| 第1周 | 数据库 + 接口文档  | 页面框架搭建、Mock 数据 |
| 第3周 | 用户、菜品模块接口 | 登录注册、菜品展示页面  |
| 第5周 | 订单、评价接口     | 下单、后台管理          |
| 第7周 | 系统联调与测试     | 页面优化、部署          |

---

## 六、良好协作原则

1. **先沟通后提交**：接口改动、命名变化先讨论确认。  
2. **少量多次提交**：避免一次性提交大批代码。  
3. **注释清晰**：代码逻辑复杂处需写注释。  
4. **责任清晰**：每人对自己模块的质量负责。  
5. **周会复盘**：每周一次进度检查，记录问题与下周目标。  

---

## 七、附录：常用 Git 命令备忘

```bash
git clone <url>             # 克隆项目
git checkout -b <branch>    # 创建并切换分支
git add .                   # 添加修改
git commit -m "message"     # 提交修改
git push origin <branch>    # 推送到远程
git pull origin <branch>    # 拉取远程更新
git merge <branch>          # 合并分支
git log --oneline           # 查看提交记录
```

---

**结语：**

> 团队协作的核心不是写代码快，而是彼此信任、规范沟通。  
> GitHub 是记录协作的工具，规范是保证项目可持续的力量。  
