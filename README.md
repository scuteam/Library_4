# 网上图书管理系统

> IT项目管理大作业作品,使用项目管理的完整流程,经历了需求分析,概要设计,详细设计,编码,测试,部署六个阶段

## 文档

```

├── doc
│   ├── development
|   |   ├── 1-需求文档
|   |   │   ├── 用例图
|   |   │   │   ├── 书籍操作员用例图.png
|   |   │   │   ├── 借书.png
|   |   │   │   ├── 借阅状态查询.png
|   |   │   │   ├── 内部账户管理.png
|   |   │   │   ├── 前台操作员用例图.png
|   |   │   │   ├── 操作员用例图.png
|   |   │   │   ├── 普通用户用例图.png
|   |   │   │   ├── 用例图.png
|   |   │   │   ├── 用例图.vsdx
|   |   │   │   ├── 用户管理.png
|   |   │   │   ├── 管理员用例图.png
|   |   │   │   ├── 续期.png
|   |   │   │   └── 还书.png
|   |   │   ├── 需求文档
|   |   │   │   ├── 1-需求文档V5.6.docx
|   |   │   └── 项目原型
|   |   │       ├── 原型V2.6.rp
|   |   │       └── 原型修改意见.txt
|   |   ├── 2-概要设计
|   |   │   ├── 概要设计文档
|   |   │   │   ├── 2概要设计.txt
|   |   │   │   └── 2-概要设计文档V6.8.docx
|   |   │   └── 视图
|   |   │       ├── 物理架构视图
|   |   │       │   └── 物理视图.vsdx
|   |   │       └── 逻辑架构视图
|   |   │           ├── 系统逻辑视图V2.2.png
|   |   │           └── 逻辑架构V3.3.pdf
|   |   ├── 3-系统详细设计
|   |   │   ├── 状态图
|   |   │   │   ├── 图书状态图.vsdx
|   |   │   │   └── 用户状态图.vsdx
|   |   │   ├── 类图
|   |   │   │   ├── ControllerV1.1.png
|   |   │   │   ├── Model层V1.1.png
|   |   │   │   ├── Service层V1.1.png
|   |   │   │   ├── View层V1.1.png
|   |   │   │   └── 类图 V2.5.pdf
|   |   │   ├── 详细设计文档
|   |   │   │   └── 系统详细设计V2.7.docx
|   |   │   └── 顺序图
|   |   │       └── 顺序图V0.6.mdl
|   |   ├── 4-测试报告
|   |   │   ├── 4-测试报告V1.1.doc
|   |   │   ├── BUG.txt
|   |   │   └── Bug检查.txt
|   |   ├── 5-用户手册
|   |   │   └── 5-用户手册V1.1.doc
|   |   ├── 6-系统数据模型
|   |   │   ├── 数据模型
|   |   │   │   └── 数据模型 - 中文V0.2.ddd
|   |   │   ├── 数据模型截图
|   |   │   │   └── 数据模型.png
|   |   │   └── 系统数据模型文档
|   |   │       └── 6-系统数据模型V2.5.docx
|   |   └── 7-开发环境部署
|   |       └── env.txt
│   └── management
│       ├── 1-项目开题报告与计划
│       │   ├── Project
│       │   │   ├── 网上图书管理系统V11.11.mpp
│       │   └── 开题报告与计划文档
│       │       ├── 1-项目开题报告与计划V2.2.docx
│       ├── 2-项目章程
│       │   └── 项目章程文档
│       │       └── 2-项目章程V3.3.doc
│       ├── 3-项目周报
│       │   └── 3-Weekly Report.doc
│       ├── 4-项目范围
│       │   ├── 网上图书管理系统.bmp
│       │   ├── 网上图书管理系统WBS.xmind
│       │   └── 项目范围文档
│       │       └── 4-项目范围V2.2.doc
│       ├── 5-项目变更报告
│       │   └── 5-Project Change ReportV1.1.doc
│       ├── 6-成本估算
│       │   └── 成本估算V1.1.xls
│       ├── 7-项目结项报告
│       │   └── 7-Project ClosingV2.2.doc
│       └── 安排
│           ├── 四号图书馆初期安排-V2.2.xmind
```

### 前端

```

├── frontend
│   ├── index.html
│   ├── package.json
│   ├── README.md
│   ├── src
│   │   ├── App.vue
│   │   ├── assets
│   │   │   └── logo.png
│   │   ├── components
│   │   │   ├── templates
│   │   │   │   ├── NavTitleBar.vue
│   │   │   │   └── SearchBar.vue
│   │   │   └── views
│   │   │       ├── Admin.vue
│   │   │       ├── BookBrowser.vue
│   │   │       ├── BookInfo.vue
│   │   │       ├── BookManage.vue
│   │   │       ├── BookReturnBorrow.vue
│   │   │       ├── Borrow.vue
│   │   │       ├── InnerOperator.vue
│   │   │       ├── Login.vue
│   │   │       ├── Reception.vue
│   │   │       ├── Renew.vue
│   │   │       ├── UserAdd.vue
│   │   │       ├── UserManage.vue
│   │   │       └── UserSearchBar.vue
│   │   ├── main.js
│   │   └── router
│   │       └── index.js
│   ├── static
```

### 后端

```

Library_4
├── backend
│   ├── admin.py
│   ├── apps.py
│   ├── controllers
│   │   ├── Book_manage.py
│   │   ├── Borrow_status.py
│   │   ├── __init__.py
│   │   ├── Inner_operator.py
│   │   ├── Login.py
│   │   ├── Query_all_tags.py
│   │   ├── Query_book.py
│   │   ├── Reception.py
│   │   ├── Renew.py
│   │   ├── test_book_manage.py
│   │   ├── User_manage.py
│   ├── models
│   │   ├── Book.py
│   │   ├── Borrow.py
│   │   ├── Has_tag.py
│   │   ├── __init__.py
│   │   ├── Own.py
│   │   ├── Permission.py
│   │   ├── Role.py
│   │   ├── Tag.py
│   │   ├── User.py
│   ├── services
│   │   ├── Book_manage.py
│   │   ├── Borrow_status.py
│   │   ├── __init__.py
│   │   ├── Inner_operator.py
│   │   ├── Login.py
│   │   ├── Operator.py
│   │   ├── Query_all_tags.py
│   │   ├── Query_book.py
│   │   ├── Reception.py
│   │   ├── Renew.py
│   │   ├── test_Book_manage.py
│   │   ├── User_manage.py
│   ├── urls.py
├── db.sqlite3
├── Library_4
│   ├── db.sqlite3
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
├── manage.py
├── README.md
└── static
    └── image
```