import request from '@/utils/request'

// 获取美食列表
export const getFoodList = (params) => {
  return request({
    url: '/meishixinxi/list',
    method: 'get',
    params
  })
}

// 获取美食详情
export const getFoodDetail = (id) => {
  return request({
    url: `/meishixinxi/info/${id}`,
    method: 'get'
  })
}

// 获取美食分类
export const getFoodCategories = () => {
  return request({
    url: '/meishifenlei/list',
    method: 'get',
    params: { page: 1, limit: 100 }
  })
}

// 获取推荐美食
export const getRecommendFoods = (limit = 8) => {
  return request({
    url: '/meishixinxi/list',
    method: 'get',
    params: {
      page: 1,
      limit,
      sort: 'clicknum',
      order: 'desc'
    }
  })
}
