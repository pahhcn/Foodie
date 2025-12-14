<template>
  <div v-loading="loading" class="shop-detail">
    <div class="container">
      <el-page-header @back="router.back()" title="返回">
        <template #content>
          <span class="page-title">美食店详情</span>
        </template>
      </el-page-header>
      
      <el-card v-if="shop" class="detail-card" style="margin-top: 20px;">
        <el-row :gutter="30">
          <!-- 左侧图片 -->
          <el-col :span="10">
            <el-carousel v-if="images.length" height="350px" indicator-position="outside">
              <el-carousel-item v-for="(img, index) in images" :key="index">
                <el-image :src="img" fit="cover" style="width: 100%; height: 100%;" />
              </el-carousel-item>
            </el-carousel>
          </el-col>
          
          <!-- 右侧信息 -->
          <el-col :span="14">
            <div class="shop-info">
              <h1 class="shop-name">{{ shop.dianpumingcheng }}</h1>
              
              <div class="info-item">
                <span class="label">店铺类型：</span>
                <el-tag>{{ shop.dianpuleixing }}</el-tag>
              </div>
              
              <div class="info-item">
                <span class="label">地址：</span>
                <span class="value">{{ shop.dianpudizhi }}</span>
              </div>
              
              <div class="info-item">
                <span class="label">联系电话：</span>
                <span class="value">{{ shop.lianxidianhua }}</span>
              </div>
              
              <div v-if="shop.yingshishijian" class="info-item">
                <span class="label">营业时间：</span>
                <span class="value">{{ shop.yingshishijian }}</span>
              </div>
              
              <el-divider />
              
              <div v-if="shop.dianpujieshao" class="description">
                <h3>店铺介绍</h3>
                <p>{{ shop.dianpujieshao }}</p>
              </div>
              
              <el-divider />
              
              <div class="action-buttons">
                <el-button 
                  type="primary" 
                  size="large"
                  @click="viewFoods"
                >
                  查看本店美食
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
      
      <!-- 店铺美食列表 -->
      <el-card v-if="shop" class="foods-card" style="margin-top: 20px;">
        <template #header>
          <span>本店美食</span>
        </template>
        
        <div v-loading="foodsLoading">
          <el-empty v-if="!foods.length && !foodsLoading" description="暂无美食" />
          
          <el-row v-else :gutter="20">
            <el-col 
              v-for="item in foods" 
              :key="item.id"
              :xs="12" :sm="8" :md="6"
            >
              <el-card 
                class="food-card" 
                :body-style="{ padding: '0px' }"
                shadow="hover"
                @click="router.push(`/food/${item.id}`)"
              >
                <el-image 
                  :src="getImageUrl(item.tupian)" 
                  fit="cover"
                  style="width: 100%; height: 160px;"
                />
                <div class="card-content">
                  <h3>{{ item.meishimingcheng }}</h3>
                  <div class="card-footer">
                    <span class="price">¥{{ item.jiage }}</span>
                  </div>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import request from '@/utils/request'
import { getFoodList } from '@/api/food'
import { addCollection, deleteCollection, checkCollection } from '@/api/collection'
import { getImageUrl } from '@/utils/image'
import { ElMessage } from 'element-plus'
import { Star, StarFilled } from '@element-plus/icons-vue'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const shop = ref(null)
const foods = ref([])
const loading = ref(false)
const foodsLoading = ref(false)
const isCollected = ref(false)
const collectionLoading = ref(false)
const collectionId = ref(null)

const images = computed(() => {
  if (!shop.value?.zhaopian) return []
  return shop.value.zhaopian.split(',').map(img => getImageUrl(img))
})

onMounted(async () => {
  await loadDetail()
  await loadFoods()
  await checkIfCollected()
})

const loadDetail = async () => {
  loading.value = true
  try {
    const res = await request({
      url: `/meishidian/detail/${route.params.id}`,
      method: 'get'
    })
    shop.value = res.data
  } catch (error) {
    console.error('加载失败：', error)
  } finally {
    loading.value = false
  }
}

const loadFoods = async () => {
  foodsLoading.value = true
  try {
    const res = await getFoodList({
      page: 1,
      limit: 8,
      dianpumingcheng: shop.value?.dianpumingcheng
    })
    foods.value = res.data.list || []
  } catch (error) {
    console.error('加载美食失败：', error)
  } finally {
    foodsLoading.value = false
  }
}

const viewFoods = () => {
  router.push({
    path: '/food/list',
    query: { shop: shop.value.dianpumingcheng }
  })
}

// 检查是否已收藏
const checkIfCollected = async () => {
  if (!userStore.isLoggedIn) return
  
  try {
    const res = await checkCollection(route.params.id, 'meishidian')
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
        refid: shop.value.id,
        tablename: 'meishidian',
        name: shop.value.dianpumingcheng,
        picture: shop.value.zhaopian
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

.shop-info {
  padding: 20px;
}

.shop-name {
  font-size: 28px;
  font-weight: 600;
  color: #333;
  margin-bottom: 20px;
}

.info-item {
  margin: 16px 0;
  font-size: 15px;
  display: flex;
  align-items: center;
}

.info-item .label {
  color: #666;
  margin-right: 8px;
  min-width: 100px;
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

.description p {
  font-size: 14px;
  color: #666;
  line-height: 1.8;
}

.action-buttons {
  display: flex;
  align-items: center;
  margin-top: 20px;
}

.food-card {
  cursor: pointer;
  transition: all 0.3s;
  margin-bottom: 20px;
}

.food-card:hover {
  transform: translateY(-4px);
}

.card-content {
  padding: 12px;
}

.card-content h3 {
  font-size: 14px;
  font-weight: 500;
  margin-bottom: 8px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.price {
  font-size: 18px;
  font-weight: 600;
  color: #FF6B6B;
}
</style>
