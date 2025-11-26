<template>
  <div class="user-layout">
    <DefaultLayout>
      <div class="container">
        <el-row :gutter="20">
          <!-- 左侧菜单 -->
          <el-col :span="5">
            <el-card class="menu-card">
              <el-menu
                :default-active="activeMenu"
                @select="handleMenuSelect"
              >
                <el-menu-item index="/user/center">
                  <el-icon><User /></el-icon>
                  <span>个人中心</span>
                </el-menu-item>
                <el-menu-item index="/user/orders">
                  <el-icon><ShoppingCart /></el-icon>
                  <span>我的订单</span>
                </el-menu-item>
                <el-menu-item index="/user/collection">
                  <el-icon><Star /></el-icon>
                  <span>我的收藏</span>
                </el-menu-item>
              </el-menu>
            </el-card>
          </el-col>
          
          <!-- 右侧内容 -->
          <el-col :span="19">
            <el-card class="content-card">
              <router-view />
            </el-card>
          </el-col>
        </el-row>
      </div>
    </DefaultLayout>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import DefaultLayout from './DefaultLayout.vue'

const router = useRouter()
const route = useRoute()

const activeMenu = computed(() => route.path)

const handleMenuSelect = (index) => {
  router.push(index)
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.menu-card {
  position: sticky;
  top: 130px;
}

.menu-card :deep(.el-card__body) {
  padding: 0;
}

.menu-card :deep(.el-menu) {
  border-right: none;
}

.menu-card :deep(.el-menu-item) {
  height: 48px;
  line-height: 48px;
}

.menu-card :deep(.el-menu-item.is-active) {
  color: #FF6B6B;
  background-color: #FFF5F5;
}

.content-card {
  min-height: 500px;
}
</style>
