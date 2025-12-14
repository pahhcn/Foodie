<template>
  <div class="news-list">
    <div class="container">
      <el-card>
        <template #header>
          <h2>美食资讯</h2>
        </template>
        
        <div v-loading="loading">
          <el-empty v-if="!list.length && !loading" description="暂无资讯" />
          
          <div v-else class="news-items">
            <el-card 
              v-for="item in list" 
              :key="item.id"
              class="news-card"
              shadow="hover"
              @click="router.push(`/news/${item.id}`)"
            >
              <el-row :gutter="20">
                <el-col :span="6">
                  <el-image 
                    :src="item.picture" 
                    fit="cover"
                    style="width: 100%; height: 140px; border-radius: 4px;"
                  />
                </el-col>
                <el-col :span="18">
                  <h3>{{ item.title }}</h3>
                  <p class="intro">{{ item.introduction }}</p>
                  <div class="meta">
                    <span>{{ item.addtime }}</span>
                  </div>
                </el-col>
              </el-row>
            </el-card>
          </div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getNewsList } from '@/api/common'

const router = useRouter()
const list = ref([])
const loading = ref(false)

onMounted(() => {
  loadList()
})

const loadList = async () => {
  loading.value = true
  try {
    const res = await getNewsList({ page: 1, limit: 20 })
    list.value = res.data.list || []
  } catch (error) {
    console.error('加载失败：', error)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

h2 {
  font-size: 20px;
  font-weight: 600;
}

.news-items {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.news-card {
  cursor: pointer;
  transition: all 0.3s;
}

.news-card:hover {
  transform: translateY(-2px);
}

.news-card h3 {
  font-size: 18px;
  font-weight: 500;
  margin-bottom: 12px;
  color: #333;
}

.intro {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin-bottom: 12px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.meta {
  font-size: 12px;
  color: #999;
}
</style>
