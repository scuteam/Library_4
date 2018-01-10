<template>
  <el-dialog title="书籍详细信息" :visible="bookInfoVisible" :modal="false" @update:visible='handle_status_change'>
    <el-row id='book-info'>
      <el-col :span='8'>
        <div>
          <el-row>
            <el-col>
              <p>ISBN: {{ ISBN }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col>
              <p>书名: {{ title }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col>
              <p>作者: {{ author }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col>
              <p>出版社: {{ publisher }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col>
              <p>数量: {{ total_number }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col>
              <p>剩余: {{ left_number }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span='4'>
              <p>简介:</p>
            </el-col>
            <el-col :span='15'>
              <p>{{ intro }}</p>
            </el-col>
          </el-row>
        </div>
      </el-col>
      <el-col :span="11" :offset="1">
        <el-row>
          <el-col :offset="9">
            <img v-if="surface" :src="surface" class="avatar">
            <i v-else class="el-icon-picture avatar-uploader-icon"></i>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </el-dialog>
</template>

<script>
  export default {
    name: 'bookInfo',
    props: ['bookInfoVisible', 'bookInfo'],
    data () {
      return {
        ISBN: '',
        title: '',
        total_number: '',
        author: '',
        left_number: '',
        intro: '',
        surface: '',
        publisher: ''
      }
    },
    methods: {
      handle_status_change: function (visible) {
        if (!visible) {
          this.$emit('close')
        } else {
          this.ISBN = this.bookInfo.ISBN
          this.title = this.bookInfo.title
          this.total_number = this.bookInfo.total_number
          this.author = this.bookInfo.author
          this.left_number = this.bookInfo.left_number
          this.intro = this.bookInfo.intro
          this.surface = this.bookInfo.surface
          this.publisher = this.bookInfo.publisher
        }
      }
    }
  }
</script>

<style scoped lang="stylus">
  .avatar-uploader-icon {
    font-size: 28px
    color: #bfccff
    width: 178px
    height: 178px
    line-height: 178px
    text-align: center
  }
  .avatar {
    width: 150px
    height: 200px
    border 3px
    border-color #528CE0
    display: block
  }
  #book-info
    text-align: left
</style>
