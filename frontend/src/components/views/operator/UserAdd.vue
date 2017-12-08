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
        <el-col :span="5" :offset="6">
          <el-form-item label="密码">
            <el-input v-model="userInfo.password"></el-input>
          </el-form-item>
        </el-col>
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
    name: 'user-add.vue',
    data () {
      return {
        userInfo: {
          ID: '',
          name: '',
          password: ''
        }
      }
    },
    method: {
      deal_create_user () {
        var qs = require('qs')
        this.$http.post('api/create_user/', qs.stringify(this.userInfo))
          .then((res) => {
            if (res.data.createStatus === 200) {
              this.close_create_user_view()
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
