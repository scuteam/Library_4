# -*- coding: utf-8 -*-
from django.db import models
from Book import Book
from Tag import Tag


class Has_tag(models.Model):
    # """django 中不允许两列主键的存在,所以采用'复合主键'来代替,
    # 默认另外生成的id作为主键,设置unique_together为所需主键
    # 这种只是权宜之计
    # tag,book要不要改为tag_id,ISBN?
    # 在数据库表设计的时候是tag_id,ISBN,但在代码中使用Has_tag时,tag_id和ISBN表述不清
    # 比如:获取一本书所有tag的tag_name
    # book = Book.objects.get(ISBN='XXXXXXXXXXXXX')
    # has_tag = Has_tag.objects.get(book=book)
    # has_tag.tag.tag_name
    # 如果沿用数据库的名字
    # has_tag = Has_tag.objects.get(ISBN=book)
    # has_tag.tag_id.tag_name
    # 表述比较奇怪,不方便阅读理解"""
    tag = models.ForeignKey(Tag, db_column='tag_id')  # 复合主键,不在此处设置primary_key
    book = models.ForeignKey(Book, db_column='ISBN')  # 复合主键,不在此处设置primary_key

    class Meta:
        db_table = 'book_tag_r'  # 表名
        verbose_name = 'has_tag'  # 在 Admin 界面显示的名称
        verbose_name_plural = 'has_tag'  # 在 Admin 界面显示的名称的复数形式
        unique_together = ('tag', 'book')  # 在此处设置
