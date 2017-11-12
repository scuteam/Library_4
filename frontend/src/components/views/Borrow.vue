<template>
  <div>
    <NavTitleBar></NavTitleBar>
    <div>
      <el-carousel indicator-position="outside" height="580px">
        <el-carousel-item  :key="1">
          <div>
            <div align="center">
              <img src="../../assets/logo.png">
            </div>
            <el-row :gutter="20">
              <el-col :span="12" :offset="6">
                <div style="margin-top: 15px;">
                  <el-input placeholder="请输入搜索内容" v-model="input5" class="input-with-select">
                    <el-select v-model="borrowType" slot="prepend" placeholder="书名">
                      <el-option label="书名" value="bookName"></el-option>
                      <el-option label="书籍出版社" value="bookPublisher"></el-option>
                      <el-option label="作者" value="bookAuthor"></el-option>
                      <el-option label="ISBN" value="bookISBN"></el-option>
                    </el-select>
                    <el-button slot="append" icon="el-icon-search"></el-button>
                  </el-input>
                </div>
              </el-col>
            </el-row>
          </div>
        </el-carousel-item>
        <el-carousel-item  :key="2">

        </el-carousel-item>
      </el-carousel>
    </div>
  </div>
</template>

<script>
  import NavTitleBar from '../templates/NavTitleBar.vue'
  export default {
    name: 'borrow',
    components: {
      NavTitleBar
    },
    data () {
      return {
        borrowType: 'bookName'
      }
    }

  }
</script>
<style>
  .el-select .el-input {
    width: 130px;
  }
  .input-with-select .el-input-group__prepend {
    background-color: #fff;
  }
</style>
