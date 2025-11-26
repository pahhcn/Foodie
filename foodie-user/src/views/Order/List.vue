<template>
  <div class="order-list">
    <div class="header">
      <h2>我的订单</h2>
      <el-button 
        :icon="Refresh" 
        @click="loadOrders"
        :loading="loading"
      >
        刷新
      </el-button>
    </div>
    
    <!-- 订单列表 -->
    <div v-loading="loading" class="list-content">
      <el-empty v-if="!orders.length && !loading" description="暂无订单数据" />
      
      <div v-else class="order-items">
        <el-card 
          v-for="order in orders" 
          :key="order.id"
          class="order-card"
          shadow="hover"
        >
          <div class="order-header">
            <div class="order-info">
              <span class="order-no">订单号：{{ order.dingdanhao }}</span>
              <span class="order-time">{{ order.xiadanshijian }}</span>
            </div>
            <el-tag :type="getStatusType(order.sfsh)">
              {{ order.sfsh === '是' ? '已审核' : '待审核' }}
            </el-tag>
          </div>
          
          <el-divider />
          
          <div class="order-body">
            <div class="food-info">
              <el-image 
                v-if="order.tupian"
                :src="order.tupian.split(',')[0]"
                fit="cover"
                class="food-image"
              >
                <template #error>
                  <div class="image-slot">
                    <el-icon><Picture /></el-icon>
                  </div>
                </template>
              </el-image>
              <div class="food-details">
                <h3>{{ order.meishimingcheng }}</h3>
                <p class="shop-name">店铺：{{ order.dianpumingcheng }}</p>
                <p class="quantity">数量：{{ order.shuliang }}</p>
              </div>
            </div>
            
            <div class="order-summary">
              <div class="price">
                <span class="label">总价：</span>
                <span class="amount">¥{{ order.zongjia }}</span>
              </div>
              <div class="delivery">
                <p>配送地址：{{ order.peisongdizhi }}</p>
                <p>联系方式：{{ order.lianxifangshi }}</p>
              </div>
            </div>
          </div>
          
          <el-divider />
          
          <div class="order-actions">
            <el-button 
              size="small" 
              @click="viewDetail(order.id)"
            >
              查看详情
            </el-button>
            
            <el-button 
              v-if="order.ispay === '未支付'"
              type="primary" 
              size="small"
              @click="handlePay(order.id)"
            >
              去支付
            </el-button>
            
            <el-button 
              v-if="order.sfsh === '是' && !order.pingjia"
              type="success" 
              size="small"
              @click="handleEvaluate(order)"
            >
              评价
            </el-button>
            
            <el-button 
              type="danger" 
              size="small"
              @click="handleDelete(order.id)"
            >
              删除
            </el-button>
          </div>
        </el-card>
      </div>
      
      <!-- 分页 -->
      <div v-if="total > pageSize" class="pagination">
        <el-pagination
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          :total="total"
          :page-sizes="[10, 20, 30, 50]"
          layout="total, sizes, prev, pager, next, jumper"
          @current-change="loadOrders"
          @size-change="loadOrders"
        />
      </div>
    </div>
    
    <!-- 评价对话框 -->
    <el-dialog
      v-model="evaluateDialogVisible"
      title="订单评价"
      width="500px"
    >
      <el-form :model="evaluateForm" label-width="80px">
        <el-form-item label="评分">
          <el-rate v-model="evaluateForm.pingfen" />
        </el-form-item>
        <el-form-item label="评价内容">
          <el-input
            v-model="evaluateForm.pingjianeirong"
            type="textarea"
            :rows="4"
            placeholder="请输入评价内容"
          />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="evaluateDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="submitEvaluate">提交</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useOrderStore } from '@/stores/order'
import { Refresh } from '@element-plus/icons-vue'
import { storeToRefs } from 'pinia'

const router = useRouter()
const orderStore = useOrderStore()
const { orders, loading, total } = storeToRefs(orderStore)

const currentPage = ref(1)
const pageSize = ref(10)
const evaluateDialogVisible = ref(false)
const evaluateForm = ref({
  orderId: null,
  pingfen: 5,
  pingjianeirong: ''
})

onMounted(() => {
  loadOrders()
})

const loadOrders = async () => {
  await orderStore.fetchMyOrders(currentPage.value, pageSize.value)
}

const getStatusType = (status) => {
  return status === '是' ? 'success' : 'warning'
}

const viewDetail = (id) => {
  router.push(`/user/orders/${id}`)
}

const handlePay = async (id) => {
  await orderStore.payOrder(id)
}

const handleEvaluate = (order) => {
  evaluateForm.value = {
    orderId: order.id,
    meishixinxiid: order.meishixinxiid,
    meishimingcheng: order.meishimingcheng,
    dianpumingcheng: order.dianpumingcheng,
    pingfen: 5,
    pingjianeirong: ''
  }
  evaluateDialogVisible.value = true
}

const submitEvaluate = async () => {
  await orderStore.evaluateOrder(evaluateForm.value.orderId, evaluateForm.value)
  evaluateDialogVisible.value = false
}

const handleDelete = async (id) => {
  await orderStore.deleteOrder([id])
}
</script>

<style scoped>
.order-list {
  padding: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.header h2 {
  font-size: 20px;
  font-weight: 600;
  color: #333;
}

.order-items {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.order-card {
  transition: all 0.3s;
}

.order-card:hover {
  transform: translateY(-2px);
}

.order-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.order-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.order-no {
  font-size: 14px;
  font-weight: 500;
  color: #333;
}

.order-time {
  font-size: 12px;
  color: #999;
}

.order-body {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}

.food-info {
  display: flex;
  gap: 16px;
  flex: 1;
}

.food-image {
  width: 100px;
  height: 100px;
  border-radius: 8px;
  flex-shrink: 0;
}

.image-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background: #f5f5f5;
  color: #909399;
}

.food-details {
  flex: 1;
}

.food-details h3 {
  font-size: 16px;
  font-weight: 500;
  color: #333;
  margin-bottom: 8px;
}

.food-details p {
  font-size: 14px;
  color: #666;
  margin: 4px 0;
}

.order-summary {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 12px;
}

.price {
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.price .label {
  font-size: 14px;
  color: #666;
}

.price .amount {
  font-size: 20px;
  font-weight: 600;
  color: #FF6B6B;
}

.delivery p {
  font-size: 12px;
  color: #999;
  text-align: right;
  margin: 2px 0;
}

.order-actions {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}
</style>
