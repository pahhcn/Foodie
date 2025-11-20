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
        <el-upload
          class="avatar-uploader"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload"
        >
          <el-avatar v-if="userForm.touxiang" :src="userForm.touxiang" :size="100" />
          <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
        </el-upload>
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
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'

const router = useRouter()
const userStore = useUserStore()
const loading = ref(false)
const formRef = ref(null)

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

onMounted(() => {
  if (userStore.userInfo) {
    Object.assign(userForm.value, userStore.userInfo)
  }
})

const handleUpdate = async () => {
  loading.value = true
  try {
    await userStore.updateUserInfo(userForm.value)
    ElMessage.success('更新成功')
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

const handleAvatarSuccess = (response) => {
  if (response.code === 0) {
    userForm.value.touxiang = response.file
  }
}

const beforeAvatarUpload = (file) => {
  const isImage = file.type.startsWith('image/')
  const isLt2M = file.size / 1024 / 1024 < 2
  
  if (!isImage) {
    ElMessage.error('只能上传图片文件!')
  }
  if (!isLt2M) {
    ElMessage.error('图片大小不能超过 2MB!')
  }
  return isImage && isLt2M
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

.avatar-uploader {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.3s;
}

.avatar-uploader:hover {
  border-color: #409eff;
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 100px;
  height: 100px;
  line-height: 100px;
  text-align: center;
}
</style>
