<template>
  <div id="renew">
    <NavTitleBar :navTitleText="navTitleText" :navButtonText="navButtonText"></NavTitleBar>
    <el-container id="container">
      <el-aside width="200px" id="aside">
        <el-menu
          default-active="bookReturn"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          @select="handleMenuSelection">
          <el-menu-item index="bookReturn">
            <span slot="title">借书/还书</span>
          </el-menu-item>
          <el-menu-item index="bookAdd">
            <span slot="title">添加人员</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <book-return v-show="returnBookVisible"></book-return>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import NavTitleBar from '../../templates/NavTitleBar.vue'
  import BookReturn from './BookReturnBorrow.vue'
  export default {
    name: 'bookManage',
    components: {
      NavTitleBar,
      BookReturn
    },
    data () {
      return {
        navTitleText: '前台操作员',
        navButtonText: '注销',
        activeIndex: 'bookReturn',
        totalTags: [],
        returnBookVisible: true
      }
    },
    mounted: function () {
    },
    methods: {
      handleMenuSelection (index) {
        if (index === 'bookAdd') {
          this.activeIndex = 'bookAdd'
          this.bookAddVisible = true
          this.returnBookVisible = false
        } else if (index === 'bookReturn') {
          this.activeIndex = 'bookReturn'
          this.returnBookVisible = true
        }
      }
    }
  }
</script>

<style scoped lang="stylus">
  #container {
    height: 610px
    border: 1px solid #eee
  }
  #aside {
    background-color: rgb(238, 241, 246)
  }
</style>
