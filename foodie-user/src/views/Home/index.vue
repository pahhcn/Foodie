<template>
  <div class="home">
    <!-- 轮播图 -->
    <div class="banner-section">
      <el-carousel height="400px" indicator-position="outside">
        <el-carousel-item v-for="(item, index) in banners" :key="index">
          <el-image :src="item.img" fit="cover" style="width: 100%; height: 100%;" />
        </el-carousel-item>
      </el-carousel>
    </div>
    
    <div class="container">
      <!-- 美食推荐 -->
      <section class="section">
        <div class="section-header">
          <h2>美食推荐</h2>
          <el-button text @click="router.push('/food/list')">
            查看更多 <el-icon><ArrowRight /></el-icon>
          </el-button>
        </div>
        <el-row :gutter="20">
          <el-col 
            v-for="item in recommendFoods" 
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
                style="width: 100%; height: 200px;"
              >
                <template #error>
                  <div class="image-slot">
                    <el-icon><Picture /></el-icon>
                  </div>
                </template>
              </el-image>
              <div class="card-content">
                <h3>{{ item.meishimingcheng }}</h3>
                <div class="card-footer">
                  <span class="price">¥{{ item.jiage }}</span>
                  <el-tag size="small" type="warning">{{ item.meishifenlei }}</el-tag>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </section>
      
      <!-- 美食资讯 -->
      <section class="section">
        <div class="section-header">
          <h2>美食资讯</h2>
          <el-button text @click="router.push('/news/list')">
            查看更多 <el-icon><ArrowRight /></el-icon>
          </el-button>
        </div>
        <el-row :gutter="20">
          <el-col 
            v-for="item in newsList" 
            :key="item.id"
            :xs="24" :sm="12" :md="8"
          >
            <el-card 
              class="news-card" 
              shadow="hover"
              @click="router.push(`/news/${item.id}`)"
            >
              <el-image 
                :src="item.picture" 
                fit="cover"
                style="width: 100%; height: 160px; border-radius: 4px;"
              />
              <h3>{{ item.title }}</h3>
              <p class="intro">{{ item.introduction }}</p>
            </el-card>
          </el-col>
        </el-row>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getBanners, getNewsList } from '@/api/common'
import { getRecommendFoods } from '@/api/food'
import { ArrowRight } from '@element-plus/icons-vue'

const router = useRouter()

const banners = ref([])
const recommendFoods = ref([])
const newsList = ref([])

onMounted(async () => {
  await loadData()
})

const loadData = async () => {
  try {
    // 加载轮播图
    const bannerRes = await getBanners()
    banners.value = bannerRes.data.list.map(item => ({ img: item.value }))
    
    // 加载推荐美食
    const foodRes = await getRecommendFoods(8)
    recommendFoods.value = foodRes.data.list || []
    
    // 加载资讯
    const newsRes = await getNewsList({ page: 1, limit: 6 })
    newsList.value = newsRes.data.list || []
  } catch (error) {
    console.error('加载数据失败：', error)
  }
}
</script>

<style scoped>
.home {
  background: #fafafa;
}

.banner-section {
  margin-bottom: 40px;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.section {
  margin-bottom: 60px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.section-header h2 {
  font-size: 24px;
  font-weight: 600;
  color: #333;
}

.food-card {
  cursor: pointer;
  transition: all 0.3s;
  margin-bottom: 20px;
}

.food-card:hover {
  transform: translateY(-4px);
}

.image-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background: #f5f5f5;
  color: #909399;
  font-size: 30px;
}

.card-content {
  padding: 16px;
}

.card-content h3 {
  font-size: 16px;
  font-weight: 500;
  color: #333;
  margin-bottom: 12px;
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
  font-size: 20px;
  font-weight: 600;
  color: #FF6B6B;
}

.news-card {
  cursor: pointer;
  transition: all 0.3s;
  margin-bottom: 20px;
}

.news-card:hover {
  transform: translateY(-4px);
}

.news-card h3 {
  font-size: 16px;
  font-weight: 500;
  color: #333;
  margin: 12px 0 8px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.intro {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
