<template>
  <div class="main-container">
    <div class="main-content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndexMain'
}
</script>

<style lang="scss" scoped>
.main-container {
  position: fixed;
  top: 64px;
  left: 240px;
  right: 0;
  bottom: 0;
  background: #f0f2f5;
  overflow-y: auto;
  overflow-x: hidden;
  transition: left 0.3s;

  // 自定义滚动条
  &::-webkit-scrollbar {
    width: 8px;
  }

  &::-webkit-scrollbar-track {
    background: #f1f1f1;
  }

  &::-webkit-scrollbar-thumb {
    background: #c0c0c0;
    border-radius: 4px;

    &:hover {
      background: #a0a0a0;
    }
  }

  .main-content {
    padding: 24px;
    min-height: calc(100vh - 64px);
  }
}

// 响应式设计
@media (max-width: 768px) {
  .main-container {
    left: 64px;
  }
}
</style>
