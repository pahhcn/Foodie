<template>
  <div v-loading="loading" class="food-detail">
    <div class="container">
      <el-page-header @back="router.back()" title="返回">
        <template #content>
          <span class="page-title">美食详情</span>
        </template>
      </el-page-header>
      
      <el-card v-if="food" class="detail-card" style="margin-top: 20px;">
        <el-row :gutter="30">
          <!-- 左侧图片 -->
          <el-col :span="10">
            <el-carousel v-if="images.length" height="400px" indicator-position="outside">
              <el-carousel-item v-for="(img, index) in images" :key="index">
                <el-image :src="img" fit="cover" style="width: 100%; height: 100%;" />
              </el-carousel-item>
            </el-carousel>
          </el-col>
          
          <!-- 右侧信息 -->
          <el-col :span="14">
            <div class="food-info">
              <h1 class="food-name">{{ food.meishimingcheng }}</h1>
              
              <div class="food-meta">
                <el-tag type="warning" size="large">{{ food.meishifenlei }}</el-tag>
                <span class="click-count">
                  <el-icon><View /></el-icon> {{ food.clicknum || 0 }} 次浏览
                </span>
              </div>
              
              <div class="price-section">
                <span class="price-label">价格：</span>
                <span class="price">¥{{ food.jiage }}</span>
                <span class="unit">/ {{ food.guige }}</span>
              </div>
              
              <el-divider />
              
              <div class="info-item">
                <span class="label">店铺：</span>
                <span class="value">{{ food.dianpumingcheng }}</span>
              </div>
              
              <div class="info-item">
                <span class="label">口味：</span>
                <span class="value">{{ food.kouwei }}</span>
              </div>
              
              <div v-if="food.meishijieshao" class="description">
                <h3>美食介绍</h3>
                <div v-html="food.meishijieshao"></div>
              </div>
              
              <el-divider />
              
              <!-- 点餐操作（核心功能） -->
              <div class="order-section">
                <el-input-number 
                  v-model="quantity" 
                  :min="1" 
                  :max="99"
                  size="large"
                />
                <el-button 
                  type="primary" 
                  size="large"
                  :icon="ShoppingCart"
                  @click="handleOrder"
                  :loading="orderLoading"
                  style="margin-left: 20px;"
                >
                  立即点餐
                </el-button>
                <el-button 
                  :icon="Star"
                  size="large"
                  @click="handleCollection"
                >
                  {{ isCollected ? '已收藏' : '收藏' }}
                </el-button>
              </div>
            </div>
          </el-col>
        </el-row>
      </el-card>
      
      <!-- 评价列表 -->
      <el-card v-if="food" class="review-card" style="margin-top: 20px;">
        <template #header>
          <span>用户评价</span>
        </template>
        <el-empty v-if="!reviews.length" description="暂无评价" />
        <div v-else class="reviews">
          <div v-for="review in reviews" :key="review.id" class="review-item">
            <div class="review-header">
              <el-avatar :src="review.touxiang">
                <el-icon><User /></el-icon>
              </el-avatar>
              <div class="review-info">
                <span class="username">{{ review.yonghuxingming }}</span>
                <el-rate v-model="review.pingfen" disabled size="small" />
              </div>
              <span class="review-time">{{ review.pingjiashijian }}</span>
            </div>
            <div class="review-content">{{ review.pingjianeirong }}</div>
          </div>
        </div>
      </el-card>
    </div>
    
    <!-- 点餐对话框（解决"一闪而过"问题的关键） -->
    <el-dialog
      v-model="orderDialogVisible"
      title="确认订单"
      width="600px"
      :close-on-click-modal="false"
    >
      <el-form :model="orderForm" label-width="100px">
        <el-form-item label="美食名称">
          <el-input v-model="orderForm.meishimingcheng" disabled />
        </el-form-item>
        <el-form-item label="店铺名称">
          <el-input v-model="orderForm.dianpumingcheng" disabled />
        </el-form-item>
        <el-form-item label="单价">
          <el-input v-model="orderForm.danjia" disabled>
            <template #prepend>¥</template>
          </el-input>
        </el-form-item>
        <el-form-item label="数量">
          <el-input-number v-model="orderForm.shuliang" :min="1" :max="99" />
        </el-form-item>
        <el-form-item label="总价">
          <el-input :value="'¥' + totalPrice" disabled />
        </el-form-item>
        <el-form-item label="配送地址" required>
          <el-input 
            v-model="orderForm.peisongdizhi" 
            placeholder="请输入配送地址"
          />
        </el-form-item>
        <el-form-item label="联系方式" required>
          <el-input 
            v-model="orderForm.lianxifangshi" 
            placeholder="请输入联系方式"
          />
        </el-form-item>
        <el-form-item label="备注">
          <el-input 
            v-model="orderForm.beizhu" 
            type="textarea"
            :rows="3"
            placeholder="选填"
          />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="orderDialogVisible = false">取消</el-button>
        <el-button 
          type="primary" 
          @click="submitOrder"
          :loading="orderLoading"
        >
          确认下单
        </el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useOrderStore } from '@/stores/order'
