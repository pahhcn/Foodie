<template>
  <div class="user-center">
    <h2>个人中心</h2>
    
    <el-form
      ref="formRef"
      :model="userForm"
      label-width="120px"
      v-loading="loading"
    >
      <el-form-item label="用户账号">
        <el-input v-model="userForm.yonghuzhanghao" disabled />
      </el-form-item>
      
      <el-form-item label="密码">
        <el-input v-model="userForm.mima" type="password" placeholder="不修改请留空" />
      </el-form-item>
      
      <el-form-item label="用户姓名">
        <el-input v-model="userForm.yonghuxingming" />
      </el-form-item>
      
      <el-form-item label="性别">
        <el-radio-group v-model="userForm.xingbie">
          <el-radio label="男">男</el-radio>
          <el-radio label="女">女</el-radio>
        </el-radio-group>
      </el-form-item>
      
      <el-form-item label="年龄">
        <el-input-number v-model="userForm.nianling" :min="1" :max="120" />
      </el-form-item>
      
      <el-form-item label="头像">
        <div class="avatar-section">
          <el-upload
            class="avatar-uploader"
            action="/foodie/file/upload"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :on-error="handleAvatarError"
            :before-upload="beforeAvatarUpload"
            :headers="uploadHeaders"
            name="file"
          >
            <el-avatar v-if="avatarUrl" :src="avatarUrl" :size="100" class="avatar-preview">
              <el-icon><User /></el-icon>
            </el-avatar>
            <div v-else class="avatar-uploader-icon">
              <el-icon><Plus /></el-icon>
              <div class="upload-text">点击上传头像</div>
            </div>
          </el-upload>
          <el-text type="info" size="small">
            支持 jpg、png、gif 格式，大小不超过 2MB
          </el-text>
        </div>
      </el-form-item>
      
      <el-form-item label="手机号">
        <el-input v-model="userForm.yonghushouji" />
      </el-form-item>
      
      <el-form-item label="配送地址">
        <el-input v-model="userForm.peisongdizhi" type="textarea" :rows="2" />
      </el-form-item>
      
      <el-form-item>
        <el-button type="primary" @click="handleUpdate">更新信息</el-button>
        <el-button @click="handleLogout">退出登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { ElMessage, ElMessageBox } from 'element-plus'
import { User, Plus } from '@element-plus/icons-vue'

const router = useRouter()
const userStore = useUserStore()
const loading = ref(false)
const formRef = ref(null)

// 上传请求头
const uploadHeaders = {
  'Token': localStorage.getItem('Token') || ''
}

const userForm = ref({
  yonghuzhanghao: '',
  mima: '',
  yonghuxingming: '',
  xingbie: '',
  nianling: null,
  touxiang: '',
  yonghushouji: '',
  peisongdizhi: ''
})

// 头像 URL（完整路径）
const avatarUrl = computed(() => {
  if (!userForm.value.touxiang) return ''
  // 如果已经是完整 URL，直接返回
  if (userForm.value.touxiang.startsWith('http')) {
    return userForm.value.touxiang
  }
  // 否则拼接为完整 URL
  return `http://localhost:8080/foodie/upload/${userForm.value.touxiang}`
})

onMounted(async () => {
  loading.value = true
  try {
    // 重新获取最新的用户信息
    await userStore.fetchUserInfo()
    
    if (userStore.userInfo) {
      // 复制用户信息到表单，但不包括密码
      Object.assign(userForm.value, {
        ...userStore.userInfo,
        mima: '' // 密码字段留空
      })
    }
  } catch (error) {
    console.error('加载用户信息失败：', error)
  } finally {
    loading.value = false
  }
})

const handleUpdate = async () => {
  loading.value = true
  try {
    console.log('提交更新的用户信息：', userForm.value)
    await userStore.updateUserInfo(userForm.value)
    // 更新成功后清空密码字段
    userForm.value.mima = ''
  } catch (error) {
    console.error('更新失败：', error)
  } finally {
    loading.value = false
  }
}

const handleLogout = () => {
  ElMessageBox.confirm('确认退出登录吗？', '提示', {
    confirmButtonText: '确认',
    cancelButtonText: '取消',
    type: 'warning'
  }).then(() => {
    userStore.logout()
    router.push('/')
  }).catch(() => {})
}

// 头像上传成功
const handleAvatarSuccess = (response, file) => {
  console.log('上传响应：', response)
  console.log('上传文件：', file)
  if (response.code === 0) {
    // 后端返回的是文件名，保存到表单
    userForm.value.touxiang = response.file
    ElMessage.success('头像上传成功')
  } else {
    ElMessage.error(response.msg || '头像上传失败')
  }
}

// 上传失败
const handleAvatarError = (error) => {
  console.error('上传失败：', error)
  ElMessage.error('头像上传失败，请重试')
}

// 上传前验证
const beforeAvatarUpload = (file) => {
  const isImage = file.type.startsWith('image/')
  const isLt2M = file.size / 1024 / 1024 < 2
  
  if (!isImage) {
    ElMessage.error('只能上传图片文件!')
    return false
  }
  if (!isLt2M) {
    ElMessage.error('图片大小不能超过 2MB!')
    return false
  }
  return true
}


</script>

<style scoped>
.user-center {
  padding: 20px;
}

h2 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 24px;
}

.avatar-section {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.avatar-uploader {
  display: inline-block;
}

.avatar-uploader :deep(.el-upload) {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: all 0.3s;
}

.avatar-uploader :deep(.el-upload:hover) {
  border-color: #409eff;
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 100px;
  height: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.avatar-uploader-icon .el-icon {
  font-size: 32px;
}

.upload-text {
  font-size: 12px;
  color: #999;
}

.avatar-preview {
  display: block;
  cursor: pointer;
}

.avatar-preview:hover {
  opacity: 0.8;
}
</style>
