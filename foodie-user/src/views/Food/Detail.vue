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
            <el-image 
              v-if="food.tupian" 
              :src="getImageUrl(food.tupian)" 
              fit="cover" 
              style="width: 100%; height: 400px; border-radius: 8px;" 
            />
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
              </div>
              
              <el-divider />
              
              <div class="info-item">
                <span class="label">店铺：</span>
                <span class="value">{{ food.dianpumingcheng }}</span>
              </div>
              
              <div class="info-item">
                <span class="label">联系电话：</span>
                <span class="value">{{ food.lianxidianhua }}</span>
              </div>
              
              <div class="info-item">
                <span class="label">口味：</span>
                <span class="value">{{ food.kouwei }}</span>
              </div>
              
              <div class="info-item">
                <span class="label">特色：</span>
                <span class="value">{{ food.tese }}</span>
              </div>
              
              <div v-if="food.xiangqing" class="description">
                <h3>详情介绍</h3>
                <div v-html="food.xiangqing"></div>
              </div>
              
              <el-divider />
              
              <!-- 点餐操作 -->
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
                  @click="handleOrder"
                  :loading="orderLoading"
                  style="margin-left: 20px;"
                >
                  立即点餐
                </el-button>
                <el-button 
                  :type="isCollected ? 'warning' : 'default'"
                  :icon="isCollected ? StarFilled : Star"
                  size="large"
                  @click="handleCollection"
                  :loading="collectionLoading"
                  style="margin-left: 12px;"
                >
                  {{ isCollected ? '已收藏' : '收藏' }}
                </el-button>
              </div>
            </div>
          </el-col>
        </el-row>
      </el-card>
    </div>
    
    <!-- 下单对话框 -->
    <el-dialog
      v-model="orderDialogVisible"
      title="确认订单"
      width="500px"
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
          <el-input v-model="orderForm.jiage" disabled>
            <template #prepend>¥</template>
          </el-input>
        </el-form-item>
        <el-form-item label="数量">
          <el-input-number v-model="orderForm.goumaishuliang" :min="1" :max="99" />
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
            v-model="orderForm.yonghushouji" 
            placeholder="请输入联系方式"
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
import { getFoodDetail } from '@/api/food'
import { createOrder } from '@/api/order'
import { addCollection, deleteCollection, checkCollection } from '@/api/collection'
import { getImageUrl } from '@/utils/image'
import { ElMessage, ElMessageBox } from 'element-plus'
import { View, Star, StarFilled } from '@element-plus/icons-vue'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const food = ref(null)
const loading = ref(false)
const quantity = ref(1)
const orderDialogVisible = ref(false)
const orderLoading = ref(false)
const isCollected = ref(false)
const collectionLoading = ref(false)
const collectionId = ref(null)

const totalPrice = computed(() => {
  if (!orderForm.value.jiage || !orderForm.value.goumaishuliang) return '0.00'
  return (parseFloat(orderForm.value.jiage) * orderForm.value.goumaishuliang).toFixed(2)
})

const orderForm = ref({
  meishimingcheng: '',
  dianpuzhanghao: '',
  dianpumingcheng: '',
  lianxidianhua: '',
  jiage: '',
  goumaishuliang: 1,
  zongjiage: '',
  yonghuzhanghao: '',
  yonghuxingming: '',
  yonghushouji: '',
  peisongdizhi: ''
})

onMounted(async () => {
  console.log('=== 美食详情页面已加载 ===')
  await loadFoodDetail()
  await checkIfCollected()
})

const loadFoodDetail = async () => {
  loading.value = true
  try {
    const res = await getFoodDetail(route.params.id)
    food.value = res.data
    console.log('美食信息：', food.value)
  } catch (error) {
    console.error('加载失败：', error)
    ElMessage.error('加载美食信息失败')
  } finally {
    loading.value = false
  }
}

// 检查是否已收藏
const checkIfCollected = async () => {
  if (!userStore.isLoggedIn) return
  
  try {
    const res = await checkCollection(route.params.id, 'meishixinxi')
    if (res.data.list && res.data.list.length > 0) {
      isCollected.value = true
      collectionId.value = res.data.list[0].id
    }
  } catch (error) {
    console.error('检查收藏状态失败：', error)
  }
}

