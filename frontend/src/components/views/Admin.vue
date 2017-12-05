<template>
  <div id="InnerOperator">
    <NavTitleBar :navTitleText="navTitleText" :navButtonText="navButtonText"></NavTitleBar>
    <el-container id="container">
      <el-aside id="aside" width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu
          default-active="1"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          @select="handleMenuSelection">
          <el-menu-item index="1">
            <span slot="title">内部人员管理</span>
          </el-menu-item>
          <el-menu-item index="2">
            <span slot="title">普通用户管理</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <!--内部人员管理-->
        <template v-if="activeIndex=== '1'">
          <br/><br/>
          <InnerOperator :innerOperatorTableData="innerOperatorTableData"></InnerOperator>
        </template >
        <!--普通用户管理-->
        <template v-if="activeIndex=== '2'">
          <user-manage :userTableData="userTableData"></user-manage>
        </template>
      </el-main>

    </el-container>
  </div>
</template>

<script>
  import NavTitleBar from '../templates/NavTitleBar.vue'
  import InnerOperator from '../views/InnerOperator.vue'
  import UserManage from '../views/UserManage.vue'
  export default {
    name: 'Admin',
    components: {
      NavTitleBar,
      InnerOperator,
      UserManage
    },
    data () {
      return {
        navTitleText: '管理员',
        navButtonText: '注销',
        activeIndex: '1',
        innerOperatorTableData: [],
        userTableData: []
      }
    },
    mounted: function () {
      console.log('get_user_and_operator_info invoked')
      this.get_user_and_operator_info()
    },
    methods: {
      handleMenuSelection (index) {
        if (index === '1') {
          this.activeIndex = '1'
        } else if (index === '2') {
          this.activeIndex = '2'
        }
      },
      get_user_and_operator_info () {
        this.$http.get('/api/get_all_operator/').then((res) => {
          let tmpInnerOperatorTableData = res.data.innerOperatorTableData
          this.innerOperatorTableData = tmpInnerOperatorTableData
        }, (err) => {
          console.log('处理操作人员信息查询过程出现错误,错误信息如下:')
          console.log(err)
          console.log('错误信息输出完毕')
        })

        this.$http.get('/api/get_all_user/').then((res) => {
          let tmpUserTableData = res.data.userTableData
          this.userTableData = tmpUserTableData
        }, (err) => {
          console.log('处理用户信息查询过程出现错误,错误信息如下:')
          console.log(err)
          console.log('错误信息输出完毕')
        })
      }
    }
  }
</script>

<style scoped="">
  #container{
    height: 610px;
    border: 1px solid #eee;
  }

</style>
