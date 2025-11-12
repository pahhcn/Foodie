<template>
  <div v-loading="loading" class="news-detail">
    <div class="container">
      <el-page-header @back="router.back()" title="返回">
        <template #content>
          <span class="page-title">资讯详情</span>
        </template>
      </el-page-header>
      
      <el-card v-if="news" class="detail-card" style="margin-top: 20px;">
        <h1 class="title">{{ news.title }}</h1>
        
        <div class="meta">
          <span class="author">{{ news.author || '管理员' }}</span>
          <el-divider direction="vertical" />
          <span class="time">{{ news.addtime }}</span>
        </div>
        
        <el-divider />
        
        <div class="introduction">
          {{ news.introduction }}
        </div>
        
        <el-image 
          v-if="news.picture"
          :src="news.picture" 
          fit="cover"
          style="width: 100%; max-height: 400px; border-radius: 8px; margin: 20px 0;"
        />
        
        <div class="content" v-html="news.content"></div>
      </el-card>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { getNewsDetail } from '@/api/common'

const router = useRouter()
const route = useRoute()

const news = ref(null)
const loading = ref(false)

onMounted(async () => {
  await loadDetail()
})

const loadDetail = async () => {
  loading.value = true
  try {
    const res = await getNewsDetail(route.params.id)
    news.value = res.data
  } catch (error) {
    console.error('加载失败：', error)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

.page-title {
  font-size: 18px;
  font-weight: 600;
}

.title {
  font-size: 28px;
  font-weight: 600;
  color: #333;
  margin-bottom: 16px;
  line-height: 1.4;
}

.meta {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  color: #999;
}

.introduction {
  font-size: 16px;
  color: #666;
  line-height: 1.8;
  padding: 20px;
  background: #f8f8f8;
  border-radius: 8px;
  margin: 20px 0;
}

.content {
  font-size: 15px;
  color: #333;
  line-height: 1.8;
  margin-top: 20px;
}

.content :deep(img) {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  margin: 16px 0;
}

.content :deep(p) {
  margin: 12px 0;
}
</style>
