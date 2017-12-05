# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
from controllers import Query_book
from django.contrib import auth
from django.http import HttpResponse
import json
from controllers import Query_book

# Create your views here.
def verify_account(request):
    account = request.GET.get('account')
    password = request.GET.get('password')
    role = request.GET.get('role')
    if role == 'user':
        if account == 'user' and password == 'user':
            return HttpResponse(json.dumps({'loginStatus': 200}))
        else:
            return HttpResponse(json.dumps({'loginStatus': 304, 'reason': 'name or role incorrect'}))
    elif role == 'bookManager':
        if account == 'bookManage' and password == 'bookManage':
            return HttpResponse(json.dumps({'loginStatus': 200}))
        else:
            return HttpResponse(json.dumps({'loginStatus': 304, 'reason': 'name or role incorrect'}))
    elif role == 'innerOperator':
        if account == 'innerOperator' and password == 'innerOperator':
            return HttpResponse(json.dumps({'loginStatus': 200}))
        else:
            return HttpResponse(json.dumps({'loginStatus': 304, 'reason': 'name or role incorrect'}))
    elif role == 'reception':
        if account == 'reception' and password == 'reception':
            return HttpResponse(json.dumps({'loginStatus': 200}))
        else:
            return HttpResponse(json.dumps({'loginStatus': 304, 'reason': 'name or role incorrect'}))
    else:
        return HttpResponse(json.dumps({'loginStatus': 404, 'reason': 'role not found'}))

