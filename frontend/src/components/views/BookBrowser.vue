<template>
  <div>
    <el-row>
      <el-col id='search-bar' :xs="24" :sm="{span: 20, offset: 2}">
        <SearchBar @getQueryResult="deal_query_result"></SearchBar>
      </el-col>
    </el-row>
    <el-row>
      <el-col id='radio-group' :xs="24" :sm="{span: 20, offset: 2}">
        <el-radio-group v-for="tag in totalTags" :key="tag.key" v-model="selectTag">
            <el-col :sm="{span: 2, offset: 1}">
              <el-radio :label="tag.label"> {{ tag.label }} </el-radio>
            </el-col>
        </el-radio-group>
      </el-col>
    </el-row>
    <el-row>
      <el-col id='book-list' :xs="24" :sm="{span: 20, offset: 2}">
        <el-table :data="bookList" @row-click='handle_row_click' style="width: 100%">
          <el-table-column  label="封面">
            <template slot-scope="scope">
              <img v-if="scope.row.surface" :src="scope.row.surface"  class="avatar">
            </template>
          </el-table-column>
          <el-table-column  label="作者">
            <template slot-scope="scope">
              <p>{{scope.row.author}}</p>
            </template>
          </el-table-column>
          <el-table-column label="ISBN">
            <template slot-scope="scope">
              <p>{{scope.row.ISBN}}</p>
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
      <el-pagination layout="prev, pager, next" :total="bookList.length" :current-page="currentPage" :page-size="5" @current-change="deal_page_change"></el-pagination>
    </el-row>
    <BookInfo :book-info-visible='infoVisible' :book-info="bookInfo" @close="_=>this.infoVisible = false"></BookInfo>
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
        bookList: [],
        bookTagList: [],
        bookInfo: {},
        infoVisible: false,
        currentPage: 0
      }
    },
    components: {
      SearchBar,
      BookInfo
    },
    mounted: function () {
      this.init_tags()
      this.init_books()
    },
    watch: {
      bookData: function (nBookData) {
        var blist = []
        console.log('bookData update')
        for (var b of nBookData) {
          if (b.left_number === 0) {
            b.available = '不在馆'
            blist.push(b)
          }
          else {
            b.available = '在馆'
            blist.push(b)
          }
        }
        this.currentPage = 0
        this.selectTag = 0
        this.bookTagList = blist
        this.bookList = blist.slice(0, 5>=blist.length?blist.length:5)
      },
      selectTag: function (tagKey) {
        var blist =[]
        console.log(tagKey)
        for(var b of this.bookData) {
          if (b.tags.includes(tagKey)){
            blist.push(b)
          }
        }
        console.log(blist)
        this.currentPage = 0
        this.bookTagList = blist
        this.bookList = blist.slice(0, 5>=blist.length?blist.length:5)
      }
    },
    methods: {
      init_tags () {
        console.log('account is' + this.$route.params.account)
      // TODO:
      // get total tags from server
        this.$http.get('/api/query_all_tags/')
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
      init_books () {
        console.log('searching === start ===')
        console.log('searching === end ===')
        // query book
        this.$http.get('/api/query_book/', {
          'params': {
            query_type: 'bookISBN',
            query_keyword: ''
          }
        }).then((res) => {
          let bookList = res.data.book_list
          console.log('query book from server, get result: === start ===')
          console.log(bookList)
          this.bookData = bookList
          console.log('query book from server, get result: === end ===')
        }, (err) => {
          console.log('query book from server, get error: === start ===')
          console.log(err)
          console.log('query book from server, get error: === end ===')
        })
      },
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
      deal_query_result (queryResult) {
        this.bookData = queryResult
      },
      deal_page_change (currentPage) {
        this.currentPage = currentPage
        this.bookList = this.bookTagList.slice(currentPage*5, (currentPage+1)*5>=blist.length?blist.length:(currentPage+1)*5)
      },

      handle_row_click (bookInfo) {
        this.infoVisible = true
        this.bookInfo = bookInfo
      }
    }
  }
</script>
<<style lang="stylus" scoped>
  .avatar
    height: 100px
    width: 70px
  #search-bar
    margin-top: 50px
  #radio-group
    margin-top: 40px
  #book-list
    margin-top: 20px
    text-align: left
  #radio-group
    text-align left
  #page-control
    margin-top: 40px
</style>
