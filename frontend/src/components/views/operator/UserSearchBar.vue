<template>
  <el-input autofocus placeholder="请输入搜索内容" v-model="searchContent" class="input-with-select">
    <el-select v-model="searchType" slot="prepend" placeholder="书名">
      <el-option label="姓名" value="name"></el-option>
      <el-option label="身份证" value="id"></el-option>
    </el-select>
    <el-button slot="append" icon="el-icon-search" @click="deal_query_book"></el-button>
  </el-input>
</template>
<script>
  export default {
    data () {
      return {
        searchType: 'name',
        searchContent: ''
      }
    },
    methods: {
      deal_query_book () {
        console.log('searching === start ===')
        console.log('searchType is ' + this.searchType)
        console.log('searchContent is ' + this.searchContent)
        if (this.searchContent.length === 0) {
          this.$message.error('请输入搜索内容')
          return
        }
        console.log('searching === end ===')
        let win = this
        // query book
        var qs = require('qs')
        this.$http.post('/api/get_borrow_status_by_userInfo/', qs.stringify({
          userInfoType: this.searchType,
          userInfo: this.searchContent
        })
        ).then((res) => {
          if (res.data.getStatus === 304) {
            this.$message.error('用户不存在')
            return
          }
          let bookList = res.data.borrowTableData
          let id = res.data.userId
          this.$message.success('载入用户成功')
          console.log('query book from server, get result: === start ===')
          console.log(res.data)
          win.$emit('getQueryResult', bookList, id)
          console.log('query book from server, get result: === end ===')
        }, (err) => {
          console.log('query book from server, get error: === start ===')
          console.log(err)
          console.log('query book from server, get error: === end ===')
        })
      }
    }
  }
</script>
