# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
from backend.services import Query_all_tags

def query_all_tags(request):
    tags = Query_all_tags.query_all_tags()
    return HttpResponse(json.dumps({'tags': tags}))