import request from '@/utils/request'

// 创建订单
export const createOrder = (data) => {
  return request({
    url: '/meishidingdan/add',
    method: 'post',
    data
  })
}

// 获取订单列表
export const getOrderList = (params) => {
  return request({
    url: '/meishidingdan/list',
    method: 'get',
    params
  })
}

// 获取订单详情
export const getOrderDetail = (id) => {
  return request({
    url: `/meishidingdan/info/${id}`,
    method: 'get'
  })
}

// 更新订单
export const updateOrder = (data) => {
  return request({
    url: '/meishidingdan/update',
    method: 'post',
    data
  })
}

// 删除订单
export const deleteOrder = (ids) => {
  return request({
    url: '/meishidingdan/delete',
    method: 'post',
    data: ids
  })
}

// 支付订单
export const payOrder = (id) => {
  return request({
    url: `/meishidingdan/pay/${id}`,
    method: 'post'
  })
}

// 评价订单
export const evaluateOrder = (orderId, data) => {
  return request({
    url: '/meishipingjia/add',
    method: 'post',
    data: {
      ...data,
      dingdanid: orderId
    }
  })
}
