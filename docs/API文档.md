# 食客在线 - 完整API接口文档

> **项目名称**: 食客在线 (FoodieOnline)  
> **基础路径**: `http://localhost:8080/foodie-online`  
> **文档版本**: v1.0  
> **更新日期**: 2025-11-06

---

## 📋 目录

- [1. 全局说明](#1-全局说明)
- [2. 认证鉴权](#2-认证鉴权)
- [3. 管理员接口](#3-管理员接口)
- [4. 用户接口](#4-用户接口)
- [5. 美食店接口](#5-美食店接口)
- [6. 美食分类接口](#6-美食分类接口)
- [7. 美食信息接口](#7-美食信息接口)
- [8. 美食订单接口](#8-美食订单接口)
- [9. 美食评价接口](#9-美食评价接口)
- [10. 收藏接口](#10-收藏接口)
- [11. 美食资讯接口](#11-美食资讯接口)
- [12. 文件上传下载](#12-文件上传下载)
- [13. 系统配置接口](#13-系统配置接口)
- [14. 数据模型](#14-数据模型)
- [附录A: TypeScript类型定义](#附录a-typescript类型定义)
- [附录B: Axios封装示例](#附录b-axios封装示例)
- [附录C: 前端集成示例](#附录c-前端集成示例)

---

## 1. 全局说明

### 1.1 响应格式

所有接口返回统一JSON格式：

```typescript
// 成功响应
{
  "code": 0,           // 0表示成功
  "msg": "操作成功",    // 消息提示（可选）
  "data": {...}        // 返回数据（可选）
}

// 失败响应
{
  "code": 500,         // 错误码（500或其他）
  "msg": "错误信息"     // 错误描述
}
```

### 1.2 分页响应格式

```typescript
{
  "code": 0,
  "data": {
    "totalCount": 100,      // 总记录数
    "pageSize": 10,         // 每页大小
    "totalPage": 10,        // 总页数
    "currPage": 1,          // 当前页
    "list": [...]           // 数据列表
  }
}
```

### 1.3 通用分页参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `page` | Number | 否 | 页码，默认1 |
| `limit` | Number | 否 | 每页条数，默认10 |
| `sort` | String | 否 | 排序字段，如：`id` |
| `order` | String | 否 | 排序方式：`asc`/`desc` |

### 1.4 认证说明

- **需要认证的接口**：默认需要在请求头携带 Token
- **无需认证的接口**：标注了 `@IgnoreAuth` 的接口

```http
Token: <token>
```

**说明**：后端通过 `Token` 请求头获取认证信息。

### 1.5 日期格式

所有日期字段统一使用格式：`yyyy-MM-dd HH:mm:ss`

示例：`2025-11-06 15:30:00`

### 1.6 密码安全说明

⚠️ **重要提示**：当前系统密码以**明文**形式存储和传输，不适用于生产环境。建议在生产环境中：
- 使用MD5、SHA256或BCrypt等算法加密密码
- 使用HTTPS协议传输敏感信息
- 实施密码强度策略

### 1.7 异常处理

所有接口在发生错误时返回统一格式：

```json
{
  "code": 500,
  "msg": "具体错误描述"
}
```

常见错误码：
- `0`: 操作成功
- `500`: 服务器错误或业务逻辑错误
- 具体错误信息通过 `msg` 字段返回

---

---

## 2. 认证鉴权

### 2.1 管理员登录

**接口**: `POST /users/login`  
**无需认证**: ✅

**请求参数** (Form Data):
```typescript
{
  username: string;    // 管理员账号
  password: string;    // 密码
  captcha?: string;    // 验证码（可选）
}
```

**响应示例**:
```json
{
  "code": 0,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

### 2.2 用户登录

**接口**: `POST /yonghu/login`  
**无需认证**: ✅

**请求参数** (Form Data):
```typescript
{
  username: string;    // 用户账号
  password: string;    // 密码
  captcha?: string;    // 验证码（可选）
}
```

**响应示例**:
```json
{
  "code": 0,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

### 2.3 美食店登录

**接口**: `POST /meishidian/login`  
**无需认证**: ✅

**请求参数** (Form Data):
```typescript
{
  username: string;    // 店铺账号
  password: string;    // 密码
  captcha?: string;    // 验证码（可选）
}
```

**响应示例**:
```json
{
  "code": 0,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

### 2.4 用户注册

**接口**: `POST /yonghu/register`  
**无需认证**: ✅

**请求体** (JSON):
```typescript
{
  yonghuzhanghao: string;    // 用户账号（必填）
  mima: string;              // 密码（必填）
  yonghuxingming?: string;   // 用户姓名
  xingbie?: string;          // 性别
  nianling?: number;         // 年龄
  touxiang?: string;         // 头像URL
  yonghushouji?: string;     // 用户手机
  peisongdizhi?: string;     // 配送地址
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "注册成功"
}
```

---

### 2.5 美食店注册

**接口**: `POST /meishidian/register`  
**无需认证**: ✅

**请求体** (JSON):
```typescript
{
  dianpuzhanghao: string;    // 店铺账号（必填）
  mima: string;              // 密码（必填）
  dianpumingcheng?: string;  // 店铺名称
  zhaopian?: string;         // 照片URL
  lianxidianhua?: string;    // 联系电话
  dianpujieshao?: string;    // 店铺介绍
  dianpudizhi?: string;      // 店铺地址
  zhaopaimeishi?: string;    // 招牌美食
  lianxiren?: string;        // 联系人
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "注册成功"
}
```

---

### 2.6 退出登录

**接口**: `GET /users/logout` | `POST /yonghu/logout` | `POST /meishidian/logout`  
**需要认证**: ✅

**说明**：管理员退出使用GET方法，用户和美食店退出使用POST方法（或RequestMapping支持所有方法）。

**响应示例**:
```json
{
  "code": 0,
  "msg": "退出成功"
}
```

---

### 2.7 获取当前用户信息

**接口**: `GET /users/session` | `/yonghu/session` | `/meishidian/session`  
**需要认证**: ✅

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "id": 1615458232000,
    "yonghuzhanghao": "user001",
    "yonghuxingming": "张三",
    "xingbie": "男",
    "nianling": 25,
    "touxiang": "upload/1615458232000.jpg",
    "yonghushouji": "13800138000",
    "peisongdizhi": "上海市浦东新区",
    "addtime": "2025-11-06 10:30:00"
  }
}
```

---

### 2.8 密码重置

**接口**: `POST /users/resetPass` | `/yonghu/resetPass` | `/meishidian/resetPass`  
**无需认证**: ✅

**请求参数** (Form Data):
```typescript
{
  username: string;    // 账号
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "密码已重置为：123456"
}
```

---

## 3. 管理员接口

### 3.1 管理员分页列表

**接口**: `GET /users/page`  
**需要认证**: ✅

**请求参数**:
```typescript
{
  page?: number;        // 页码
  limit?: number;       // 每页条数
  username?: string;    // 用户名（模糊查询）
}
```

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "totalCount": 5,
    "pageSize": 10,
    "totalPage": 1,
    "currPage": 1,
    "list": [
      {
        "id": 1,
        "username": "admin",
        "role": "管理员",
        "addtime": "2025-11-06 10:00:00"
      }
    ]
  }
}
```

---

### 3.2 管理员详情

**接口**: `GET /users/info/{id}`  
**需要认证**: ✅

**路径参数**:
- `id`: 管理员ID

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "id": 1,
    "username": "admin",
    "role": "管理员",
    "addtime": "2025-11-06 10:00:00"
  }
}
```

---

### 3.3 添加管理员

**接口**: `POST /users/save`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  username: string;    // 用户名（必填）
  password: string;    // 密码（必填）
  role?: string;       // 角色
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "添加成功"
}
```

---

### 3.4 更新管理员

**接口**: `POST /users/update`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  id: number;          // ID（必填）
  username?: string;   // 用户名
  password?: string;   // 密码
  role?: string;       // 角色
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "更新成功"
}
```

---

### 3.5 删除管理员

**接口**: `POST /users/delete`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
[1, 2, 3]    // 管理员ID数组
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "删除成功"
}
```

---

## 4. 用户接口

### 4.1 用户分页列表

**接口**: `GET /yonghu/page`  
**需要认证**: ✅

**请求参数**:
```typescript
{
  page?: number;            // 页码
  limit?: number;           // 每页条数
  yonghuzhanghao?: string;  // 用户账号（模糊查询）
  yonghuxingming?: string;  // 用户姓名（模糊查询）
  yonghushouji?: string;    // 用户手机（模糊查询）
}
```

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "totalCount": 50,
    "pageSize": 10,
    "totalPage": 5,
    "currPage": 1,
    "list": [
      {
        "id": 1615458232000,
        "yonghuzhanghao": "user001",
        "yonghuxingming": "张三",
        "xingbie": "男",
        "nianling": 25,
        "touxiang": "upload/1615458232000.jpg",
        "yonghushouji": "13800138000",
        "peisongdizhi": "上海市浦东新区",
        "addtime": "2025-11-06 10:30:00"
      }
    ]
  }
}
```

---

### 4.2 前端用户列表（带分页）

**接口**: `GET /yonghu/list`  
**需要认证**: ✅

参数和响应同 `4.1`

---

### 4.3 用户列表（不分页）

**接口**: `GET /yonghu/lists`  
**需要认证**: ✅

**响应示例**:
```json
{
  "code": 0,
  "data": [
    {
      "id": 1615458232000,
      "yonghuzhanghao": "user001",
      "yonghuxingming": "张三",
      // ...其他字段
    }
  ]
}
```

---

### 4.4 用户详情

**接口**: `GET /yonghu/info/{id}` (后端) | `GET /yonghu/detail/{id}` (前端)  
**需要认证**: ✅

**路径参数**:
- `id`: 用户ID

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "id": 1615458232000,
    "yonghuzhanghao": "user001",
    "yonghuxingming": "张三",
    "xingbie": "男",
    "nianling": 25,
    "touxiang": "upload/1615458232000.jpg",
    "yonghushouji": "13800138000",
    "peisongdizhi": "上海市浦东新区",
    "addtime": "2025-11-06 10:30:00"
  }
}
```

---

### 4.5 添加用户（后端）

**接口**: `POST /yonghu/save`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  yonghuzhanghao: string;    // 用户账号（必填）
  mima: string;              // 密码（必填）
  yonghuxingming?: string;   // 用户姓名
  xingbie?: string;          // 性别
  nianling?: number;         // 年龄
  touxiang?: string;         // 头像URL
  yonghushouji?: string;     // 用户手机
  peisongdizhi?: string;     // 配送地址
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "添加成功"
}
```

---

### 4.6 添加用户（前端）

**接口**: `POST /yonghu/add`  
**需要认证**: ✅

请求体同 `4.5`

---

### 4.7 更新用户

**接口**: `POST /yonghu/update`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  id: number;                // ID（必填）
  yonghuzhanghao?: string;   // 用户账号
  mima?: string;             // 密码
  yonghuxingming?: string;   // 用户姓名
  xingbie?: string;          // 性别
  nianling?: number;         // 年龄
  touxiang?: string;         // 头像URL
  yonghushouji?: string;     // 用户手机
  peisongdizhi?: string;     // 配送地址
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "更新成功"
}
```

---

### 4.8 删除用户

**接口**: `POST /yonghu/delete`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
[1615458232000, 1615458233000]    // 用户ID数组
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "删除成功"
}
```

---

## 5. 美食店接口

### 5.1 美食店分页列表

**接口**: `GET /meishidian/page`  
**需要认证**: ✅

**请求参数**:
```typescript
{
  page?: number;              // 页码
  limit?: number;             // 每页条数
  dianpuzhanghao?: string;    // 店铺账号（模糊查询）
  dianpumingcheng?: string;   // 店铺名称（模糊查询）
  lianxidianhua?: string;     // 联系电话（模糊查询）
}
```

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "totalCount": 20,
    "pageSize": 10,
    "totalPage": 2,
    "currPage": 1,
    "list": [
      {
        "id": 1615458232000,
        "dianpuzhanghao": "shop001",
        "dianpumingcheng": "老王烧烤店",
        "zhaopian": "upload/shop001.jpg",
        "lianxidianhua": "13900139000",
        "dianpujieshao": "正宗东北烧烤",
        "dianpudizhi": "上海市徐汇区",
        "zhaopaimeishi": "羊肉串、烤鸡翅",
        "lianxiren": "王老板",
        "addtime": "2025-11-06 09:00:00"
      }
    ]
  }
}
```

---

### 5.2 前端美食店列表（带分页）

**接口**: `GET /meishidian/list`  
**无需认证**: ✅

参数和响应同 `5.1`

---

### 5.3 美食店详情

**接口**: `GET /meishidian/info/{id}` (后端) | `GET /meishidian/detail/{id}` (前端)  
**需要认证**: ✅ (后端) / ❌ (前端 detail)

**路径参数**:
- `id`: 美食店ID

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "id": 1615458232000,
    "dianpuzhanghao": "shop001",
    "dianpumingcheng": "老王烧烤店",
    "zhaopian": "upload/shop001.jpg",
    "lianxidianhua": "13900139000",
    "dianpujieshao": "正宗东北烧烤",
    "dianpudizhi": "上海市徐汇区",
    "zhaopaimeishi": "羊肉串、烤鸡翅",
    "lianxiren": "王老板",
    "addtime": "2025-11-06 09:00:00"
  }
}
```

---

### 5.4 添加美食店（后端）

**接口**: `POST /meishidian/save`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  dianpuzhanghao: string;    // 店铺账号（必填）
  mima: string;              // 密码（必填）
  dianpumingcheng?: string;  // 店铺名称
  zhaopian?: string;         // 照片URL
  lianxidianhua?: string;    // 联系电话
  dianpujieshao?: string;    // 店铺介绍
  dianpudizhi?: string;      // 店铺地址
  zhaopaimeishi?: string;    // 招牌美食
  lianxiren?: string;        // 联系人
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "添加成功"
}
```

---

### 5.5 更新美食店

**接口**: `POST /meishidian/update`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  id: number;                // ID（必填）
  dianpuzhanghao?: string;   // 店铺账号
  mima?: string;             // 密码
  dianpumingcheng?: string;  // 店铺名称
  zhaopian?: string;         // 照片URL
  lianxidianhua?: string;    // 联系电话
  dianpujieshao?: string;    // 店铺介绍
  dianpudizhi?: string;      // 店铺地址
  zhaopaimeishi?: string;    // 招牌美食
  lianxiren?: string;        // 联系人
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "更新成功"
}
```

---

### 5.6 删除美食店

**接口**: `POST /meishidian/delete`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
[1615458232000, 1615458233000]    // 美食店ID数组
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "删除成功"
}
```

---

## 6. 美食分类接口

### 6.1 美食分类分页列表

**接口**: `GET /meishifenlei/page`  
**需要认证**: ✅

**请求参数**:
```typescript
{
  page?: number;          // 页码
  limit?: number;         // 每页条数
  meishifenlei?: string;  // 美食分类（模糊查询）
}
```

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "totalCount": 10,
    "pageSize": 10,
    "totalPage": 1,
    "currPage": 1,
    "list": [
      {
        "id": 1615458232000,
        "meishifenlei": "川菜",
        "addtime": "2025-11-06 08:00:00"
      },
      {
        "id": 1615458233000,
        "meishifenlei": "粤菜",
        "addtime": "2025-11-06 08:10:00"
      }
    ]
  }
}
```

---

### 6.2 前端美食分类列表（带分页）

**接口**: `GET /meishifenlei/list`  
**需要认证**: ✅

**请求参数**: 同 6.1

---

### 6.3 美食分类列表（不分页）

**接口**: `GET /meishifenlei/lists`  
**需要认证**: ✅

**响应示例**:
```json
{
  "code": 0,
  "data": [
    { "id": 1615458232000, "meishifenlei": "川菜" },
    { "id": 1615458233000, "meishifenlei": "粤菜" },
    { "id": 1615458234000, "meishifenlei": "湘菜" }
  ]
}
```

---

### 6.4 美食分类详情

**接口**: `GET /meishifenlei/info/{id}` (后端) | `GET /meishifenlei/detail/{id}` (前端)  
**需要认证**: ✅

**路径参数**:
- `id`: 美食分类ID

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "id": 1615458232000,
    "meishifenlei": "川菜",
    "addtime": "2025-11-06 08:00:00"
  }
}
```

---

### 6.5 添加美食分类

**接口**: `POST /meishifenlei/save` (后端) | `POST /meishifenlei/add` (前端)  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  meishifenlei: string;    // 美食分类（必填）
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "添加成功"
}
```

---

### 6.6 更新美食分类

**接口**: `POST /meishifenlei/update`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  id: number;              // ID（必填）
  meishifenlei?: string;   // 美食分类
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "更新成功"
}
```

---

### 6.7 删除美食分类

**接口**: `POST /meishifenlei/delete`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
[1615458232000, 1615458233000]    // 美食分类ID数组
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "删除成功"
}
```

---

## 7. 美食信息接口

### 7.1 美食信息分页列表

**接口**: `GET /meishixinxi/page`  
**需要认证**: ✅

**特殊说明**:
- 如果是美食店登录，自动过滤只显示该店铺的美食

**请求参数**:
```typescript
{
  page?: number;             // 页码
  limit?: number;            // 每页条数
  meishimingcheng?: string;  // 美食名称（模糊查询）
  meishifenlei?: string;     // 美食分类（精确查询）
  dianpuzhanghao?: string;   // 店铺账号（精确查询）
  dianpumingcheng?: string;  // 店铺名称（模糊查询）
  kouwei?: string;           // 口味（模糊查询）
}
```

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "totalCount": 100,
    "pageSize": 10,
    "totalPage": 10,
    "currPage": 1,
    "list": [
      {
        "id": 1615458232000,
        "meishimingcheng": "宫保鸡丁",
        "meishifenlei": "川菜",
        "dianpuzhanghao": "shop001",
        "dianpumingcheng": "老王烧烤店",
        "lianxidianhua": "13900139000",
        "tupian": "upload/meishi001.jpg",
        "kouwei": "香辣",
        "tese": "传统川菜，麻辣鲜香",
        "jiage": 38,
        "xiangqing": "选用优质鸡腿肉...",
        "clicktime": "2025-11-06 14:20:00",
        "clicknum": 156,
        "addtime": "2025-11-05 10:00:00"
      }
    ]
  }
}
```

---

### 7.2 前端美食信息列表（无需登录）

**接口**: `GET /meishixinxi/list`  
**无需认证**: ✅

参数和响应同 `7.1`

---

### 7.3 美食信息详情

**接口**: `GET /meishixinxi/info/{id}` (后端) | `GET /meishixinxi/detail/{id}` (前端)  
**需要认证**: ✅ (后端) / ❌ (前端 detail)

**特殊说明**:
- 访问时自动增加点击次数 `clicknum + 1`
- 更新最近点击时间 `clicktime`

**路径参数**:
- `id`: 美食信息ID

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "id": 1615458232000,
    "meishimingcheng": "宫保鸡丁",
    "meishifenlei": "川菜",
    "dianpuzhanghao": "shop001",
    "dianpumingcheng": "老王烧烤店",
    "lianxidianhua": "13900139000",
    "tupian": "upload/meishi001.jpg",
    "kouwei": "香辣",
    "tese": "传统川菜，麻辣鲜香",
    "jiage": 38,
    "xiangqing": "选用优质鸡腿肉，配以花生米、干辣椒...",
    "clicktime": "2025-11-06 15:30:00",
    "clicknum": 157,
    "addtime": "2025-11-05 10:00:00"
  }
}
```

---

### 7.4 添加美食信息

**接口**: `POST /meishixinxi/save` (后端) | `POST /meishixinxi/add` (前端)  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  meishimingcheng: string;   // 美食名称（必填）
  meishifenlei: string;      // 美食分类（必填）
  dianpuzhanghao: string;    // 店铺账号（必填）
  dianpumingcheng: string;   // 店铺名称（必填）
  lianxidianhua?: string;    // 联系电话
  tupian?: string;           // 图片URL
  kouwei?: string;           // 口味
  tese?: string;             // 特色
  jiage: number;             // 价格（必填）
  xiangqing?: string;        // 详情
  clicknum?: number;         // 点击次数（默认0）
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "添加成功"
}
```

---

### 7.5 更新美食信息

**接口**: `POST /meishixinxi/update`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  id: number;                // ID（必填）
  meishimingcheng?: string;  // 美食名称
  meishifenlei?: string;     // 美食分类
  dianpuzhanghao?: string;   // 店铺账号
  dianpumingcheng?: string;  // 店铺名称
  lianxidianhua?: string;    // 联系电话
  tupian?: string;           // 图片URL
  kouwei?: string;           // 口味
  tese?: string;             // 特色
  jiage?: number;            // 价格
  xiangqing?: string;        // 详情
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "更新成功"
}
```

---

### 7.6 删除美食信息

**接口**: `POST /meishixinxi/delete`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
[1615458232000, 1615458233000]    // 美食信息ID数组
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "删除成功"
}
```

---

### 7.7 智能排序（按点击量）

**接口**: `GET /meishixinxi/autoSort`  
**无需认证**: ✅

**请求参数**:
```typescript
{
  page?: number;       // 页码
  limit?: number;      // 每页条数
  // 其他查询参数同 7.1
}
```

**特殊说明**:
- 自动按 `clicknum` 降序排序
- 用于首页热门美食推荐

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "totalCount": 100,
    "list": [
      {
        "id": 1615458232000,
        "meishimingcheng": "红烧肉",
        "clicknum": 1280,
        // ...其他字段
      },
      {
        "id": 1615458233000,
        "meishimingcheng": "糖醋排骨",
        "clicknum": 950,
        // ...其他字段
      }
    ]
  }
}
```

