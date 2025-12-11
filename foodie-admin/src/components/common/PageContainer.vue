<template>
  <div class="page-container">
    <!-- 页面头部 -->
    <div class="page-header" v-if="title">
      <div class="header-left">
        <h1 class="page-title">
          <i :class="icon" v-if="icon"></i>
          {{ title }}
        </h1>
        <p class="page-description" v-if="description">{{ description }}</p>
      </div>
      <div class="header-right">
        <slot name="header-actions"></slot>
      </div>
    </div>

    <!-- 页面内容 -->
    <div class="page-content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PageContainer',
  props: {
    title: {
      type: String,
      default: ''
    },
    description: {
      type: String,
      default: ''
    },
    icon: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="scss" scoped>
.page-container {
  padding: 24px;
  min-height: calc(100vh - 64px);
  background: #f5f7fa;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  padding: 24px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);

  .header-left {
    flex: 1;
  }

  .header-right {
    display: flex;
    gap: 12px;
    align-items: center;
  }

  .page-title {
    font-size: 24px;
    font-weight: 600;
    color: #333;
    margin: 0 0 8px 0;
    display: flex;
    align-items: center;
    gap: 12px;

    i {
      font-size: 28px;
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
  min-height: 400px;
}

// 响应式设计
@media (max-width: 768px) {
  .page-container {
    padding: 16px;
  }

  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
    padding: 16px;

    .header-right {
      width: 100%;
      justify-content: flex-start;
    }
  }

  .page-content {
    padding: 16px;
  }
}
</style>
