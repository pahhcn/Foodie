# Foodie 团队协作指南

## （4）代码审核与合并

多人协作的核心目标：
1. 防止代码冲突；
2. 保证功能质量；
3. 维持项目稳定分支结构。

---

### 一、发起 Pull Request（PR）后

假设开发者 B 完成了“订单模块”功能，并已推送到远程分支：

```bash
git push origin feature-order-module
```

接下来他需要：

1. 打开 GitHub 仓库页面；
2. 点击上方菜单栏的 **Pull requests → New pull request**；
3. 选择：

```
base: dev ← compare: feature-order-module
```
4. 填写：
   - **Title**：`feat(order): 完成订单接口开发`
   - **Description**：
     ```
     - 新增订单创建、查询、取消接口
     - 完成对应数据库操作
     - 本地测试通过
     - 待联调验证
     ```
   - 在右侧 **Reviewers** 中选择对应审核人（后端 → A，前端 → C）。
5. 点击 “Create pull request”。

> 此时 PR 会出现在仓库的“Pull Requests”列表中，等待审核。

---

### 二、代码审核流程

审核人（Reviewer）操作步骤：

1. 打开该 Pull Request；
2. 检查以下内容：
   - 代码逻辑是否符合项目规范；
   - 命名是否统一；
   - 是否引入了不必要的依赖；
   - 是否影响已有接口或样式；
   - 是否有遗漏的异常处理；
3. 点击右上角 “Files changed”，逐行查看改动；
4. 在行下方可评论建议；
5. 审核完毕后在底部选择：
   - ✅ **Approve**：通过；
   - 🟡 **Request changes**：退回修改；
   - ⚪ **Comment**：仅留言不合并。

---

### 三、PR 通过后合并操作

当审核人点击 “Approve” 后，由 **仓库管理员（通常是 A）** 进行合并操作。

#### 1. 在 GitHub 网页合并

在 PR 页面底部点击：

- “**Merge pull request**”
- “**Confirm merge**”

GitHub 会自动将 `feature-order-module` 合并入 `dev` 分支。

#### 2. 删除功能分支（推荐）

在 PR 页面点击：

- “**Delete branch**” 删除远程功能分支；

本地执行：

```bash
git branch -d feature-order-module
```

保持仓库整洁，避免旧分支堆积。

---

### 四、冲突处理流程（若合并失败）

若提示：

> “This branch has conflicts that must be resolved”

说明分支与 `dev` 存在冲突。  
提交者本人解决：

```bash
git checkout feature-order-module
git pull origin dev
# 解决冲突后：
git add .
git commit -m "fix: merge conflicts with dev"
git push origin feature-order-module
```

GitHub 页面状态会更新为“可合并”，再由审核人确认合并。

---

### 五、合并完成后测试人员（E）的步骤

1. 拉取最新的 `dev` 分支：

```bash
git checkout dev
git pull origin dev
```
2. 启动本地或测试服务器；
3. 按模块测试新功能；
4. 在 `/docs/test-report.md` 中记录结果：
   ```
   [x] 订单创建接口正常返回
   [ ] 订单取消后状态未更新数据库（反馈B修复）
   ```
5. 若有问题，在 GitHub 上提 Issue 或在 PR 下评论。

---

### 六、定期合并到主分支（Main）

功能开发完成、测试通过后：

```bash
git checkout main
git pull origin main
git merge dev
git push origin main
```

添加版本号：

```bash
git tag -a v1.0 -m "First stable release of FoodieOK"
git push origin v1.0
```

---

### 七、典型工作循环总结

| 阶段 | 操作人 | 动作 |
|------|---------|------|
| 开发 | 任意成员 | 新建分支开发功能 |
| 提交 | 开发者 | 推送至远程并发起 PR |
| 审核 | 模块负责人 | 代码审查、通过或退回 |
| 合并 | 管理员 | 将功能分支合并入 dev |
| 测试 | 测试人员 | 拉取 dev 分支验证功能 |
| 发布 | 管理员 | 将 dev 合并入 main，部署上线 |

---

**完成后，所有人每日保持以下循环：**

```bash
git pull origin dev      # 拉取最新开发分支
git checkout -b feature-xxx   # 新建功能分支
git add .
git commit -m "feat: 新增功能说明"
git push origin feature-xxx
# 发起 PR → 审核 → 合并 → 删除分支
```
