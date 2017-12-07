# -*- coding: utf-8 -*-
from backend.models import User
from backend.models import Role
from django.db.models import Q


def get_all():
    print "inner_operator get_all method in services"
    operators = []
    book_manage = Role.objects.filter(appellation='bookManage')
    reception = Role.objects.filter(appellation='reception')
    if not book_manage:
        return
    if not reception:
        return
    book_manage = Role.objects.get(appellation='bookManage')
    reception = Role.objects.get(appellation='reception')
    results = User.objects.filter(Q(role=book_manage) | Q(role=reception))
    for result in results:
        operator = {
            'ID': result.username,
            'role': result.role.appellation,
            'name': result.name
        }
        operators.append(operator)
    return operators


def create(account, role, password, name):
    print 'create invoked'
    print 'account', account
    print 'role',role
    print 'password', password
    check_account = User.objects.filter(username=account)
    print 'check_account', check_account
    if check_account:
        return -1      #账号已存在
    check_role = Role.objects.filter(appellation=role)
    print 'check_role', check_role
    if not check_role:
        return -2      #角色不存在
    role = Role.objects.get(appellation=role)
    inner_operator = User.objects.create_user(username=account, password=password, role=role, name=name)
    inner_operator.save()
    return 0           #创建成功


def update(ID, role):
    check_ID = User.objects.filter(username=ID)
    if not check_ID:
        return -1          #账号不存在
    check_role = Role.objects.filter(appellation=role)
    if not check_role:
        return -2          #角色不存在
    role = Role.objects.get(appellation=role)
    user = User.objects.get(username=ID)
    user.role = role
    user.save()
    return 0


def delete(ID):
    check_ID = User.objects.filter(username=ID)
    if not check_ID:
        return -1  # 账号不存在
    user = User.objects.get(username=ID)
    user.delete()
    return 0