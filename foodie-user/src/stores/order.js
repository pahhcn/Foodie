import { defineStore } from 'pinia'
import { ref } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import * as orderApi from '@/api/order'

export const useOrderStore = defineStore('order', () => {
  // 状态
  const orders = ref([])
  const currentOrder = ref(null)
  const loading = ref(false)
  const total = ref(0)
  
  // 创建订单（核心功能，解决"一闪而过"问题）
  const createOrder = async (orderData) => {
    loading.value = true
    try {
      const res = await orderApi.createOrder(orderData)
      currentOrder.value = res.data
      
      // 不跳转页面，使用消息提示
      await ElMessageBox.confirm(
        `订单创建成功！订单号：${res.data.dingdanhao || ''}`,
        '下单成功',
        {
          confirmButtonText: '查看订单',
          cancelButtonText: '继续浏览',
          type: 'success',
          distinguishCancelAndClose: true
        }
      )
      
      return { success: true, goToOrders: true }
    } catch (error) {
      if (error === 'cancel' || error === 'close') {
        // 用户选择继续浏览
        return { success: true, goToOrders: false }
      }
      console.error('创建订单失败：', error)
      ElMessage.error('下单失败，请重试')
      throw error
    } finally {
      loading.value = false
    }
  }
  
  // 获取我的订单列表
  const fetchMyOrders = async (page = 1, limit = 10, filters = {}) => {
    loading.value = true
    try {
      const username = localStorage.getItem('adminName')
      const params = {
        page,
        limit,
        yonghuzhanghao: username,
        sfsh: '是',
        ...filters
      }
      
      const res = await orderApi.getOrderList(params)
      orders.value = res.data.list || []
      total.value = res.data.total || 0
      
      return res.data
    } catch (error) {
      console.error('获取订单列表失败：', error)
      orders.value = []
      throw error
    } finally {
      loading.value = false
    }
  }
  
  // 获取订单详情
  const fetchOrderDetail = async (id) => {
    loading.value = true
    try {
      const res = await orderApi.getOrderDetail(id)
      currentOrder.value = res.data
      return res.data
    } catch (error) {
      console.error('获取订单详情失败：', error)
      throw error
    } finally {
      loading.value = false
    }
  }
  
  // 支付订单
  const payOrder = async (id) => {
    try {
      await ElMessageBox.confirm(
        '确认支付该订单吗？',
        '支付确认',
        {
          confirmButtonText: '确认支付',
          cancelButtonText: '取消',
          type: 'warning'
        }
      )
      
      // 调用支付接口
      await orderApi.payOrder(id)
      
      ElMessage.success('支付成功')
      
      // 刷新订单列表
      await fetchMyOrders()
    } catch (error) {
      if (error !== 'cancel') {
        console.error('支付失败：', error)
      }
    }
  }
  
  // 删除订单
  const deleteOrder = async (ids) => {
    try {
      await ElMessageBox.confirm(
        '确认删除该订单吗？删除后无法恢复',
        '删除确认',
        {
          confirmButtonText: '确认删除',
          cancelButtonText: '取消',
          type: 'warning'
        }
      )
      
      await orderApi.deleteOrder(ids)
      
      ElMessage.success('删除成功')
      
      // 刷新订单列表
      await fetchMyOrders()
    } catch (error) {
      if (error !== 'cancel') {
        console.error('删除失败：', error)
      }
    }
  }
  
  // 评价订单
  const evaluateOrder = async (orderId, evaluationData) => {
    try {
      await orderApi.evaluateOrder(orderId, evaluationData)
      ElMessage.success('评价成功')
      
      // 刷新订单列表
      await fetchMyOrders()
    } catch (error) {
      console.error('评价失败：', error)
      throw error
    }
  }
  
  return {
    orders,
    currentOrder,
    loading,
    total,
    createOrder,
    fetchMyOrders,
    fetchOrderDetail,
    payOrder,
    deleteOrder,
    evaluateOrder
  }
})
