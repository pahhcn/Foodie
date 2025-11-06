# API命名转换方案

> **项目**: 食客在线 (FoodieOnline)  
> **日期**: 2025-11-06  
> **说明**: 将拼音命名转换为标准英文RESTful API命名

---

## 1. 接口路径映射表

### 1.1 核心业务接口

| 原路径（拼音） | 新路径（英文） | 说明 | 状态 |
|--------------|--------------|------|------|
| `/yonghu` | `/users` | 用户 | 待迁移 |
| `/meishidian` | `/restaurants` | 美食店/餐厅 | 待迁移 |
| `/meishifenlei` | `/categories` | 美食分类 | 待迁移 |
| `/meishixinxi` | `/foods` | 美食信息 | 待迁移 |
| `/meishidingdan` | `/orders` | 美食订单 | 待迁移 |
| `/meishipingjia` | `/reviews` | 美食评价 | 待迁移 |
| `/storeup` | `/favorites` | 收藏 | 待迁移 |
| `/news` | `/news` | 资讯 | ✅ 已英文 |
| `/config` | `/config` | 系统配置 | ✅ 已英文 |
| `/users` (管理员) | `/admins` | 管理员 | 待迁移 |
| `/file` | `/files` | 文件上传下载 | 建议复数 |

### 1.2 详细接口对照

#### 用户接口 (Users)
```
POST   /yonghu/login          →  POST   /users/login
POST   /yonghu/register       →  POST   /users/register
POST   /yonghu/logout         →  POST   /users/logout
GET    /yonghu/session        →  GET    /users/session
POST   /yonghu/resetPass      →  POST   /users/reset-password
GET    /yonghu/page           →  GET    /users
GET    /yonghu/list           →  GET    /users/public
GET    /yonghu/lists          →  GET    /users/all
GET    /yonghu/info/{id}      →  GET    /users/{id}
GET    /yonghu/detail/{id}    →  GET    /users/{id}/detail
POST   /yonghu/save           →  POST   /users
POST   /yonghu/add            →  POST   /users
POST   /yonghu/update         →  PUT    /users/{id}
POST   /yonghu/delete         →  DELETE /users
```

#### 餐厅接口 (Restaurants)
```
POST   /meishidian/login      →  POST   /restaurants/login
POST   /meishidian/register   →  POST   /restaurants/register
POST   /meishidian/logout     →  POST   /restaurants/logout
GET    /meishidian/session    →  GET    /restaurants/session
POST   /meishidian/resetPass  →  POST   /restaurants/reset-password
GET    /meishidian/page       →  GET    /restaurants
GET    /meishidian/list       →  GET    /restaurants/public
GET    /meishidian/info/{id}  →  GET    /restaurants/{id}
GET    /meishidian/detail/{id}→  GET    /restaurants/{id}/detail
POST   /meishidian/save       →  POST   /restaurants
POST   /meishidian/update     →  PUT    /restaurants/{id}
POST   /meishidian/delete     →  DELETE /restaurants
```

#### 分类接口 (Categories)
```
GET    /meishifenlei/page     →  GET    /categories
GET    /meishifenlei/list     →  GET    /categories
GET    /meishifenlei/lists    →  GET    /categories/all
GET    /meishifenlei/info/{id}→  GET    /categories/{id}
GET    /meishifenlei/detail/{id}→ GET   /categories/{id}
POST   /meishifenlei/save     →  POST   /categories
POST   /meishifenlei/add      →  POST   /categories
POST   /meishifenlei/update   →  PUT    /categories/{id}
POST   /meishifenlei/delete   →  DELETE /categories
```

#### 美食接口 (Foods)
```
GET    /meishixinxi/page      →  GET    /foods
GET    /meishixinxi/list      →  GET    /foods/public
GET    /meishixinxi/info/{id} →  GET    /foods/{id}
GET    /meishixinxi/detail/{id}→ GET    /foods/{id}/detail
POST   /meishixinxi/save      →  POST   /foods
POST   /meishixinxi/add       →  POST   /foods
POST   /meishixinxi/update    →  PUT    /foods/{id}
POST   /meishixinxi/delete    →  DELETE /foods
GET    /meishixinxi/autoSort  →  GET    /foods/popular
```

