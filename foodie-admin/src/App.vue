<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "app"
};
</script>

<style lang="scss">
// ==================== 全局重置 ====================
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

html, body {
  width: 100%;
  height: 100%;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  height: 100%;
  background: #f0f2f5;
}

// ==================== 全局滚动条 ====================
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb {
  background: #c0c0c0;
  border-radius: 4px;
  transition: background 0.3s;

  &:hover {
    background: #a0a0a0;
  }
}

// ==================== 全局过渡动画 ====================
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

.slide-fade-enter-active {
  transition: all 0.3s ease;
}

.slide-fade-leave-active {
  transition: all 0.2s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}

.slide-fade-enter, .slide-fade-leave-to {
  transform: translateX(10px);
  opacity: 0;
}

// ==================== Element UI 组件优化 ====================

// 按钮
.el-button {
  border-radius: 8px;
  font-weight: 500;
  transition: all 0.3s;
  
  &.el-button--primary {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    border: none;
    
    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(30, 60, 114, 0.4);
    }
    
    &:active {
      transform: translateY(0);
    }
  }
  
  &.el-button--success {
    background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
    border: none;
  }
  
  &.el-button--warning {
    background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
    border: none;
  }
  
  &.el-button--danger {
    background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
    border: none;
  }
  
  &.el-button--info {
    background: linear-gradient(135deg, #95a5a6 0%, #7f8c8d 100%);
    border: none;
  }
}

// 卡片
.el-card {
  border-radius: 12px;
  border: none;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s;
  
  &:hover {
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12);
    transform: translateY(-2px);
  }
  
  .el-card__header {
    border-bottom: 1px solid #f0f0f0;
    padding: 18px 20px;
    background: #fafafa;
    font-weight: 600;
    color: #333;
  }
  
  .el-card__body {
    padding: 20px;
  }
}

// 表格
.el-table {
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  
  th {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%) !important;
    color: #fff !important;
    font-weight: 600;
    border: none !important;
  }
  
  td {
    border-bottom: 1px solid #f0f0f0;
  }
  
  tr:hover > td {
    background: #f8f9fa !important;
  }
  
  .el-table__empty-block {
    border-radius: 12px;
  }
}

// 分页
.el-pagination {
  margin-top: 20px;
  text-align: center;
  
  .el-pager li {
    border-radius: 6px;
    margin: 0 4px;
    
    &.active {
      background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
      color: #fff;
    }
  }
  
  .btn-prev, .btn-next {
    border-radius: 6px;
  }
}

// 对话框
.el-dialog {
  border-radius: 16px;
  overflow: hidden;
  
  .el-dialog__header {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    padding: 20px;
    
    .el-dialog__title {
      color: #fff;
      font-weight: 600;
      font-size: 18px;
    }
    
    .el-dialog__headerbtn {
      top: 20px;
      
      .el-dialog__close {
        color: #fff;
        font-size: 20px;
        
        &:hover {
          color: #fff;
        }
      }
    }
  }
  
  .el-dialog__body {
    padding: 24px;
  }
  
  .el-dialog__footer {
    padding: 16px 24px;
    border-top: 1px solid #f0f0f0;
  }
}

// 消息框
.el-message-box {
  border-radius: 16px;
  overflow: hidden;
  
  .el-message-box__header {
    padding: 20px 20px 10px;
    
    .el-message-box__title {
      font-weight: 600;
      color: #333;
    }
  }
  
  .el-message-box__btns {
    padding: 10px 20px 20px;
  }
}

// 表单
.el-form {
  .el-form-item__label {
    font-weight: 500;
    color: #606266;
  }
  
  .el-input__inner,
  .el-textarea__inner {
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    transition: all 0.3s;
    
    &:focus {
      border-color: #1e3c72;
      box-shadow: 0 0 0 2px rgba(30, 60, 114, 0.1);
    }
  }
  
  .el-select {
    width: 100%;
    
    .el-input__inner {
      border-radius: 8px;
    }
  }
}

