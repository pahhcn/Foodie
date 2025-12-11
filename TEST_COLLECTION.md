# 收藏功能测试指南

## 功能说明

用户可以收藏喜欢的美食和店铺，并在"我的收藏"页面查看和管理。

### 功能特点
- ✅ 美食收藏
- ✅ 店铺收藏
- ✅ 收藏状态显示（已收藏/未收藏）
- ✅ 一键取消收藏
- ✅ 收藏列表分类展示
- ✅ 快速跳转到详情页

## 测试步骤

### 1. 收藏美食

1. **访问美食详情页**
   ```
   http://localhost:3000/food/41
   ```

2. **点击收藏按钮**
   - 未登录：提示"请先登录"
   - 已登录：显示"收藏成功"
   - 按钮变为"已收藏"（黄色）

3. **再次点击**
   - 显示"已取消收藏"
   - 按钮变回"收藏"（灰色）

### 2. 收藏店铺

1. **访问店铺详情页**
   ```
   http://localhost:3000/shop/21
   ```

2. **点击收藏按钮**
   - 操作同美食收藏

### 3. 查看我的收藏

1. **访问我的收藏页面**
   ```
   http://localhost:3000/user/collection
   ```

2. **查看美食收藏**
   - 默认显示"美食收藏"标签页
   - 显示所有收藏的美食
   - 每个卡片显示：图片、名称、收藏时间、删除按钮

3. **查看店铺收藏**
   - 切换到"店铺收藏"标签页
   - 显示所有收藏的店铺

4. **点击卡片**
   - 跳转到对应的详情页

5. **删除收藏**
   - 点击"删除"按钮
   - 确认删除
   - 收藏从列表中移除

## 数据结构

### 收藏表（storeup）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | Long | 主键 |
| userid | Long | 用户ID |
| refid | Long | 收藏对象ID |
| tablename | String | 表名（meishixinxi/meishidian） |
| name | String | 收藏名称 |
| picture | String | 收藏图片 |
| addtime | Date | 收藏时间 |

### 收藏数据示例

```json
{
  "userid": 1615534336642,
  "refid": 41,
  "tablename": "meishixinxi",
  "name": "美食名称1",
  "picture": "meishixinxi_tupian1.jpg"
}
```

## API 接口

### 1. 添加收藏
```
POST /foodie/storeup/add
Content-Type: application/json

{
  "refid": 41,
  "tablename": "meishixinxi",
  "name": "美食名称",
  "picture": "图片路径"
}
```

### 2. 获取收藏列表
```
GET /foodie/storeup/list?page=1&limit=100&tablename=meishixinxi
```

### 3. 删除收藏
```
POST /foodie/storeup/delete
Content-Type: application/json

[收藏ID]
```

### 4. 检查是否已收藏
```
GET /foodie/storeup/list?refid=41&tablename=meishixinxi&page=1&limit=1
```

## 前端实现

### 1. 收藏 API（src/api/collection.js）
```javascript
// 添加收藏
export const addCollection = (data) => {
  return request({
    url: '/storeup/add',
    method: 'post',
    data
  })
}

// 获取收藏列表
export const getCollectionList = (params) => {
  return request({
    url: '/storeup/list',
    method: 'get',
    params
  })
}

// 删除收藏
export const deleteCollection = (ids) => {
  return request({
    url: '/storeup/delete',
    method: 'post',
    data: ids
  })
}

// 检查是否已收藏
export const checkCollection = (refid, tablename) => {
  return request({
    url: '/storeup/list',
    method: 'get',
    params: { refid, tablename, page: 1, limit: 1 }
  })
}
```

### 2. 美食详情页收藏按钮
```vue
<el-button 
  :type="isCollected ? 'warning' : 'default'"
  :icon="isCollected ? StarFilled : Star"
  @click="handleCollection"
>
  {{ isCollected ? '已收藏' : '收藏' }}
</el-button>
```

