<template>
  <div id="renew">
    <NavTitleBar :navTitleText="navTitleText" :navButtonText="navButtonText"></NavTitleBar>
    <el-container id="container">
      <el-aside width="200px" id="aside">
        <el-menu
          default-active="borrowStatus"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          @select="handleMenuSelection">
          <el-menu-item index="borrowStatus">
            <span slot="title">借阅状态</span>
          </el-menu-item>
          <el-menu-item index="historyBorrowRecord">
            <span slot="title">历史借阅</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <el-table ref="multiSelectionTable"
                  id="bookTable"
                  :data="tableData"
                  :default-sort="{prop: 'returnDate', order: 'ascending'}"
                  @selection-change="handleSelectionChange">
          <el-table-column type="selection" v-if="activeIndex=='borrowStatus'" width="55">
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
          <el-table-column prop="borrowDate" label="借阅日期">
            <template slot-scope="scope">
              <p>{{scope.row.borrowDate}}</p>
            </template>
          </el-table-column>
          <el-table-column prop="returnDate" sortable @sort-method="sortDate" label="应还日期">
            <template slot-scope="scope">
              <p>{{scope.row.returnDate}}</p>
            </template>
          </el-table-column>
        </el-table>
        <div id="multiRenew">
          <el-button
                v-show="multiRenewButtonVisible"
                size="mini"
                type="primary"
                @click="handleRenew">批量续期</el-button>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import NavTitleBar from '../templates/NavTitleBar.vue'
  export default {
    name: 'renew',
    components: {
      NavTitleBar
    },
    data () {
      return {
        navTitleText: '用户',
        navButtonText: '注销',
        activeIndex: 'borrowStatus',
        borrowTableData: [],
        historyTableData: [],
        tableData: [],
        selectedBookList: [],
        multiRenewButtonVisible: false
      }
    },
    mounted: function () {
      // example data which got by http
      let tmpBorrowTableData = [{
        'ISBN': 111,
        'bookName': 'borrow1',
        'borrowDate': '22',
        'returnDate': '2017-10-11'
      },
      {
        'ISBN': 222,
        'bookName': 'borrow2',
        'borrowDate': '44',
        'returnDate': '2017-10-25'
      },
      {
        'ISBN': 333,
        'bookName': 'borrow3',
        'borrowDate': '55',
        'returnDate': '2017-10-09'
      }]
      let tmpHistoryTableData = [{
        'ISBN': 111,
        'bookName': 'history1',
        'borrowDate': '22',
        'returnDate': '2017-11-06'
      },
      {
        'ISBN': 222,
        'bookName': 'history2',
        'borrowDate': '44',
        'returnDate': '2017-11-04'
      },
      {
        'ISBN': 333,
        'bookName': 'history3',
        'borrowDate': '55',
        'returnDate': '2017-11-05'
      }]
      this.borrowTableData = tmpBorrowTableData
      this.historyTableData = tmpHistoryTableData
      // initial
      this.tableData = this.borrowTableData
    },
    methods: {
      handleMenuSelection (index) {
        if (index === 'borrowStatus') {
          this.activeIndex = 'borrowStatus'
          this.tableData = this.borrowTableData
        } else if (index === 'historyBorrowRecord') {
          this.activeIndex = 'historyBorrowRecord'
          this.tableData = this.historyTableData
        }
      },
      handleSelectionChange (val) {
        this.selectedBookList = val
        if (val.length === 0) {
          console.log('select nothing')
          this.multiRenewButtonVisible = false
          return
        }
        this.multiRenewButtonVisible = true
        console.log('selection change === start ===')
        for (let i = 0; i < val.length; i++) {
          console.log(val[i])
        }
        console.log('selection change === end ===')
      },
      handleRenew () {
        console.log('renewing books === start ===')
        for (let i = 0; i < this.selectedBookList.length; i++) {
          console.log(this.selectedBookList[i])
          // request backend to deal
          // waiting for result
          // message to user
          // remove it from table data
        }
        this.$message.success('成功为' + this.selectedBookList.length + '本书续期!')
        console.log('renewing books === start ===')
      },
      sortDate (a, b) {
        let dateA = new Date(a)
        let dateB = new Date(b)
        return dateA > dateB
      }
    }
  }
</script>

<style scoped lang="stylus">
  #containter {
    height: 610px
    border: 1px solid #eee
  };
  #aside {
    background-color: rgb(238, 241, 246)
  };
  #bookTable {
    margin-top 20px
    margin-left 20px
  };
  #multiRenew {
    margin-top 50px
    float right
    margin-right 100px
  }
</style>
