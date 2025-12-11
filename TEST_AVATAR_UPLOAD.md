# 头像上传功能测试指南

## 功能说明

用户可以通过上传本地图片文件来更新头像，支持：
- 点击上传区域选择图片
- 支持 jpg、png、gif 格式
- 文件大小限制 2MB
- 上传成功后自动更新头像显示
- 导航栏头像同步更新

## 技术实现

### 后端接口
```
POST /foodie/file/upload
Content-Type: multipart/form-data

参数：
- file: 文件对象

返回：
{
  "code": 0,
  "file": "1733241234567.jpg"  // 文件名
}
```

### 前端实现

#### 1. 上传组件
```vue
<el-upload
  action="/foodie/file/upload"
  :show-file-list="false"
  :on-success="handleAvatarSuccess"
  :before-upload="beforeAvatarUpload"
  :headers="uploadHeaders"
>
  <el-avatar v-if="avatarUrl" :src="avatarUrl" :size="100" />
  <div v-else class="avatar-uploader-icon">
    <el-icon><Plus /></el-icon>
    <div>点击上传头像</div>
  </div>
</el-upload>
```

#### 2. 头像 URL 处理
```javascript
const avatarUrl = computed(() => {
  if (!userForm.value.touxiang) return ''
  // 如果已经是完整 URL，直接返回
  if (userForm.value.touxiang.startsWith('http')) {
    return userForm.value.touxiang
  }
  // 否则拼接为完整 URL
  return `http://localhost:8080/foodie/upload/${userForm.value.touxiang}`
})
```

#### 3. 上传处理
```javascript
// 上传成功
const handleAvatarSuccess = (response) => {
  if (response.code === 0) {
    userForm.value.touxiang = response.file
    ElMessage.success('头像上传成功')
  }
}

// 上传前验证
const beforeAvatarUpload = (file) => {
  const isImage = file.type.startsWith('image/')
  const isLt2M = file.size / 1024 / 1024 < 2
  
  if (!isImage) {
    ElMessage.error('只能上传图片文件!')
    return false
  }
  if (!isLt2M) {
    ElMessage.error('图片大小不能超过 2MB!')
    return false
  }
  return true
}
```

## 测试步骤

### 1. 访问个人中心
```
http://localhost:3000/user/center
```

### 2. 上传头像
1. 点击头像上传区域（显示"点击上传头像"）
2. 在文件选择对话框中选择图片文件
3. 等待上传完成
4. 看到"头像上传成功"提示
5. 头像立即显示为上传的图片

### 3. 保存更新
1. 头像上传成功后，文件名已保存到表单
2. 点击"更新信息"按钮
3. 头像信息保存到数据库
4. 导航栏头像同步更新

### 4. 验证持久化
1. 刷新页面
2. 头像保持为上传的图片
3. 退出登录后重新登录
4. 头像仍然是上传的图片

## 数据流程

### 上传流程
```
1. 用户选择图片文件
   ↓
2. beforeAvatarUpload 验证文件
   ↓
3. 发送 POST /foodie/file/upload
   ↓
4. 后端保存文件到 /upload/ 目录
   ↓
5. 返回文件名：{ code: 0, file: "1733241234567.jpg" }
   ↓
6. handleAvatarSuccess 处理响应
   ↓
7. 更新 userForm.touxiang = "1733241234567.jpg"
   ↓
8. 头像显示为：http://localhost:8080/foodie/upload/1733241234567.jpg
```

### 保存流程
```
1. 点击"更新信息"
   ↓
2. 调用 userStore.updateUserInfo()
   ↓
3. POST /foodie/yonghu/update
   ↓
4. 数据库更新 touxiang 字段
   ↓
5. 重新获取用户信息
   ↓