### 3. 收藏处理逻辑
```javascript
const handleCollection = async () => {
  if (!userStore.isLoggedIn) {
    ElMessage.warning('请先登录')
    return
  }
  
  if (isCollected.value) {
    // 取消收藏
    await deleteCollection([collectionId.value])
    isCollected.value = false
    ElMessage.success('已取消收藏')
  } else {
    // 添加收藏
    const collectionData = {
      refid: food.value.id,
      tablename: 'meishixinxi',
      name: food.value.meishimingcheng,
      picture: food.value.tupian
    }
    await addCollection(collectionData)
    isCollected.value = true
    ElMessage.success('收藏成功')
  }
}
```

## 测试用例

### 测试用例 1：收藏美食
1. 未登录状态点击收藏
2. 验证：提示"请先登录"
3. 登录后点击收藏
4. 验证：显示"收藏成功"，按钮变为"已收藏"

### 测试用例 2：取消收藏
1. 在已收藏状态下点击按钮
2. 验证：显示"已取消收藏"，按钮变回"收藏"

### 测试用例 3：查看收藏列表
1. 访问"我的收藏"页面
2. 验证：显示所有收藏的美食和店铺
3. 点击卡片
4. 验证：跳转到对应详情页

### 测试用例 4：删除收藏
1. 在收藏列表中点击"删除"
2. 确认删除
3. 验证：收藏从列表中移除

### 测试用例 5：收藏状态持久化
1. 收藏一个美食
2. 刷新页面
3. 验证：按钮仍显示"已收藏"
4. 访问收藏列表
5. 验证：收藏仍然存在

### 测试用例 6：重复收藏
1. 收藏一个美食
2. 取消收藏
3. 再次收藏
4. 验证：可以正常收藏

## 常见问题

### 1. 收藏按钮不显示
**原因：** 页面未正确加载或组件未导入

**解决方法：**
- 检查浏览器控制台错误
- 确认图标组件已导入

### 2. 点击收藏无反应
**原因：** 未登录或后端接口问题

**解决方法：**
- 确认已登录
- 查看 Network 标签页的请求
- 检查后端日志

### 3. 收藏列表为空
**原因：** 没有收藏数据或查询条件错误

**解决方法：**
- 先收藏一些内容
- 检查 API 请求参数
- 查看后端返回数据

### 4. 收藏状态不同步
**原因：** 页面缓存或状态未更新

**解决方法：**
- 刷新页面
- 检查 `checkIfCollected` 函数
- 查看控制台日志

## 调试方法

### 浏览器控制台
打开开发者工具（F12），查看：
```
检查收藏状态失败：...
收藏操作失败：...
```

### Network 标签页
查看以下请求：
1. GET `/foodie/storeup/list` - 检查收藏状态
2. POST `/foodie/storeup/add` - 添加收藏
3. POST `/foodie/storeup/delete` - 删除收藏

### 后端日志
确认后端正确处理收藏请求

## 功能扩展

### 可以添加的功能

1. **收藏数量统计**
   - 在用户中心显示收藏总数
   - 在详情页显示被收藏次数

2. **收藏排序**
   - 按时间排序
   - 按名称排序

3. **收藏搜索**
   - 在收藏列表中搜索

4. **批量操作**
   - 批量删除收藏
   - 批量导出收藏

5. **收藏分享**
   - 分享收藏列表给好友

## 文件清单

### 新增文件
- `foodie-user/src/api/collection.js` - 收藏 API
- `foodie-user/src/views/User/Collection.vue` - 我的收藏页面

### 修改文件
- `foodie-user/src/views/Food/Detail.vue` - 添加收藏按钮
- `foodie-user/src/views/Shop/Detail.vue` - 添加收藏按钮

### 后端文件（已存在）
- `StoreupController.java` - 收藏控制器
- `StoreupEntity.java` - 收藏实体
- `StoreupService.java` - 收藏服务

## 总结

收藏功能已完整实现，包括：
- ✅ 美食收藏
- ✅ 店铺收藏
- ✅ 收藏列表展示
- ✅ 收藏管理（删除）
- ✅ 收藏状态同步
- ✅ 快速跳转

用户可以方便地收藏喜欢的美食和店铺，并在"我的收藏"页面统一管理。
