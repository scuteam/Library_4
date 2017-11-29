<template>
  <el-dialog title="书籍详细信息" :visible="bookInfoVisible" @update:visible='handle_status_change'>
    <el-row id='book-info'>
      <el-col :span='8'>
        <div>
          <el-row>
            <el-col>
              <p>ISBN: {{ bookISBN }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col>
              <p>书名: {{ bookName }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col>
              <p>作者: {{ bookAuthor }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col>
              <p>出版社: {{ bookPublisher }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col>
              <p>数量: {{ bookNumber }}</p>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span='4'>
              <p>简介:</p>
            </el-col>
            <el-col :span='15'>
              <p>{{ bookIntroduction }}</p>
            </el-col>
          </el-row>
        </div>
      </el-col>
      <el-col :span="11" :offset="1">
        <el-row>
          <el-col :offset="9">
            <img v-if="bookImageUrl" :src="bookImageUrl" class="avatar">
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
    props: ['bookInfoVisible'],
    data () {
      return {
        bookISBN: '',
        bookName: '',
        bookAuthor: '',
        bookPublisher: '',
        bookNumber: '',
        bookIntroduction: '',
        bookImageUrl: ''
      }
    },
    methods: {
      handle_status_change: function (visible) {
        if (!visible) {
          this.$emit('close')
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
    width: 120px
    height: 150px
    border 3px
    border-color #528CE0
    display: block
  }
</style>