---

## 8. 美食订单接口

### 8.1 美食订单分页列表

**接口**: `GET /meishidingdan/page`  
**需要认证**: ✅

**特殊说明**:
- 如果是美食店登录，自动过滤只显示该店铺的订单
- 如果是用户登录，自动过滤只显示该用户的订单

**请求参数**:
```typescript
{
  page?: number;             // 页码
  limit?: number;            // 每页条数
  dingdanbianhao?: string;   // 订单编号（模糊查询）
  meishimingcheng?: string;  // 美食名称（模糊查询）
  dianpuzhanghao?: string;   // 店铺账号（精确查询）
  yonghuzhanghao?: string;   // 用户账号（精确查询）
  sfsh?: string;             // 是否审核：'是'/'否'
  ispay?: string;            // 是否支付：'已支付'/'未支付'
}
```

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "totalCount": 200,
    "pageSize": 10,
    "totalPage": 20,
    "currPage": 1,
    "list": [
      {
        "id": 1615458232000,
        "dingdanbianhao": "DD202511061530001",
        "meishimingcheng": "宫保鸡丁",
        "dianpuzhanghao": "shop001",
        "dianpumingcheng": "老王烧烤店",
        "lianxidianhua": "13900139000",
        "jiage": "38",
        "goumaishuliang": 2,
        "zongjiage": "76",
        "yonghuzhanghao": "user001",
        "yonghuxingming": "张三",
        "yonghushouji": "13800138000",
        "peisongdizhi": "上海市浦东新区XX路XX号",
        "xiadanshijian": "2025-11-06 15:30:00",
        "sfsh": "是",
        "shhf": "订单已确认",
        "ispay": "已支付",
        "addtime": "2025-11-06 15:30:00"
      }
    ]
  }
}
```

---

### 8.2 订单详情

**接口**: `GET /meishidingdan/info/{id}` (后端) | `GET /meishidingdan/detail/{id}` (前端)  
**需要认证**: ✅

**路径参数**:
- `id`: 订单ID

**响应示例**: 同 `8.1` 中的单个订单对象

---

### 8.3 创建订单

**接口**: `POST /meishidingdan/save` (后端) | `POST /meishidingdan/add` (前端)  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  dingdanbianhao: string;    // 订单编号（必填，建议前端生成）
  meishimingcheng: string;   // 美食名称（必填）
  dianpuzhanghao: string;    // 店铺账号（必填）
  dianpumingcheng: string;   // 店铺名称（必填）
  lianxidianhua?: string;    // 联系电话
  jiage: string;             // 单价（必填）
  goumaishuliang: number;    // 购买数量（必填）
  zongjiage: string;         // 总价格（必填，前端计算）
  yonghuzhanghao: string;    // 用户账号（必填）
  yonghuxingming: string;    // 用户姓名（必填）
  yonghushouji: string;      // 用户手机（必填）
  peisongdizhi: string;      // 配送地址（必填）
  xiadanshijian?: string;    // 下单时间（可选，默认当前时间）
  sfsh?: string;             // 是否审核（默认'否'）
  shhf?: string;             // 审核回复
  ispay?: string;            // 是否支付（默认'未支付'）
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "下单成功"
}
```

