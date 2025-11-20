# API文档

## 项目概述
基于Spring Boot的Web应用，提供用户管理、美食信息管理、订单管理等功能。系统采用前后端分离架构，后端提供RESTful API接口，前端通过调用这些接口实现业务功能。


## 目录
1. [用户管理API](#1-用户管理api)
2. [美食信息API](#2-美食信息api)
3. [美食分类API](#3-美食分类api)
4. [美食店API](#4-美食店api)
5. [订单API](#5-订单api)
6. [评价API](#6-评价api)
7. [收藏API](#7-收藏api)
8. [新闻API](#8-新闻api)
9. [文件上传API](#9-文件上传api)
10. [通用API](#10-通用api)
11. [错误码说明](#11-错误码说明)
12. [示例代码](#12-示例代码)

---

## 1. 用户管理API

### 1.1 用户登录
- URL: `/yonghu/login`
- 方法: POST
- 权限: 公开
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | username | String | 是 | 用户名 |
  | password | String | 是 | 密码 |
  | captcha | String | 否 | 验证码 |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 数据 |
  | data.token | String | 登录令牌 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
  }
  ```

### 1.2 用户注册
- URL: `/yonghu/register`
- 方法: POST
- 权限: 公开
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | yonghuzhanghao | String | 是 | 用户账号 |
  | mima | String | 是 | 密码 |
  | xingming | String | 是 | 姓名 |
  | shouji | String | 是 | 手机 |
  | youxiang | String | 否 | 邮箱 |
  | xingbie | String | 否 | 性别 |
  | touxiang | String | 否 | 头像 |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 数据 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": null
  }
  ```

### 1.3 获取用户信息
- URL: `/yonghu/session`
- 方法: GET
- 权限: 登录用户
- 请求头:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | Authorization | String | 是 | Bearer token |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 用户信息 |
  | data.id | Long | 用户ID |
  | data.yonghuzhanghao | String | 用户账号 |
  | data.xingming | String | 姓名 |
  | data.shouji | String | 手机 |
  | data.youxiang | String | 邮箱 |
  | data.xingbie | String | 性别 |
  | data.touxiang | String | 头像 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "id": 1,
      "yonghuzhanghao": "testuser",
      "xingming": "测试用户",
      "shouji": "13800138000",
      "youxiang": "test@example.com",
      "xingbie": "男",
      "touxiang": "http://example.com/upload/avatar.jpg"
    }
  }
  ```

---

## 2. 美食信息API

### 2.1 获取美食列表
- URL: `/meishixinxi/list`
- 方法: GET
- 权限: 公开
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | page | Integer | 否 | 页码，默认1 |
  | limit | Integer | 否 | 每页数量，默认10 |
  | keyword | String | 否 | 搜索关键词 |
  | meishifenlei | String | 否 | 美食分类 |
  | minprice | Double | 否 | 最低价格 |
  | maxprice | Double | 否 | 最高价格 |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 数据 |
  | data.total | Integer | 总记录数 |
  | data.list | Array | 美食列表 |
  | data.list[].id | Long | 美食ID |
  | data.list[].meishimingcheng | String | 美食名称 |
  | data.list[].meishifenlei | String | 美食分类 |
  | data.list[].jiage | Double | 价格 |
  | data.list[].tupian | String | 图片 |
  | data.list[].clicknum | Integer | 点击量 |
  | data.list[].shangjiashijian | String | 上架时间 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "total": 100,
      "list": [
        {
          "id": 1,
          "meishimingcheng": "宫保鸡丁",
          "meishifenlei": "川菜",
          "jiage": 38.00,
          "tupian": "http://example.com/images/gongbao.jpg",
          "clicknum": 123,
          "shangjiashijian": "2023-06-15"
        },
        // 更多美食...
      ]
    }
  }
  ```

### 2.2 获取美食详情
- URL: `/meishixinxi/detail/{id}`
- 方法: GET
- 权限: 公开
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | id | Long | 是 | 美食ID |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 美食详情 |
  | data.id | Long | 美食ID |
  | data.meishimingcheng | String | 美食名称 |
  | data.meishifenlei | String | 美食分类 |
  | data.jiage | Double | 价格 |
  | data.tupian | String | 图片 |
  | data.beizhu | String | 备注 |
  | data.shangjiashijian | String | 上架时间 |
  | data.dianpumingcheng | String | 店铺名称 |
  | data.dianpuzhanghao | String | 店铺账号 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "id": 1,
      "meishimingcheng": "宫保鸡丁",
      "meishifenlei": "川菜",
      "jiage": 38.00,
      "tupian": "http://example.com/images/gongbao.jpg",
      "beizhu": "传统川菜，麻辣鲜香",
      "shangjiashijian": "2023-06-15",
      "dianpumingcheng": "川味居",
      "dianpuzhanghao": "chuanweiju"
    }
  }
  ```

---

## 3. 美食分类API

### 3.1 获取美食分类列表
- URL: `/meishifenlei/list`
- 方法: GET
- 权限: 公开
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | page | Integer | 否 | 页码，默认1 |
  | limit | Integer | 否 | 每页数量，默认10 |
  | keyword | String | 否 | 搜索关键词 |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 数据 |
  | data.total | Integer | 总记录数 |
  | data.list | Array | 分类列表 |
  | data.list[].id | Long | 分类ID |
  | data.list[].fenleimingcheng | String | 分类名称 |
  | data.list[].tupian | String | 分类图片 |
  | data.list[].shangchuanren | String | 上传人 |
  | data.list[].shangchuanshijian | String | 上传时间 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "total": 10,
      "list": [
        {
          "id": 1,
          "fenleimingcheng": "川菜",
          "tupian": "http://example.com/images/chuan cai.jpg",
          "shangchuanren": "admin",
          "shangchuanshijian": "2023-06-15"
        },
        // 更多分类...
      ]
    }
  }
  ```

---

## 4. 美食店API

### 4.1 获取美食店列表
- URL: `/meishidian/list`
- 方法: GET
- 权限: 公开
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | page | Integer | 否 | 页码，默认1 |
  | limit | Integer | 否 | 每页数量，默认10 |
  | keyword | String | 否 | 搜索关键词 |
  | diqu | String | 否 | 地区 |
  | pingfen | Double | 否 | 最低评分 |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 数据 |
  | data.total | Integer | 总记录数 |
  | data.list | Array | 美食店列表 |
  | data.list[].id | Long | 美食店ID |
  | data.list[].dianpumingcheng | String | 店铺名称 |
  | data.list[].dianpuzhanghao | String | 店铺账号 |
  | data.list[].dianpudizhi | String | 店铺地址 |
  | data.list[].dianhua | String | 联系电话 |
  | data.list[].fengmian | String | 封面图片 |
  | data.list[].pingfen | Double | 评分 |
  | data.list[].canyurenshu | Integer | 参与人数 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "total": 50,
      "list": [
        {
          "id": 1,
          "dianpumingcheng": "川味居",
          "dianpuzhanghao": "chuanweiju",
          "dianpudizhi": "北京市朝阳区",
          "dianhua": "010-12345678",
          "fengmian": "http://example.com/images/chuanweiju.jpg",
          "pingfen": 4.8,
          "canyurenshu": 1234
        },
        // 更多美食店...
      ]
    }
  }
  ```

---

## 5. 订单API

### 5.1 创建订单
- URL: `/meishidingdan/add`
- 方法: POST
- 权限: 登录用户
- 请求头:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | Authorization | String | 是 | Bearer token |
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | meishimingcheng | String | 是 | 美食名称 |
  | meishidian | String | 是 | 美食店 |
  | shuliang | Integer | 是 | 数量 |
  | zongjine | Double | 是 | 总金额 |
  | shouhuodizhi | String | 是 | 收货地址 |
  | shouji | String | 是 | 联系电话 |
  | beizhu | String | 否 | 备注 |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 数据 |
  | data.id | Long | 订单ID |
  | data.dingdanbianhao | String | 订单编号 |
  | data.zhifu fangshi | String | 支付方式 |
  | data.zhifu zhuangtai | String | 支付状态 |
  | data.addtime | String | 创建时间 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "id": 1001,
      "dingdanbianhao": "ORD20230615001",
      "zhifufangshi": "微信支付",
      "zhifuzhuangtai": "未支付",
      "addtime": "2023-06-15 12:34:56"
    }
  }
  ```

### 5.2 获取订单列表
- URL: `/meishidingdan/list`
- 方法: GET
- 权限: 登录用户
- 请求头:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | Authorization | String | 是 | Bearer token |
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | page | Integer | 否 | 页码，默认1 |
  | limit | Integer | 否 | 每页数量，默认10 |
  | zhuangtai | String | 否 | 订单状态 |
  | starttime | String | 否 | 开始时间 |
  | endtime | String | 否 | 结束时间 |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 数据 |
  | data.total | Integer | 总记录数 |
  | data.list | Array | 订单列表 |
  | data.list[].id | Long | 订单ID |
  | data.list[].dingdanbianhao | String | 订单编号 |
  | data.list[].meishimingcheng | String | 美食名称 |
  | data.list[].meishidian | String | 美食店 |
  | data.list[].shuliang | Integer | 数量 |
  | data.list[].zongjine | Double | 总金额 |
  | data.list[].zhifuzhuangtai | String | 支付状态 |
  | data.list[].fahuo zhuangtai | String | 发货状态 |
  | data.list[].addtime | String | 创建时间 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "total": 10,
      "list": [
        {
          "id": 1001,
          "dingdanbianhao": "ORD20230615001",
          "meishimingcheng": "宫保鸡丁",
          "meishidian": "川味居",
          "shuliang": 2,
          "zongjine": 76.00,
          "zhifuzhuangtai": "已支付",
          "fahuozhuangtai": "已发货",
          "addtime": "2023-06-15 12:34:56"
        },
        // 更多订单...
      ]
    }
  }
  ```

---

## 6. 评价API

### 6.1 添加美食评价
- URL: `/meishipingjia/add`
- 方法: POST
- 权限: 登录用户
- 请求头:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | Authorization | String | 是 | Bearer token |
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | meishimingcheng | String | 是 | 美食名称 |
  | meishidian | String | 是 | 美食店 |
  | pingfen | Integer | 是 | 评分（1-5） |
  | pingjiabiaoti | String | 是 | 评价标题 |
  | pingjiacontent | String | 是 | 评价内容 |
  | tupian | String | 否 | 图片 |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 数据 |
  | data.id | Long | 评价ID |
  | data.addtime | String | 创建时间 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "id": 2001,
      "addtime": "2023-06-16 10:23:45"
    }
  }
  ```

---

## 7. 收藏API

### 7.1 添加收藏
- URL: `/storeup/add`
- 方法: POST
- 权限: 登录用户
- 请求头:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | Authorization | String | 是 | Bearer token |
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | tablename | String | 是 | 表名（meishixinxi, meishidian等） |
  | refid | Long | 是 | 关联ID |
  | name | String | 是 | 名称 |
  | picture | String | 否 | 图片 |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 数据 |
  | data.id | Long | 收藏ID |
  | data.addtime | String | 创建时间 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "id": 3001,
      "addtime": "2023-06-17 09:12:34"
    }
  }
  ```

---

## 8. 新闻API

### 8.1 获取新闻列表
- URL: `/news/list`
- 方法: GET
- 权限: 公开
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | page | Integer | 否 | 页码，默认1 |
  | limit | Integer | 否 | 每页数量，默认10 |
  | keyword | String | 否 | 搜索关键词 |
  | newsleibie | String | 否 | 新闻类别 |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 数据 |
  | data.total | Integer | 总记录数 |
  | data.list | Array | 新闻列表 |
  | data.list[].id | Long | 新闻ID |
  | data.list[].newsbiaoti | String | 新闻标题 |
  | data.list[].newsneirong | String | 新闻内容 |
  | data.list[].newsleibie | String | 新闻类别 |
  | data.list[].picture | String | 图片 |
  | data.list[].addtime | String | 创建时间 |
  | data.list[].clicknum | Integer | 点击量 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "total": 20,
      "list": [
        {
          "id": 4001,
          "newsbiaoti": "新品上市：夏季特饮",
          "newsneirong": "夏季特饮系列已全新上市，欢迎品尝！",
          "newsleibie": "新品推荐",
          "picture": "http://example.com/images/drink.jpg",
          "addtime": "2023-06-18 14:23:45",
          "clicknum": 567
        },
        // 更多新闻...
      ]
    }
  }
  ```

---

## 9. 文件上传API

### 9.1 文件上传
- URL: `/file/upload`
- 方法: POST
- 权限: 登录用户
- 请求头:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | Authorization | String | 是 | Bearer token |
  | Content-Type | String | 是 | multipart/form-data |
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | file | File | 是 | 上传文件 |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Object | 数据 |
  | data.url | String | 文件URL |
  | data.filename | String | 文件名 |
  | data.size | Long | 文件大小 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "url": "http://example.com/upload/20230615/abcdef123456.jpg",
      "filename": "abcdef123456.jpg",
      "size": 123456
    }
  }
  ```

---

## 10. 通用API

### 10.1 获取验证码
- URL: `/common/getCaptcha`
- 方法: GET
- 权限: 公开
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | uuid | String | 是 | UUID |
- 响应: 图片流

### 10.2 验证验证码
- URL: `/common/checkCaptcha`
- 方法: POST
- 权限: 公开
- 请求参数:
  | 参数名 | 类型 | 是否必填 | 描述 |
  |--------|------|----------|------|
  | uuid | String | 是 | UUID |
  | code | String | 是 | 验证码 |
- 响应参数:
  | 参数名 | 类型 | 描述 |
  |--------|------|------|
  | code | Integer | 错误码 |
  | msg | String | 消息 |
  | data | Boolean | 是否验证通过 |
- 响应示例:
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": true
  }
  ```

