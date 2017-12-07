# -*- coding: utf-8 -*-
from backend.models import User
from backend.models import Role

def get_all():
    print "user get_all method in services"
    users = []
    user = Role.objects.get(appellation='user')
    results = User.objects.filter(role=user)
    for result in results:
        user = {
            'ID': result.username,
            'name': result.name
        }
        users.append(user)
    return users

def get_by_id(id):
    user = User.objects.filter(username=id)
    if user.__len__()==0:
        return None
    return user

def get_by_name(name):
    user =User.objects.filter(name=name)
    if user.__len__()==0:
        return None
    return user

def get(type, info):
    print "user get_all method in services"
    switcher = {
        'id': get_by_id,
        'name': get_by_name
    }
    func = switcher.get(type, lambda : None)
    user = func(info)
    return user

def create(account,name,password):
    print 'create invoked'
    print 'account', account
    print 'name', name
    print 'password', password
    check_account = User.objects.filter(username=account)
    if check_account:
        return -1      #账号已存在
    user = Role.objects.get(appellation='user')
    user = User.objects.create_user(username=account, password=password, name=name, role=user)
    user.save()
    return 0           #创建成功


def update(account, name):
    pass


def delete(account):
    check_account = User.objects.filter(username=account)
    if not check_account:
        return -1  # 账号不存在
    user = User.objects.get(username=account)
    user.delete()
    return 0