<template>
  <div>
    <NavTitleBar :navTitleText="navTitleText" :navButtonText="navButtonText"></NavTitleBar>
    <div>
      <el-carousel indicator-position="outside" height="580px">
        <el-carousel-item  :key="1">
          <div>
            <div id="photo" align="center">
              <img src="../../assets/logo.png">
            </div>
            <el-row :gutter="20">
              <el-col :span="12" :offset="6">
                <div id="search-bar">
                  <search-bar></search-bar>
                </div>
              </el-col>
            </el-row>
          </div>
        </el-carousel-item>
        <el-carousel-item  :key="2">
          <BookBrowser></BookBrowser>
        </el-carousel-item>
      </el-carousel>
    </div>
  </div>
</template>

<script>
  import NavTitleBar from '../templates/NavTitleBar.vue'
  import SearchBar from '../templates/SearchBar.vue'
  import BookBrowser from '../views/BookBrowser.vue'
  export default {
    name: 'borrow',
    components: {
      NavTitleBar,
      SearchBar,
      BookBrowser
    },
    data () {
      return {
        searchContent: '',
        navTitleText: '网上图书管理系统',
        navButtonText: '登录'
      }
    }

  }
</script>
<style>
  .el-select .el-input {
    width: 130px
  }
  .input-with-select .el-input-group__prepend {
    background-color: #fff
  }
  #search-bar {
    margin-top: 30px
  }
  #photo {
    margin-top: 20px
  }
</style>
