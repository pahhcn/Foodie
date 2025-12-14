<template>
  <div class="admin-header">
    <div class="header-content">
      <!-- 左侧品牌区 -->
      <div class="header-left">
        <div class="brand-logo">
          <i class="el-icon-s-shop"></i>
        </div>
        <div class="brand-info">
          <h1 class="brand-title">{{ this.$project.projectName }}</h1>
          <span class="brand-subtitle">后台管理系统</span>
        </div>
      </div>

      <!-- 右侧操作区 -->
      <div class="header-right">
        <!-- 快捷功能 -->
        <div class="quick-actions">
          <el-tooltip content="返回前台" placement="bottom">
            <div class="action-item" @click="goToIndex">
              <i class="el-icon-s-home"></i>
            </div>
          </el-tooltip>
          
          <el-tooltip content="通知消息" placement="bottom">
            <el-badge :value="notificationCount" :hidden="notificationCount === 0" class="notification-badge">
              <div class="action-item">
                <i class="el-icon-bell"></i>
              </div>
            </el-badge>
          </el-tooltip>
        </div>

        <!-- 用户信息 -->
        <el-dropdown trigger="click" @command="handleCommand" class="user-dropdown">
          <div class="user-info">
            <el-avatar :size="36" class="user-avatar">
              <i class="el-icon-user-solid"></i>
            </el-avatar>
            <div class="user-details">
              <span class="user-name">{{ this.$storage.get('adminName') }}</span>
              <span class="user-role">{{ this.$storage.get('role') }}</span>
            </div>
            <i class="el-icon-arrow-down dropdown-icon"></i>
          </div>
          
          <el-dropdown-menu slot="dropdown" class="user-menu">
            <el-dropdown-item command="center">
              <i class="el-icon-user"></i>
              个人中心
            </el-dropdown-item>
            <el-dropdown-item command="password">
              <i class="el-icon-lock"></i>
              修改密码
            </el-dropdown-item>
            <el-dropdown-item divided command="logout">
              <i class="el-icon-switch-button"></i>
              退出登录
            </el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "IndexHeader",
  data() {
    return {
      user: {},
      notificationCount: 0
    };
  },
  mounted() {
    this.getUserInfo();
  },
  methods: {
    // 获取用户信息
    getUserInfo() {
      let sessionTable = this.$storage.get("sessionTable");
      if (!sessionTable) return;
      
      this.$http({
        url: sessionTable + '/session',
        method: "get"
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.user = data.data;
        }
      }).catch(() => {
        // 静默处理错误
      });
    },

    // 下拉菜单命令处理
    handleCommand(command) {
      switch (command) {
        case 'center':
          this.$router.push('/center');
          break;
        case 'password':
          this.$router.push('/updatePassword');
          break;
        case 'logout':
          this.handleLogout();
          break;
      }
    },

    // 返回前台
    goToIndex() {
      window.location.href = `${this.$base.indexUrl}`;
    },

    // 退出登录
    handleLogout() {
      this.$confirm('确定要退出登录吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$storage.remove("Token");
        this.$storage.remove("role");
        this.$storage.remove("sessionTable");
        this.$storage.remove("adminName");
        this.$message.success('退出成功');
        this.$router.replace({ name: "login" });
      }).catch(() => {
        // 取消操作
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.admin-header {
  width: 100%;
  height: 64px;
  background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  padding: 0 24px;
  max-width: 1920px;
  margin: 0 auto;
}

// 左侧品牌区
.header-left {
  display: flex;
  align-items: center;
  gap: 16px;

  .brand-logo {
    width: 44px;
    height: 44px;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s;
    cursor: pointer;

    i {
      font-size: 24px;
      color: #fff;
    }

    &:hover {
      background: rgba(255, 255, 255, 0.25);
      transform: scale(1.05) rotate(5deg);
    }
  }

  .brand-info {
    display: flex;
    flex-direction: column;
    gap: 2px;

    .brand-title {
      font-size: 20px;
      font-weight: 700;
      color: #fff;
      margin: 0;
      line-height: 1;
      letter-spacing: 0.5px;
    }

    .brand-subtitle {
      font-size: 12px;
      color: rgba(255, 255, 255, 0.8);
      line-height: 1;
    }
  }
}

// 右侧操作区
.header-right {
  display: flex;
  align-items: center;
  gap: 24px;

  .quick-actions {
    display: flex;
    align-items: center;
    gap: 12px;

    .action-item {
      width: 40px;
      height: 40px;
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(10px);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.3s;

      i {
        font-size: 18px;
        color: #fff;
      }

      &:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
      }
    }

    .notification-badge {
      ::v-deep .el-badge__content {
        background: #f56c6c;
        border: 2px solid #1e3c72;
      }
    }
  }

  .user-dropdown {
    .user-info {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 8px 16px;
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(10px);
      border-radius: 24px;
      cursor: pointer;
      transition: all 0.3s;
      user-select: none;

      &:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
      }

      .user-avatar {
        background: rgba(255, 255, 255, 0.2);
        color: #fff;
        font-size: 18px;
      }

      .user-details {
        display: flex;
        flex-direction: column;
        gap: 2px;

        .user-name {
          font-size: 14px;
          font-weight: 600;
          color: #fff;
          line-height: 1;
        }

        .user-role {
          font-size: 12px;
          color: rgba(255, 255, 255, 0.8);
          line-height: 1;
        }
      }

      .dropdown-icon {
        font-size: 12px;
        color: rgba(255, 255, 255, 0.8);
        transition: transform 0.3s;
      }

      &:hover .dropdown-icon {
        transform: rotate(180deg);
      }
    }
  }
}

// 下拉菜单样式
::v-deep .user-menu {
  margin-top: 12px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  border: none;
  padding: 8px;
  min-width: 180px;

  .el-dropdown-menu__item {
    padding: 12px 16px;
    font-size: 14px;
    color: #606266;
    border-radius: 8px;
    transition: all 0.3s;
    margin-bottom: 4px;

    &:last-child {
      margin-bottom: 0;
    }

    i {
      margin-right: 8px;
      font-size: 16px;
      color: #1e3c72;
    }

    &:hover {
      background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
      color: #fff;

      i {
        color: #fff;
      }
    }

    &.is-divided {
      margin-top: 8px;
      border-top: 1px solid #e8e8e8;
      padding-top: 12px;
    }
  }
}

// 响应式设计
@media (max-width: 768px) {
  .header-content {
    padding: 0 16px;
  }

  .header-left {
    .brand-info {
      .brand-subtitle {
        display: none;
      }
    }
  }

  .header-right {
    gap: 12px;

    .quick-actions {
      gap: 8px;

      .action-item {
        width: 36px;
        height: 36px;

        i {
          font-size: 16px;
        }
      }
    }

    .user-dropdown {
      .user-info {
        padding: 6px 12px;

        .user-details {
          .user-role {
            display: none;
          }
        }
      }
    }
  }
}
</style>
