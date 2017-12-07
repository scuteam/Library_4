# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
from backend.services import Renew

@login_required()
def renew(request):
    user = request.user
    book_list = request.POST.get('renew_book_list')
    book_list = json.loads(book_list)
    fail_list = []
    for book in book_list:
        ISBN = book['ISBN']
        is_success = Renew.renew(user,ISBN)
        if not is_success:
            fail_list.append(book)
    renew_status = 200
    if len(fail_list) != 0:
        renew_status = 304
    response = HttpResponse(json.dumps({'renewStatus': renew_status, 'fail_list': fail_list}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response