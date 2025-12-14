<template>
  <div class="register-container">
    <!-- 左侧信息展示区 -->
    <div class="register-left">
      <div class="left-content">
        <div class="brand-section">
          <div class="brand-logo">
            <i class="el-icon-s-shop"></i>
          </div>
          <h1 class="brand-title">食客在线</h1>
          <p class="brand-subtitle">网上点餐系统 · 商家注册</p>
        </div>
        
        <div class="feature-list">
          <div class="feature-item">
            <div class="feature-icon">
              <i class="el-icon-s-shop"></i>
            </div>
            <div class="feature-text">
              <h3>开店简单</h3>
              <p>快速注册，轻松开启线上经营</p>
            </div>
          </div>
          
          <div class="feature-item">
            <div class="feature-icon">
              <i class="el-icon-s-order"></i>
            </div>
            <div class="feature-text">
              <h3>订单管理</h3>
              <p>实时接单，高效处理订单</p>
            </div>
          </div>
          
          <div class="feature-item">
            <div class="feature-icon">
              <i class="el-icon-s-data"></i>
            </div>
            <div class="feature-text">
              <h3>数据分析</h3>
              <p>全面的数据统计，助力经营决策</p>
            </div>
          </div>
          
          <div class="feature-item">
            <div class="feature-icon">
              <i class="el-icon-s-finance"></i>
            </div>
            <div class="feature-text">
              <h3>收益透明</h3>
              <p>清晰的财务报表，收益一目了然</p>
            </div>
          </div>
        </div>

        <div class="copyright">
          <p>© 2025 食客在线. All rights reserved.</p>
        </div>
      </div>
    </div>

    <!-- 右侧注册表单区 -->
    <div class="register-right">
      <div class="register-form-wrapper">
        <div class="form-header">
          <h2 class="form-title">{{ registerTitle }}</h2>
          <p class="form-desc">填写以下信息完成注册</p>
        </div>

        <el-form ref="registerForm" :model="ruleForm" :rules="rules" class="register-form">
          <!-- 用户注册表单 -->
          <template v-if="tableName === 'yonghu'">
            <el-form-item prop="yonghuzhanghao">
              <div class="form-item-label">
                <i class="el-icon-user"></i>
                <span>用户账号</span>
              </div>
              <el-input
                v-model="ruleForm.yonghuzhanghao"
                placeholder="请输入用户账号"
                prefix-icon="el-icon-user"
                clearable
              />
            </el-form-item>

            <el-form-item prop="mima">
              <div class="form-item-label">
                <i class="el-icon-lock"></i>
                <span>密码</span>
              </div>
              <el-input
                v-model="ruleForm.mima"
                type="password"
                placeholder="请输入密码"
                prefix-icon="el-icon-lock"
                show-password
              />
            </el-form-item>

            <el-form-item prop="yonghuxingming">
              <div class="form-item-label">
                <i class="el-icon-user-solid"></i>
                <span>用户姓名</span>
              </div>
              <el-input
                v-model="ruleForm.yonghuxingming"
                placeholder="请输入用户姓名"
                prefix-icon="el-icon-user-solid"
                clearable
              />
            </el-form-item>

            <el-form-item prop="nianling">
              <div class="form-item-label">
                <i class="el-icon-date"></i>
                <span>年龄</span>
              </div>
              <el-input
                v-model="ruleForm.nianling"
                placeholder="请输入年龄"
                prefix-icon="el-icon-date"
                clearable
              />
            </el-form-item>

            <el-form-item prop="yonghushouji">
              <div class="form-item-label">
                <i class="el-icon-mobile-phone"></i>
                <span>用户手机</span>
              </div>
              <el-input
                v-model="ruleForm.yonghushouji"
                placeholder="请输入手机号码"
                prefix-icon="el-icon-mobile-phone"
                clearable
              />
            </el-form-item>

            <el-form-item prop="peisongdizhi">
              <div class="form-item-label">
                <i class="el-icon-location"></i>
                <span>配送地址</span>
              </div>
              <el-input
                v-model="ruleForm.peisongdizhi"
                placeholder="请输入配送地址"
                prefix-icon="el-icon-location"
                clearable
              />
            </el-form-item>
          </template>

          <!-- 美食店注册表单 -->
          <template v-if="tableName === 'meishidian'">
            <el-form-item prop="dianpuzhanghao">
              <div class="form-item-label">
                <i class="el-icon-user"></i>
                <span>店铺账号</span>
              </div>
              <el-input
                v-model="ruleForm.dianpuzhanghao"
                placeholder="请输入店铺账号"
                prefix-icon="el-icon-user"
                clearable
              />
            </el-form-item>

            <el-form-item prop="mima">
              <div class="form-item-label">
                <i class="el-icon-lock"></i>
                <span>密码</span>
              </div>
              <el-input
                v-model="ruleForm.mima"
                type="password"
                placeholder="请输入密码"
                prefix-icon="el-icon-lock"
                show-password
              />
            </el-form-item>

            <el-form-item prop="dianpumingcheng">
              <div class="form-item-label">
                <i class="el-icon-s-shop"></i>
                <span>店铺名称</span>
              </div>
              <el-input
                v-model="ruleForm.dianpumingcheng"
                placeholder="请输入店铺名称"
                prefix-icon="el-icon-s-shop"
                clearable
              />
            </el-form-item>

            <el-form-item prop="lianxidianhua">
              <div class="form-item-label">
                <i class="el-icon-mobile-phone"></i>
                <span>联系电话</span>
              </div>
              <el-input
                v-model="ruleForm.lianxidianhua"
                placeholder="请输入联系电话"
                prefix-icon="el-icon-mobile-phone"
                clearable
              />
            </el-form-item>

            <el-form-item prop="dianpudizhi">
              <div class="form-item-label">
                <i class="el-icon-location"></i>
                <span>店铺地址</span>
              </div>
              <el-input
                v-model="ruleForm.dianpudizhi"
                placeholder="请输入店铺地址"
                prefix-icon="el-icon-location"
                clearable
              />
            </el-form-item>

            <el-form-item prop="lianxiren">
              <div class="form-item-label">
                <i class="el-icon-user-solid"></i>
                <span>联系人</span>
              </div>
              <el-input
                v-model="ruleForm.lianxiren"
                placeholder="请输入联系人姓名"
                prefix-icon="el-icon-user-solid"
                clearable
              />
            </el-form-item>
          </template>

          <!-- 注册按钮 -->
          <el-form-item>
            <el-button
              type="primary"
              :loading="loading"
              class="register-btn"
              @click="handleRegister"
            >
              <span v-if="!loading">立即注册</span>
              <span v-else>注册中...</span>
            </el-button>
          </el-form-item>

          <!-- 返回登录 -->
          <div class="form-footer">
            <span>已有账号？</span>
            <a @click="goToLogin" class="login-link">立即登录</a>
          </div>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      ruleForm: {},
      tableName: "",
      loading: false,
      rules: {
        yonghuzhanghao: [
          { required: true, message: "请输入用户账号", trigger: "blur" }
        ],
        dianpuzhanghao: [
          { required: true, message: "请输入店铺账号", trigger: "blur" }
        ],
        mima: [
          { required: true, message: "请输入密码", trigger: "blur" },
          { min: 3, max: 20, message: "长度在 3 到 20 个字符", trigger: "blur" }
        ],
        dianpumingcheng: [
          { required: true, message: "请输入店铺名称", trigger: "blur" }
        ],
        yonghushouji: [
          { pattern: /^1[3-9]\d{9}$/, message: "请输入正确的手机号码", trigger: "blur" }
        ],
        lianxidianhua: [
          { pattern: /^1[3-9]\d{9}$/, message: "请输入正确的手机号码", trigger: "blur" }
        ],
        nianling: [
          { pattern: /^\d+$/, message: "请输入正确的年龄", trigger: "blur" }
        ]
      }
    };
  },
  computed: {
    registerTitle() {
      return this.tableName === 'yonghu' ? '用户注册' : '商家注册';
    }
  },
  mounted() {
    let table = this.$storage.get("loginTable");
    this.tableName = table || 'meishidian';
  },
  methods: {
    // 注册
    handleRegister() {
      this.$refs.registerForm.validate(valid => {
        if (!valid) {
          return false;
        }

        // 额外验证
        if (this.tableName === 'yonghu') {
          if (this.ruleForm.nianling && !this.$validate.isIntNumer(this.ruleForm.nianling)) {
            this.$message.error('年龄应输入整数');
            return;
          }
          if (this.ruleForm.yonghushouji && !this.$validate.isMobile(this.ruleForm.yonghushouji)) {
            this.$message.error('请输入正确的手机号码');
            return;
          }
        }

        if (this.tableName === 'meishidian') {
          if (this.ruleForm.lianxidianhua && !this.$validate.isMobile(this.ruleForm.lianxidianhua)) {
            this.$message.error('请输入正确的联系电话');
            return;
          }
        }

        // 发送注册请求
        this.loading = true;
        this.$http({
          url: `${this.tableName}/register`,
          method: "post",
          data: this.ruleForm
        })
          .then(({ data }) => {
            if (data && data.code === 0) {
              this.$message({
                message: "注册成功",
                type: "success",
                duration: 1500,
                onClose: () => {
                  this.$router.replace({ path: "/login" });
                }
              });
            } else {
              this.$message.error(data.msg || '注册失败');
            }
          })
          .catch(error => {
            console.error('注册错误', error);
            this.$message.error('注册失败，请检查网络连接');
          })
          .finally(() => {
            this.loading = false;
          });
      });
    },

    // 返回登录
    goToLogin() {
      this.$router.push({ path: '/login' });
    }
  }
};
</script>

<style lang="scss" scoped>
.register-container {
  display: flex;
  width: 100%;
  min-height: 100vh;
  background: #f0f2f5;
}

// 左侧信息区（与登录页面相同）
.register-left {
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
.register-right {
  width: 520px;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  box-shadow: -5px 0 20px rgba(0, 0, 0, 0.05);
  overflow-y: auto;
}

.register-form-wrapper {
  width: 100%;
  max-width: 400px;

  .form-header {
    text-align: center;
    margin-bottom: 30px;

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

  .register-form {
    .el-form-item {
      margin-bottom: 20px;

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

    // 注册按钮
    .register-btn {
      width: 100%;
      height: 44px;
      font-size: 16px;
      font-weight: 600;
      border-radius: 8px;
      background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
      border: none;
      transition: all 0.3s;
      margin-top: 10px;

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

      .login-link {
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
  .register-left {
    display: none;
  }

  .register-right {
    width: 100%;
  }
}

@media (max-width: 768px) {
  .register-right {
    padding: 20px;
  }

  .register-form-wrapper {
    .form-header {
      .form-title {
        font-size: 24px;
      }
    }
  }
}
</style>