#### 订单接口 (Orders)
```
GET    /meishidingdan/page    →  GET    /orders
GET    /meishidingdan/info/{id}→ GET    /orders/{id}
GET    /meishidingdan/detail/{id}→GET   /orders/{id}
POST   /meishidingdan/save    →  POST   /orders
POST   /meishidingdan/add     →  POST   /orders
POST   /meishidingdan/update  →  PUT    /orders/{id}
POST   /meishidingdan/delete  →  DELETE /orders
```

#### 评价接口 (Reviews)
```
GET    /meishipingjia/page    →  GET    /reviews
GET    /meishipingjia/list    →  GET    /reviews/public
GET    /meishipingjia/info/{id}→ GET    /reviews/{id}
GET    /meishipingjia/detail/{id}→GET   /reviews/{id}
POST   /meishipingjia/save    →  POST   /reviews
POST   /meishipingjia/add     →  POST   /reviews
POST   /meishipingjia/update  →  PUT    /reviews/{id}
POST   /meishipingjia/delete  →  DELETE /reviews
```

#### 收藏接口 (Favorites)
```
GET    /storeup/page          →  GET    /favorites
GET    /storeup/list          →  GET    /favorites
GET    /storeup/info/{id}     →  GET    /favorites/{id}
GET    /storeup/detail/{id}   →  GET    /favorites/{id}
POST   /storeup/save          →  POST   /favorites
POST   /storeup/add           →  POST   /favorites
POST   /storeup/update        →  PUT    /favorites/{id}
POST   /storeup/delete        →  DELETE /favorites
```

#### 管理员接口 (Admins)
```
POST   /users/login           →  POST   /admins/login
GET    /users/logout          →  POST   /admins/logout
GET    /users/session         →  GET    /admins/session
POST   /users/resetPass       →  POST   /admins/reset-password
GET    /users/page            →  GET    /admins
GET    /users/info/{id}       →  GET    /admins/{id}
POST   /users/save            →  POST   /admins
POST   /users/update          →  PUT    /admins/{id}
POST   /users/delete          →  DELETE /admins
```

#### 文件接口 (Files)
```
POST   /file/upload           →  POST   /files/upload
GET    /file/download         →  GET    /files/download
访问路径 /upload/{fileName}    →  /uploads/{fileName}
```

#### 资讯接口 (News)
```
GET    /news/page             →  GET    /news
GET    /news/list             →  GET    /news/public
GET    /news/info/{id}        →  GET    /news/{id}
GET    /news/detail/{id}      →  GET    /news/{id}
POST   /news/save             →  POST   /news
POST   /news/add              →  POST   /news
POST   /news/update           →  PUT    /news/{id}
POST   /news/delete           →  DELETE /news
```

#### 配置接口 (Config)
```
GET    /config/page           →  GET    /config
GET    /config/info/{id}      →  GET    /config/{id}
GET    /config/detail/{id}    →  GET    /config/{id}
GET    /config/info?name=xxx  →  GET    /config?name=xxx
POST   /config/save           →  POST   /config
POST   /config/update         →  PUT    /config/{id}
POST   /config/delete         →  DELETE /config
```

---

## 2. 数据库表名映射

### 2.1 表名对照

| 原表名（拼音） | 新表名（英文） | 说明 |
|--------------|--------------|------|
| `yonghu` | `users` | 用户表 |
| `meishidian` | `restaurants` | 餐厅表 |
| `meishifenlei` | `food_categories` | 美食分类表 |
| `meishixinxi` | `foods` | 美食信息表 |
| `meishidingdan` | `orders` | 订单表 |
| `meishipingjia` | `reviews` | 评价表 |
| `storeup` | `favorites` | 收藏表 |
| `news` | `news` | 资讯表 |
| `config` | `system_config` | 系统配置表 |
| `users` | `admins` | 管理员表 |
| `token` | `tokens` | Token表 |

### 2.2 字段命名对照

