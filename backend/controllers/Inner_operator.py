# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
from backend.services.Inner_operator import create, get_all, update, delete


def get_all_operator(request):
    print "inner_operator get_all_operator method in controllers"
    operators = get_all()
    response = HttpResponse(json.dumps({
        'innerOperatorTableData': operators
    }))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response


def create_operator(request):
    account = request.POST.get('account')
    role = request.POST.get('role')
    password = request.POST.get('password')
    name = request.POST.get('name')
    status = create(account, role, password, name)
    reason = ''
    if status == -2:
        createStatus = 304
        reason = '角色不存在'
    elif status == -1:
        createStatus = 304
        reason = '账号已存在'
    else:
        createStatus = 200
    response = HttpResponse(json.dumps({'createStatus': createStatus, 'reason': reason}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response


def update_operator(request):
    ID = request.POST.get('account')
    role = request.POST.get('role')
    status = update(ID=ID, role=role)
    reason = ''
    if status == -2:
        updateStatus = 304
        reason = '角色不存在'
    elif status == -1:
        updateStatus = 304
        reason = '账号不存在'
    else:
        updateStatus = 200
    response = HttpResponse(json.dumps({'updateStatus': updateStatus, 'reason': reason}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response


def delete_operator(request):
    operatorList = request.POST.get('delete_operator_list')
    operatorList = json.loads(operatorList)
    deleteStatus = 200
    reason = ''
    for operator in operatorList:
        ID = operator['ID']
        status = delete(ID)
        if status == -1:
            deleteStatus = 304
            reason = "账号不存在"
            break
    response = HttpResponse(json.dumps({'deleteStatus': deleteStatus, 'reason': reason}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response





