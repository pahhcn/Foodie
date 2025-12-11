<template>
  <div class="page-container">
    <!-- 页面头部 -->
    <div class="page-header">
      <h1 class="page-title">
        <i class="el-icon-s-home"></i>
        欢迎回来，{{ adminName }}
      </h1>
      <p class="page-description">{{ currentTime }} | {{ role }}</p>
    </div>

    <!-- 统计卡片 -->
    <el-row :gutter="20" class="stat-cards">
      <el-col :xs="24" :sm="12" :md="6" v-for="(stat, index) in stats" :key="index">
        <div class="stat-card">
          <div :class="['stat-icon', stat.type]">
            <i :class="stat.icon"></i>
          </div>
          <div class="stat-value">{{ stat.value }}</div>
          <div class="stat-label">{{ stat.label }}</div>
          <div class="stat-trend" :class="stat.trend > 0 ? 'up' : 'down'">
            <i :class="stat.trend > 0 ? 'el-icon-top' : 'el-icon-bottom'"></i>
            {{ Math.abs(stat.trend) }}%
          </div>
        </div>
      </el-col>
    </el-row>

    <!-- 快捷操作 -->
    <div class="page-content" style="margin-top: 20px;">
      <h2 class="section-title">
        <i class="el-icon-s-operation"></i>
        快捷操作
      </h2>
      <el-row :gutter="16" class="quick-actions">
        <el-col :xs="12" :sm="8" :md="6" v-for="(action, index) in quickActions" :key="index">
          <div class="action-card" @click="handleAction(action.path)">
            <div class="action-icon" :style="{ background: action.color }">
              <i :class="action.icon"></i>
            </div>
            <div class="action-name">{{ action.name }}</div>
          </div>
        </el-col>
      </el-row>
    </div>

    <!-- 数据分析 -->
    <el-row :gutter="20" style="margin-top: 20px;">
      <el-col :xs="24" :md="16">
        <div class="page-content">
          <h2 class="section-title">
            <i class="el-icon-s-data"></i>
            数据概览
          </h2>
          <div class="chart-container">
            <div id="salesChart" style="width: 100%; height: 300px;"></div>
          </div>
        </div>
      </el-col>
      
      <el-col :xs="24" :md="8">
        <div class="page-content">
          <h2 class="section-title">
            <i class="el-icon-bell"></i>
            系统通知
          </h2>
          <div class="notification-list">
            <div class="notification-item" v-for="(notice, index) in notifications" :key="index">
              <div class="notice-dot" :class="notice.type"></div>
              <div class="notice-content">
                <div class="notice-title">{{ notice.title }}</div>
                <div class="notice-time">{{ notice.time }}</div>
              </div>
            </div>
            <div class="notification-empty" v-if="notifications.length === 0">
              <i class="el-icon-bell"></i>
              <p>暂无通知</p>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import echarts from 'echarts'