| 原字段名（拼音） | 新字段名（英文） | 类型 | 说明 |
|----------------|----------------|------|------|
| `yonghuzhanghao` | `username` | VARCHAR(200) | 用户账号 |
| `mima` | `password` | VARCHAR(200) | 密码 |
| `yonghuxingming` | `full_name` | VARCHAR(200) | 用户姓名 |
| `xingbie` | `gender` | VARCHAR(200) | 性别 |
| `nianling` | `age` | INT | 年龄 |
| `touxiang` | `avatar` | VARCHAR(255) | 头像 |
| `yonghushouji` | `phone` | VARCHAR(200) | 手机号 |
| `peisongdizhi` | `delivery_address` | VARCHAR(200) | 配送地址 |
| `dianpuzhanghao` | `restaurant_account` | VARCHAR(200) | 店铺账号 |
| `dianpumingcheng` | `restaurant_name` | VARCHAR(200) | 店铺名称 |
| `zhaopian` | `photo` | VARCHAR(255) | 照片 |
| `lianxidianhua` | `contact_phone` | VARCHAR(200) | 联系电话 |
| `dianpujieshao` | `description` | LONGTEXT | 店铺介绍 |
| `dianpudizhi` | `address` | VARCHAR(200) | 店铺地址 |
| `zhaopaimeishi` | `signature_dishes` | VARCHAR(200) | 招牌美食 |
| `lianxiren` | `contact_person` | VARCHAR(200) | 联系人 |
| `meishifenlei` | `category_name` | VARCHAR(200) | 美食分类 |
| `meishimingcheng` | `food_name` | VARCHAR(200) | 美食名称 |
| `tupian` | `image` | VARCHAR(255) | 图片 |
| `kouwei` | `flavor` | VARCHAR(200) | 口味 |
| `tese` | `features` | VARCHAR(200) | 特色 |
| `jiage` | `price` | DECIMAL(10,2) | 价格 |
| `xiangqing` | `details` | LONGTEXT | 详情 |
| `clicktime` | `last_click_time` | DATETIME | 最近点击时间 |
| `clicknum` | `click_count` | INT | 点击次数 |
| `dingdanbianhao` | `order_number` | VARCHAR(200) | 订单编号 |
| `goumaishuliang` | `quantity` | INT | 购买数量 |
| `zongjiage` | `total_price` | DECIMAL(10,2) | 总价格 |
| `xiadanshijian` | `order_time` | DATETIME | 下单时间 |
| `sfsh` | `is_reviewed` | VARCHAR(200) | 是否审核 |
| `shhf` | `review_reply` | LONGTEXT | 审核回复 |
| `ispay` | `payment_status` | VARCHAR(200) | 支付状态 |
| `pingfen` | `rating` | VARCHAR(200) | 评分 |
| `pingjianeirong` | `content` | LONGTEXT | 评价内容 |
| `pingjiashijian` | `review_time` | DATETIME | 评价时间 |
| `userid` | `user_id` | BIGINT | 用户ID |
| `refid` | `reference_id` | BIGINT | 引用对象ID |
| `tablename` | `table_name` | VARCHAR(100) | 表名 |
| `name` | `name` | VARCHAR(100) | 名称 |
| `picture` | `picture` | VARCHAR(200) | 图片 |
| `addtime` | `created_at` | TIMESTAMP | 创建时间 |
| `title` | `title` | VARCHAR(200) | 标题 |
| `introduction` | `introduction` | LONGTEXT | 简介 |
| `content` | `content` | LONGTEXT | 内容 |
| `value` | `value` | VARCHAR(500) | 配置值 |

---

## 3. Java实体类映射

### 3.1 实体类重命名

| 原实体类 | 新实体类 | 表名 |
|---------|---------|------|
| `YonghuEntity` | `UserEntity` | `users` |
| `MeishidianEntity` | `RestaurantEntity` | `restaurants` |
| `MeishifenleiEntity` | `FoodCategoryEntity` | `food_categories` |
| `MeishixinxiEntity` | `FoodEntity` | `foods` |
| `MeishidingdanEntity` | `OrderEntity` | `orders` |
| `MeishipingjiaEntity` | `ReviewEntity` | `reviews` |
| `StoreupEntity` | `FavoriteEntity` | `favorites` |
| `NewsEntity` | `NewsEntity` | `news` |
| `ConfigEntity` | `SystemConfigEntity` | `system_config` |
| `UserEntity` (管理员) | `AdminEntity` | `admins` |
| `TokenEntity` | `TokenEntity` | `tokens` |

