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
            <el-table-column prop="bookName" label="书名">
              <template slot-scope="scope">
                <p>{{scope.row.bookName}}</p>
              </template>
            </el-table-column>
            <el-table-column prop="borrowAuthor" label="作者">
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
        borrowButtonVisible: true,
        tableData: [{
        'ISBN': 111,
        'bookName': 'borrow1',
        'bookAuthor': '22'
       },
       {
         'ISBN': 222,
         'bookName': 'borrow2',
         'bookAuthor': '44'
       },
       {
         'ISBN': 333,
         'bookName': 'borrow3',
         'bookAuthor': '55'
       }],
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
      handleQueryResultShow (bookList) {
        this.tableData.length = 0 // clear the tableData
        for (let i = 0; i < bookList.length; i++) {
          let tmpBook = {
            ISBN: bookList[i].ISBN,
            bookName: bookList[i].title,
            bookAuthor: bookList[i].author
          }
          this.tableData.push(tmpBook)
        }
      },
      handleReturnBook () {
        this.$confirm('确认将所选图书归还吗?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          // TODO:
          // tell the server to add book
          this.deal_return_book()
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消下架'
          })
        })
      },
      handleBorrowBook () {
        this.$prompt('请输入ISBN', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
        }).then(({ value }) => {
          // this.$message({
          //   type: 'success',
          //   message: '你的邮箱是: ' + value
          // })
        }).catch(() => {
          // this.$message({
          //   type: 'info',
          //   message: '取消输入'
          // })    
        })
      },
      deal_return_book () {
        if (this.selectedBookList.length !== 0) {
          this.$http.get('/api/return_book', {
            params: {
              'delete_book_list': JSON.stringify(this.selectedBookList)
            }
          }).then((res) => {
            console.log('deleting a book, === start ===')
            if (res.data.deleteStatus === 200) {
              this.$message.success('下架成功')
              // TODO: delete selected book from local tableData list
              // TODO: what to show next?
            }
            console.log()
            console.log('deleting a book, === end ===')
          }, (err) => {
            console.log('deleting a book, got error, error msg: === start ===')
            console.log(err)
            console.log('deleting a book, got error, error msg: === end ===')
          })
        }
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