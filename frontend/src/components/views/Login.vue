<template>
  <div>
    <NavTitleBar></NavTitleBar>
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
                      <el-option label="管理员" value="innerOperator"></el-option>
                      <el-option label="前台操作员" value="reception"></el-option>
                    </el-select>
                  </el-form-item>
                </el-col>
              </el-row>
              <el-row>
                <el-col :offset="10">
                  <el-button type="primary" round @click="handleLogin">登录</el-button>
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
        account: '',
        password: '',
        role: ''
      }
    },
    methods: {
      handleLogin () {
        console.log('views.Login.handleLogin ===start===')
        console.log('account:', this.account)
        console.log('password:', this.password)
        console.log('role:', this.role)
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