### 3.2 Controller重命名

| 原Controller | 新Controller | 路径前缀 |
|-------------|-------------|---------|
| `YonghuController` | `UserController` | `/users` |
| `MeishidianController` | `RestaurantController` | `/restaurants` |
| `MeishifenleiController` | `FoodCategoryController` | `/categories` |
| `MeishixinxiController` | `FoodController` | `/foods` |
| `MeishidingdanController` | `OrderController` | `/orders` |
| `MeishipingjiaController` | `ReviewController` | `/reviews` |
| `StoreupController` | `FavoriteController` | `/favorites` |
| `NewsController` | `NewsController` | `/news` |
| `ConfigController` | `SystemConfigController` | `/config` |
| `UserController` (管理员) | `AdminController` | `/admins` |
| `FileController` | `FileController` | `/files` |

---

## 4. RESTful API规范建议

### 4.1 HTTP方法使用规范

| 操作 | HTTP方法 | 路径示例 | 说明 |
|-----|---------|---------|------|
| 查询列表 | GET | `/foods?page=1&limit=10` | 获取美食列表（分页） |
| 查询详情 | GET | `/foods/{id}` | 获取单个美食详情 |
| 创建资源 | POST | `/foods` | 创建美食 |
| 更新资源 | PUT | `/foods/{id}` | 更新美食（完整更新） |
| 部分更新 | PATCH | `/foods/{id}` | 更新美食（部分字段） |
| 删除资源 | DELETE | `/foods/{id}` | 删除单个美食 |
| 批量删除 | DELETE | `/foods` | 删除多个美食（Body传ID数组） |

### 4.2 URL命名规范

✅ **推荐**：
- 使用复数名词：`/users`, `/foods`, `/orders`
- 使用小写字母：`/food-categories`
- 使用连字符分隔：`/reset-password`, `/favorite-foods`
- RESTful风格：`GET /users/{id}`, `PUT /users/{id}`

❌ **不推荐**：
- 动词形式：`/getUsers`, `/createFood`
- 驼峰命名：`/foodCategories`
- 下划线分隔：`/food_categories`（API路径建议用连字符，数据库用下划线）

### 4.3 状态码使用规范

| 状态码 | 说明 | 使用场景 |
|-------|------|---------|
| 200 OK | 成功 | GET, PUT, PATCH成功 |
| 201 Created | 已创建 | POST成功创建资源 |
| 204 No Content | 无内容 | DELETE成功 |
| 400 Bad Request | 请求错误 | 参数验证失败 |
| 401 Unauthorized | 未授权 | Token失效或未登录 |
| 403 Forbidden | 禁止访问 | 无权限 |
| 404 Not Found | 未找到 | 资源不存在 |
| 500 Internal Server Error | 服务器错误 | 服务器异常 |

---

## 5. 迁移实施步骤

### 阶段1: 准备阶段
1. ✅ 完成API命名映射方案设计
2. ⬜ 备份现有数据库
3. ⬜ 创建新的数据库表结构（英文命名）
4. ⬜ 准备数据迁移脚本

### 阶段2: 后端重构
1. ⬜ 创建新的Entity类（英文命名）
2. ⬜ 创建新的Controller（RESTful风格）
3. ⬜ 更新Service和DAO层
4. ⬜ 配置MyBatis-Plus表名和字段映射
5. ⬜ 编写单元测试

### 阶段3: 数据迁移
1. ⬜ 执行数据库表结构迁移
2. ⬜ 执行数据迁移脚本
3. ⬜ 验证数据完整性

### 阶段4: 前端适配
1. ⬜ 更新前端API调用路径
2. ⬜ 更新TypeScript类型定义
3. ⬜ 更新axios接口封装
4. ⬜ 前后端联调测试

### 阶段5: 兼容性支持（可选）
1. ⬜ 保留旧接口作为兼容层
2. ⬜ 添加接口版本控制（v1, v2）
3. ⬜ 逐步废弃旧接口

---

## 6. 示例代码对比

### 6.1 旧版本（拼音）

