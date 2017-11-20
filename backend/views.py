# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json

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
    pass