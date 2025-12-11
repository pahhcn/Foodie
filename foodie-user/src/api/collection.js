import request from '@/utils/request'

// 添加收藏
export const addCollection = (data) => {
  return request({
    url: '/storeup/add',
    method: 'post',
    data
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

// 删除收藏
export const deleteCollection = (ids) => {
  return request({
    url: '/storeup/delete',
    method: 'post',
    data: ids
  })
}

// 检查是否已收藏
export const checkCollection = (refid, tablename) => {
  return request({
    url: '/storeup/list',
    method: 'get',
    params: {
      refid,
      tablename,
      page: 1,
      limit: 1
    }
  })
}