---

## 11. 错误码说明

| 错误码 | 说明 |
|--------|------|
| 0 | 成功 |
| 1 | 参数错误 |
| 2 | 未登录 |
| 3 | 权限不足 |
| 4 | 数据不存在 |
| 5 | 服务器错误 |
| 6 | 重复操作 |
| 7 | 验证码错误 |
| 8 | 账号或密码错误 |
| 9 | 账号已存在 |
| 10 | 订单不存在 |
| 11 | 订单状态错误 |
| 12 | 支付失败 |
| 13 | 库存不足 |
| 14 | 文件上传失败 |
| 15 | 文件大小超过限制 |
| 16 | 文件类型不允许 |
| 17 | 收藏已存在 |
| 18 | 评价已存在 |
| 19 | 数据已被删除 |
| 20 | 数据已被锁定 |

---

## 12. 示例代码

### JavaScript示例
```javascript
// 用户登录
async function login(username, password) {
  try {
    const response = await fetch('http://localhost:8080/yonghu/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `username=${username}&password=${password}`
    });
    const data = await response.json();
    if (data.code === 0) {
      localStorage.setItem('token', data.data.token);
      return true;
    } else {
      console.error(data.msg);
      return false;
    }
  } catch (error) {
    console.error('登录失败:', error);
    return false;
  }
}

// 获取美食列表
async function getFoodList(page = 1, limit = 10, keyword = '') {
  try {
    const token = localStorage.getItem('token');
    const response = await fetch(`http://localhost:8080/meishixinxi/list?page=${page}&limit=${limit}&keyword=${keyword}`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    const data = await response.json();
    if (data.code === 0) {
      return data.data;
    } else {
      console.error(data.msg);
      return null;
    }
  } catch (error) {
    console.error('获取美食列表失败:', error);
    return null;
  }
}
```

### Python示例
```python
import requests

