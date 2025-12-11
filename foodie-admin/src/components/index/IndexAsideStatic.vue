<template>
  <el-aside class="admin-sidebar" width="240px">
    <div class="sidebar-content">
      <div v-for="item in menuList" :key="item.roleName" v-if="role === item.roleName">
        <el-menu
          mode="vertical"
          :unique-opened="true"
          :default-active="activeMenu"
          class="sidebar-menu"
          @select="handleMenuSelect"
        >
          <!-- 首页 -->
          <el-menu-item index="home" class="menu-item">
            <div class="menu-item-content">
              <i class="el-icon-s-home menu-icon"></i>
              <span class="menu-title">首页</span>
            </div>
          </el-menu-item>

          <!-- 个人中心 -->
          <el-submenu index="personal" class="menu-submenu">
            <template slot="title">
              <div class="menu-item-content">
                <i class="el-icon-user menu-icon"></i>
                <span class="menu-title">个人中心</span>
              </div>
            </template>
            <el-menu-item index="updatePassword" class="submenu-item">
              <i class="el-icon-lock"></i>
              <span>修改密码</span>
            </el-menu-item>
            <el-menu-item index="center" class="submenu-item">
              <i class="el-icon-user-solid"></i>
              <span>个人信息</span>
            </el-menu-item>
          </el-submenu>

          <!-- 动态菜单 -->
          <template v-for="(menu, index) in item.backMenu">
            <!-- 只有一个子菜单的直接显示为一级菜单 -->
            <el-menu-item
              v-if="menu.child && menu.child.length === 1"
              :key="menu.menu"
              :index="menu.child[0].tableName"
              class="menu-item"
            >
              <div class="menu-item-content">
                <i :class="getMenuIcon(index)" class="menu-icon"></i>
                <span class="menu-title">{{ menu.menu }}</span>
              </div>
            </el-menu-item>

            <!-- 多个子菜单的显示为折叠菜单 -->
            <el-submenu
              v-else
              :key="menu.menu"
              :index="'menu-' + index"
              class="menu-submenu"
            >
              <template slot="title">
                <div class="menu-item-content">
                  <i :class="getMenuIcon(index)" class="menu-icon"></i>
                  <span class="menu-title">{{ menu.menu }}</span>
                </div>
              </template>
              <el-menu-item
                v-for="(child, sort) in menu.child"
                :key="sort"
                :index="child.tableName"
                class="submenu-item"
              >
                <i class="el-icon-document"></i>
                <span>{{ child.menu }}</span>
              </el-menu-item>
            </el-submenu>
          </template>
        </el-menu>
      </div>
    </div>
  </el-aside>
</template>

<script>
import menu from '@/utils/menu';

export default {
  name: "IndexAsideStatic",
  data() {
    return {
      menuList: [],
      role: '',
      activeMenu: 'home',
      menuIcons: [
        'el-icon-s-goods',
        'el-icon-s-order',
        'el-icon-s-shop',
        'el-icon-s-marketing',
        'el-icon-s-data',
        'el-icon-s-cooperation',
        'el-icon-s-platform',
        'el-icon-s-management',
        'el-icon-s-custom',
        'el-icon-s-finance',
        'el-icon-s-comment',
        'el-icon-s-flag',
        'el-icon-s-ticket',
        'el-icon-s-release',
        'el-icon-s-promotion'
      ]
    };
  },
  mounted() {
    const menus = menu.list();
    this.menuList = menus;
    this.role = this.$storage.get('role');
    this.setActiveMenu();
  },
  watch: {
    $route() {
      this.setActiveMenu();
    }
  },
  methods: {
    // 设置当前激活菜单
    setActiveMenu() {
      const path = this.$route.path;
      if (path === '/index/' || path === '/') {
        this.activeMenu = 'home';
      } else {
        const pathName = path.replace('/', '');
        this.activeMenu = pathName;
      }
    },

    // 菜单选择处理
    handleMenuSelect(index) {
      if (index === 'home') {
        this.$router.push('/');
      } else {
        this.$router.push('/' + index);
      }
    },

    // 获取菜单图标
    getMenuIcon(index) {
      return this.menuIcons[index % this.menuIcons.length];
    }
  }
};
</script>

