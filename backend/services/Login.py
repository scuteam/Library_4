# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from backend.models import User
from backend.models import Role

def query_account_by_id(username,password,role):
    try:
        r = Role.objects.get(appellation=role)
        check_role = User.objects.get(username=username,role=r)
    except ObjectDoesNotExist:
        print 'user and role not fit'
        return -1
    user = authenticate(username=username,password=password)
    if user is None:
        print 'password is wrong'
        return 1
    else:
        print 'password is right'
        return 0