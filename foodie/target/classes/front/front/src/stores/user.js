import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { ElMessage } from 'element-plus'
import { login as loginApi, register as registerApi, getUserInfo } from '@/api/user'

export const useUserStore = defineStore('user', () => {
  // 状态
  const token = ref(localStorage.getItem('Token') || '')
  const userInfo = ref(null)
  const userTable = ref(localStorage.getItem('userTable') || '')
  
  // 计算属性
  const isLoggedIn = computed(() => !!token.value)
  const username = computed(() => userInfo.value?.yonghuzhanghao || '')
  const avatar = computed(() => userInfo.value?.touxiang || '')
  
  // 登录
  const login = async (loginForm) => {
    try {
      const res = await loginApi(loginForm)
      
      token.value = res.token
      userTable.value = 'yonghu'
      
      localStorage.setItem('Token', res.token)
      localStorage.setItem('userTable', 'yonghu')
      localStorage.setItem('userid', res.userid)
      localStorage.setItem('adminName', loginForm.username)
      
      // 获取用户信息
      await fetchUserInfo()
      
      ElMessage.success('登录成功')
      return res
    } catch (error) {
      console.error('登录失败：', error)
      throw error
    }
  }
  
  // 注册
  const register = async (registerForm) => {
    try {
      await registerApi(registerForm)
      ElMessage.success('注册成功，请登录')
    } catch (error) {
      console.error('注册失败：', error)
      throw error
    }
  }
  
  // 获取用户信息
  const fetchUserInfo = async () => {
    try {
      const userid = localStorage.getItem('userid')
      if (!userid) return
      
      const res = await getUserInfo(userid)
      userInfo.value = res.data
    } catch (error) {
      console.error('获取用户信息失败：', error)
    }
  }
  
  // 登出
  const logout = () => {
    token.value = ''
    userInfo.value = null
    userTable.value = ''
    
    localStorage.removeItem('Token')
    localStorage.removeItem('userTable')
    localStorage.removeItem('userid')
    localStorage.removeItem('adminName')
    
    ElMessage.success('已退出登录')
  }
  
  // 更新用户信息
  const updateUserInfo = async (data) => {
    try {
      // 调用更新 API
      userInfo.value = { ...userInfo.value, ...data }
      ElMessage.success('更新成功')
    } catch (error) {
      console.error('更新失败：', error)
      throw error
    }
  }
  
  return {
    token,
    userInfo,
    userTable,
    isLoggedIn,
    username,
    avatar,
    login,
    register,
    logout,
    fetchUserInfo,
    updateUserInfo
  }
})