6. 导航栏头像自动更新
```

## 文件存储

### 存储位置
```
foodie-backend/target/classes/static/upload/
```

### 文件命名
```
时间戳.扩展名
例如：1733241234567.jpg
```

### 访问 URL
```
http://localhost:8080/foodie/upload/文件名
例如：http://localhost:8080/foodie/upload/1733241234567.jpg
```

## 测试用例

### 测试用例 1：上传 JPG 图片
1. 选择一个 JPG 格式的图片
2. 文件大小 < 2MB
3. 验证：上传成功，头像显示正确

### 测试用例 2：上传 PNG 图片
1. 选择一个 PNG 格式的图片
2. 文件大小 < 2MB
3. 验证：上传成功，头像显示正确

### 测试用例 3：上传过大文件
1. 选择一个 > 2MB 的图片
2. 验证：提示"图片大小不能超过 2MB!"
3. 上传被阻止

### 测试用例 4：上传非图片文件
1. 选择一个 PDF 或其他非图片文件
2. 验证：提示"只能上传图片文件!"
3. 上传被阻止

### 测试用例 5：更换头像
1. 已有头像的情况下
2. 点击头像区域
3. 选择新图片
4. 验证：头像更新为新图片

### 测试用例 6：导航栏同步
1. 上传新头像
2. 点击"更新信息"
3. 不刷新页面
4. 验证：导航栏头像立即更新

## 常见问题

### 1. 上传失败
**可能原因：**
- 后端服务未启动
- 文件太大
- 文件格式不支持
- 网络问题

**解决方法：**
1. 确认后端正在运行
2. 检查文件大小和格式
3. 查看浏览器控制台错误信息
4. 查看 Network 标签页的请求详情

### 2. 头像不显示
**可能原因：**
- 文件上传成功但路径不正确
- 文件被删除
- 跨域问题

**解决方法：**
1. 检查 avatarUrl 的值
2. 在浏览器中直接访问图片 URL
3. 确认文件存在于 upload 目录

### 3. 导航栏头像没更新
**可能原因：**
- 没有点击"更新信息"按钮
- 数据未保存到数据库

**解决方法：**
1. 上传头像后必须点击"更新信息"
2. 查看 Network 标签页确认更新请求成功
3. 刷新页面验证

### 4. 上传目录不存在
**可能原因：**
- 首次运行，upload 目录未创建

**解决方法：**
- 后端代码会自动创建目录
- 或手动创建：`foodie-backend/target/classes/static/upload/`

## 调试方法

### 浏览器控制台
打开开发者工具（F12），查看：
```
上传成功：{ code: 0, file: "1733241234567.jpg" }
提交更新的用户信息：{ touxiang: "1733241234567.jpg", ... }
```

### Network 标签页
查看以下请求：
1. POST `/foodie/file/upload` - 上传文件
   - 请求类型：multipart/form-data
   - 响应：{ code: 0, file: "文件名" }

2. POST `/foodie/yonghu/update` - 更新用户信息
   - 请求体：{ id: xxx, touxiang: "文件名", ... }
   - 响应：{ code: 0 }

3. GET `/foodie/yonghu/info/{id}` - 获取用户信息
   - 响应：{ code: 0, data: { touxiang: "文件名", ... } }

### 后端日志
查看后端控制台，确认：
- 文件上传成功
- 文件保存路径
- 用户信息更新成功

## 优化建议

### 1. 添加图片裁剪
可以集成图片裁剪库，让用户上传前裁剪图片：
```javascript
import VueCropper from 'vue-cropper'
```

### 2. 添加压缩
上传前压缩图片，减少文件大小：
```javascript
import imageCompression from 'browser-image-compression'
```

### 3. 添加预览
上传前预览图片：
```javascript
const previewImage = (file) => {
  const reader = new FileReader()
  reader.onload = (e) => {
    previewUrl.value = e.target.result
  }
  reader.readAsDataURL(file)
}
```

### 4. 云存储
将文件上传到云存储（OSS、S3）而不是本地：
```java
// 使用阿里云 OSS
OSSClient ossClient = new OSSClient(endpoint, accessKeyId, accessKeySecret)
ossClient.putObject(bucketName, objectName, inputStream)
```

## 安全建议

1. **文件类型验证**
   - 前端验证文件扩展名
   - 后端验证文件 MIME 类型
   - 检查文件内容（防止伪造）

2. **文件大小限制**
   - 前端限制 2MB
   - 后端也应该限制

3. **文件名处理**
   - 使用时间戳生成唯一文件名
   - 避免使用用户提供的文件名

4. **访问控制**
   - 上传的文件应该是公开可访问的
   - 或者添加权限验证

5. **病毒扫描**
   - 对上传的文件进行病毒扫描
   - 使用第三方服务如 ClamAV
