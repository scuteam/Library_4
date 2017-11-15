<template>
  <div>
    <el-row>
      <el-menu theme="dark" class="top-menu" mode="horizontal" >
        <el-menu-item index="1" id="navTitle">{{titleText}}</el-menu-item>
        <el-col :span="1" :offset="19">
            <el-menu-item index="2" id="nav_button"><el-button type="primary" round @click="handleClick">{{buttonText}}</el-button></el-menu-item>
          </el-col>
      </el-menu>
    </el-row>
  </div>
</template>

<script>
  export default {
    props: ['navTitleText', 'navButtonText'],
    data () {
      return {
        titleText: this.navTitleText,
        buttonText: this.navButtonText
      }
    },
    methods: {
      handleClick () {
        if (this.buttonText === '登录') {
          // 跳转到 /Login
          this.$router.push('/login')
        } else if (this.buttonText === '注销') {
          // 注销,且跳转到主界面?还是登录界面
          this.$router.push('/')
        }
      }
    }
  }
</script>

<style>
  #app {
    margin-top: 0px;
  }
  #nav_button {
    margin-right: 10px;
  }
</style>
