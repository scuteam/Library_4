# -*- coding: utf-8 -*-
from django.db import models


class Role(models.Model):
    role_id = models.AutoField(primary_key=True, db_column='role_id')
    appellation = models.CharField(max_length=20, unique=True, db_column='appellation')

    class Meta:
        db_table = 'role'  # 表名
        verbose_name = 'role'  # 在 Admin 界面显示的名称
        verbose_name_plural = 'roles'  # 在 Admin 界面显示的名称的复数形式