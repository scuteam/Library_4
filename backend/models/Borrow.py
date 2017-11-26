# -*- coding: utf-8 -*-
from django.db import models
from User import User
from Book import Book


class Borrow(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    right = models.CharField(max_length=20, unique=True, db_column='right')

    class Meta:
        db_table = 'permission'  # 表名
        verbose_name = 'permission'  # 在 Admin 界面显示的名称
        verbose_name_plural = 'permissions'  # 在 Admin 界面显示的名称的复数形式