<style lang="scss" scoped>
.admin-sidebar {
  height: 100vh;
  background: linear-gradient(180deg, #ffffff 0%, #f8f9fa 100%);
  box-shadow: 2px 0 12px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  transition: width 0.3s;
  position: fixed;
  left: 0;
  top: 64px;
  bottom: 0;
}

.sidebar-content {
  height: 100%;
  overflow-x: hidden;
  overflow-y: auto;
  padding: 20px 0;

  // 自定义滚动条
  &::-webkit-scrollbar {
    width: 6px;
  }

  &::-webkit-scrollbar-track {
    background: transparent;
  }

  &::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #d0d0d0 0%, #b0b0b0 100%);
    border-radius: 3px;

    &:hover {
      background: linear-gradient(180deg, #b0b0b0 0%, #909090 100%);
    }
  }
}

.sidebar-menu {
  border: none;
  background: transparent;

  // 菜单项内容
  .menu-item-content {
    display: flex;
    align-items: center;
    width: 100%;

    .menu-icon {
      font-size: 18px;
      margin-right: 12px;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .menu-title {
      font-size: 14px;
      font-weight: 500;
      flex: 1;
      transition: all 0.3s;
    }
  }

  // 一级菜单项
  .menu-item {
    height: 50px;
    line-height: 50px;
    margin: 0 12px 10px;
    padding: 0 18px !important;
    border-radius: 12px;
    color: #606266;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    background: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);

    &::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 4px;
      background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
      border-radius: 0 4px 4px 0;
      transform: translateX(-4px);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    &::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, rgba(30, 60, 114, 0.05) 0%, rgba(42, 82, 152, 0.05) 100%);
      opacity: 0;
      transition: opacity 0.3s;
      border-radius: 12px;
    }

    .menu-icon {
      color: #909399;
      position: relative;
      z-index: 1;
    }

    .menu-title {
      position: relative;
      z-index: 1;
    }

    &:hover {
      background: #fff;
      color: #1e3c72;
      transform: translateX(4px);
      box-shadow: 0 4px 12px rgba(30, 60, 114, 0.15);

      &::before {
        transform: translateX(0);
        width: 5px;
      }

      &::after {
        opacity: 1;
      }

      .menu-icon {
        color: #1e3c72;
        transform: scale(1.15) rotate(5deg);
      }

      .menu-title {
        font-weight: 600;
      }
    }

    &.is-active {
      background: linear-gradient(135deg, rgba(30, 60, 114, 0.1) 0%, rgba(42, 82, 152, 0.08) 100%);
      color: #1e3c72;
      font-weight: 600;
      box-shadow: 0 4px 12px rgba(30, 60, 114, 0.2);
      transform: translateX(4px);

      &::before {
        transform: translateX(0);
        width: 5px;
        box-shadow: 2px 0 8px rgba(30, 60, 114, 0.3);
      }

      .menu-icon {
        color: #1e3c72;
        transform: scale(1.1);
      }

      .menu-title {
        font-weight: 600;
      }
    }
  }

  // 子菜单
  .menu-submenu {
    margin: 0 12px 10px;

    ::v-deep .el-submenu__title {
      height: 50px;
      line-height: 50px;
      padding: 0 18px !important;
      border-radius: 12px;
      color: #606266;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
      overflow: hidden;
      background: #fff;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);

      &::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        border-radius: 0 4px 4px 0;
        transform: translateX(-4px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      }

      &::after {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(30, 60, 114, 0.05) 0%, rgba(42, 82, 152, 0.05) 100%);
        opacity: 0;
        transition: opacity 0.3s;
        border-radius: 12px;
      }

      .menu-icon {
        color: #909399;
        position: relative;
        z-index: 1;
      }

      .menu-title {
        position: relative;
        z-index: 1;
      }

      .el-submenu__icon-arrow {
        right: 18px;
        font-size: 12px;
        color: #909399;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        z-index: 1;
      }

      &:hover {
        background: #fff;
        color: #1e3c72;
        transform: translateX(4px);
        box-shadow: 0 4px 12px rgba(30, 60, 114, 0.15);

        &::before {
          transform: translateX(0);
          width: 5px;
        }

        &::after {
          opacity: 1;
        }

        .menu-icon {
          color: #1e3c72;
          transform: scale(1.15) rotate(5deg);
        }

        .menu-title {
          font-weight: 600;
        }

        .el-submenu__icon-arrow {
          color: #1e3c72;
          transform: translateX(2px);
        }
      }
    }

    &.is-opened {
      ::v-deep .el-submenu__title {
        color: #1e3c72;
        font-weight: 600;
        background: linear-gradient(135deg, rgba(30, 60, 114, 0.08) 0%, rgba(42, 82, 152, 0.06) 100%);
        box-shadow: 0 2px 8px rgba(30, 60, 114, 0.1);

        &::before {
          transform: translateX(0);
          width: 5px;
        }

        .menu-icon {
          color: #1e3c72;
        }

        .el-submenu__icon-arrow {
          color: #1e3c72;
          transform: rotate(180deg);
        }
      }
    }

    // 子菜单列表
    ::v-deep .el-menu {
      background: linear-gradient(135deg, #f8f9fa 0%, #f0f2f5 100%);
      border-radius: 10px;
      margin: 6px 0 10px;
      padding: 6px 0;
      box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.03);
    }

    // 子菜单项
    .submenu-item {
      height: 44px;
      line-height: 44px;
      padding: 0 18px 0 50px !important;
      margin: 0 8px;
      border-radius: 10px;
      color: #606266;
      font-size: 13px;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
      background: transparent;

      &::before {
        content: '';
        position: absolute;
        left: 32px;
        top: 50%;
        transform: translateY(-50%);
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #c0c4cc;
        transition: all 0.3s;
      }

      i {
        margin-right: 8px;
        font-size: 14px;
        color: #c0c4cc;
        transition: all 0.3s;
        display: none;
      }

      &:hover {
        background: #fff;
        color: #1e3c72;
        padding-left: 54px !important;
        box-shadow: 0 3px 10px rgba(30, 60, 114, 0.12);
        transform: translateX(2px);

        &::before {
          background: #1e3c72;
          transform: translateY(-50%) scale(1.3);
          box-shadow: 0 0 8px rgba(30, 60, 114, 0.4);
        }

        i {
          color: #1e3c72;
        }
      }

      &.is-active {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: #fff;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(30, 60, 114, 0.35);
        transform: translateX(2px);

        &::before {
          background: #fff;
          transform: translateY(-50%) scale(1.4);
          box-shadow: 0 0 10px rgba(255, 255, 255, 0.6);
        }

        i {
          color: #fff;
        }
      }
    }
  }
}

// 响应式设计
@media (max-width: 768px) {
  .admin-sidebar {
    width: 64px !important;

    .menu-title {
      display: none;
    }

    .menu-item,
    .menu-submenu ::v-deep .el-submenu__title {
      padding: 0 20px !important;
      justify-content: center;
    }

    .submenu-item {
      display: none;
    }
  }
}
</style>