---

### 8.4 更新订单（审核、支付等）

**接口**: `POST /meishidingdan/update`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  id: number;           // ID（必填）
  sfsh?: string;        // 是否审核：'是'/'否'
  shhf?: string;        // 审核回复
  ispay?: string;       // 是否支付：'已支付'/'未支付'
  // 其他字段可选更新
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "更新成功"
}
```

---

### 8.5 删除订单

**接口**: `POST /meishidingdan/delete`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
[1615458232000, 1615458233000]    // 订单ID数组
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "删除成功"
}
```

---

## 9. 美食评价接口

### 9.1 美食评价分页列表

**接口**: `GET /meishipingjia/page`  
**需要认证**: ✅

**特殊说明**:
- 如果是美食店登录，自动过滤只显示该店铺的评价
- 如果是用户登录，自动过滤只显示该用户的评价

**请求参数**:
```typescript
{
  page?: number;             // 页码
  limit?: number;            // 每页条数
  meishimingcheng?: string;  // 美食名称（模糊查询）
  dianpuzhanghao?: string;   // 店铺账号（精确查询）
  yonghuzhanghao?: string;   // 用户账号（精确查询）
  pingfen?: string;          // 评分（精确查询）
}
```

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "totalCount": 150,
    "pageSize": 10,
    "totalPage": 15,
    "currPage": 1,
    "list": [
      {
        "id": 1615458232000,
        "dianpuzhanghao": "shop001",
        "dianpumingcheng": "老王烧烤店",
        "meishimingcheng": "宫保鸡丁",
        "yonghuzhanghao": "user001",
        "yonghuxingming": "张三",
        "tupian": "upload/pingjia001.jpg",
        "pingfen": "5",
        "pingjianeirong": "非常好吃，味道正宗，下次还会再来！",
        "pingjiashijian": "2025-11-06 16:00:00",
        "addtime": "2025-11-06 16:00:00"
      }
    ]
  }
}
```

---

### 9.2 前端评价列表（无需登录）

**接口**: `GET /meishipingjia/list`  
**无需认证**: ✅

参数和响应同 `9.1`

---

### 9.3 评价详情

**接口**: `GET /meishipingjia/info/{id}` (后端) | `GET /meishipingjia/detail/{id}` (前端)  
**需要认证**: ✅ (后端) / ❌ (前端 detail)

**路径参数**:
- `id`: 评价ID

**响应示例**: 同 `9.1` 中的单个评价对象

---

### 9.4 添加评价

**接口**: `POST /meishipingjia/save` (后端) | `POST /meishipingjia/add` (前端)  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  dianpuzhanghao: string;    // 店铺账号（必填）
  dianpumingcheng: string;   // 店铺名称（必填）
  meishimingcheng: string;   // 美食名称（必填）
  yonghuzhanghao: string;    // 用户账号（必填）
  yonghuxingming: string;    // 用户姓名（必填）
  tupian?: string;           // 图片URL（可选）
  pingfen: string;           // 评分（必填，如：'5'）
  pingjianeirong: string;    // 评价内容（必填）
  pingjiashijian?: string;   // 评价时间（可选，默认当前时间）
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "评价成功"
}
```