# 用户登录
def login(username, password):
    url = 'http://localhost:8080/yonghu/login'
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        result = response.json()
        if result['code'] == 0:
            return result['data']['token']
    return None

# 获取美食列表
def get_food_list(token, page=1, limit=10, keyword=''):
    url = f'http://localhost:8080/meishixinxi/list?page={page}&limit={limit}&keyword={keyword}'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        if result['code'] == 0:
            return result['data']
    return None
```

### Java示例
```java
import okhttp3.*;
import org.json.JSONObject;

import java.io.IOException;

public class ApiExample {
    private static final String BASE_URL = "http://localhost:8080";
    private static String token;

    // 用户登录
    public static boolean login(String username, String password) throws IOException {
        OkHttpClient client = new OkHttpClient();
        RequestBody formBody = new FormBody.Builder()
                .add("username", username)
                .add("password", password)
                .build();

        Request request = new Request.Builder()
                .url(BASE_URL + "/yonghu/login")
                .post(formBody)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (response.isSuccessful()) {
                JSONObject json = new JSONObject(response.body().string());
                if (json.getInt("code") == 0) {
                    token = json.getJSONObject("data").getString("token");
                    return true;
                }
            }
            return false;
        }
    }

    // 获取美食列表
    public static JSONObject getFoodList(int page, int limit, String keyword) throws IOException {
        OkHttpClient client = new OkHttpClient();
        HttpUrl.Builder urlBuilder = HttpUrl.parse(BASE_URL + "/meishixinxi/list").newBuilder()
                .addQueryParameter("page", String.valueOf(page))
                .addQueryParameter("limit", String.valueOf(limit));
        
        if (keyword != null && !keyword.isEmpty()) {
            urlBuilder.addQueryParameter("keyword", keyword);
        }

        Request request = new Request.Builder()
                .url(urlBuilder.build())
                .addHeader("Authorization", "Bearer " + token)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (response.isSuccessful()) {
                return new JSONObject(response.body().string());
            }
            return null;
        }
    }
}
```
