<template>
  <div>
    <el-row>
    <el-col :span="1" :offset="14">
      <el-button @click="open_create_operator_view" type="primary" size="mini">新增</el-button>
    </el-col>
    <el-col :span="1" :offset="1">
      <el-button @click="deal_delete_operator" type="primary" size="mini" v-show="innerRemoveButtonVisible">删除</el-button>
    </el-col>
  </el-row>
    <el-row>
      <el-col :span="14" :offset="4">
      <el-table id="table" ref="multiSelectionTable" :data="innerOperatorTableData"
          :default-sort= "{prop: 'ID', order: 'ascending'}"
          @selection-change="handleInnerSelectionChange"
          @cell-click="cell_click">
          <el-table-column type="selection"></el-table-column>
          <el-table-column prop="ID" label="身份证号">
            <template slot-scope="scope">
          <p>{{scope.row.ID}}</p>
        </template>
          </el-table-column>
          <el-table-column prop="Role" label="角色">
            <template slot-scope="scope">
          <el-select v-model= scope.row.role @change="deal_update_operator" style="width: 130px" >
            <el-option label="书籍操作员" value="bookManage"></el-option>
            <el-option label="前台操作员" value="reception"></el-option>
          </el-select>
        </template>
          </el-table-column>
          <el-table-column prop="Name" label="姓名">
            <template slot-scope="scope">
            <p>{{scope.row.name}}</p>
          </template>
          </el-table-column>
      </el-table>
      </el-col>
    </el-row>
    <el-dialog :visible.sync="dialogVisible">
      <el-row>
        <el-form :model="operatorInfo" labelWidth="50px">
          <el-col :span="12" :offset="6">
            <el-form-item label="账号">
              <el-input v-model="operatorInfo.account"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12" :offset="6">
            <el-form-item label="角色">
              <el-select v-model="operatorInfo.role">
                <el-option label="书籍操作员" value="bookManage"></el-option>
                <el-option label="前台操作员" value="reception"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12" :offset="6">
            <el-form-item label="姓名">
              <el-input v-model="operatorInfo.name"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12" :offset="6">
            <el-form-item label="密码">
              <el-input v-model="operatorInfo.password" type="password"></el-input>
            </el-form-item>
          </el-col>
        </el-form>
      </el-row>
      <el-row>
        <el-col :span="1" :offset="10">
          <el-button @click="close_create_operator_view" type="primary" size="mini">取消</el-button>
        </el-col>
        <el-col :span="1" :offset="2">
          <el-button @click="deal_create_operator" type="primary" size="mini">保存</el-button>
        </el-col>
      </el-row>
    </el-dialog>
  </div>
</template>

<script>
  export default {
    name: 'InnerOperator',
    props: ['innerOperatorTableData'],
    data () {
      return {
        innerRemoveButtonVisible: false,
        selectedList: [],
        dialogVisible: false,
        operatorInfo: {
          account: '',
          role: '',
          password: '',
          name: ''
        },
        selectedRow: {
          account: '',
          role: '',
          name: ''
        }
      }
    },
    methods: {
      cell_click (row) {
        this.selectedRow.account = row.ID
        this.selectedRow.role = row.role
        this.selectedRow.name = row.name
      },
      handleInnerSelectionChange (val) {
        console.log('handleInnerSelectionChange')
        this.selectedList = val
        if (val.length === 0) {
          console.log('select nothing')
          this.innerRemoveButtonVisible = false
          return
        }
        this.innerRemoveButtonVisible = true
      },
      open_create_operator_view () {
        this.dialogVisible = true
      },
      close_create_operator_view () {
        this.dialogVisible = false
      },
      deal_create_operator () {
        var qs = require('qs')
        this.$http.post('api/create_operator/', qs.stringify(this.operatorInfo))
          .then((res) => {
            if (res.data.createStatus === 200) {
              this.close_create_operator_view()
              this.$message.success('添加成功')
            } else if (res.data.createStatus === 304) {
              this.$message.error(res.data.reason)
            } else {
              this.$message.error('未知的错误')
            }
          })
      },
      deal_delete_operator () {
        var qs = require('qs')
        let obj = {
          'delete_operator_list': JSON.stringify(this.selectedList)
        }
        this.$http.post('api/delete_operator/', qs.stringify(obj))
          .then((res) => {
            if (res.data.deleteStatus === 200) {
              this.$message.success('success')
            } else if (res.data.deleteStats === 304) {
              this.$message.error(res.data.reason)
            }
          })
      },
      deal_update_operator (val) {
        this.selectedRow.role = val
        var qs = require('qs')
        console.log(this.selectedRow.account, this.selectedRow.role)
        this.$http.post('api/update_operator/', qs.stringify(this.selectedRow))
          .then((res) => {
            console.log(this.selectedRow.account, this.selectedRow.role)
            if (res.data.updateStatus === 200) {
              this.$message.success('success')
            } else if (res.data.updateStatus === 304) {
              this.$message.error(res.data.reason)
            } else {
              this.$message.error('未知的错误')
            }
          })
      }
    }
  }
</script>
