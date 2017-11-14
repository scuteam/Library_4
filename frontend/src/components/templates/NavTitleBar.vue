<template>
  <div>
    <el-row>
      <el-menu theme="dark" class="top-menu" mode="horizontal" >
        <el-menu-item index="1" id="navTitle">{{navTitle}}</el-menu-item>
        <el-col :span="1" :offset="19">
            <el-menu-item index="2" id="nav_button"><el-button type="primary" round @click="handleClick">{{buttonText}}</el-button></el-menu-item>
          </el-col>
      </el-menu>
    </el-row>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        navTitle: '网上图书管理系统',
        buttonText: '登录'
      }
    },
    methods: {
      handleClick () {
        if (this.buttonText === '登录') {
          // 跳转到 /Login
        } else if (this.buttonText === '注销') {
          // 注销,且跳转到主界面?还是登录界面
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