**Controller**:
```java
@RestController
@RequestMapping("/meishixinxi")
public class MeishixinxiController {
    @GetMapping("/page")
    public R page(@RequestParam Map<String, Object> params) {
        // ...
    }
}
```

**Entity**:
```java
@TableName("meishixinxi")
public class MeishixinxiEntity {
    private String meishimingcheng;
    private String meishifenlei;
    private Double jiage;
}
```

### 6.2 新版本（英文 + RESTful）

**Controller**:
```java
@RestController
@RequestMapping("/api/v1/foods")
public class FoodController {
    
    @GetMapping
    public ResponseEntity<PageResponse<FoodDTO>> getFoods(
        @RequestParam(defaultValue = "1") int page,
        @RequestParam(defaultValue = "10") int size
    ) {
        // ...
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<FoodDTO> getFoodById(@PathVariable Long id) {
        // ...
    }
    
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public ResponseEntity<FoodDTO> createFood(@RequestBody @Valid FoodDTO food) {
        // ...
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<FoodDTO> updateFood(
        @PathVariable Long id, 
        @RequestBody @Valid FoodDTO food
    ) {
        // ...
    }
    
    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteFood(@PathVariable Long id) {
        // ...
    }
}
```

**Entity**:
```java
@TableName("foods")
public class FoodEntity {
    
    @TableId(type = IdType.AUTO)
    private Long id;
    
    @TableField("food_name")
    private String foodName;
    
    @TableField("category_id")
    private Long categoryId;
    
    @TableField("price")
    private BigDecimal price;
    
    @TableField("created_at")
    private LocalDateTime createdAt;
}
```

---

## 7. 配置文件示例

### application.yml
```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/foodie_online?useUnicode=true&characterEncoding=UTF-8
    username: root
    password: root
    
mybatis-plus:
  configuration:
    # 驼峰转下划线
    map-underscore-to-camel-case: true
  global-config:
    db-config:
      # 逻辑删除
      logic-delete-field: deleted
      logic-delete-value: 1
      logic-not-delete-value: 0
      # 主键类型
      id-type: auto
```

---

## 8. 前端TypeScript类型定义

### 新版类型定义

```typescript
// types/api.ts

/** 用户 */
export interface User {
  id: number;
  username: string;
  password?: string;
  fullName: string;
  gender: string;
  age: number;
  avatar: string;
  phone: string;
  deliveryAddress: string;
  createdAt: string;
}

/** 餐厅 */
export interface Restaurant {
  id: number;
  restaurantAccount: string;
  restaurantName: string;
  photo: string;
  contactPhone: string;
  description: string;
  address: string;
  signatureDishes: string;
  contactPerson: string;
  createdAt: string;
}

/** 美食 */
export interface Food {
  id: number;
  foodName: string;
  categoryId: number;
  categoryName: string;
  restaurantId: number;
  restaurantName: string;
  image: string;
  flavor: string;
  features: string;
  price: number;
  details: string;
  clickCount: number;
  lastClickTime: string;
  createdAt: string;
}

/** 订单 */
export interface Order {
  id: number;
  orderNumber: string;
  foodId: number;
  foodName: string;
  restaurantId: number;
  restaurantName: string;
  userId: number;
  username: string;
  price: number;
  quantity: number;
  totalPrice: number;
  deliveryAddress: string;
  orderTime: string;
  isReviewed: boolean;
  reviewReply?: string;
  paymentStatus: 'paid' | 'unpaid';
  createdAt: string;
}

/** 评价 */
export interface Review {
  id: number;
  restaurantId: number;
  restaurantName: string;
  foodId: number;
  foodName: string;
  userId: number;
  username: string;
  rating: number;
  content: string;
  images?: string[];
  reviewTime: string;
  createdAt: string;
}
```

---

## 9. 注意事项

### 9.1 兼容性
- 建议保留旧接口一段时间，添加 `@Deprecated` 注解
- 使用版本控制：`/api/v1/foods`, `/api/v2/foods`
- 前端逐步迁移，避免一次性全部修改

### 9.2 数据库迁移
- **务必备份**原数据库
- 编写可回滚的迁移脚本
- 在测试环境充分测试后再上生产

### 9.3 团队协作
- 提前通知前后端开发人员
- 更新API文档
- 提供迁移指南和时间表

---

**END**

