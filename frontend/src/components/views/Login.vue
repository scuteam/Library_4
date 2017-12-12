<template>
  <div>
    <NavTitleBar :navTitleText="navTitleText" :navButtonText="navButtonText"></NavTitleBar>
    <el-row class="content">
      <el-col :xs="24" :sm="{span: 6, offset: 9}">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>登录</span>
          </div>
          <div>
            <el-form labelWidth="50px">
              <el-row>
                <el-col>
                  <el-form-item label="账号"  required="">
                    <el-input v-model="account" placeholder="帐号" type="text" autofocus></el-input>
                    </el-form-item>
                </el-col>
              </el-row>
              <el-row>
                <el-col>
                  <el-form-item label="密码"  required="">
                    <el-input v-model="password" placeholder="密码" type="password"></el-input>
                  </el-form-item>
                </el-col>
              </el-row>
              <el-row>
                <el-col :span="17">
                  <el-form-item label="角色"  required="">
                    <el-select v-model="role" placeholder="角色">
                      <el-option label="用户" value="user"></el-option>
                      <el-option label="书籍操作员" value="bookManager"></el-option>
                      <el-option label="管理员" value="admin"></el-option>
                      <el-option label="前台操作员" value="reception"></el-option>
                    </el-select>
                  </el-form-item>
                </el-col>
              </el-row>
              <el-row>
                <el-col :offset="10">
                  <el-button type="primary" round @click="deal_login">登录</el-button>
                </el-col>
              </el-row>
            </el-form>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import NavTitleBar from '../templates/NavTitleBar.vue'
  export default {
    name: 'login',
    components: {
      NavTitleBar
    },
    data () {
      return {
        navTitleText: '网上图书管理系统',
        navButtonText: '登录',
        account: '',
        password: '',
        role: ''
      }
    },
    methods: {
      deal_login () {
        console.log('views.Login.handleLogin ===start===')
        console.log('account:', this.account)
        console.log('password:', this.password, 'ss')
        console.log('role:', this.role)
        if (this.account === '' || this.password === '') {
          this.$message.error('输入不能为空')
          return
        }
        if (this.role === '') {
          this.$message.error('请选择角色')
          return
        }
        let obj = {
          account: this.account,
          password: this.password,
          role: this.role
        }
        var qs = require('qs')
        this.$http.post('/api/verify_account/', qs.stringify(obj))
          .then((res) => {
            console.log('success')
            if (res.data.loginStatus === 200) {
              if (this.role === 'user') {
                this.$router.push({path: '/renew/:account', name: 'Renew', params: {account: this.account}})
              } else if (this.role === 'bookManager') {
                this.$router.push({path: '/book_manage/:account', name: 'BookManage', params: {account: this.account}})
              } else if (this.role === 'admin') {
                this.$router.push({path: '/admin/:account', name: 'Admin', params: {account: this.account}})
              } else if (this.role === 'reception') {
                this.$router.push({path: '/reception/', name: 'Reception', params: {account: this.account}})
              }
              this.$message.success('登录成功')
            } else {
              this.$message.error('帐号密码不匹配')
            }
          }, (err) => {
            console.log('处理登录过程出现错误,错误信息如下:')
            console.log(err)
            console.log('错误信息输出完毕')
          })
        console.log('views.Login.handleLogin ===end===')
      }
    }
  }
</script>
<style lang="stylus" scoped>
  .el-card
    margin-top 80px
    margin-bottom 200px
</style>
