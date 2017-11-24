# -*- coding: utf-8 -*-
from django.db import models

class Book(models.Model):
    ISBN = models.CharField(max_length=13, primary_key=True, db_column='ISBN')
    author = models.CharField(max_length=20, db_column='author')
    publisher = models.CharField(max_length=40, db_column='publisher')
    total_number = models.IntegerField(db_column='total_number')
    left_number = models.IntegerField(db_column='left_number')
    intro = models.CharField(max_length=10240, blank=True, db_column='intro')
    title = models.CharField(max_length=50, db_column='title')
    surface = models.CharField(max_length=40, db_column='surface')

    class Meta:
        db_table = 'book'  # 表名
        verbose_name = 'book'  # 在 Admin 界面显示的名称
        verbose_name_plural = 'books'  # 在 Admin 界面显示的名称的复数形式