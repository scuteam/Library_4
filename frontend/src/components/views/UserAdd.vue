<template>
  <div id="user-add">
    <el-row>
      <el-form :model="userInfo" labelWidth="80px">
        <el-row>
          <el-col :span="5" :offset="6">
            <el-form-item label="身份证号">
              <el-input v-model="userInfo.ID"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="5" :offset="6">
            <el-form-item label="姓名">
              <el-input v-model="userInfo.name" ></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="5" :offset="6">
            <el-form-item label="密码">
              <el-input v-model="userInfo.password" type="password"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="5" :offset="6">
            <el-form-item label="确认密码">
              <el-input v-model="userInfo.passwordTemp" type="password"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-row>
    <el-row>
      <el-col :span="1" :offset="14">
        <el-button @click="deal_create_user" type="primary" size="mini">保存</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'userAdd',
    data () {
      return {
        userInfo: {
          ID: '',
          name: '',
          password: '',
          passwordTemp: ''
        }
      }
    },
    methods: {
      deal_create_user () {
        if (this.userInfo.ID === '') {
          this.$message.error('身份证号不能为空')
          return
        }
        if (this.userInfo.name === '') {
          this.$message.error('姓名不能为空')
          return
        }
        if (this.userInfo.password.length < 6 || this.userInfo.password.length > 20) {
          this.$message.error('密码长度应为6-20位')
          return
        }

        if (this.userInfo.password !== this.userInfo.passwordTemp) {
          this.$message.error('两次密码不同')
          return
        }
        let reg = /[1-9][0-9]{16}[x0-9]/
        if (!reg.test(this.userInfo.ID)) {
          this.$message.error('身份证号错误')
          return false
        }
        var qs = require('qs')
        this.$http.post('api/create_user/', qs.stringify(this.userInfo))
          .then((res) => {
            if (res.data.createStatus === 200) {
              this.close_create_user_view()
              this.userTableData.unshift({
                ID: this.userInfo.ID,
                name: this.userInfo.name
              })
              this.$message.success('添加成功')
            } else if (res.data.createStatus === 304) {
              this.$message.error(res.data.reason)
            } else {
              this.$message.error('未知的错误')
            }
          })
      }
    }
  }
</script>

<style scoped lang="stylus">
  #user-add
    margin-top: 100px
</style>
