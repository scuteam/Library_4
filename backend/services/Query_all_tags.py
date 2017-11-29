# -*- coding: utf-8 -*-
from backend.models import Tag

def query_all_tags():
    tag_list = []
    tags = Tag.objects.all()
    for tag in tags:
        print tag.tag_name
        tag_list.append(tag.tag_name)
    return tag_list