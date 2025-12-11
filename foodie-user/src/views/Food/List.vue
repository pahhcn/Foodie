<template>
  <div class="food-list">
    <div class="container">
      <el-card>
        <template #header>
          <div class="header">
            <h2>美食信息</h2>
            <el-input
              v-model="searchKeyword"
              placeholder="搜索美食名称"
              style="width: 300px;"
              clearable
              @clear="handleSearch"
              @keyup.enter="handleSearch"
            >
              <template #append>
                <el-button :icon="Search" @click="handleSearch" />
              </template>
            </el-input>
          </div>
        </template>
        
        <!-- 分类筛选 -->
        <div class="filters">
          <span class="filter-label">分类：</span>
          <el-radio-group v-model="selectedCategory" @change="handleSearch">
            <el-radio-button label="">全部</el-radio-button>
            <el-radio-button 
              v-for="cat in categories" 
              :key="cat.id"
              :label="cat.meishifenlei"
            >
              {{ cat.meishifenlei }}
            </el-radio-button>
          </el-radio-group>
        </div>
        
        <el-divider />
        
        <!-- 美食列表 -->
        <div v-loading="loading" class="list-content">
          <el-empty v-if="!foodList.length && !loading" description="暂无数据" />
          
          <el-row v-else :gutter="20">
            <el-col 
              v-for="item in foodList" 
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
                  <p class="shop">{{ item.dianpumingcheng }}</p>
                  <div class="card-footer">
                    <span class="price">¥{{ item.jiage }}</span>
                    <el-tag size="small" type="warning">{{ item.meishifenlei }}</el-tag>
                  </div>
                </div>
              </el-card>
            </el-col>
          </el-row>
          
          <!-- 分页 -->
          <div v-if="total > pageSize" class="pagination">
            <el-pagination
              v-model:current-page="currentPage"
              v-model:page-size="pageSize"
              :total="total"
              :page-sizes="[12, 24, 36, 48]"
              layout="total, sizes, prev, pager, next, jumper"
              @current-change="loadList"
              @size-change="loadList"
            />
          </div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getFoodList, getFoodCategories } from '@/api/food'
import { Search } from '@element-plus/icons-vue'

const router = useRouter()

const foodList = ref([])
const categories = ref([])
const loading = ref(false)
const total = ref(0)
const currentPage = ref(1)
const pageSize = ref(12)
const searchKeyword = ref('')
const selectedCategory = ref('')

onMounted(async () => {
  await loadCategories()
  await loadList()
})

const loadCategories = async () => {
  try {
    const res = await getFoodCategories()
    categories.value = res.data.list || []
  } catch (error) {
    console.error('加载分类失败：', error)
  }
}

const loadList = async () => {
  loading.value = true
  try {
    const params = {
      page: currentPage.value,
      limit: pageSize.value
    }
    
    if (searchKeyword.value) {
      params.meishimingcheng = `%${searchKeyword.value}%`
    }
    
    if (selectedCategory.value) {
      params.meishifenlei = selectedCategory.value
    }
    
    const res = await getFoodList(params)
    foodList.value = res.data.list || []
    total.value = res.data.total || 0
  } catch (error) {
    console.error('加载列表失败：', error)
  } finally {
    loading.value = false
  }
}

const handleSearch = () => {
  currentPage.value = 1
  loadList()
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h2 {
  font-size: 20px;
  font-weight: 600;
  color: #333;
}

.filters {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.filter-label {
  font-size: 14px;
  color: #666;
  font-weight: 500;
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
  margin-bottom: 8px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.shop {
  font-size: 14px;
  color: #999;
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

.pagination {
  margin-top: 24px;
  display: flex;
  justify-content: center;
}
</style>