---

### 9.5 更新评价

**接口**: `POST /meishipingjia/update`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  id: number;                // ID（必填）
  tupian?: string;           // 图片URL
  pingfen?: string;          // 评分
  pingjianeirong?: string;   // 评价内容
  // 其他字段可选更新
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "更新成功"
}
```

---

### 9.6 删除评价

**接口**: `POST /meishipingjia/delete`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
[1615458232000, 1615458233000]    // 评价ID数组
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "删除成功"
}
```

---

## 10. 收藏接口

### 10.1 收藏分页列表

**接口**: `GET /storeup/page` | `GET /storeup/list`  
**需要认证**: ✅

**特殊说明**:
- 自动过滤只显示当前登录用户的收藏（除非是管理员）

**请求参数**:
```typescript
{
  page?: number;       // 页码
  limit?: number;      // 每页条数
  tablename?: string;  // 表名（精确查询）
  name?: string;       // 收藏名称（模糊查询）
}
```

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "totalCount": 30,
    "pageSize": 10,
    "totalPage": 3,
    "currPage": 1,
    "list": [
      {
        "id": 1615458232000,
        "userid": 1615458230000,
        "refid": 1615458232000,
        "tablename": "meishixinxi",
        "name": "宫保鸡丁",
        "picture": "upload/meishi001.jpg",
        "addtime": "2025-11-06 14:00:00"
      }
    ]
  }
}
```

---

### 10.2 收藏详情

**接口**: `GET /storeup/info/{id}` | `GET /storeup/detail/{id}`  
**需要认证**: ✅

**路径参数**:
- `id`: 收藏ID

**响应示例**: 同 `10.1` 中的单个收藏对象

---

### 10.3 添加收藏

**接口**: `POST /storeup/save` (后端) | `POST /storeup/add` (前端)  
**需要认证**: ✅

**特殊说明**:
- `userid` 自动从 session 中获取

**请求体** (JSON):
```typescript
{
  refid: number;       // 收藏对象ID（必填）
  tablename: string;   // 表名（必填，如：'meishixinxi'）
  name: string;        // 收藏名称（必填）
  picture?: string;    // 收藏图片URL
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "收藏成功"
}
```

---

### 10.4 更新收藏

**接口**: `POST /storeup/update`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  id: number;          // ID（必填）
  name?: string;       // 收藏名称
  picture?: string;    // 收藏图片URL
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "更新成功"
}
```

