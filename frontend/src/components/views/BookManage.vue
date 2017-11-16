<template>
  <div id="renew">
    <NavTitleBar :navTitleText="navTitleText" :navButtonText="navButtonText"></NavTitleBar>
    <el-container style="height: 610px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu
          default-active="1"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          @select="handleMenuSelection">
          <el-menu-item index="1">
            <span slot="title">图书上架</span>
          </el-menu-item>
          <el-menu-item index="2">
            <span slot="title">图书下架</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <el-row style="margin-top: 10px">
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
                        <el-input v-model="bookIntroduction" type="textarea" :rows=6 ></el-input>
                      </el-form-item>
                    </el-col>
                  </el-row>
                  <el-row :gutter="20">
                    <el-col :span="2" :offset="6">
                      <el-button type="success" @click="handleAddBook">保存</el-button>
                    </el-col>
                    <el-col :span="2" :offset="10">
                      <el-button type="danger" @click="handleCancelAddBook">取消</el-button>
                    </el-col>
                  </el-row>
                </el-form>
            </div>
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
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import NavTitleBar from '../templates/NavTitleBar.vue'
  export default {
    name: 'bookManage',
    components: {
      NavTitleBar
    },
    data () {
      return {
        navTitleText: '书籍操作员',
        navButtonText: '注销',
        activeIndex: '1',
        bookISBN: '',
        bookName: '',
        bookAuthor: '',
        bookPublisher: '',
        bookNumber: '',
        bookIntroduction: '',
        bookImageUrl: '',
        totalTags: [{key: 1, label: 'tag1'}, {key: 2, label: 'tag2'}, {key: 3, label: 'tag3'},
          {key: 4, label: 'tag4'}, {key: 5, label: 'tag5'}, {key: 6, label: 'tag6'},
          {key: 7, label: 'tag7'}, {key: 8, label: 'tag8'}, {key: 9, label: 'tag9'}],
        hasTagsIndexList: [],
        hasTagsLabelList: []
      }
    },
    mounted: function () {
      // TODO:
      // get total tags from server
    },
    methods: {
      handleMenuSelection (index) {
        if (index === '1') {
          this.activeIndex = '1'
        } else if (index === '2') {
          this.activeIndex = '2'
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
          this.$message({
            type: 'success',
            message: '上架成功!'
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消上架'
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
      }
    }
  }
</script>

<style scoped lang="stylus">
  .avatar-uploader .el-upload {
    border: 5px dashed #51#2b81af;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border: 7px;
    border-color: #ff5b84;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #bfccff;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 120px;
    height: 150px;
    border 3px;
    border-color #528CE0
    display: block;
  }
</style>
