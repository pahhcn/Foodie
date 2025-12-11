# 头像更新功能测试指南

## 功能说明

用户可以通过输入图片 URL 来更新头像，更新后：
- 个人中心页面的头像会立即更新
- 顶部导航栏的头像会自动更新
- 下次登录时会显示新头像

## 修改说明

### 为什么改为输入 URL？

原来的上传功能需要后端提供文件上传接口，但后端目前没有这个接口。为了简化实现，改为直接输入图片 URL 的方式。

### 如何获取图片 URL？

有几种方式：

1. **使用在线图床**
   - 访问图床网站（如：https://imgbb.com, https://imgur.com）
   - 上传图片
   - 复制图片的直链地址

2. **使用项目中已有的图片**
   - 例如：`http://localhost:8080/foodie/upload/yonghu_touxiang1.jpg`
   - 数据库中已有的图片地址

3. **使用外部图片**
   - 任何可访问的图片 URL
   - 例如：`https://example.com/avatar.jpg`

## 测试步骤

### 1. 访问个人中心
```
http://localhost:3000/user/center
```

### 2. 更新头像
1. 在"头像"字段中输入图片 URL
2. 例如：`http://localhost:8080/foodie/upload/yonghu_touxiang1.jpg`
3. 点击"更新信息"按钮

### 3. 验证更新
1. 看到"更新成功"提示
2. 个人中心页面的头像立即更新
3. 查看顶部导航栏，头像也已更新
4. 刷新页面，头像保持更新后的状态

### 4. 测试响应式更新
1. 打开浏览器开发者工具（F12）
2. 切换到 Console 标签页
3. 更新头像
4. 观察控制台输出：
   ```
   提交更新的用户信息：{...}
   更新用户信息：{...}
   ```

## 数据流程

1. **用户输入图片 URL**
   - 在输入框中输入或粘贴图片地址

2. **点击更新按钮**
   - 调用 `userStore.updateUserInfo()`
   - 发送 POST 请求到 `/yonghu/update`
   - 包含 `touxiang` 字段

3. **后端更新数据库**
   - 更新用户表的 `touxiang` 字段

4. **前端同步更新**
   - 调用 `fetchUserInfo()` 重新获取用户信息
   - 更新 `userInfo.value.touxiang`
   - 触发 `avatar` computed 属性更新
   - 导航栏自动显示新头像

## 技术实现

### 前端代码

#### 个人中心页面
```vue
<el-form-item label="头像">
  <div class="avatar-section">
    <el-avatar v-if="userForm.touxiang" :src="userForm.touxiang" :size="100">
      <el-icon><User /></el-icon>
    </el-avatar>
    <el-avatar v-else :size="100">
      <el-icon><User /></el-icon>
    </el-avatar>
    <div class="avatar-input">
      <el-input 
        v-model="userForm.touxiang" 
        placeholder="请输入头像图片URL"
        clearable
      />
      <el-text type="info" size="small">
        提示：请输入图片的完整URL地址
      </el-text>
    </div>
  </div>
</el-form-item>
```

#### 用户 Store
```javascript
// 计算属性 - 响应式更新
const avatar = computed(() => userInfo.value?.touxiang || '')

// 更新用户信息
const updateUserInfo = async (data) => {
  // 调用后端 API
  await updateUserInfoApi(updateData)
  
  // 更新本地状态
  userInfo.value = { ...userInfo.value, ...data }
  
  // 重新获取用户信息
  await fetchUserInfo()
}
```

#### 导航栏
```vue
<el-avatar :src="avatar" :size="32">
  <el-icon><User /></el-icon>
</el-avatar>
```

## 常见问题

### 1. 头像不显示
**原因：**
- 图片 URL 不正确
- 图片服务器不允许跨域访问
- 图片已被删除

**解决方法：**
- 检查 URL 是否正确
- 在浏览器中直接访问 URL，确认图片可访问
- 使用项目内的图片地址

### 2. 更新后导航栏头像没变
**原因：**
- 浏览器缓存
- 数据未正确同步

**解决方法：**
1. 打开开发者工具（F12）
2. 查看 Network 标签页
3. 确认 `/yonghu/update` 请求成功
4. 确认 `/yonghu/info/{id}` 请求返回了新头像
5. 刷新页面（Ctrl + Shift + R 强制刷新）

### 3. 头像显示为默认图标
**原因：**
- `touxiang` 字段为空
- 图片加载失败

**解决方法：**
- 输入有效的图片 URL
- 使用 `<el-icon><User /></el-icon>` 作为默认头像

## 测试用例

### 测试用例 1：使用项目内图片
1. 输入：`http://localhost:8080/foodie/upload/yonghu_touxiang1.jpg`
2. 点击更新
3. 验证：头像显示为该图片

### 测试用例 2：使用外部图片
1. 输入：`https://via.placeholder.com/150`
2. 点击更新
3. 验证：头像显示为该图片

### 测试用例 3：清空头像
1. 清空头像 URL
2. 点击更新
3. 验证：显示默认用户图标

### 测试用例 4：导航栏同步
1. 更新头像
2. 不刷新页面
3. 验证：导航栏头像立即更新

## 推荐的测试图片 URL

如果数据库中有以下图片，可以直接使用：
```
http://localhost:8080/foodie/upload/yonghu_touxiang1.jpg
http://localhost:8080/foodie/upload/yonghu_touxiang2.jpg
http://localhost:8080/foodie/upload/yonghu_touxiang3.jpg
http://localhost:8080/foodie/upload/yonghu_touxiang4.jpg
http://localhost:8080/foodie/upload/yonghu_touxiang5.jpg
http://localhost:8080/foodie/upload/yonghu_touxiang6.jpg
```

或使用占位图片服务：
```
https://via.placeholder.com/150
https://i.pravatar.cc/150
```

## 未来改进

如果需要实现真正的文件上传功能，需要：

1. **后端添加文件上传接口**
   ```java
   @PostMapping("/upload")
   public R upload(@RequestParam("file") MultipartFile file) {
       // 保存文件
       // 返回文件 URL
   }
   ```

2. **前端使用 el-upload 组件**
   ```vue
   <el-upload
     action="/foodie/upload"
     :on-success="handleAvatarSuccess"
   >
     <el-avatar :src="avatar" />
   </el-upload>
   ```

3. **配置文件存储**
   - 本地文件系统
   - 云存储（OSS、S3 等）
