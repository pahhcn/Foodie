import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/DefaultLayout.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        component: () => import('@/views/Home/index.vue'),
        meta: { title: '首页' }
      },
      {
        path: 'food/list',
        name: 'FoodList',
        component: () => import('@/views/Food/List.vue'),
        meta: { title: '美食信息' }
      },
      {
        path: 'food/:id',
        name: 'FoodDetail',
        component: () => import('@/views/Food/Detail.vue'),
        meta: { title: '美食详情' }
      },
      {
        path: 'shop/list',
        name: 'ShopList',
        component: () => import('@/views/Shop/List.vue'),
        meta: { title: '美食店' }
      },
      {
        path: 'shop/:id',
        name: 'ShopDetail',
        component: () => import('@/views/Shop/Detail.vue'),
        meta: { title: '店铺详情' }
      },
      {
        path: 'news/list',
        name: 'NewsList',
        component: () => import('@/views/News/List.vue'),
        meta: { title: '美食资讯' }
      },
      {
        path: 'news/:id',
        name: 'NewsDetail',
        component: () => import('@/views/News/Detail.vue'),
        meta: { title: '资讯详情' }
      }
    ]
  },
  {
    path: '/user',
    component: () => import('@/layouts/UserLayout.vue'),
    meta: { requiresAuth: true },
    children: [
      {
        path: 'center',
        name: 'UserCenter',
        component: () => import('@/views/User/Center.vue'),
        meta: { title: '个人中心' }
      },
      {
        path: 'orders',
        name: 'OrderList',
        component: () => import('@/views/Order/List.vue'),
        meta: { title: '我的订单' }
      },
      {
        path: 'orders/:id',
        name: 'OrderDetail',
        component: () => import('@/views/Order/Detail.vue'),
        meta: { title: '订单详情' }
      },
      {
        path: 'collection',
        name: 'Collection',
        component: () => import('@/views/User/Collection.vue'),
        meta: { title: '我的收藏' }
      }
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Auth/Login.vue'),
    meta: { title: '登录' }
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/views/Auth/Register.vue'),
    meta: { title: '注册' }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/Error/404.vue')
  }
]

const router = createRouter({
  history: createWebHistory('/vue3/'),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// 路由守卫
router.beforeEach((to, from, next) => {
  // 设置页面标题
  document.title = to.meta.title ? `${to.meta.title} - 网上点餐系统` : '网上点餐系统'
  
  // 验证登录
  if (to.meta.requiresAuth) {
    const userStore = useUserStore()
    if (!userStore.token) {
      next({
        name: 'Login',
        query: { redirect: to.fullPath }
      })
      return
    }
  }
  
  next()
})

export default router
