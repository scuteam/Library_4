# -*- coding: utf-8 -*-

import time
from datetime import datetime
from datetime import timedelta
from backend.models import Book
from backend.models import Borrow

def renew(user,ISBN):
    book = Book.objects.get(ISBN=ISBN)
    if book is None:
        return False  # 图书馆里没有该书
    query_result = Borrow.objects.filter(user=user,book=book)  # 返回的是符合条件的书籍的Query_set
    for b in query_result:
        if b.return_date == b.borrow_date + timedelta((2-b.renew_number)*15):  # 等于,说明还没还
            if b.renew_number == 1:  # 如果还可以续期
                b.renew_number = 0
                b.return_date = b.return_date + timedelta(15)
                b.save()
                return True
            else:
                print '续期次数已达到最大'
        else:
            print '这本书已经还了,不是待续期的那本'
    return False