---

### 10.5 取消收藏

**接口**: `POST /storeup/delete`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
[1615458232000, 1615458233000]    // 收藏ID数组
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "取消成功"
}
```

---

## 11. 美食资讯接口

### 11.1 美食资讯分页列表

**接口**: `GET /news/page`  
**需要认证**: ✅

**请求参数**:
```typescript
{
  page?: number;       // 页码
  limit?: number;      // 每页条数
  title?: string;      // 标题（模糊查询）
}
```

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "totalCount": 50,
    "pageSize": 10,
    "totalPage": 5,
    "currPage": 1,
    "list": [
      {
        "id": 1615458232000,
        "title": "春季美食推荐：养生又美味",
        "introduction": "春季是养生的好时节，这些美食值得一试...",
        "picture": "upload/news001.jpg",
        "content": "<p>春季养生美食详细介绍...</p>",
        "addtime": "2025-11-06 08:00:00"
      }
    ]
  }
}
```

---

### 11.2 前端资讯列表（无需登录）

**接口**: `GET /news/list`  
**无需认证**: ✅

参数和响应同 `11.1`

---

### 11.3 资讯详情

**接口**: `GET /news/info/{id}` (后端) | `GET /news/detail/{id}` (前端)  
**需要认证**: ✅ (后端) / ❌ (前端 detail)

