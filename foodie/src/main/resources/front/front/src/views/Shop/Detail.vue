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
              
              <el-button 
                type="primary" 
                size="large"
                @click="viewFoods"
              >
                查看本店美食
              </el-button>
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
                  :src="item.tupian?.split(',')[0]" 
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
import request from '@/utils/request'
import { getFoodList } from '@/api/food'

const router = useRouter()
const route = useRoute()

const shop = ref(null)
const foods = ref([])
const loading = ref(false)
const foodsLoading = ref(false)

const images = computed(() => {
  if (!shop.value?.zhaopian) return []
  return shop.value.zhaopian.split(',')
})

onMounted(async () => {
  await loadDetail()
  await loadFoods()
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
