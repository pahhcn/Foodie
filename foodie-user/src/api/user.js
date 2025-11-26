import request from '@/utils/request'

// 登录
export const login = (data) => {
  // 将 JSON 数据转换为表单格式
  const formData = new URLSearchParams()
  formData.append('username', data.username)
  formData.append('password', data.password)
  
  return request({
    url: '/yonghu/login',
    method: 'post',
    data: formData,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })
}

// 注册
export const register = (data) => {
  return request({
    url: '/yonghu/register',
    method: 'post',
    data
  })
}

// 获取用户信息
export const getUserInfo = (id) => {
  return request({
    url: `/yonghu/info/${id}`,
    method: 'get'
  })
}

// 更新用户信息
export const updateUserInfo = (data) => {
  return request({
    url: '/yonghu/update',
    method: 'post',
    data
  })
}

// 退出登录
export const logout = () => {
  return request({
    url: '/yonghu/logout',
    method: 'post'
  })
}
