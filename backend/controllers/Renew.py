# -*- coding: utf-8 -*-
from django.http import HttpResponse

import json
import time
from datetime import datetime
from datetime import timedelta

from backend.services import Renew

def renew(request):
    book_list = request.POST.get('renew_book_list')
    book_list = json.loads(book_list)
    print type(book_list)
    for book in book_list:
        print book
        date = time.strptime(book['returnDate'], "%Y-%m-%d")
        date = datetime(* date[:6])
        renew_date = date + timedelta(days=15)
        print renew_date
        renew_date = datetime.timetuple(renew_date)
        str_date = time.strftime("%Y-%m-%d", renew_date)
        book['returnDate'] = str_date
    # renew from database
    for book in book_list:
        ISBN = book['ISBN']
        Renew.renew(ISBN)
    # return HttpResponse(json.dumps({'renewStatus': 200, 'new_book_list': book_list}))
    return HttpResponse(json.dumps({'renewStatus': 200}))