export default {
  name: "Home",
  data() {
    return {
      adminName: '',
      role: '',
      currentTime: '',
      salesChart: null,
      stats: [
        {
          icon: 'el-icon-s-order',
          label: '今日订单',
          value: '128',
          trend: 12.5,
          type: 'primary'
        },
        {
          icon: 'el-icon-s-goods',
          label: '商品总数',
          value: '256',
          trend: 8.3,
          type: 'success'
        },
        {
          icon: 'el-icon-user',
          label: '用户总数',
          value: '1,024',
          trend: 15.2,
          type: 'warning'
        },
        {
          icon: 'el-icon-s-finance',
          label: '今日营收',
          value: '¥8,520',
          trend: -3.5,
          type: 'danger'
        }
      ],
      quickActions: [
        {
          name: '订单管理',
          icon: 'el-icon-s-order',
          color: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
          path: '/dingdan'
        },
        {
          name: '商品管理',
          icon: 'el-icon-s-goods',
          color: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
          path: '/shangpin'
        },
        {
          name: '用户管理',
          icon: 'el-icon-user',
          color: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
          path: '/yonghu'
        },
        {
          name: '数据统计',
          icon: 'el-icon-s-data',
          color: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
          path: '/tongji'
        },
        {
          name: '系统设置',
          icon: 'el-icon-setting',
          color: 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
          path: '/shezhi'
        },
        {
          name: '个人中心',
          icon: 'el-icon-user-solid',
          color: 'linear-gradient(135deg, #30cfd0 0%, #330867 100%)',
          path: '/center'
        }
      ],
      notifications: [
        {
          title: '系统更新通知',
          time: '2小时前',
          type: 'primary'
        },
        {
          title: '新订单提醒',
          time: '5小时前',
          type: 'success'
        },
        {
          title: '库存预警',
          time: '1天前',
          type: 'warning'
        }
      ]
    };
  },
  mounted() {
    this.adminName = this.$storage.get('adminName') || '管理员';
    this.role = this.$storage.get('role') || '系统管理员';
    this.updateTime();
    setInterval(this.updateTime, 1000);
    this.$nextTick(() => {
      this.initSalesChart();
    });
  },
  beforeDestroy() {
    if (this.salesChart) {
      this.salesChart.dispose();
    }
  },
  methods: {
    initSalesChart() {
      const chartDom = document.getElementById('salesChart');
      if (!chartDom) return;
      
      this.salesChart = echarts.init(chartDom);
      
      const option = {
        title: {
          text: '近7天订单趋势',
          left: 'center',
          textStyle: {
            fontSize: 16,
            fontWeight: 600,
            color: '#333'
          }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: ['订单数', '营收'],
          bottom: 10
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '15%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
          axisLine: {
            lineStyle: {
              color: '#e0e0e0'
            }
          },
          axisLabel: {
            color: '#666'
          }
        },
        yAxis: [
          {
            type: 'value',
            name: '订单数',
            position: 'left',
            axisLine: {
              lineStyle: {
                color: '#e0e0e0'
              }
            },
            axisLabel: {
              color: '#666'
            },
            splitLine: {
              lineStyle: {
                color: '#f0f0f0'
              }
            }
          },
          {
            type: 'value',
            name: '营收(元)',
            position: 'right',
            axisLine: {
              lineStyle: {
                color: '#e0e0e0'
              }
            },
            axisLabel: {
              color: '#666',
              formatter: '¥{value}'
            },
            splitLine: {
              show: false
            }
          }
        ],
        series: [
          {
            name: '订单数',
            type: 'bar',
            data: [85, 92, 78, 105, 120, 145, 128],
            itemStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: '#667eea' },
                { offset: 1, color: '#764ba2' }
              ]),
              borderRadius: [8, 8, 0, 0]
            },
            barWidth: '40%'
          },
          {
            name: '营收',
            type: 'line',
            yAxisIndex: 1,
            data: [5200, 6100, 4800, 7200, 8500, 9800, 8520],
            smooth: true,
            itemStyle: {
              color: '#f5576c'
            },
            lineStyle: {
              width: 3,
              color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                { offset: 0, color: '#f093fb' },
                { offset: 1, color: '#f5576c' }
              ])
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: 'rgba(240, 147, 251, 0.3)' },
                { offset: 1, color: 'rgba(245, 87, 108, 0.1)' }
              ])
            }
          }
        ]
      };
      
      this.salesChart.setOption(option);
      
      // 响应式调整
      window.addEventListener('resize', () => {
        if (this.salesChart) {
          this.salesChart.resize();
        }
      });
    },
    
    updateTime() {
      const now = new Date();
      const hours = now.getHours();
      let greeting = '早上好';
      if (hours >= 12 && hours < 18) {
        greeting = '下午好';
      } else if (hours >= 18) {
        greeting = '晚上好';
      }
      
      const timeStr = now.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      });
      
      this.currentTime = `${greeting}，${timeStr}`;
    },
    
    handleAction(path) {
      if (path) {
        this.$router.push(path);
      } else {
        this.$message.info('功能开发中...');
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.page-container {
  padding: 24px;
  min-height: calc(100vh - 64px);
  background: #f5f7fa;
}

.page-header {
  margin-bottom: 24px;
  padding: 24px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);

  .page-title {
    font-size: 28px;
    font-weight: 600;
    color: #333;
    margin: 0 0 8px 0;
    display: flex;
    align-items: center;
    gap: 12px;

    i {
      font-size: 32px;
      color: #1e3c72;
    }
  }

  .page-description {
    font-size: 14px;
    color: #8c8c8c;
    margin: 0;
  }
}

.page-content {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
}

.stat-cards {
  margin-bottom: 20px;
  
  .stat-card {
    position: relative;
    background: #fff;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
    transition: all 0.3s;
    overflow: hidden;

    &::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
    }

    &:hover {
      transform: translateY(-4px);
      box-shadow: 0 6px 24px rgba(0, 0, 0, 0.1);
    }

    .stat-icon {
      width: 56px;
      height: 56px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 16px;

      i {
        font-size: 28px;
        color: #fff;
      }

      &.primary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      }

      &.success {
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
      }

      &.warning {
        background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
      }

      &.danger {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
      }
    }

    .stat-value {
      font-size: 28px;
      font-weight: 700;
      color: #333;
      margin-bottom: 8px;
    }

    .stat-label {
      font-size: 14px;
      color: #8c8c8c;
      font-weight: 500;
    }
    
    .stat-trend {
      position: absolute;
      top: 20px;
      right: 20px;
      font-size: 14px;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 4px;
      padding: 4px 8px;
      border-radius: 6px;
      
      &.up {
        color: #2ecc71;
        background: rgba(46, 204, 113, 0.1);
      }
      
      &.down {
        color: #e74c3c;
        background: rgba(231, 76, 60, 0.1);
      }
    }
  }
}

