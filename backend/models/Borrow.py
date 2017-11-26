# -*- coding: utf-8 -*-
from django.db import models
import time
from datetime import datetime
from datetime import timedelta
from User import User
from Book import Book


class Borrow(models.Model):
    user = models.ForeignKey(User, db_column='user_id')
    book = models.ForeignKey(Book, db_column='ISBN')
    # 初次建立时调用系统时间,创建时不用指定,修改时要指定
    borrow_date = models.DateField(default=datetime.now(), db_column='borrow_date')
    # 初次建立时不用指明
    return_date = models.DateField(default=datetime.now()+timedelta(15), db_column='return_date')
    # 借了几本该ISBN的书,创建数据库要指定默认值,此处为1,代码创建时要指定一定要注意
    number = models.IntegerField(default=1, db_column='number')
    # 改为renew_time比较好吧?
    renew_number = models.IntegerField(default=1, db_column='renew_number')

    class Meta:
        db_table = 'borrow'  # 表名
        verbose_name = 'borrow'  # 在 Admin 界面显示的名称
        verbose_name_plural = 'borrow'  # 在 Admin 界面显示的名称的复数形式
        unique_together = ('user', 'book')