**路径参数**:
- `id`: 资讯ID

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "id": 1615458232000,
    "title": "春季美食推荐：养生又美味",
    "introduction": "春季是养生的好时节，这些美食值得一试...",
    "picture": "upload/news001.jpg",
    "content": "<p>春季养生美食详细介绍：\n1. 春笋炒肉...\n2. 荠菜饺子...</p>",
    "addtime": "2025-11-06 08:00:00"
  }
}
```

---

### 11.4 添加资讯

**接口**: `POST /news/save` (后端) | `POST /news/add` (前端)  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  title: string;           // 标题（必填）
  introduction?: string;   // 简介
  picture?: string;        // 图片URL
  content: string;         // 内容（必填，支持HTML）
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "添加成功"
}
```

---

### 11.5 更新资讯

**接口**: `POST /news/update`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  id: number;              // ID（必填）
  title?: string;          // 标题
  introduction?: string;   // 简介
  picture?: string;        // 图片URL
  content?: string;        // 内容（支持HTML）
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "更新成功"
}
```

---

### 11.6 删除资讯

**接口**: `POST /news/delete`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
[1615458232000, 1615458233000]    // 资讯ID数组
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "删除成功"
}
```

---

## 12. 文件上传下载

### 12.1 文件上传

**接口**: `POST /file/upload`  
**需要认证**: ✅

**请求类型**: `multipart/form-data`

**请求参数**:
```typescript
{
  file: File;      // 文件对象（必填）
  type?: string;   // 类型：'1' 表示人脸识别文件
}
```

**响应示例**:
```json
{
  "code": 0,
  "file": "1699259400000.jpg"
}
```

**前端示例 (Axios)**:
```typescript
const formData = new FormData();
formData.append('file', fileObject);

axios.post('/foodie-online/file/upload', formData, {
  headers: {
    'Content-Type': 'multipart/form-data',
    'Token': localStorage.getItem('token')
  }
}).then(res => {
  console.log('文件名:', res.data.file);
  // 完整URL: http://localhost:8080/foodie-online/upload/1699259400000.jpg
});
```

---

### 12.2 文件下载

**接口**: `GET /file/download`  
**无需认证**: ✅

**请求参数**:
```typescript
{
  fileName: string;    // 文件名（必填）
}
```

**示例**:
```
GET /foodie-online/file/download?fileName=1699259400000.jpg
```

**响应**: 文件流 (直接下载)

---

### 12.3 图片访问路径

上传成功后，可以通过以下路径访问图片：

```
http://localhost:8080/foodie-online/upload/{fileName}
```

**示例**:
```html
<img src="http://localhost:8080/foodie-online/upload/1699259400000.jpg" />
```

---

## 13. 系统配置接口

### 13.1 配置分页列表

**接口**: `GET /config/page`  
**需要认证**: ✅

**请求参数**:
```typescript
{
  page?: number;       // 页码
  limit?: number;      // 每页条数
}
```

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "totalCount": 10,
    "list": [
      {
        "id": 1,
        "name": "systemName",
        "value": "食客在线",
        "addtime": "2025-11-06 08:00:00"
      }
    ]
  }
}
```

---

### 13.2 配置详情

**接口**: `GET /config/info/{id}` | `GET /config/detail/{id}`  
**需要认证**: ✅ (info) / ❌ (detail)

**路径参数**:
- `id`: 配置ID

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "id": 1,
    "name": "systemName",
    "value": "食客在线"
  }
}
```

