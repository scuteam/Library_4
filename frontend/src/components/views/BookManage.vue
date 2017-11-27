<template>
  <div id="renew">
    <NavTitleBar :navTitleText="navTitleText" :navButtonText="navButtonText"></NavTitleBar>
    <el-container id="container">
      <el-aside width="200px" id="aside">
        <el-menu
          default-active="bookRemove"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          @select="handleMenuSelection">
          <el-menu-item index="bookRemove">
            <span slot="title">图书下架</span>
          </el-menu-item>
          <el-menu-item index="bookAdd">
            <span slot="title">图书上架</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <el-row id="book-add" v-show="bookAddVisible">
          <el-col :span="8" >
            <div id="bookInfoInput">
                <el-form labelWidth="100px">
                  <el-row>
                    <el-col>
                      <el-form-item label="ISBN:"  required="">
                        <el-input v-model="bookISBN" type="text" autofocus></el-input>
                      </el-form-item>
                    </el-col>
                  </el-row>
                  <el-row>
                    <el-col>
                      <el-form-item label="书名"  required="">
                        <el-input v-model="bookName"></el-input>
                      </el-form-item>
                    </el-col>
                  </el-row>
                  <el-row>
                    <el-col>
                      <el-form-item label="作者"  required="">
                        <el-input v-model="bookAuthor"></el-input>
                      </el-form-item>
                    </el-col>
                  </el-row>
                  <el-row>
                    <el-col>
                      <el-form-item label="出版社"  required="">
                        <el-input v-model="bookPublisher"></el-input>
                      </el-form-item>
                    </el-col>
                  </el-row>
                  <el-row>
                    <el-col>
                      <el-form-item label="数量"  required="">
                        <el-input v-model="bookNumber"></el-input>
                      </el-form-item>
                    </el-col>
                  </el-row>
                  <el-row>
                    <el-col>
                      <el-form-item label="简介"  required="">
                        <el-input v-model="bookIntroduction" type='textarea' :rows='6'></el-input>
                      </el-form-item>
                    </el-col>
                  </el-row>
                </el-form>
              </div>
              <el-row :gutter="20">
                <el-col :span="2" :offset="6">
                  <el-button type="success" @click="handleAddBook">保存</el-button>
                </el-col>
                <el-col :span="2" :offset="10">
                  <el-button type="danger" @click="handleCancelAddBook">取消</el-button>
                </el-col>
              </el-row>
          </el-col>
          <el-col :span="11" :offset="1">
            <el-row>
              <el-col :offset="9">
                <el-upload
                  class="avatar-uploader"
                  action=""
                  :show-file-list="false"
                  :on-success="handleAvatarSuccess"
                  :before-upload="beforeAvatarUpload">
                  <img v-if="bookImageUrl" :src="bookImageUrl" class="avatar">
                  <i v-else class="el-icon-picture avatar-uploader-icon"></i>
                </el-upload>
              </el-col>
            </el-row>
            <el-transfer :data="totalTags" v-model="hasTagsIndexList"
                         :titles="['全部标签', '添加标签']"
                         @change="handleMoveTags"
                         style="margin-top: 10px; margin-left: 50px">
              <el-button class="transfer-footer" slot="left-footer" size="small" @click="handleAddNewTag">新增标签</el-button>
            </el-transfer>
          </el-col>
        </el-row>
        <el-row style="margin-top: 10px" v-show="bookRemoveVisible">
          <el-col :span="12" :offset="6">
            <div id="search-bar">
              <search-bar @getQueryResult="handleQueryResultShow"></search-bar>
            </div>
          </el-col>
        </el-row>
        <el-row v-show="bookRemoveVisible" id="book-remove">
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
            <el-button type="primary" v-show="multiRemoveButtonVisible&&(activeIndex==='bookRemove')" id="multiRemoveButton" @click="handleDeleteBook">批量下架</el-button>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import NavTitleBar from '../templates/NavTitleBar.vue'
  import SearchBar from '../templates/SearchBar.vue'
  export default {
    name: 'bookManage',
    components: {
      NavTitleBar,
      SearchBar
    },
    data () {
      return {
        navTitleText: '书籍操作员',
        navButtonText: '注销',
        activeIndex: 'bookRemove',
        bookISBN: '',
        bookName: '',
        bookAuthor: '',
        bookPublisher: '',
        bookNumber: '',
        bookIntroduction: '',
        bookImageUrl: '',
        totalTags: [],
//        totalTags: [{key: 1, label: 'tag1'}, {key: 2, label: 'tag2'}, {key: 3, label: 'tag3'},
//          {key: 4, label: 'tag4'}, {key: 5, label: 'tag5'}, {key: 6, label: 'tag6'},
//          {key: 7, label: 'tag7'}, {key: 8, label: 'tag8'}, {key: 9, label: 'tag9'}],
        hasTagsIndexList: [],
        hasTagsLabelList: [],
        bookAddVisible: false,
        bookRemoveVisible: true,
        tableData: [],
//        tableData: [{
//          'ISBN': 111,
//          'bookName': 'borrow1',
//          'bookAuthor': '22'
//        },
//        {
//          'ISBN': 222,
//          'bookName': 'borrow2',
//          'bookAuthor': '44'
//        },
//        {
//          'ISBN': 333,
//          'bookName': 'borrow3',
//          'bookAuthor': '55'
//        }],
        multiRemoveButtonVisible: false,
        selectedBookList: []
      }
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
          console.log('query all tags from server, query error: === start ===')
        })
    },
    methods: {
      handleMenuSelection (index) {
        if (index === 'bookAdd') {
          this.activeIndex = 'bookAdd'
          this.bookAddVisible = true
          this.bookRemoveVisible = false
        } else if (index === 'bookRemove') {
          this.activeIndex = 'bookRemove'
          this.bookAddVisible = false
          this.bookRemoveVisible = true
        }
      },
      handleMoveTags (value, direction, movedKeys) {
        this.hasTagsLabelList.length = 0
        for (let i = 0; i < this.hasTagsIndexList.length; i++) {
          for (let j = 0; j < this.totalTags.length; j++) {
            if (this.hasTagsIndexList[i] === this.totalTags[j].key) {
              this.hasTagsLabelList.push(this.totalTags[j].label)
            }
          }
        }
        console.log('this book has tags', this.hasTagsLabelList)
      },
      handleAddNewTag () {
        this.$prompt('请输入新增标签', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消'
        }).then(({ value }) => {
          // TODO:
          // connect to server to tell the database add tags ?
          // NO! if user add tags and then cancel to add book,
          // the tags which shouldn't be uploaded to the server actually do
          let tag = {key: this.totalTags.length + 1, label: value}
          this.totalTags.push(tag)
        }).catch(() => {
          console.log('cancel add new tag')
        })
      },
      handleAddBook () {
        this.$confirm('确认将该图书上架吗?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          // TODO:
          // tell the server to add book
          this.deal_create_book()
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消上架'
          })
        })
      },
      handleDeleteBook () {
        this.$confirm('确认将所选图书下架吗?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          // TODO:
          // tell the server to add book
          this.deal_delete_book()
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消下架'
          })
        })
      },
      handleCancelAddBook () {
        // TODO:
        // clear all the input?
      },
      handleAvatarSuccess (res, file) {
        this.bookImageUrl = URL.createObjectURL(file.raw)
      },
      beforeAvatarUpload (file) {
        const isJPG = file.type === 'image/jpeg'
        const isLt2M = file.size / 1024 / 1024 < 2
        if (!isJPG) {
          this.$message.error('上传图片只能是 JPG 格式!')
        }
        if (!isLt2M) {
          this.$message.error('上传图片大小不能超过 2MB!')
        }
        return isJPG && isLt2M
      },
      handleSelectionChange (val) {
        this.selectedBookList = val
        if (val.length === 0) {
          console.log('select nothing')
          this.multiRemoveButtonVisible = false
          return
        }
        this.multiRemoveButtonVisible = true
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
      deal_create_book () {
        let newBook = {
          'ISBN': this.bookISBN,
          'author': this.bookAuthor,
          'publisher': this.bookPublisher,
          'total_number': this.bookNumber,
          'left_number': this.bookNumber,
          'intro': this.bookIntroduction,
          'title': this.bookName,
          'surface': this.bookImageUrl,
          'tag': this.hasTagsLabelList
        }
        this.$http.get('/api/create_book/', {
          params: {'newBook': newBook}
        }).then((res) => {
          console.log('creating a book, === start ===')
          if (res.data.createStatus === 200) {
            this.$message({
              type: 'success',
              message: '上架成功!'
            })
            // should clear the data?
          }
          console.log('creating a book, === end ===')
        }, (err) => {
          console.log('creating a book, got error, error msg === start ===')
          console.log(err)
          console.log('creating a book, got error, error msg === end ===')
        })
      },
      deal_delete_book () {
        if (this.selectedBookList.length !== 0) {
          this.$http.get('/api/delete_book', {
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
  .avatar-uploader .el-upload {
    border: 5px dashed #51#2b81af
    border-radius: 6px
    cursor: pointer
    position: relative
    overflow: hidden
  }
  .avatar-uploader .el-upload:hover {
    border: 7px
    border-color: #ff5b84
  }
  .avatar-uploader-icon {
    font-size: 28px
    color: #bfccff
    width: 178px
    height: 178px
    line-height: 178px
    text-align: center
  }
  .avatar {
    width: 120px
    height: 150px
    border 3px
    border-color #528CE0
    display: block
  }
  #container {
    height: 610px
    border: 1px solid #eee
  }
  #aside {
    background-color: rgb(238, 241, 246)
  }
  #book-add {
    margin-top: 10px
  }
  #book-remove {
    margin-top: 20px
  }
  #search-bar {
    margin-top: 15px
  }
  #multiRemoveButton {
    margin-top 50px
    float right
    margin-right 100px
  }
</style>
