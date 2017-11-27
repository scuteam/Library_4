<template>
  <div>
    <el-row>
      <el-col id='search-bar' :xs="24" :sm="{span: 20, offset: 2}">
        <SearchBar @getQueryResult="deal_query_result"></SearchBar>
      </el-col>
    </el-row>
    <el-row>
      <el-col id='radio-group' :xs="24" :sm="{span: 20, offset: 2}">
        <el-radio-group v-model="selectTag">
          <el-radio :label="0">全部</el-radio>
          <el-radio :label="1">科幻</el-radio>
          <el-radio :label="2">计算机</el-radio>
          <el-radio :label="3">教育</el-radio>
          <el-radio :label="4">历史</el-radio>
        </el-radio-group>
      </el-col>
    </el-row>
    <el-row>
      <el-col id='book-list' :xs="24" :sm="{span: 20, offset: 2}">
        <el-table :data="bookData" @row-click='handle_row_click' style="width: 100%">
          <el-table-column  label="封面">
            <template slot-scope="scope">
              <img v-if="scope.row.bookImageUrl" :src="scope.row.bookImageUrl"  class="avatar">
            </template>
          </el-table-column>
          <el-table-column  label="作者">
            <template slot-scope="scope">
              <p>{{scope.row.bookAuthor}}</p>
            </template>
          </el-table-column>
          <el-table-column label="ISBN">
            <template slot-scope="scope">
              <p>{{scope.row.bookISBN}}</p>
            </template>
          </el-table-column>
          <el-table-column label="是否在馆">
            <template slot-scope="scope"> 
              <el-tag size="medium">{{ scope.row.available }}</el-tag>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <el-row id='page-control'>
      <el-pagination layout="prev, pager, next" :total="50"></el-pagination>
    </el-row>
    <BookInfo :book-info-visible='infoVisible' @close="_=>this.infoVisible = false"></BookInfo>
  </div>
</template>
<script>
  import SearchBar from '../templates/SearchBar.vue'
  import BookInfo from './BookInfo.vue'
  export default {
    data () {
      return {
        selectTag: 0,
        totalTags: [],
        bookData: [
          {
            bookAuthor: 'mike',
            bookISBN: '123425'
          }
        ],
        infoVisible: false
      }
    },
    components: {
      SearchBar,
      BookInfo
    },
    mounted: function () {
      console.log('account is' + this.$route.params.account)
      // TODO:
      // get total tags from server
      this.$http.get('/api/query_all_tags')
        .then((res) => {
          this.totalTags.length = 0 // clear the data
          let index = 1
          for (let i = 0; i < res.data.tags.length; i++) {
            let tmpTag = {
              key: index,
              label: res.data.tags[i]
            }
            this.totalTags.push(tmpTag)
            index++
          }
        }, (err) => {
          console.log('query all tags from server, query error: === start ===')
          console.log(err)
          console.log('query all tags from server, query error: === end ===')
        })
    },
    methods: {
      deal_query_book () {
        console.log('searching === start ===')
        console.log('searchType is ' + this.searchType)
        console.log('searchContent is ' + this.searchContent)
        console.log('searching === end ===')
        let win = this
        // query book
        this.$http.get('/api/query_book', {
          'params': {
            query_type: this.searchType,
            query_keyword: this.searchContent
          }
        }).then((res) => {
          let bookList = res.data.book_list
          console.log('query book from server, get result: === start ===')
          console.log(bookList)
          win.$emit('getQueryResult', bookList)
          console.log('query book from server, get result: === end ===')
        }, (err) => {
          console.log('query book from server, get error: === start ===')
          console.log(err)
          console.log('query book from server, get error: === end ===')
        })
      },
      deal_query_result () {
      },
      deal_last_page () {
      },
      deal_next_page () {
      },
      handle_row_click (bookInfo) {
        this.infoVisible = true
      }
    }
  }
</script>
<<style lang="stylus" scoped>
  #search-bar
    margin-top: 50px
  #radio-group
    margin-top: 40px
  #book-list
    margin-top: 20px
    text-align: left
  #page-control
    margin-top: 40px
</style>
