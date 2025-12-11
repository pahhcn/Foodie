# 文件上传失败调试指南

## 问题：点击上传文件显示文件上传失败

## 调试步骤

### 1. 查看浏览器控制台

打开浏览器开发者工具（F12），切换到 Console 标签页，查看：

```
准备上传文件：{ name: "xxx.jpg", type: "image/jpeg", size: xxx, sizeInMB: "0.5MB" }
文件验证通过，开始上传...
上传响应：{ ... }
上传文件：{ ... }
```

如果看到错误信息，记录下来。

### 2. 查看 Network 标签页

1. 切换到 Network 标签页
2. 选择文件上传
3. 找到 `/foodie/file/upload` 请求
4. 查看：
   - **Status Code**：应该是 200
   - **Request Headers**：检查是否包含 Token
   - **Request Payload**：检查文件是否正确发送
   - **Response**：查看后端返回的内容

### 3. 常见错误及解决方法

#### 错误 1：401 Unauthorized
**原因：** 需要登录认证

**解决方法：**
1. 确认已登录
2. 后端添加 `@IgnoreAuth` 注解（已添加）
3. 重新编译后端

#### 错误 2：404 Not Found
**原因：** 接口路径不正确

**解决方法：**
- 检查上传地址：`/foodie/file/upload`
- 确认后端正在运行
- 检查后端路由配置

#### 错误 3：500 Internal Server Error
**原因：** 后端处理出错

**解决方法：**
1. 查看后端控制台日志
2. 检查文件保存路径是否有权限
3. 检查文件大小限制

#### 错误 4：跨域问题
**原因：** CORS 配置问题

**解决方法：**
- 已添加 CorsConfig，应该不会有跨域问题
- 如果有，检查 CorsConfig 配置

#### 错误 5：文件参数名不匹配
**原因：** 前端发送的参数名与后端接收的不一致

**解决方法：**
- 前端：`name="file"`（已设置）
- 后端：`@RequestParam("file")`（已匹配）

## 修改内容

### 后端修改
```java
// FileController.java
@IgnoreAuth  // 添加此注解，允许未登录用户上传
@RequestMapping("/upload")
public R upload(@RequestParam("file") MultipartFile file,String type) throws Exception {
    // ...
}
```

### 前端修改
```vue
<!-- 添加错误处理和调试日志 -->
<el-upload
  action="/foodie/file/upload"
  :on-success="handleAvatarSuccess"
  :on-error="handleAvatarError"
  :before-upload="beforeAvatarUpload"
  name="file"
>
```

```javascript
// 添加详细日志
const beforeAvatarUpload = (file) => {
  console.log('准备上传文件：', {
    name: file.name,
    type: file.type,
    size: file.size
  })
  // ...
}

const handleAvatarSuccess = (response, file) => {
  console.log('上传响应：', response)
  console.log('上传文件：', file)
  // ...
}

const handleAvatarError = (error) => {
  console.error('上传失败：', error)
  // ...
}
```

## 重新编译后端

修改后端代码后，需要重新编译：

```bash
cd Foodie-main/foodie-backend
mvn clean package -DskipTests
```

然后重启后端应用。

## 测试步骤

1. **确认后端已重启**
2. **刷新浏览器页面**（Ctrl + Shift + R）
3. **打开开发者工具**（F12）
4. **切换到 Console 标签页**
5. **点击上传头像**
6. **选择一张图片**
7. **查看控制台输出**

## 预期输出

### 成功的情况
```
准备上传文件：{ name: "test.jpg", type: "image/jpeg", size: 123456, sizeInMB: "0.12MB" }
文件验证通过，开始上传...
上传响应：{ code: 0, file: "1733241234567.jpg" }
上传文件：{ name: "test.jpg", ... }
头像上传成功
```

### 失败的情况
```
准备上传文件：{ ... }
文件验证通过，开始上传...
上传失败：Error: Request failed with status code 401
头像上传失败，请重试
```

## 检查清单

- [ ] 后端正在运行
- [ ] 后端已添加 `@IgnoreAuth` 注解
- [ ] 后端已重新编译
- [ ] 前端已刷新页面
- [ ] 浏览器控制台无 JavaScript 错误
- [ ] Network 标签页显示请求已发送
- [ ] 文件大小 < 2MB
- [ ] 文件格式为图片（jpg/png/gif）

## 手动测试上传接口

可以使用 Postman 或 curl 测试上传接口：

### 使用 curl
```bash
curl -X POST http://localhost:8080/foodie/file/upload \
  -F "file=@/path/to/image.jpg"
```

### 使用 Postman
1. 创建 POST 请求：`http://localhost:8080/foodie/file/upload`
2. 选择 Body → form-data
3. 添加字段：key = `file`，type = `File`
4. 选择一张图片
5. 发送请求
6. 查看响应：`{ "code": 0, "file": "1733241234567.jpg" }`

## 后端日志

查看后端控制台，应该看到类似的日志：
```
接收到文件上传请求
文件名：test.jpg
文件大小：123456 bytes
保存路径：/path/to/upload/1733241234567.jpg
上传成功
```

如果看到错误日志，记录下来并分析。

## 常见后端错误

### 错误 1：上传文件不能为空
```
com.entity.EIException: 上传文件不能为空
```
**原因：** 文件参数名不匹配或文件未正确发送

### 错误 2：文件保存失败
```
java.io.IOException: Permission denied
```
**原因：** 没有写入权限

**解决方法：** 检查 upload 目录权限

### 错误 3：路径不存在
```
java.io.FileNotFoundException: /path/to/upload
```
**原因：** upload 目录不存在

**解决方法：** 代码会自动创建，如果还是失败，手动创建目录

## 如果还是失败

请提供以下信息：

1. **浏览器控制台的完整错误信息**
2. **Network 标签页中请求的详细信息**
   - Status Code
   - Request Headers
   - Response
3. **后端控制台的错误日志**
4. **文件信息**
   - 文件名
   - 文件大小
   - 文件格式

这样我可以更准确地帮你定位问题。