.section-title {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin: 0 0 20px 0;
  display: flex;
  align-items: center;
  gap: 8px;
  
  i {
    font-size: 20px;
    color: #1e3c72;
  }
}

.quick-actions {
  .action-card {
    background: #fff;
    border: 2px solid #f0f0f0;
    border-radius: 12px;
    padding: 24px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s;
    margin-bottom: 16px;
    
    &:hover {
      border-color: #1e3c72;
      transform: translateY(-4px);
      box-shadow: 0 6px 24px rgba(30, 60, 114, 0.15);
    }
    
    .action-icon {
      width: 64px;
      height: 64px;
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 16px;
      
      i {
        font-size: 32px;
        color: #fff;
      }
    }
    
    .action-name {
      font-size: 15px;
      font-weight: 500;
      color: #333;
    }
  }
}

.chart-container {
  height: 300px;
  
  .chart-placeholder {
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: #f8f9fa;
    border-radius: 12px;
    color: #8c8c8c;
    
    i {
      font-size: 64px;
      margin-bottom: 16px;
      color: #d0d0d0;
    }
    
    p {
      font-size: 16px;
      margin: 0 0 8px 0;
    }
    
    span {
      font-size: 14px;
      color: #b0b0b0;
    }
  }
}

.notification-list {
  .notification-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 16px;
    border-radius: 8px;
    margin-bottom: 12px;
    background: #f8f9fa;
    transition: all 0.3s;
    
    &:hover {
      background: #e8eaf0;
      transform: translateX(4px);
    }
    
    .notice-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      margin-top: 6px;
      flex-shrink: 0;
      
      &.primary {
        background: #1e3c72;
      }
      
      &.success {
        background: #2ecc71;
      }
      
      &.warning {
        background: #f39c12;
      }
      
      &.danger {
        background: #e74c3c;
      }
    }
    
    .notice-content {
      flex: 1;
      
      .notice-title {
        font-size: 14px;
        color: #333;
        margin-bottom: 4px;
      }
      
      .notice-time {
        font-size: 12px;
        color: #8c8c8c;
      }
    }
  }
  
  .notification-empty {
    text-align: center;
    padding: 40px 20px;
    color: #8c8c8c;
    
    i {
      font-size: 48px;
      color: #d0d0d0;
      margin-bottom: 12px;
    }
    
    p {
      margin: 0;
      font-size: 14px;
    }
  }
}
</style>
