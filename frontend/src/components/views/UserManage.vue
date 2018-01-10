<template>
  <div>
    <el-row :gutter="20">
        <el-col :span="3" :offset="4">
          <el-select v-model="searchKey">
            <el-option value="姓名"></el-option>
            <el-option value="身份证号"></el-option>
          </el-select>
        </el-col>
        <el-col :span="8">
          <el-input v-model="searchString"></el-input>
        </el-col>
        <el-col :span="4">
          <el-button @click="handleSearch" type="primary">搜索</el-button>
        </el-col>
    </el-row>
    <br/><br/>
    <el-row>
    <el-col :span="1" :offset="14">
    <el-button @click="open_create_user_view" type="primary" size="mini">新增</el-button>
    </el-col>
    <el-col :span="1" :offset="1" >
    <el-button @click="deal_delete_user" type="primary" size="mini" v-show="userRemoveButtonVisible">删除</el-button>
    </el-col>
    </el-row>
    <el-row>
    <el-col :span="14" :offset="4">
    <el-table ref="multiSelectionTable" :data="tableData"
        :default-sort= "{prop: 'ID', order: 'ascending'}"
        @selection-change="handleUserSelectionChange">
    <el-table-column type="selection"  width='55'></el-table-column>
    <el-table-column prop="ID" label="身份证号">
    <template slot-scope="scope">
      <p>{{scope.row.ID}}</p>
    </template>
    </el-table-column>
    <el-table-column prop="name" label="姓名">
    <template slot-scope="scope">
        <p>{{scope.row.name}}</p>
    </template>
    </el-table-column>
    </el-table>
    </el-col>
    </el-row>
    <el-dialog :visible.sync="dialogVisible">
      <el-row>
        <el-form :model="userInfo" labelWidth="100px">
          <el-col :span="12" :offset="6">
            <el-form-item label="身份证号">
              <el-input v-model="userInfo.ID"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12" :offset="6">
            <el-form-item label="姓名">
              <el-input v-model="userInfo.name" ></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12" :offset="6">
            <el-form-item label="密码">
              <el-input v-model="userInfo.password" type="password"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12" :offset="6">
            <el-form-item label="确认密码">
              <el-input v-model="userInfo.passwordTemp" type="password"></el-input>
            </el-form-item>
          </el-col>
        </el-form>
      </el-row>
      <el-row>
        <el-col :span="1" :offset="10">
          <el-button @click="close_create_user_view" type="primary" size="mini">取消</el-button>
        </el-col>
        <el-col :span="1" :offset="2">
          <el-button @click="deal_create_user" type="primary" size="mini">保存</el-button>
        </el-col>
      </el-row>
    </el-dialog>
  </div>
</template>
<script>
  export default {
    name: 'UserManage',
    props: ['userTableData'],
    data () {
      return {
        userRemoveButtonVisible: false,
        searchKey: '姓名',
        searchString: '',
        selectedList: [],
        dialogVisible: false,
        userInfo: {
          ID: '',
          name: '',
          password: '',
          passwordTemp: ''
        }
      }
    },
    methods: {
      handleSearch () {
        this.$message.success('搜索成功')
      },
      handleUserSelectionChange (val) {
        this.selectedList = val
        if (val.length === 0) {
          console.log('select nothing')
          this.userRemoveButtonVisible = false
          return
        }
        this.userRemoveButtonVisible = true
      },
      open_create_user_view () {
        this.dialogVisible = true
      },
      close_create_user_view () {
        this.dialogVisible = false
      },
      deal_create_user () {
        if (this.userInfo.ID === '') {
          this.$message.error('身份证号不能为空')
          return
        }
        if (this.userInfo.name === '') {
          this.$message.error('姓名不能为空')
          return
        }
        if (this.userInfo.password.length < 6 || this.userInfo.password.length > 20) {
          this.$message.error('密码长度应为6-20位')
          return
        }
        if (this.userInfo.password !== this.userInfo.passwordTemp) {
          this.$message.error('两次密码不同')
          return
        }
        let reg = /[1-9][0-9]{16}[x0-9]/
        if (!reg.test(this.userInfo.ID)) {
          this.$message.error('身份证号错误')
          return false
        }
        var qs = require('qs')
        this.$http.post('api/create_user/', qs.stringify(this.userInfo))
          .then((res) => {
            if (res.data.createStatus === 200) {
              this.close_create_user_view()
              this.userTableData.unshift({
                ID: this.userInfo.ID,
                name: this.userInfo.name
              })
              this.$message.success('添加成功')
            } else if (res.data.createStatus === 304) {
              this.$message.error(res.data.reason)
            } else {
              this.$message.error('未知的错误')
            }
          })
      },
      deal_delete_user () {
        this.$confirm('确认删除?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          var qs = require('qs')
          let obj = {
            'delete_user_list': JSON.stringify(this.selectedList)
          }
          this.$http.post('api/delete_user/', qs.stringify(obj))
            .then((res) => {
              if (res.data.deleteStatus === 200) {
                this.selectedList.forEach(this.deleteItem)
                this.$message.success('删除成功')
              } else if (res.data.deleteStats === 304) {
                this.$message.error(res.data.reason)
              }
            })
        })
      },
      deal_update_user () {
        this.$http.get('api/update_user/')
          .then((res) => {
            if (res.data.loginStatus === 200) {
              this.$message.success('更改成功')
            }
          })
      },
      searchByName (obj) {
        return obj.name.indexOf(this.searchString) !== -1
      },
      searchByID (obj) {
        return obj.ID.indexOf(this.searchString) !== -1
      },
      deleteItem (item) {
        let index = this.userTableData.indexOf(item)
        this.userTableData.splice(index, 1)
      }
    },
    computed: {
      tableData: function () {
        this.searchString = this.searchString.trim()
        let tmpTableData = []
        if (this.searchString === '') {
          tmpTableData = this.userTableData
          return tmpTableData
        }
        if (this.searchKey === '姓名') {
          tmpTableData = this.userTableData.filter(this.searchByName)
        } else if (this.searchKey === '身份证号') {
          tmpTableData = this.userTableData.filter(this.searchByID)
        }
        return tmpTableData
      }
    }
  }
</script>
