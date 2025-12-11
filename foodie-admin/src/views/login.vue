<template>
  <div class="admin-login-container">
    <!-- 左侧信息展示区 -->
    <div class="login-left">
      <div class="left-content">
        <div class="brand-section">
          <div class="brand-logo">
            <i class="el-icon-s-shop"></i>
          </div>
          <h1 class="brand-title">食客在线</h1>
          <p class="brand-subtitle">网上点餐系统 · 后台管理</p>
        </div>
        
        <div class="feature-list">
          <div class="feature-item" v-for="(item, index) in features" :key="index">
            <div class="feature-icon">
              <i :class="item.icon"></i>
            </div>
            <div class="feature-text">
              <h3>{{ item.title }}</h3>
              <p>{{ item.desc }}</p>
            </div>
          </div>
        </div>

        <div class="copyright">
          <p>© 2025 食客在线. All rights reserved.</p>
        </div>
      </div>
    </div>

    <!-- 右侧登录表单区 -->
    <div class="login-right">
      <div class="login-form-wrapper">
        <div class="form-header">
          <h2 class="form-title">管理员登录</h2>
          <p class="form-desc">欢迎回来，请登录您的账户</p>
        </div>

        <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form">
          <!-- 用户名 -->
          <el-form-item prop="username">
            <div class="form-item-label">
              <i class="el-icon-user"></i>
              <span>用户名</span>
            </div>
            <el-input
              v-model="loginForm.username"
              placeholder="请输入用户名"
              prefix-icon="el-icon-user"
              clearable
              @keyup.enter.native="handleLogin"
            >
            </el-input>
          </el-form-item>

          <!-- 密码 -->
          <el-form-item prop="password">
            <div class="form-item-label">
              <i class="el-icon-lock"></i>
              <span>密码</span>
            </div>
            <el-input
              v-model="loginForm.password"
              type="password"
              placeholder="请输入密码"
              prefix-icon="el-icon-lock"
              show-password
              @keyup.enter.native="handleLogin"
            >
            </el-input>
          </el-form-item>

          <!-- 验证码 -->
          <el-form-item v-if="captchaEnabled" prop="code">
            <div class="form-item-label">
              <i class="el-icon-picture"></i>
              <span>验证码</span>
            </div>
            <div class="captcha-input-wrapper">
              <el-input
                v-model="loginForm.code"
                placeholder="请输入验证码"
                prefix-icon="el-icon-picture"
                maxlength="4"
                @keyup.enter.native="handleLogin"
              >
              </el-input>
              <div class="captcha-display" @click="refreshCaptcha">
                <span
                  v-for="(item, index) in captchaCode"
                  :key="index"
                  :style="{
                    color: item.color,
                    transform: item.rotate,
                    fontSize: item.size
                  }"
                  class="captcha-char"
                >{{ item.char }}</span>
                <div class="captcha-refresh">
                  <i class="el-icon-refresh"></i>
                </div>
              </div>
            </div>
          </el-form-item>

          <!-- 角色选择 -->
          <el-form-item prop="role">
            <div class="form-item-label">
              <i class="el-icon-s-custom"></i>
              <span>登录角色</span>
            </div>
            <div class="role-selector">
              <div
                v-for="item in roleList"
                v-if="item.hasBackLogin === '是'"
                :key="item.roleName"
                :class="['role-item', { active: loginForm.role === item.roleName }]"
                @click="selectRole(item.roleName)"
              >
                <i :class="getRoleIcon(item.roleName)"></i>
                <span>{{ item.roleName }}</span>
              </div>
            </div>
          </el-form-item>

          <!-- 记住密码 -->
          <el-form-item class="remember-row">
            <el-checkbox v-model="rememberMe">记住密码</el-checkbox>
            <a class="forgot-password" @click="handleForgotPassword">忘记密码？</a>
          </el-form-item>

          <!-- 登录按钮 -->
          <el-form-item>
            <el-button
              type="primary"
              :loading="loading"
              class="login-btn"
              @click="handleLogin"
            >
              <span v-if="!loading">立即登录</span>
              <span v-else>登录中...</span>
            </el-button>
          </el-form-item>

          <!-- 注册链接 -->
          <div class="form-footer">
            <span>还没有账号？</span>
            <a @click="handleRegister" class="register-link">立即注册</a>
          </div>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import menu from "@/utils/menu";

