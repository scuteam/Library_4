<template>
  <el-input autofocus placeholder="请输入搜索内容" v-model="searchContent" class="input-with-select">
    <el-select v-model="searchType" slot="prepend" placeholder="书名">
      <el-option label="书名" value="bookName"></el-option>
      <el-option label="书籍出版社" value="bookPublisher"></el-option>
      <el-option label="作者" value="bookAuthor"></el-option>
      <el-option label="ISBN" value="bookISBN"></el-option>
    </el-select>
    <el-button slot="append" icon="el-icon-search" @click="handleSearch"></el-button>
  </el-input>
</template>
<script>
  export default {
    data () {
      return {
        searchType: 'bookName',
        searchContent: ''
      }
    },
    methods: {
      handleSearch () {
        console.log('searching === start ===')
        console.log('searchType is ' + this.searchType)
        console.log('searchContent is ' + this.searchContent)
        console.log('searching === end ===')
      }
    }
  }
</script>
