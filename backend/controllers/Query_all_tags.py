# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
from backend.services import Query_all_tags

def query_all_tags(request):
    tags = Query_all_tags.query_all_tags()
    response = HttpResponse(json.dumps({'tags': tags}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response