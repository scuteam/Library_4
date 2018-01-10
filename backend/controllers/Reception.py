from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
from backend.services.Borrow_status import query
from backend.services.Reception import borrow
from backend.services.Reception import return_book_
from backend.services.User_manage import get

def query_borrow_status(request):
    print 'service start'
    type = request.POST.get('userInfoType')
    info = request.POST.get('userInfo')
    user = get(type, info)
    if user == None:
        response = HttpResponse(json.dumps({'getStatus': 304, 'reason': 'no user error'}))
        response['access-Control-Allow-Origin'] = '127.0.0.1:8080'  # add it to prevent 'ACAO is not allow to be *'
        response['Access-Control-Allow-Credentials'] = 'true'  # add it to prevent 'ACAC is not allow to be '',and should be *'
        return response
    tmpBorrowTableData, tmpHistoryTableData = query(user)
    response = HttpResponse(json.dumps({
        'borrowTableData': tmpBorrowTableData,
        'historyTableData': tmpHistoryTableData,
        'userId': user[0].username
    }))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'  # add it to prevent 'ACAO is not allow to be *'
    response[
        'Access-Control-Allow-Credentials'] = 'true'  # add it to prevent 'ACAC is not allow to be '',and should be *'
    return response

def borrow_book(request):
    userId = request.POST.get('userId')
    bookISBN = request.POST.get('bookISBN')
    if request.user.is_authenticated():
        print 'is authenticated'
    else:
        print 'not authenticated yet'
    user = get('id', userId)
    if user == None:
        response = HttpResponse(json.dumps({'borrowStatus': 304, 'reason': 'no user error'}))
        response['access-Control-Allow-Origin'] = '127.0.0.1:8080'  # add it to prevent 'ACAO is not allow to be *'
        response[
            'Access-Control-Allow-Credentials'] = 'true'  # add it to prevent 'ACAC is not allow to be '',and should be *'
        return response
    isSuccess = borrow(user, bookISBN)
    if isSuccess == None:
        response = HttpResponse(json.dumps({'borrowStatus': 304, 'reason': 'ISBN error'}))
    else:
        response = HttpResponse(json.dumps({'borrowStatus': 200}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'  # add it to prevent 'ACAO is not allow to be *'
    response['Access-Control-Allow-Credentials'] = 'true'  # add it to prevent 'ACAC is not allow to be '',and should be *'
    return response

def return_book(request):
    userId = request.POST.get('userId')
    bookISBN = request.POST.get('bookISBN')
    if request.user.is_authenticated():
        print 'is authenticated'
    else:
        print 'not authenticated yet'
    user = get('id', userId)
    if user == None:
        response = HttpResponse(json.dumps({'returnStatus': 304, 'reason': 'no user error'}))
        response['access-Control-Allow-Origin'] = '127.0.0.1:8080'  # add it to prevent 'ACAO is not allow to be *'
        response[
            'Access-Control-Allow-Credentials'] = 'true'  # add it to prevent 'ACAC is not allow to be '',and should be *'
        return response
    isSuccess = return_book_(user, bookISBN)
    if isSuccess == None:
        response = HttpResponse(json.dumps({'returnStatus': 304, 'reason': 'ISBN error'}))
    else:
        response = HttpResponse(json.dumps({'returnStatus': 200}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'  # add it to prevent 'ACAO is not allow to be *'
    response['Access-Control-Allow-Credentials'] = 'true'  # add it to prevent 'ACAC is not allow to be '',and should be *'
    return response