---

### 13.3 根据name获取配置

**接口**: `GET /config/info?name={name}`  
**需要认证**: ✅

**请求参数**:
```typescript
{
  name: string;    // 配置名称（必填，但当前代码中固定查询 "faceFile"）
}
```

⚠️ **重要提示**：当前代码存在BUG，该接口硬编码查询 `"faceFile"` 配置，忽略传入的 `name` 参数。建议修复代码：
```java
// 修复前（当前代码）
ConfigEntity config = configService.selectOne(new EntityWrapper<ConfigEntity>().eq("name", "faceFile"));

// 修复后（建议）
ConfigEntity config = configService.selectOne(new EntityWrapper<ConfigEntity>().eq("name", name));
```

**响应示例**:
```json
{
  "code": 0,
  "data": {
    "id": 1,
    "name": "faceFile",
    "value": "upload/face/1234567890.jpg"
  }
}
```

---

### 13.4 添加配置

**接口**: `POST /config/save`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  name: string;     // 配置名称（必填）
  value: string;    // 配置值（必填）
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "添加成功"
}
```

---

### 13.5 更新配置

**接口**: `POST /config/update`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
{
  id: number;       // ID（必填）
  name?: string;    // 配置名称
  value?: string;   // 配置值
}
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "更新成功"
}
```

---

### 13.6 删除配置

**接口**: `POST /config/delete`  
**需要认证**: ✅

**请求体** (JSON):
```typescript
[1, 2, 3]    // 配置ID数组
```

**响应示例**:
```json
{
  "code": 0,
  "msg": "删除成功"
}
```

---

## 14. 数据模型

### 14.1 用户 (Yonghu)

```typescript
interface Yonghu {
  id: number;                   // 主键ID
  yonghuzhanghao: string;       // 用户账号
  mima: string;                 // 密码
  yonghuxingming: string;       // 用户姓名
  xingbie: string;              // 性别
  nianling: number;             // 年龄
  touxiang: string;             // 头像URL
  yonghushouji: string;         // 用户手机
  peisongdizhi: string;         // 配送地址
  addtime: string;              // 添加时间 (yyyy-MM-dd HH:mm:ss)
}
```

---

### 14.2 美食店 (Meishidian)

```typescript
interface Meishidian {
  id: number;                   // 主键ID
  dianpuzhanghao: string;       // 店铺账号
  mima: string;                 // 密码
  dianpumingcheng: string;      // 店铺名称
  zhaopian: string;             // 照片URL
  lianxidianhua: string;        // 联系电话
  dianpujieshao: string;        // 店铺介绍
  dianpudizhi: string;          // 店铺地址
  zhaopaimeishi: string;        // 招牌美食
  lianxiren: string;            // 联系人
  addtime: string;              // 添加时间
}
```

---

### 14.3 美食分类 (Meishifenlei)

```typescript
interface Meishifenlei {
  id: number;                   // 主键ID
  meishifenlei: string;         // 美食分类
  addtime: string;              // 添加时间
}
```

---

### 14.4 美食信息 (Meishixinxi)

```typescript
interface Meishixinxi {
  id: number;                   // 主键ID
  meishimingcheng: string;      // 美食名称
  meishifenlei: string;         // 美食分类
  dianpuzhanghao: string;       // 店铺账号
  dianpumingcheng: string;      // 店铺名称
  lianxidianhua: string;        // 联系电话
  tupian: string;               // 图片URL
  kouwei: string;               // 口味
  tese: string;                 // 特色
  jiage: number;                // 价格
  xiangqing: string;            // 详情（富文本）
  clicktime: string;            // 最近点击时间
  clicknum: number;             // 点击次数
  addtime: string;              // 添加时间
}
```

---

### 14.5 美食订单 (Meishidingdan)

```typescript
interface Meishidingdan {
  id: number;                   // 主键ID
  dingdanbianhao: string;       // 订单编号
  meishimingcheng: string;      // 美食名称
  dianpuzhanghao: string;       // 店铺账号
  dianpumingcheng: string;      // 店铺名称
  lianxidianhua: string;        // 联系电话
  jiage: string;                // 价格（使用String避免浮点精度问题）
  goumaishuliang: number;       // 购买数量
  zongjiage: string;            // 总价格（使用String避免浮点精度问题）
  yonghuzhanghao: string;       // 用户账号
  yonghuxingming: string;       // 用户姓名
  yonghushouji: string;         // 用户手机
  peisongdizhi: string;         // 配送地址
  xiadanshijian: string;        // 下单时间（格式：yyyy-MM-dd HH:mm:ss）
  sfsh: string;                 // 是否审核：'是'/'否'
  shhf: string;                 // 审核回复
  ispay: string;                // 是否支付：'已支付'/'未支付'
  addtime: string;              // 添加时间
}
```

**说明**：价格字段（`jiage`、`zongjiage`）使用字符串类型，这是为了避免浮点数运算精度问题，在金融相关场景中这是常见做法。

---

### 14.6 美食评价 (Meishipingjia)

```typescript
interface Meishipingjia {
  id: number;                   // 主键ID
  dianpuzhanghao: string;       // 店铺账号
  dianpumingcheng: string;      // 店铺名称
  meishimingcheng: string;      // 美食名称
  yonghuzhanghao: string;       // 用户账号
  yonghuxingming: string;       // 用户姓名
  tupian: string;               // 图片URL
  pingfen: string;              // 评分（'1'-'5'）
  pingjianeirong: string;       // 评价内容
  pingjiashijian: string;       // 评价时间
  addtime: string;              // 添加时间
}
```

---

### 14.7 收藏表 (Storeup)

```typescript
interface Storeup {
  id: number;                   // 主键ID
  userid: number;               // 用户ID
  refid: number;                // 收藏对象ID
  tablename: string;            // 表名（如：'meishixinxi'）
  name: string;                 // 收藏名称
  picture: string;              // 收藏图片URL
  addtime: string;              // 添加时间
}
```