def get_borrow_status(request):
    account = request.GET.get('account')
    print account
    # query borrow_status and history_borrow_record by account
    # some temporary example data
    tmpBorrowTableData = [{
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
    tmpHistoryTableData = [{
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
    return HttpResponse(json.dumps({
        'borrowTableData': tmpBorrowTableData,
        'historyTableData': tmpHistoryTableData
    }))

def query_book(request):
    query_type = request.GET.get('query_type')
    query_keyword = request.GET.get('query_keyword')
    print query_type, query_keyword
    # search from database
    # mock data
    book_list = [{
        'ISBN': 'isbn',
        'author': 'author',
        'publisher': 'publisher',
        'total_number': 20,
        'left_number': 13,
        'intro': 'this is a string of introduction',
        'title': 'book title',
        'surface': 'http://XXX/xxx.jpg'
    },{
        'ISBN': 'isbn',
        'author': 'author',
        'publisher': 'publisher',
        'total_number': 20,
        'left_number': 13,
        'intro': 'this is a string of introduction',
        'title': 'book title',
        'surface': 'http://XXX/xxx.jpg'
    }]
    return HttpResponse(json.dumps({'book_list': book_list}))

def query_all_tags(request):
    # mock data
    tags = ['tag1', 'tag2', 'tag3', 'tag4', 'tag5']
    return HttpResponse(json.dumps({'tags': tags}))

def create_book(request):
    book = request.GET.get('newBook')
    book = json.loads(book)
    print type(book)
    print book['ISBN']
    print book['author']
    print book['publisher']
    print book['total_number']
    print book['left_number']
    print book['intro']
    print book['title']
    print book['surface']
    print book['tag']
    # TODO: check tag if in tags table, if not, create one
    # TODO: create book in database
    return HttpResponse(json.dumps({'createStatus': 200}))

def delete_book(request):
    book_list = request.GET.get('delete_book_list')
    book_list = json.loads(book_list)
    print type(book_list)
    for book in book_list:
        print book
    # delete from database
    return HttpResponse(json.dumps({'deleteStatus': 200}))

def renew(request):
    book_list = request.GET.get('renew_book_list')
    book_list = json.loads(book_list)
    print type(book_list)
    for book in book_list:
        print book
        # TODO: add 15 days to the returnDate
    # renew from database
    return HttpResponse(json.dumps({'renewStatus': 200}))


def get_operator_info(request):
    account = request.GET.get('account')
    print account
    tmp_inner_operator_table_data = [
        {
            'ID': 333333222222111111,
            'role': '书籍操作员'
        }, {
            'ID': 111111222222333333,
            'role': '前台操作员'
        }
    ]
    tmp_user_operator_table_data = [{
            'ID': 999999888888777777,
            'name': '何小麦'
        }, {
            'ID': 777777888888999999,
            'name': '梁肖剑'
        }
    ]
    return HttpResponse(json.dumps({
        'innerOperatorTableData': tmp_inner_operator_table_data,
        'userTableData': tmp_user_operator_table_data
    }))

def create_operator(request):
    return HttpResponse(json.dumps({'loginStatus': 200}))

def delete_operator(request):
    return HttpResponse(json.dumps({'loginStatus': 200}))

def update_operator(request):
    return HttpResponse(json.dumps({'loginStatus': 200}))

def create_user(request):
    return HttpResponse(json.dumps({'loginStatus': 200}))

def delete_user(request):
    return HttpResponse(json.dumps({'loginStatus': 200}))

def update_user(request):
    return HttpResponse(json.dumps({'loginStatus': 200}))




#
# def get_borrow_status(request):
#     user = request.user
#     print user.username
#     # account = request.GET.get('account')
#     # print account
#     # query borrow_status and history_borrow_record by account
#     # some temporary example data
#     if request.user.is_authenticated():
#         print 'is authenticated'
#     else:
#         print 'not authenticated yet'
#     tmpBorrowTableData = [{
#             'ISBN': 111,
#             'bookName': 'borrow1',
#             'borrowDate': '22',
#             'returnDate': '2017-10-11'
#         },
#         {
#             'ISBN': 222,
#             'bookName': 'borrow2',
#             'borrowDate': '44',
#             'returnDate': '2017-10-25'
#         },
#         {
#             'ISBN': 333,
#             'bookName': 'borrow3',
#             'borrowDate': '55',
#             'returnDate': '2017-10-09'
#         }]
#     tmpHistoryTableData = [{
#             'ISBN': 111,
#             'bookName': 'history1',
#             'borrowDate': '22',
#             'returnDate': '2017-11-06'
#         },
#         {
#             'ISBN': 222,
#             'bookName': 'history2',
#             'borrowDate': '44',
#             'returnDate': '2017-11-04'
#         },
#         {
#             'ISBN': 333,
#             'bookName': 'history3',
#             'borrowDate': '55',
#             'returnDate': '2017-11-05'
#         }]
#
#     response = HttpResponse(json.dumps({
#         'borrowTableData': tmpBorrowTableData,
#         'historyTableData': tmpHistoryTableData
#     }))
#     response['access-Control-Allow-Origin'] = '127.0.0.1:8080'  # add it to prevent 'ACAO is not allow to be *'
#     response['Access-Control-Allow-Credentials'] = 'true'  # add it to prevent 'ACAC is not allow to be '',and should be *'
#     return response


def query_book(request):
    query_type = request.GET.get('query_type')
    query_keyword = request.GET.get('query_keyword')
    if query_keyword == '':  # user didn't input any keyword, use space to replace
        query_keyword = ' '
    # print query_type
    # print query_keyword == ''
    # print type(query_keyword)
    # search from database
    query_result = Query_book.query_book(query_type,query_keyword)
    print query_result
    book_list = []
    for book in query_result:
        tmp_book = {
            'ISBN': book.ISBN,
            'author': book.author,
            'publisher': book.publisher,
            'total_number': book.total_number,
            'left_number': book.left_number,
            'intro': book.intro,
            'title': book.title,
            'surface': book.surface
        }
        book_list.append(tmp_book)
    # mock data
    # book_list = [{
    #     'ISBN': 'isbn',
    #     'author': 'author',
    #     'publisher': 'publisher',
    #     'total_number': 20,
    #     'left_number': 13,
    #     'intro': 'this is a string of introduction',
    #     'title': 'book title',
    #     'surface': 'http://XXX/xxx.jpg'
    # },{
    #     'ISBN': 'isbn',
    #     'author': 'author',
    #     'publisher': 'publisher',
    #     'total_number': 20,
    #     'left_number': 13,
    #     'intro': 'this is a string of introduction',
    #     'title': 'book title',
    #     'surface': 'http://XXX/xxx.jpg'
    # }]
    return HttpResponse(json.dumps({'book_list': book_list}))


def logout(request):
    auth.logout(request)
    response = HttpResponse(json.dumps({'logoutStatus': 200}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response