export default {
  name: "AdminLogin",
  data() {
    return {
      loginForm: {
        username: "",
        password: "",
        code: "",
        role: ""
      },
      loginRules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { min: 2, max: 20, message: "长度在 2 到 20 个字符", trigger: "blur" }
        ],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          { min: 3, max: 20, message: "长度在 3 到 20 个字符", trigger: "blur" }
        ],
        role: [
          { required: true, message: "请选择登录角色", trigger: "change" }
        ]
      },
      roleList: [],
      loading: false,
      rememberMe: false,
      captchaEnabled: false,
      captchaCode: [],
      tableName: "",
      features: [
        {
          icon: "el-icon-s-data",
          title: "数据统计",
          desc: "实时查看订单、销售等数据"
        },
        {
          icon: "el-icon-s-order",
          title: "订单管理",
          desc: "高效处理订单，提升服务质量"
        },
        {
          icon: "el-icon-s-goods",
          title: "商品管理",
          desc: "轻松管理菜品信息和库存"
        },
        {
          icon: "el-icon-s-custom",
          title: "用户管理",
          desc: "完善的用户信息管理系统"
        }
      ]
    };
  },
  mounted() {
    this.initRoleList();
    if (this.captchaEnabled) {
      this.generateCaptcha();
    }
    this.loadRememberedAccount();
  },
  methods: {
    // 初始化角色列表
    initRoleList() {
      const menus = menu.list();
      this.roleList = menus;
      // 如果只有一个角色，自动选中
      const availableRoles = menus.filter(item => item.hasBackLogin === '是');
      if (availableRoles.length === 1) {
        this.loginForm.role = availableRoles[0].roleName;
      }
    },

    // 选择角色
    selectRole(roleName) {
      this.loginForm.role = roleName;
    },

    // 获取角色图标
    getRoleIcon(roleName) {
      const iconMap = {
        '管理员': 'el-icon-user-solid',
        '美食店': 'el-icon-s-shop',
        '用户': 'el-icon-user',
        '骑手': 'el-icon-bicycle'
      };
      return iconMap[roleName] || 'el-icon-s-custom';
    },

    // 生成验证码
    generateCaptcha() {
      const chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
      const colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c'];
      const sizes = ['18px', '20px', '22px', '24px'];
      
      this.captchaCode = [];
      for (let i = 0; i < 4; i++) {
        const char = chars[Math.floor(Math.random() * chars.length)];
        const color = colors[Math.floor(Math.random() * colors.length)];
        const size = sizes[Math.floor(Math.random() * sizes.length)];
        const rotate = `rotate(${Math.random() * 40 - 20}deg)`;
        
        this.captchaCode.push({ char, color, size, rotate });
      }
    },

    // 刷新验证码
    refreshCaptcha() {
      this.generateCaptcha();
      this.loginForm.code = '';
    },

    // 加载记住的账号
    loadRememberedAccount() {
      const remembered = localStorage.getItem('rememberedAccount');
      if (remembered) {
        try {
          const account = JSON.parse(remembered);
          this.loginForm.username = account.username;
          this.loginForm.password = account.password;
          this.rememberMe = true;
        } catch (e) {
          console.error('加载记住的账号失败', e);
        }
      }
    },

    // 保存账号
    saveAccount() {
      if (this.rememberMe) {
        const account = {
          username: this.loginForm.username,
          password: this.loginForm.password
        };
        localStorage.setItem('rememberedAccount', JSON.stringify(account));
      } else {
        localStorage.removeItem('rememberedAccount');
      }
    },

    // 登录
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        if (!valid) {
          return false;
        }

        // 验证码校验
        if (this.captchaEnabled) {
          const inputCode = this.loginForm.code.toLowerCase();
          const correctCode = this.captchaCode.map(item => item.char).join('').toLowerCase();
          if (inputCode !== correctCode) {
            this.$message.error('验证码错误');
            this.refreshCaptcha();
            return;
          }
        }

        // 获取表名
        const selectedRole = this.roleList.find(item => item.roleName === this.loginForm.role);
        if (!selectedRole) {
          this.$message.error('角色信息错误');
          return;
        }
        this.tableName = selectedRole.tableName;

        // 发送登录请求
        this.loading = true;
        this.$http({
          url: `${this.tableName}/login?username=${this.loginForm.username}&password=${this.loginForm.password}`,
          method: "post"
        })
          .then(({ data }) => {
            if (data && data.code === 0) {
              // 保存登录信息
              this.$storage.set("Token", data.token);
              this.$storage.set("role", this.loginForm.role);
              this.$storage.set("sessionTable", this.tableName);
              this.$storage.set("adminName", this.loginForm.username);
              
              // 保存账号
              this.saveAccount();
              
              this.$message.success('登录成功');
              
              // 跳转到首页
              setTimeout(() => {
                this.$router.replace({ path: "/index/" });
              }, 500);
            } else {
              this.$message.error(data.msg || '登录失败');
              if (this.captchaEnabled) {
                this.refreshCaptcha();
              }
            }
          })
          .catch(error => {
            console.error('登录错误', error);
            this.$message.error('登录失败，请检查网络连接');
            if (this.captchaEnabled) {
              this.refreshCaptcha();
            }
          })
          .finally(() => {
            this.loading = false;
          });
      });
    },

    // 忘记密码
    handleForgotPassword() {
      this.$message.info('请联系管理员重置密码');
    },

    // 注册
    handleRegister() {
      this.$storage.set("loginTable", "meishidian");
      this.$router.push({ path: '/register' });
    }
  }
};
</script>

