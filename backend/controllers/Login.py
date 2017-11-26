# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
import json
from backend.services.Login import query_account_by_id


def verify_account(request):
    account = request.POST.get('account')
    password = request.POST.get('password')
    role = request.POST.get('role')
    print 'account:', account
    print 'password', password
    print 'role', role
    status = query_account_by_id(username=account, password=password, role=role)
    if status == -1:
        return HttpResponse(json.dumps({'loginStatus': 304, 'reason': 'name or role incorrect'}))
    elif status == 1:
        return HttpResponse(json.dumps({'loginStatus': 304, 'reason': 'name or password incorrect'}))
    else:
        user = authenticate(username=account, password=password)
        print type(user)
        login(request, user)
        response = HttpResponse(json.dumps({'loginStatus': 200}))
        response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response


