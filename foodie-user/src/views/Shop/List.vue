<template>
  <div class="shop-list">
    <div class="container">
      <el-card>
        <template #header>
          <h2>美食店</h2>
        </template>
        
        <div v-loading="loading">
          <el-empty v-if="!list.length && !loading" description="暂无数据" />
          
          <el-row v-else :gutter="20">
            <el-col 
              v-for="item in list" 
              :key="item.id"
              :xs="12" :sm="8" :md="6"
            >
              <el-card 
                class="shop-card" 
                :body-style="{ padding: '0px' }"
                shadow="hover"
                @click="router.push(`/shop/${item.id}`)"
              >
                <el-image 
                  :src="item.zhaopian?.split(',')[0]" 
                  fit="cover"
                  style="width: 100%; height: 180px;"
                />
                <div class="card-content">
                  <h3>{{ item.dianpumingcheng }}</h3>
                  <p class="address">{{ item.dianpudizhi }}</p>
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
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import request from '@/utils/request'

const router = useRouter()
const list = ref([])
const loading = ref(false)

onMounted(() => {
  loadList()
})

const loadList = async () => {
  loading.value = true
  try {
    const res = await request({
      url: '/meishidian/list',
      method: 'get',
      params: { page: 1, limit: 100 }
    })
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

.shop-card {
  cursor: pointer;
  transition: all 0.3s;
  margin-bottom: 20px;
}

.shop-card:hover {
  transform: translateY(-4px);
}

.card-content {
  padding: 16px;
}

.card-content h3 {
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 8px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.address {
  font-size: 13px;
  color: #999;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
