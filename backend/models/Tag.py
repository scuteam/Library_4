# -*- coding: utf-8 -*-
from django.db import models


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True, db_column='tag_id')
    tag_name = models.CharField(max_length=20, db_column='tag_name')

    class Meta:
        db_table = 'tag'  # 表名
        verbose_name = 'tag'  # 在 Admin 界面显示的名称
        verbose_name_plural = 'tags'  # 在 Admin 界面显示的名称的复数形式