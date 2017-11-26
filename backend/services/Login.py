# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate
import json
from backend.models import User
from backend.models import Role

def query_account_by_id(username,password,role):
    r = Role.objects.get(appellation=role)
    check_role = User.objects.get(username=username,role=r)
    if not check_role:
        print 'user did not has such role'
        return -1
    user = authenticate(username=username,password=password)
    if user is None:
        print 'password is wrong'
        return 1
    else:
        print 'password is right'
        return 0