---

### 14.8 美食资讯 (News)

```typescript
interface News {
  id: number;                   // 主键ID
  title: string;                // 标题
  introduction: string;         // 简介
  picture: string;              // 图片URL
  content: string;              // 内容（富文本HTML）
  addtime: string;              // 添加时间
}
```

---

### 14.9 系统配置 (Config)

```typescript
interface Config {
  id: number;                   // 主键ID
  name: string;                 // 配置名称
  value: string;                // 配置值
}
```

---

## 附录A: TypeScript类型定义文件

可以将以下内容保存为 `api.types.ts`，供前端使用：

```typescript
/**
 * 食客在线 - API类型定义
 * Generated: 2025-11-06
 */

// ==================== 通用类型 ====================

/** 统一响应格式 */
export interface ApiResponse<T = any> {
  code: number;
  msg?: string;
  data?: T;
  token?: string;
}

/** 分页响应格式 */
export interface PageResponse<T = any> {
  totalCount: number;
  pageSize: number;
  totalPage: number;
  currPage: number;
  list: T[];
}

/** 分页请求参数 */
export interface PageParams {
  page?: number;
  limit?: number;
  sort?: string;
  order?: 'asc' | 'desc';
}

// ==================== 实体类型 ====================

/** 用户 */
export interface Yonghu {
  id: number;
  yonghuzhanghao: string;
  mima: string;
  yonghuxingming: string;
  xingbie: string;
  nianling: number;
  touxiang: string;
  yonghushouji: string;
  peisongdizhi: string;
  addtime: string;
}

/** 美食店 */
export interface Meishidian {
  id: number;
  dianpuzhanghao: string;
  mima: string;
  dianpumingcheng: string;
  zhaopian: string;
  lianxidianhua: string;
  dianpujieshao: string;
  dianpudizhi: string;
  zhaopaimeishi: string;
  lianxiren: string;
  addtime: string;
}

/** 美食分类 */
export interface Meishifenlei {
  id: number;
  meishifenlei: string;
  addtime: string;
}

/** 美食信息 */
export interface Meishixinxi {
  id: number;
  meishimingcheng: string;
  meishifenlei: string;
  dianpuzhanghao: string;
  dianpumingcheng: string;
  lianxidianhua: string;
  tupian: string;
  kouwei: string;
  tese: string;
  jiage: number;
  xiangqing: string;
  clicktime: string;
  clicknum: number;
  addtime: string;
}

/** 美食订单 */
export interface Meishidingdan {
  id: number;
  dingdanbianhao: string;
  meishimingcheng: string;
  dianpuzhanghao: string;
  dianpumingcheng: string;
  lianxidianhua: string;
  jiage: string;
  goumaishuliang: number;
  zongjiage: string;
  yonghuzhanghao: string;
  yonghuxingming: string;
  yonghushouji: string;
  peisongdizhi: string;
  xiadanshijian: string;
  sfsh: '是' | '否';
  shhf: string;
  ispay: '已支付' | '未支付';
  addtime: string;
}

/** 美食评价 */
export interface Meishipingjia {
  id: number;
  dianpuzhanghao: string;
  dianpumingcheng: string;
  meishimingcheng: string;
  yonghuzhanghao: string;
  yonghuxingming: string;
  tupian: string;
  pingfen: '1' | '2' | '3' | '4' | '5';
  pingjianeirong: string;
  pingjiashijian: string;
  addtime: string;
}

/** 收藏表 */
export interface Storeup {
  id: number;
  userid: number;
  refid: number;
  tablename: string;
  name: string;
  picture: string;
  addtime: string;
}

/** 美食资讯 */
export interface News {
  id: number;
  title: string;
  introduction: string;
  picture: string;
  content: string;
  addtime: string;
}

/** 系统配置 */
export interface Config {
  id: number;
  name: string;
  value: string;
}
```

---

## 附录B: Axios封装示例

```typescript
/**
 * Axios封装 - 食客在线
 */
import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';
import type { ApiResponse } from './api.types';

// 创建Axios实例
const request: AxiosInstance = axios.create({
  baseURL: 'http://localhost:8080/foodie-online',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json;charset=UTF-8'
  }
});

// 请求拦截器
request.interceptors.request.use(
  (config) => {
    // 从localStorage获取Token
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Token'] = token;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
request.interceptors.response.use(
  (response) => {
    const res = response.data as ApiResponse;
    
    // code为0表示成功
    if (res.code === 0) {
      return res;
    } else {
      // 业务错误处理
      console.error('API Error:', res.msg);
      return Promise.reject(new Error(res.msg || '请求失败'));
    }
  },
  (error) => {
    // HTTP错误处理
    console.error('HTTP Error:', error.message);
    return Promise.reject(error);
  }
);

export default request;
```

---


## 附录C: 前端集成示例

### Vue 3 + TypeScript 示例

**1. 安装依赖**
```bash
npm install axios
```

**2. API调用示例**
```typescript
import request from '@/utils/request';

// 获取美食列表
export const getMeishiList = (params: {
  page?: number;
  limit?: number;
  meishifenlei?: string;
}) => {
  return request.get('/meishixinxi/list', { params });
};

// 用户登录
export const userLogin = (username: string, password: string) => {
  const formData = new FormData();
  formData.append('username', username);
  formData.append('password', password);
  return request.post('/yonghu/login', formData);
};

// 创建订单
export const createOrder = (data: any) => {
  return request.post('/meishidingdan/add', data);
};
```

**3. 组件中使用**
```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { getMeishiList } from '@/api/meishi';

const meishiList = ref([]);
const loading = ref(false);

const loadData = async () => {
  loading.value = true;
  try {
    const res = await getMeishiList({ page: 1, limit: 10 });
    meishiList.value = res.data.list;
  } catch (error) {
    console.error('加载失败:', error);
  } finally {
    loading.value = false;
  }
};

onMounted(() => loadData());
</script>
```

---

**END**
