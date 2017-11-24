# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
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

def query_all_tags(request):
    # mock data
    tags = ['tag1', 'tag2', 'tag3', 'tag4', 'tag5']
    return HttpResponse(json.dumps({'tags': tags}))

def renew(request):
    book_list = request.GET.get('renew_book_list')
    book_list = json.loads(book_list)
    print type(book_list)
    for book in book_list:
        print book
        # TODO: add 15 days to the returnDate
    # renew from database
    return HttpResponse(json.dumps({'renewStatus': 200}))