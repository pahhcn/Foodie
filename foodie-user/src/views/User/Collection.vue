<template>
  <div class="collection-page">
    <h2>我的收藏</h2>
    
    <!-- 分类标签 -->
    <el-tabs v-model="activeTab" @tab-change="handleTabChange">
      <el-tab-pane label="美食收藏" name="meishixinxi">
        <div v-loading="loading" class="collection-list">
          <el-empty v-if="!collections.length && !loading" description="暂无收藏" />
          
          <el-row v-else :gutter="20">
            <el-col 
              v-for="item in collections" 
              :key="item.id"
              :xs="12" :sm="8" :md="6"
            >
              <el-card 
                class="collection-card" 
                :body-style="{ padding: '0px' }"
                shadow="hover"
              >
                <el-image 
                  :src="getPictureUrl(item.picture)" 
                  fit="cover"
                  style="width: 100%; height: 180px; cursor: pointer;"
                  @click="goToDetail(item)"
                >
                  <template #error>
                    <div class="image-slot">
                      <el-icon><Picture /></el-icon>
                    </div>
                  </template>
                </el-image>
                <div class="card-content">
                  <h3 @click="goToDetail(item)">{{ item.name }}</h3>
                  <div class="card-footer">
                    <span class="time">{{ formatTime(item.addtime) }}</span>
                    <el-button 
                      type="danger" 
                      size="small"
                      :icon="Delete"
                      @click="handleDelete(item.id)"
                    >
                      删除
                    </el-button>
                  </div>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </div>
      </el-tab-pane>
      
      <el-tab-pane label="店铺收藏" name="meishidian">
        <div v-loading="loading" class="collection-list">
          <el-empty v-if="!collections.length && !loading" description="暂无收藏" />
          
          <el-row v-else :gutter="20">
            <el-col 
              v-for="item in collections" 
              :key="item.id"
              :xs="12" :sm="8" :md="6"
            >
              <el-card 
                class="collection-card" 
                :body-style="{ padding: '0px' }"
                shadow="hover"
              >
                <el-image 
                  :src="getPictureUrl(item.picture)" 
                  fit="cover"
                  style="width: 100%; height: 180px; cursor: pointer;"
                  @click="goToDetail(item)"
                >
                  <template #error>
                    <div class="image-slot">
                      <el-icon><Picture /></el-icon>
                    </div>
                  </template>
                </el-image>
                <div class="card-content">
                  <h3 @click="goToDetail(item)">{{ item.name }}</h3>
                  <div class="card-footer">
                    <span class="time">{{ formatTime(item.addtime) }}</span>
                    <el-button 
                      type="danger" 
                      size="small"
                      :icon="Delete"
                      @click="handleDelete(item.id)"
                    >
                      删除
                    </el-button>
                  </div>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getCollectionList, deleteCollection } from '@/api/collection'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Delete, Picture } from '@element-plus/icons-vue'

const router = useRouter()

const activeTab = ref('meishixinxi')
const collections = ref([])
const loading = ref(false)

onMounted(() => {
  loadCollections()
})

const handleTabChange = () => {
  loadCollections()
}

const loadCollections = async () => {
  loading.value = true
  try {
    const res = await getCollectionList({
      page: 1,
      limit: 100,
      tablename: activeTab.value
    })
    collections.value = res.data.list || []
  } catch (error) {
    console.error('加载收藏失败：', error)
    ElMessage.error('加载收藏失败')
  } finally {
    loading.value = false
  }
}

const getPictureUrl = (picture) => {
  if (!picture) return ''
  // 如果是完整 URL，直接返回
  if (picture.startsWith('http')) {
    return picture
  }
  // 如果是多张图片，取第一张
  const firstPic = picture.split(',')[0]
  // 拼接完整 URL
  return `http://localhost:8080/foodie/upload/${firstPic}`
}

const formatTime = (time) => {
  if (!time) return ''
  const date = new Date(time)
  return date.toLocaleDateString('zh-CN')
}

const goToDetail = (item) => {
  if (item.tablename === 'meishixinxi') {
    router.push(`/food/${item.refid}`)
  } else if (item.tablename === 'meishidian') {
    router.push(`/shop/${item.refid}`)
  }
}

const handleDelete = async (id) => {
  try {
    await ElMessageBox.confirm(
      '确认删除该收藏吗？',
      '删除确认',
      {
        confirmButtonText: '确认',
        cancelButtonText: '取消',
        type: 'warning'
      }
    )
    
    await deleteCollection([id])
    ElMessage.success('删除成功')
    await loadCollections()
  } catch (error) {
    if (error !== 'cancel') {
      console.error('删除失败：', error)
      ElMessage.error('删除失败')
    }
  }
}
</script>

<style scoped>
.collection-page {
  padding: 20px;
}

h2 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 24px;
}

.collection-list {
  min-height: 400px;
}

.collection-card {
  cursor: pointer;
  transition: all 0.3s;
  margin-bottom: 20px;
}

.collection-card:hover {
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
  font-size: 32px;
}

.card-content {
  padding: 12px;
}

.card-content h3 {
  font-size: 15px;
  font-weight: 500;
  margin-bottom: 12px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  cursor: pointer;
  transition: color 0.3s;
}

.card-content h3:hover {
  color: #409eff;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.time {
  font-size: 12px;
  color: #999;
}
</style>