// 标签
.el-tag {
  border-radius: 6px;
  border: none;
  padding: 0 12px;
  height: 28px;
  line-height: 28px;
  
  &.el-tag--primary {
    background: rgba(30, 60, 114, 0.1);
    color: #1e3c72;
  }
  
  &.el-tag--success {
    background: rgba(46, 204, 113, 0.1);
    color: #2ecc71;
  }
  
  &.el-tag--warning {
    background: rgba(243, 156, 18, 0.1);
    color: #f39c12;
  }
  
  &.el-tag--danger {
    background: rgba(231, 76, 60, 0.1);
    color: #e74c3c;
  }
  
  &.el-tag--info {
    background: rgba(149, 165, 166, 0.1);
    color: #95a5a6;
  }
}

// 徽章
.el-badge {
  .el-badge__content {
    border-radius: 10px;
    font-weight: 600;
  }
}

// 下拉菜单
.el-dropdown-menu {
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  border: none;
  padding: 8px;
  
  .el-dropdown-menu__item {
    border-radius: 8px;
    padding: 10px 16px;
    margin-bottom: 4px;
    
    &:last-child {
      margin-bottom: 0;
    }
    
    &:hover {
      background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
      color: #fff;
    }
  }
}

// 步骤条
.el-steps {
  .el-step__head.is-finish {
    color: #1e3c72;
    border-color: #1e3c72;
  }
  
  .el-step__title.is-finish {
    color: #1e3c72;
  }
}

// 开关
.el-switch.is-checked .el-switch__core {
  background-color: #1e3c72;
  border-color: #1e3c72;
}

// 单选框
.el-radio__input.is-checked .el-radio__inner {
  background-color: #1e3c72;
  border-color: #1e3c72;
}

.el-radio__input.is-checked + .el-radio__label {
  color: #1e3c72;
}

// 复选框
.el-checkbox__input.is-checked .el-checkbox__inner {
  background-color: #1e3c72;
  border-color: #1e3c72;
}

.el-checkbox__input.is-checked + .el-checkbox__label {
  color: #1e3c72;
}

// 进度条
.el-progress-bar__inner {
  background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
}

// 加载
.el-loading-mask {
  background-color: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(4px);
}

// ==================== 自定义工具类 ====================
.page-container {
  padding: 24px;
  min-height: 100%;
  width: 100%;
}

.page-header {
  background: #fff;
  padding: 20px 24px;
  border-radius: 12px;
  margin-bottom: 20px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  
  .page-title {
    font-size: 20px;
    font-weight: 600;
    color: #333;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 12px;
    
    i {
      font-size: 24px;
      color: #1e3c72;
    }
  }
  
  .page-description {
    font-size: 14px;
    color: #8c8c8c;
    margin: 8px 0 0 0;
  }
}

.page-content {
  background: #fff;
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

// 统计卡片
.stat-card {
  background: #fff;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s;
  
  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.12);
  }
  
  .stat-icon {
    width: 56px;
    height: 56px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    margin-bottom: 16px;
    
    &.primary {
      background: linear-gradient(135deg, rgba(30, 60, 114, 0.1) 0%, rgba(42, 82, 152, 0.1) 100%);
      color: #1e3c72;
    }
    
    &.success {
      background: linear-gradient(135deg, rgba(46, 204, 113, 0.1) 0%, rgba(39, 174, 96, 0.1) 100%);
      color: #2ecc71;
    }
    
    &.warning {
      background: linear-gradient(135deg, rgba(243, 156, 18, 0.1) 0%, rgba(230, 126, 34, 0.1) 100%);
      color: #f39c12;
    }
    
    &.danger {
      background: linear-gradient(135deg, rgba(231, 76, 60, 0.1) 0%, rgba(192, 57, 43, 0.1) 100%);
      color: #e74c3c;
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
  }
}

// 响应式
@media (max-width: 768px) {
  .page-container {
    padding: 16px;
  }
}
</style>
