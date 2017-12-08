<template>
  <div>
    <el-row style="margin-top: 10px">
      <el-col :span="15" :offset="3">
        <div id="search-bar">
          <search-bar @getQueryResult="handleQueryResultShow"></search-bar>
        </div>
      </el-col>
      <el-col :span="5">
        <div id="borrow-button">
          <el-button type="primary" v-show="borrowButtonVisible" id="borrowButton" @click="handleBorrowBook">借书</el-button>
        </div>
      </el-col>
    </el-row>
      <el-row id="book-return">
        <el-col :span="20" :offset="2">
          <el-table
            v-show="tableData.length !== 0"
            ref="multiSelectionTable"
            :data="tableData"
            @selection-change="handleSelectionChange">
            <el-table-column type="selection" width="55">
            </el-table-column>
            <el-table-column prop="ISBN" label="ISBN">
              <template slot-scope="scope">
                <p>{{scope.row.ISBN}}</p>
              </template>
            </el-table-column>
            <el-table-column prop="title" label="书名">
              <template slot-scope="scope">
                <p>{{scope.row.bookName}}</p>
              </template>
            </el-table-column>
            <el-table-column prop="author" label="作者">
              <template slot-scope="scope">
                <p>{{scope.row.bookAuthor}}</p>
              </template>
            </el-table-column>
          </el-table>
        </el-col>
      </el-row>
    <el-row>
      <el-col>
        <el-button type="primary" v-show="returnButtonVisible" id="returnButton" @click="handleReturnBook">还书</el-button>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import SearchBar from './UserSearchBar.vue'
export default {
  components: {
    SearchBar
  },
  data () {
    return {
      returnButtonVisible: false,
      borrowButtonVisible: false,
      id: '',
      tableData: [],
      selectedBookList: []
    }
  },
  methods: {
    handleSelectionChange (val) {
      this.selectedBookList = val
      this.returnButtonVisible = true
      if (val.length === 0) {
        console.log('select nothing')
        this.returnButtonVisible = false
        return
      }
      this.returnButtonVisible = true
      console.log('selection change === start ===')
      for (let i = 0; i < val.length; i++) {
        console.log(val[i])
      }
      console.log('selection change === end ===')
    },
    handleQueryResultShow (bookList, id) {
      this.tableData = bookList
      this.borrowButtonVisible = true
      this.id = id
      console.log('receive data')
    },
    handleReturnBook () {
      this.$confirm('确认将所选图书归还吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        for (var b of this.selectedBookList) {
          this.deal_return_book(b.ISBN)
        }
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消归还'
        })
      })
    },
    handleBorrowBook () {
      this.$prompt('请输入ISBN', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消'
      }).then(({ value }) => {
        console.log(value)
        var qs = require('qs')
        this.$http.post('/api/borrow_book/',
          qs.stringify({
            userId: this.id,
            bookISBN: value
          })
        ).then((res) => {
          if (res.data.borrowStatus === 200) {
            this.$message.success('借阅成功')
            this.deal_query_book()
          }
        }, (err) => {
          console.log(err)
          this.$message.error('借阅失败，请检查ISBN号')
        })
      }).catch(() => {
      })
    },
    deal_return_book (bookISBN) {
      if (this.selectedBookList.length !== 0) {
        var qs = require('qs')
        this.$http.post('/api/return_book/',
          qs.stringify({
            userId: this.id,
            bookISBN: bookISBN
          })
        ).then((res) => {
          console.log('deleting a book, === start ===')
          if (res.data.returnStatus === 200) {
            this.$message.success('还书成功')
          }
          console.log()
          console.log('deleting a book, === end ===')
        }, (err) => {
          console.log('deleting a book, got error, error msg: === start ===')
          console.log(err)
          console.log('deleting a book, got error, error msg: === end ===')
        })
      }
    },
    deal_query_book () {
      // query book
      var qs = require('qs')
      this.$http.post('/api/get_borrow_status_by_userInfo/', qs.stringify({
        userInfoType: 'id',
        userInfo: this.id
      }))
        .then((res) => {
          if (res.data.getStatus === 304) {
            this.$message.error('用户不存在')
            return
          }
          this.tableData = res.data.borrowTableData
        }, (err) => {
          console.log('query book from server, get error: === start ===')
          console.log(err)
          console.log('query book from server, get error: === end ===')
        })
    }
  }
}
</script>
<style scoped lang="stylus">
  #book-return
    margin-top: 20px
    text-align: left
  #search-bar {
    margin-top: 0px
  }
  #returnButton {
    margin-top 50px
    float right
    margin-right 100px
  }
</style>
