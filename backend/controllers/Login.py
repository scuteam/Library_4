# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
from backend.services.Login import query_account_by_id


def verify_account(request):
    account = request.POST.get('account')
    password = request.POST.get('password')
    role = request.POST.get('role')
    print 'account:',account
    print 'password',password
    print 'role',role
    status = query_account_by_id(username=account,password=password,role=role)
    if status == -1:
        return HttpResponse(json.dumps({'loginStatus': 304, 'reason': 'name or role incorrect'}))
    elif status == 1:
        return HttpResponse(json.dumps({'loginStatus': 304, 'reason': 'name or password incorrect'}))
    else:
        return HttpResponse(json.dumps({'loginStatus': 200}))


