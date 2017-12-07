# -*- coding: utf-8 -*-
from django.db import models


class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True, db_column='permission_id')
    right = models.CharField(max_length=20, unique=True, db_column='right')

    class Meta:
        db_table = 'permissions'  # 表名 permission 已经存在??  加了个s
        verbose_name = 'permission'  # 在 Admin 界面显示的名称
        verbose_name_plural = 'permissions'  # 在 Admin 界面显示的名称的复数形式