// 处理收藏
const handleCollection = async () => {
  if (!userStore.isLoggedIn) {
    ElMessage.warning('请先登录')
    router.push('/login')
    return
  }
  
  collectionLoading.value = true
  try {
    if (isCollected.value) {
      // 取消收藏
      await deleteCollection([collectionId.value])
      isCollected.value = false
      collectionId.value = null
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
      await checkIfCollected() // 重新获取收藏ID
      ElMessage.success('收藏成功')
    }
  } catch (error) {
    console.error('收藏操作失败：', error)
    ElMessage.error('操作失败，请重试')
  } finally {
    collectionLoading.value = false
  }
}

const handleOrder = () => {
  console.log('点击立即点餐按钮')
  
  if (!userStore.isLoggedIn) {
    ElMessage.warning('请先登录')
    router.push('/login')
    return
  }
  
  // 填充订单表单
  orderForm.value = {
    meishimingcheng: food.value.meishimingcheng,
    dianpuzhanghao: food.value.dianpuzhanghao || '',
    dianpumingcheng: food.value.dianpumingcheng,
    lianxidianhua: food.value.lianxidianhua || '',
    jiage: String(food.value.jiage),
    goumaishuliang: quantity.value,
    zongjiage: '',
    yonghuzhanghao: localStorage.getItem('adminName') || '',
    yonghuxingming: userStore.userInfo?.yonghuxingming || '',
    yonghushouji: userStore.userInfo?.yonghushouji || '',
    peisongdizhi: userStore.userInfo?.peisongdizhi || ''
  }
  
  console.log('打开订单对话框')
  orderDialogVisible.value = true
}

const submitOrder = async () => {
  console.log('点击确认下单按钮')
  
  if (!orderForm.value.peisongdizhi) {
    ElMessage.warning('请填写配送地址')
    return
  }
  if (!orderForm.value.yonghushouji) {
    ElMessage.warning('请填写联系方式')
    return
  }
  
  console.log('开始提交订单')
  orderLoading.value = true
  
  try {
    // 生成订单编号和时间（使用本地时间）
    const now = new Date()
    const year = now.getFullYear()
    const month = String(now.getMonth() + 1).padStart(2, '0')
    const day = String(now.getDate()).padStart(2, '0')
    const hour = String(now.getHours()).padStart(2, '0')
    const minute = String(now.getMinutes()).padStart(2, '0')
    const second = String(now.getSeconds()).padStart(2, '0')
    const random = Math.floor(Math.random() * 100000)
    const dingdanbianhao = `${year}${month}${day}${hour}${minute}${second}${random}`
    const xiadanshijian = `${year}-${month}-${day} ${hour}:${minute}:${second}`
    
    // 构建订单数据
    const orderData = {
      dingdanbianhao: dingdanbianhao,
      meishimingcheng: orderForm.value.meishimingcheng,
      dianpuzhanghao: orderForm.value.dianpuzhanghao,
      dianpumingcheng: orderForm.value.dianpumingcheng,
      lianxidianhua: orderForm.value.lianxidianhua,
      jiage: orderForm.value.jiage,
      goumaishuliang: orderForm.value.goumaishuliang,
      zongjiage: totalPrice.value,
      yonghuzhanghao: orderForm.value.yonghuzhanghao,
      yonghuxingming: orderForm.value.yonghuxingming,
      yonghushouji: orderForm.value.yonghushouji,
      peisongdizhi: orderForm.value.peisongdizhi,
      xiadanshijian: xiadanshijian,
      sfsh: '否',
      ispay: '未支付'
    }
    
    console.log('提交订单数据：', orderData)
    
    // 调用 API
    const res = await createOrder(orderData)
    console.log('订单创建成功：', res)
    
    // 关闭对话框
    orderDialogVisible.value = false
    
    // 提示用户
    await ElMessageBox.confirm(
      '订单创建成功！',
      '下单成功',
      {
        confirmButtonText: '查看订单',
        cancelButtonText: '继续浏览',
        type: 'success'
      }
    ).then(() => {
      router.push('/user/orders')
    }).catch(() => {
      // 用户选择继续浏览
    })
    
  } catch (error) {
    console.error('下单失败：', error)
    ElMessage.error('下单失败，请重试')
  } finally {
    orderLoading.value = false
  }
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
</style>
