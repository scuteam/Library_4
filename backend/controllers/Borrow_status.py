# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
from backend.services.Borrow_status import query

@login_required
def get_borrow_status(request):
    user = request.user
    print user.username
    if request.user.is_authenticated():
        print 'is authenticated'
    else:
        print 'not authenticated yet'
    tmpBorrowTableData,tmpHistoryTableData = query(user)
    response = HttpResponse(json.dumps({
        'borrowTableData': tmpBorrowTableData,
        'historyTableData': tmpHistoryTableData
    }))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'  # add it to prevent 'ACAO is not allow to be *'
    response['Access-Control-Allow-Credentials'] = 'true'  # add it to prevent 'ACAC is not allow to be '',and should be *'
    return response
