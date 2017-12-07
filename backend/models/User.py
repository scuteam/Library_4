# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, UserManager
from Role import Role

class User(User):
    borrower_available = models.IntegerField(default=15, db_column='borrower_available')  # borrower_available or borrow_available? default=15?
    name = models.CharField(default='', max_length=20, db_column='name')
    role = models.ForeignKey(Role, db_column='role')
    objects = UserManager()

    class Meta:
        db_table = 'user'  # 表名
        verbose_name = 'user'  # 在 Admin 界面显示的名称
        verbose_name_plural = 'users'  # 在 Admin 界面显示的名称的复数形式