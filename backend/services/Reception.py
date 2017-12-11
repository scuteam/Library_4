# -*- coding: utf-8 -*-
from datetime import timedelta
from backend.models import Borrow
from backend.models import Book
from datetime import datetime

def borrow(user, bookISBN):

    book = Book.objects.get(ISBN=bookISBN)
    if book == None:
        print 'no Such book has ISBN: '+bookISBN
        return None
    if book.left_number -1 < 0:
        return None
    newBorrow = Borrow.objects.create(user = user[0], book = book)
    book.left_number -= 1
    book.save()
    newBorrow.save()
    return True

def return_book(user, bookISBN):
    book = Book.objects.get(ISBN=bookISBN)
    book.left_number+=1
    borrow = Borrow.objects.filter(user = user, book = book)
    if borrow == None:
        print 'no Such borrow has ISBN: ' + bookISBN
        return None
    for b in borrow:
        if b.return_date == b.borrow_date + timedelta((2 - b.renew_number) * 15):  # 等于,说明还没还
            b.return_date = datetime.now()
            b.save()
            book.save()
            return True
    return None