<style lang="scss" scoped>
.admin-login-container {
  display: flex;
  width: 100%;
  min-height: 100vh;
  background: #f0f2f5;
}

// 左侧信息区
.login-left {
  flex: 1;
  background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px;
  position: relative;
  overflow: hidden;

  &::before {
    content: '';
    position: absolute;
    width: 500px;
    height: 500px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 50%;
    top: -200px;
    left: -200px;
  }

  &::after {
    content: '';
    position: absolute;
    width: 400px;
    height: 400px;
    background: rgba(255, 255, 255, 0.03);
    border-radius: 50%;
    bottom: -150px;
    right: -150px;
  }

  .left-content {
    position: relative;
    z-index: 1;
    max-width: 500px;
    color: #fff;

    .brand-section {
      text-align: center;
      margin-bottom: 60px;

      .brand-logo {
        width: 100px;
        height: 100px;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 30px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);

        i {
          font-size: 50px;
          color: #fff;
        }
      }

      .brand-title {
        font-size: 42px;
        font-weight: 700;
        margin: 0 0 15px 0;
        letter-spacing: 2px;
      }

      .brand-subtitle {
        font-size: 18px;
        opacity: 0.9;
        margin: 0;
      }
    }

    .feature-list {
      .feature-item {
        display: flex;
        align-items: flex-start;
        margin-bottom: 30px;
        padding: 20px;
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        transition: all 0.3s;

        &:hover {
          background: rgba(255, 255, 255, 0.12);
          transform: translateX(10px);
        }

        .feature-icon {
          width: 50px;
          height: 50px;
          background: rgba(255, 255, 255, 0.15);
          border-radius: 10px;
          display: flex;
          align-items: center;
          justify-content: center;
          margin-right: 20px;
          flex-shrink: 0;

          i {
            font-size: 24px;
            color: #fff;
          }
        }

        .feature-text {
          h3 {
            font-size: 18px;
            margin: 0 0 8px 0;
            font-weight: 600;
          }

          p {
            font-size: 14px;
            margin: 0;
            opacity: 0.8;
            line-height: 1.6;
          }
        }
      }
    }

    .copyright {
      text-align: center;
      margin-top: 60px;
      opacity: 0.7;
      font-size: 14px;
    }
  }
}

// 右侧表单区
.login-right {
  width: 520px;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  box-shadow: -5px 0 20px rgba(0, 0, 0, 0.05);
}

