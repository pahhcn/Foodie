<template>
  <div v-loading="loading" class="order-detail">
    <el-page-header @back="router.back()" title="返回">
      <template #content>
        <span class="page-title">订单详情</span>
      </template>
    </el-page-header>
    
    <el-card v-if="order" class="detail-card" style="margin-top: 20px;">
      <template #header>
        <div class="card-header">
          <span>订单信息</span>
          <el-tag :type="order.sfsh === '是' ? 'success' : 'warning'">
            {{ order.sfsh === '是' ? '已审核' : '待审核' }}
          </el-tag>
        </div>
      </template>
      
      <el-descriptions :column="2" border>
        <el-descriptions-item label="订单号">
          {{ order.dingdanhao }}
        </el-descriptions-item>
        <el-descriptions-item label="下单时间">
          {{ order.xiadanshijian }}
        </el-descriptions-item>
        <el-descriptions-item label="美食名称">
          {{ order.meishimingcheng }}
        </el-descriptions-item>
        <el-descriptions-item label="店铺名称">
          {{ order.dianpumingcheng }}
        </el-descriptions-item>
        <el-descriptions-item label="数量">
          {{ order.shuliang }}
        </el-descriptions-item>
        <el-descriptions-item label="单价">
          ¥{{ order.danjia }}
        </el-descriptions-item>
        <el-descriptions-item label="总价">
          <span style="color: #FF6B6B; font-size: 18px; font-weight: 600;">
            ¥{{ order.zongjia }}
          </span>
        </el-descriptions-item>
        <el-descriptions-item label="支付状态">
          <el-tag :type="order.ispay === '已支付' ? 'success' : 'info'">
            {{ order.ispay || '未支付' }}
          </el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="配送地址" :span="2">
          {{ order.peisongdizhi }}
        </el-descriptions-item>
        <el-descriptions-item label="联系方式" :span="2">
          {{ order.lianxifangshi }}
        </el-descriptions-item>
        <el-descriptions-item v-if="order.beizhu" label="备注" :span="2">
          {{ order.beizhu }}
        </el-descriptions-item>
      </el-descriptions>
      
      <div v-if="order.tupian" class="food-images" style="margin-top: 20px;">
        <h3>美食图片</h3>
        <el-space wrap>
          <el-image
            v-for="(img, index) in order.tupian.split(',')"
            :key="index"
            :src="img"
            fit="cover"
            style="width: 150px; height: 150px; border-radius: 8px;"
            :preview-src-list="order.tupian.split(',')"
            :initial-index="index"
          />
        </el-space>
      </div>
      
      <div class="actions" style="margin-top: 20px;">
        <el-button v-if="order.ispay === '未支付'" type="primary" @click="handlePay">
          去支付
        </el-button>
        <el-button type="danger" @click="handleDelete">删除订单</el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useOrderStore } from '@/stores/order'
import { storeToRefs } from 'pinia'

const router = useRouter()
const route = useRoute()
const orderStore = useOrderStore()
const { currentOrder: order, loading } = storeToRefs(orderStore)

onMounted(async () => {
  const id = route.params.id
  await orderStore.fetchOrderDetail(id)
})

const handlePay = async () => {
  await orderStore.payOrder(order.value.id)
  await orderStore.fetchOrderDetail(order.value.id)
}

const handleDelete = async () => {
  await orderStore.deleteOrder([order.value.id])
  router.push('/user/orders')
}
</script>

<style scoped>
.order-detail {
  padding: 20px;
}

.page-title {
  font-size: 18px;
  font-weight: 600;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.food-images h3 {
  font-size: 16px;
  margin-bottom: 12px;
}

.actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
</style>
