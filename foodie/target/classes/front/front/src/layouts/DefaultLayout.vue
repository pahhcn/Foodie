<template>
  <div class="default-layout">
    <!-- 顶部导航栏 -->
    <header class="header">
      <div class="header-top">
        <div class="container">
          <div class="logo-title">{{ projectName }}</div>
          <div class="user-actions">
            <template v-if="isLoggedIn">
              <el-dropdown @command="handleCommand">
                <span class="user-info">
                  <el-avatar :src="avatar" :size="32">
                    <el-icon><User /></el-icon>
                  </el-avatar>
                  <span class="username">{{ username }}</span>
                </span>
                <template #dropdown>
                  <el-dropdown-menu>
                    <el-dropdown-item command="center">
                      <el-icon><User /></el-icon> 个人中心
                    </el-dropdown-item>
                    <el-dropdown-item command="orders">
                      <el-icon><ShoppingCart /></el-icon> 我的订单
                    </el-dropdown-item>
                    <el-dropdown-item command="collection">
                      <el-icon><Star /></el-icon> 我的收藏
                    </el-dropdown-item>
                    <el-dropdown-item divided command="logout">
                      <el-icon><SwitchButton /></el-icon> 退出登录
                    </el-dropdown-item>
                  </el-dropdown-menu>
                </template>
              </el-dropdown>
            </template>
            <template v-else>
              <el-button text @click="router.push('/login')">登录</el-button>
              <el-button type="primary" @click="router.push('/register')">注册</el-button>
            </template>
          </div>
        </div>
      </div>
      
      <div class="header-nav">
        <div class="container">
          <el-menu
            :default-active="activeMenu"
            mode="horizontal"
            :ellipsis="false"
            @select="handleMenuSelect"
          >
            <el-menu-item index="/">
              <el-icon><HomeFilled /></el-icon> 首页
            </el-menu-item>
            <el-menu-item index="/shop/list">
              <el-icon><Shop /></el-icon> 美食店
            </el-menu-item>
            <el-menu-item index="/food/list">
              <el-icon><Food /></el-icon> 美食信息
            </el-menu-item>
            <el-menu-item index="/news/list">
              <el-icon><Document /></el-icon> 美食资讯
            </el-menu-item>
          </el-menu>
        </div>
      </div>
    </header>
    
    <!-- 主要内容区 -->
    <main class="main-content">
      <router-view />
    </main>
    
    <!-- 底部信息 -->
    <footer class="footer">
      <div class="container">
        <p class="company">{{ projectName }}</p>
        <p class="contact">电话：4008000000 | 邮箱：support@21epub.com</p>
        <p class="copyright">© 2025 网上点餐系统. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { ElMessageBox } from 'element-plus'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const projectName = '网上点餐系统'

const isLoggedIn = computed(() => userStore.isLoggedIn)
const username = computed(() => userStore.username)
const avatar = computed(() => userStore.avatar)
const activeMenu = computed(() => route.path)

const handleCommand = (command) => {
  switch (command) {
    case 'center':
      router.push('/user/center')
      break
    case 'orders':
      router.push('/user/orders')
      break
    case 'collection':
      router.push('/user/collection')
      break
    case 'logout':
      ElMessageBox.confirm('确认退出登录吗？', '提示', {
        confirmButtonText: '确认',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        userStore.logout()
        router.push('/')
      }).catch(() => {})
      break
  }
}

const handleMenuSelect = (index) => {
  router.push(index)
}
</script>

<style scoped>
.default-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  background: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.header-top {
  background: #fff;
  border-bottom: 1px solid #f0f0f0;
}

.header-top .container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo-title {
  font-size: 20px;
  font-weight: 600;
  color: #333;
}

.user-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  padding: 4px 12px;
  border-radius: 20px;
  transition: background 0.3s;
}

.user-info:hover {
  background: #f5f5f5;
}

.username {
  font-size: 14px;
  color: #333;
}

.header-nav {
  background: #fff;
}

.header-nav .container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.header-nav :deep(.el-menu) {
  border-bottom: none;
}

.header-nav :deep(.el-menu-item) {
  font-size: 15px;
  padding: 0 24px;
  height: 50px;
  line-height: 50px;
}

.header-nav :deep(.el-menu-item.is-active) {
  color: #FF6B6B;
  border-bottom-color: #FF6B6B;
}

.main-content {
  flex: 1;
  background: #fafafa;
  padding: 20px 0;
}

.footer {
  background: #f8f8f8;
  border-top: 1px solid #e8e8e8;
  padding: 30px 0;
  margin-top: 40px;
}

.footer .container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  text-align: center;
}

.footer p {
  margin: 8px 0;
  color: #666;
  font-size: 14px;
}

.footer .company {
  font-size: 16px;
  font-weight: 500;
  color: #333;
}
</style>