import { getFoodDetail } from '@/api/food'
import { ElMessage } from 'element-plus'
import { ShoppingCart, Star } from '@element-plus/icons-vue'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()
const orderStore = useOrderStore()

const food = ref(null)
const loading = ref(false)
const quantity = ref(1)
const orderDialogVisible = ref(false)
const orderLoading = ref(false)
const isCollected = ref(false)
const reviews = ref([])

const images = computed(() => {
  if (!food.value?.tupian) return []
  return food.value.tupian.split(',')
})

const totalPrice = computed(() => {
  return (orderForm.value.danjia * orderForm.value.shuliang).toFixed(2)
})

const orderForm = ref({
  meishixinxiid: '',
  meishimingcheng: '',
  meishifenlei: '',
  tupian: '',
  dianpumingcheng: '',
  danjia: 0,
  shuliang: 1,
  zongjia: 0,
  peisongdizhi: '',
  lianxifangshi: '',
  beizhu: '',
  yonghuzhanghao: '',
  yonghuxingming: ''
})

onMounted(async () => {
  await loadFoodDetail()
  // 加载用户地址和电话
  if (userStore.userInfo) {
    orderForm.value.peisongdizhi = userStore.userInfo.peisongdizhi || ''
    orderForm.value.lianxifangshi = userStore.userInfo.yonghushouji || ''
  }
})

const loadFoodDetail = async () => {
  loading.value = true
  try {
    const res = await getFoodDetail(route.params.id)
    food.value = res.data
    // 可以加载评价列表
  } catch (error) {
    console.error('加载失败：', error)
  } finally {
    loading.value = false
  }
}

const handleOrder = () => {
  if (!userStore.isLoggedIn) {
    ElMessage.warning('请先登录')
    router.push('/login')
    return
  }
  
  // 填充订单表单
  orderForm.value = {
    meishixinxiid: food.value.id,
    meishimingcheng: food.value.meishimingcheng,
    meishifenlei: food.value.meishifenlei,
    tupian: food.value.tupian,
    dianpumingcheng: food.value.dianpumingcheng,
    danjia: food.value.jiage,
    shuliang: quantity.value,
    zongjia: (food.value.jiage * quantity.value).toFixed(2),
    peisongdizhi: userStore.userInfo?.peisongdizhi || '',
    lianxifangshi: userStore.userInfo?.yonghushouji || '',
    beizhu: '',
    yonghuzhanghao: userStore.username,
    yonghuxingming: userStore.userInfo?.yonghuxingming || ''
  }
  
  // 显示对话框而不是跳转页面
  orderDialogVisible.value = true
}

const submitOrder = async () => {
  if (!orderForm.value.peisongdizhi) {
    ElMessage.warning('请填写配送地址')
    return
  }
  if (!orderForm.value.lianxifangshi) {
    ElMessage.warning('请填写联系方式')
    return
  }
  
  orderLoading.value = true
  try {
    // 更新总价
    orderForm.value.zongjia = totalPrice.value
    
    // 创建订单（不会跳转页面）
    const result = await orderStore.createOrder(orderForm.value)
    
    // 关闭对话框
    orderDialogVisible.value = false
    
    // 根据用户选择决定是否跳转到订单页
    if (result.goToOrders) {
      router.push('/user/orders')
    }
  } catch (error) {
    console.error('下单失败：', error)
  } finally {
    orderLoading.value = false
  }
}

const handleCollection = () => {
  if (!userStore.isLoggedIn) {
    ElMessage.warning('请先登录')
    router.push('/login')
    return
  }
  isCollected.value = !isCollected.value
  ElMessage.success(isCollected.value ? '收藏成功' : '取消收藏')
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.page-title {
  font-size: 18px;
  font-weight: 600;
}

.food-info {
  padding: 20px;
}

.food-name {
  font-size: 28px;
  font-weight: 600;
  color: #333;
  margin-bottom: 16px;
}

.food-meta {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 20px;
}

.click-count {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #666;
  font-size: 14px;
}

.price-section {
  display: flex;
  align-items: baseline;
  gap: 8px;
  margin: 20px 0;
}

.price-label {
  font-size: 16px;
  color: #666;
}

.price {
  font-size: 32px;
  font-weight: 600;
  color: #FF6B6B;
}

.unit {
  font-size: 14px;
  color: #999;
}

.info-item {
  margin: 12px 0;
  font-size: 15px;
}

.info-item .label {
  color: #666;
  margin-right: 8px;
}

.info-item .value {
  color: #333;
}

.description {
  margin: 20px 0;
}

.description h3 {
  font-size: 16px;
  margin-bottom: 12px;
}

.order-section {
  display: flex;
  align-items: center;
  margin-top: 30px;
}

.review-card {
  margin-top: 20px;
}

.reviews {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.review-item {
  padding: 16px;
  background: #fafafa;
  border-radius: 8px;
}

.review-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.review-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.username {
  font-size: 14px;
  font-weight: 500;
}

.review-time {
  font-size: 12px;
  color: #999;
}

.review-content {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
}
</style>