.login-form-wrapper {
  width: 100%;
  max-width: 400px;

  .form-header {
    text-align: center;
    margin-bottom: 40px;

    .form-title {
      font-size: 28px;
      font-weight: 700;
      color: #1e3c72;
      margin: 0 0 10px 0;
    }

    .form-desc {
      font-size: 14px;
      color: #8c8c8c;
      margin: 0;
    }
  }

  .login-form {
    .el-form-item {
      margin-bottom: 24px;

      .form-item-label {
        display: flex;
        align-items: center;
        margin-bottom: 8px;
        font-size: 14px;
        font-weight: 500;
        color: #333;

        i {
          margin-right: 6px;
          color: #1e3c72;
        }
      }

      ::v-deep .el-input__inner {
        height: 44px;
        line-height: 44px;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        font-size: 14px;
        transition: all 0.3s;

        &:focus {
          border-color: #1e3c72;
          box-shadow: 0 0 0 2px rgba(30, 60, 114, 0.1);
        }
      }

      ::v-deep .el-input__prefix {
        left: 12px;
        color: #8c8c8c;
      }

      ::v-deep .el-input__suffix {
        right: 12px;
      }
    }

    // 验证码输入
    .captcha-input-wrapper {
      display: flex;
      gap: 12px;

      .el-input {
        flex: 1;
      }

      .captcha-display {
        width: 120px;
        height: 44px;
        background: linear-gradient(135deg, #f5f7fa 0%, #e8eaf0 100%);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        position: relative;
        user-select: none;
        transition: all 0.3s;

        &:hover {
          transform: scale(1.05);
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);

          .captcha-refresh {
            opacity: 1;
          }
        }

        .captcha-char {
          display: inline-block;
          font-weight: 700;
          margin: 0 2px;
        }

        .captcha-refresh {
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: rgba(0, 0, 0, 0.5);
          display: flex;
          align-items: center;
          justify-content: center;
          border-radius: 8px;
          opacity: 0;
          transition: opacity 0.3s;

          i {
            color: #fff;
            font-size: 20px;
          }
        }
      }
    }

    // 角色选择
    .role-selector {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;

      .role-item {
        padding: 12px;
        border: 2px solid #e0e0e0;
        border-radius: 8px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s;
        background: #fff;

        i {
          font-size: 24px;
          color: #8c8c8c;
          display: block;
          margin-bottom: 8px;
          transition: all 0.3s;
        }

        span {
          font-size: 14px;
          color: #333;
          font-weight: 500;
        }

        &:hover {
          border-color: #1e3c72;
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(30, 60, 114, 0.15);

          i {
            color: #1e3c72;
            transform: scale(1.1);
          }
        }

        &.active {
          border-color: #1e3c72;
          background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
          box-shadow: 0 4px 12px rgba(30, 60, 114, 0.3);

          i {
            color: #fff;
          }

          span {
            color: #fff;
          }
        }
      }
    }

    // 记住密码行
    .remember-row {
      margin-bottom: 24px;

      ::v-deep .el-form-item__content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        line-height: normal;
      }

      .forgot-password {
        font-size: 14px;
        color: #1e3c72;
        cursor: pointer;
        text-decoration: none;
        transition: all 0.3s;

        &:hover {
          color: #2a5298;
          text-decoration: underline;
        }
      }
    }

    // 登录按钮
    .login-btn {
      width: 100%;
      height: 44px;
      font-size: 16px;
      font-weight: 600;
      border-radius: 8px;
      background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
      border: none;
      transition: all 0.3s;

      &:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(30, 60, 114, 0.4);
      }

      &:active {
        transform: translateY(0);
      }
    }

    // 表单底部
    .form-footer {
      text-align: center;
      margin-top: 20px;
      font-size: 14px;
      color: #8c8c8c;

      .register-link {
        color: #1e3c72;
        cursor: pointer;
        text-decoration: none;
        font-weight: 500;
        margin-left: 5px;
        transition: all 0.3s;

        &:hover {
          color: #2a5298;
          text-decoration: underline;
        }
      }
    }
  }
}

// 响应式设计
@media (max-width: 1024px) {
  .login-left {
    display: none;
  }

  .login-right {
    width: 100%;
  }
}

@media (max-width: 768px) {
  .login-right {
    padding: 20px;
  }

  .login-form-wrapper {
    .form-header {
      .form-title {
        font-size: 24px;
      }
    }

    .login-form {
      .role-selector {
        grid-template-columns: 1fr;
      }
    }
  }
}
</style>
