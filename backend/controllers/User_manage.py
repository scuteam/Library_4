# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
from backend.services.User_manage import get_all, create, update, delete


def get_all_user(request):
    print "user get_all_user method in controllers"
    users = get_all()
    response = HttpResponse(json.dumps({
        'userTableData': users
    }))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response


def create_user(request):
    account = request.POST.get('ID')
    name = request.POST.get('name')
    password = request.POST.get('password')
    status = create(account, name, password)
    reason = ''
    if status == -1:
        createStatus = 304
        reason = "账号已存在"
    else:
        createStatus = 200
    response = HttpResponse(json.dumps({'createStatus': createStatus, 'reason': reason}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response


def delete_user(request):
    userList = request.POST.get('delete_user_list')
    userList = json.loads(userList)
    deleteStatus = 200
    reason = ''
    for user in userList:
        account = user['ID']
        status = delete(account)
        if status == -1:
            deleteStatus = 304
            reason = '账号不存在'
            break
    response = HttpResponse(json.dumps({'deleteStatus': deleteStatus, 'reason': reason}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response


def update_user(request):
    pass

