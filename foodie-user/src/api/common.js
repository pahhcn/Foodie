import request from '@/utils/request'

// 获取轮播图
export const getBanners = () => {
  return request({
    url: '/config/list',
    method: 'get',
    params: { page: 1, limit: 5 }
  })
}

// 获取新闻/资讯列表
export const getNewsList = (params) => {
  return request({
    url: '/news/list',
    method: 'get',
    params
  })
}

// 获取新闻详情
export const getNewsDetail = (id) => {
  return request({
    url: `/news/info/${id}`,
    method: 'get'
  })
}

// 文件上传
export const uploadFile = (file) => {
  const formData = new FormData()
  formData.append('file', file)
  
  return request({
    url: '/file/upload',
    method: 'post',
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}

// 收藏
export const addCollection = (data) => {
  return request({
    url: '/storeup/add',
    method: 'post',
    data
  })
}

// 取消收藏
export const removeCollection = (id) => {
  return request({
    url: '/storeup/delete',
    method: 'post',
    data: [id]
  })
}

// 获取收藏列表
export const getCollectionList = (params) => {
  return request({
    url: '/storeup/list',
    method: 'get',
    params
  })
}
