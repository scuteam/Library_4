# -*- coding: utf-8 -*-

import time
from datetime import datetime
from datetime import timedelta
from backend.models import Book
from backend.models import Borrow

def renew(user,ISBN):
    book = Book.objects.get(ISBN=ISBN)
    if book is None:
        return
    b = Borrow.objects.get(user=user,book=book)
    if b.renew_number == 1:
        b.renew_number = 0
        b.return_date = b.return_date + timedelta(15)  # maybe error
        b.save()
        return True
    return False


    #"""还有个问题,如果该用户第一天借了A书,第二天还了,第三天又借了,续期,
    # Borrow.objects.get(user=user,book=book)有可能返回第一次的记录,续的是第一次,不符,
    #
    #
    # """