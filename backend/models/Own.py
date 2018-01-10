# -*- coding: utf-8 -*-
from django.db import models
from Role import Role
from Permission import Permission

class Own(models.Model):
    role = models.ForeignKey(Role, db_column='role')
    permission = models.ForeignKey(Permission, db_column='permission')

    class Meta:
        db_table = 'role_permission_r'  # 表名
        verbose_name = 'own'  # 在 Admin 界面显示的名称
        verbose_name_plural = 'own'  # 在 Admin 界面显示的名称的复数形式
        unique_together = ('role', 'permission')  # 在此处设置