<template>
  <div class="register-page">
    <div class="register-container">
      <el-card class="register-card">
        <template #header>
          <div class="card-header">
            <h2>用户注册</h2>
            <p>网上点餐系统</p>
          </div>
        </template>
        
        <el-form 
          ref="registerFormRef"
          :model="registerForm" 
          :rules="rules"
          label-width="0"
          size="large"
        >
          <el-form-item prop="yonghuzhanghao">
            <el-input 
              v-model="registerForm.yonghuzhanghao" 
              placeholder="请输入用户账号"
              :prefix-icon="User"
            />
          </el-form-item>
          
          <el-form-item prop="mima">
            <el-input 
              v-model="registerForm.mima" 
              type="password"
              placeholder="请输入密码"
              :prefix-icon="Lock"
              show-password
            />
          </el-form-item>
          
          <el-form-item prop="mima2">
            <el-input 
              v-model="registerForm.mima2" 
              type="password"
              placeholder="请确认密码"
              :prefix-icon="Lock"
              show-password
            />
          </el-form-item>
          
          <el-form-item prop="yonghuxingming">
            <el-input 
              v-model="registerForm.yonghuxingming" 
              placeholder="请输入姓名"
              :prefix-icon="User"
            />
          </el-form-item>
          
          <el-form-item prop="xingbie">
            <el-select 
              v-model="registerForm.xingbie" 
              placeholder="请选择性别"
              style="width: 100%"
            >
              <el-option label="男" value="男" />
              <el-option label="女" value="女" />
            </el-select>
          </el-form-item>
          
          <el-form-item prop="yonghushouji">
            <el-input 
              v-model="registerForm.yonghushouji" 
              placeholder="请输入手机号"
              :prefix-icon="Phone"
            />
          </el-form-item>
          
          <el-form-item>
            <el-button 
              type="primary" 
              style="width: 100%;"
              :loading="loading"
              @click="handleRegister"
            >
              注册
            </el-button>
          </el-form-item>
          
          <div class="footer-links">
            <el-button text @click="router.push('/login')">
              已有账号？立即登录
            </el-button>
            <el-button text @click="router.push('/')">
              返回首页
            </el-button>
          </div>
        </el-form>
      </el-card>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { User, Lock, Phone } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

const router = useRouter()
const userStore = useUserStore()

const registerFormRef = ref(null)
const loading = ref(false)
const registerForm = ref({
  yonghuzhanghao: '',
  mima: '',
  mima2: '',
  yonghuxingming: '',
  xingbie: '',
  yonghushouji: ''
})

const validatePass2 = (rule, value, callback) => {
  if (value === '') {
    callback(new Error('请再次输入密码'))
  } else if (value !== registerForm.value.mima) {
    callback(new Error('两次输入密码不一致!'))
  } else {
    callback()
  }
}

const rules = {
  yonghuzhanghao: [
    { required: true, message: '请输入用户账号', trigger: 'blur' },
    { min: 3, max: 20, message: '长度在 3 到 20 个字符', trigger: 'blur' }
  ],
  mima: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度不能少于6位', trigger: 'blur' }
  ],
  mima2: [
    { required: true, validator: validatePass2, trigger: 'blur' }
  ],
  yonghuxingming: [
    { required: true, message: '请输入姓名', trigger: 'blur' }
  ],
  xingbie: [
    { required: true, message: '请选择性别', trigger: 'change' }
  ],
  yonghushouji: [
    { required: true, message: '请输入手机号', trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: '手机号格式不正确', trigger: 'blur' }
  ]
}

const handleRegister = async () => {
  const valid = await registerFormRef.value.validate().catch(() => false)
  if (!valid) return
  
  loading.value = true
  try {
    await userStore.register(registerForm.value)
    ElMessage.success('注册成功！请登录')
    router.push('/login')
  } catch (error) {
    console.error('注册失败：', error)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register-page {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.register-container {
  width: 100%;
  max-width: 420px;
  padding: 20px;
}

.register-card {
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.95);
}

.card-header {
  text-align: center;
}

.card-header h2 {
  font-size: 24px;
  font-weight: 600;
  color: #333;
  margin-bottom: 8px;
}

.card-header p {
  font-size: 14px;
  color: #999;
}

.footer-links {
  display: flex;
  justify-content: space-between;
  margin-top: 12px;
}
</style>
