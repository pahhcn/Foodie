<template>
  <div class="collection">
    <h2>我的收藏</h2>
    
    <div v-loading="loading">
      <el-empty v-if="!list.length && !loading" description="暂无收藏" />
      
      <el-row v-else :gutter="20">
        <el-col 
          v-for="item in list" 
          :key="item.id"
          :xs="12" :sm="8" :md="6"
        >
          <el-card class="collection-card" shadow="hover">
            <el-image 
              :src="item.picture" 
              fit="cover"
              style="width: 100%; height: 150px; border-radius: 4px;"
            />
            <h3>{{ item.name }}</h3>
            <div class="actions">
              <el-button size="small" @click="viewDetail(item)">查看</el-button>
              <el-button size="small" type="danger" @click="removeCollection(item.id)">
                取消收藏
              </el-button>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getCollectionList, removeCollection as removeCollectionApi } from '@/api/common'
import { ElMessage, ElMessageBox } from 'element-plus'

const router = useRouter()
const list = ref([])
const loading = ref(false)

onMounted(() => {
  loadList()
})

const loadList = async () => {
  loading.value = true
  try {
    const username = localStorage.getItem('adminName')
    const res = await getCollectionList({
      page: 1,
      limit: 100,
      userid: localStorage.getItem('userid')
    })
    list.value = res.data.list || []
  } catch (error) {
    console.error('加载失败：', error)
  } finally {
    loading.value = false
  }
}

const viewDetail = (item) => {
  router.push(`/food/${item.refid}`)
}

const removeCollection = async (id) => {
  try {
    await ElMessageBox.confirm('确认取消收藏吗？', '提示', {
      confirmButtonText: '确认',
      cancelButtonText: '取消',
      type: 'warning'
    })
    
    await removeCollectionApi(id)
    ElMessage.success('已取消收藏')
    await loadList()
  } catch (error) {
    if (error !== 'cancel') {
      console.error('取消收藏失败：', error)
    }
  }
}
</script>

<style scoped>
.collection {
  padding: 20px;
}

h2 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 24px;
}

.collection-card {
  margin-bottom: 20px;
  cursor: pointer;
}

.collection-card h3 {
  font-size: 14px;
  margin: 12px 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.actions {
  display: flex;
  gap: 8px;
}
</style>
