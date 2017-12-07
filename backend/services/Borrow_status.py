# -*- coding: utf-8 -*-
from datetime import timedelta
from backend.models import Borrow
from backend.models import Book
from datetime import datetime

def query(user):
    borrow_table_data = []
    history_table_data = []
    query_result = Borrow.objects.filter(user=user)  # 返回的是符合条件的书籍的Query_set
    for b in query_result:
        book = {
            'ISBN': b.book.ISBN,
            'bookName': b.book.title,
            'borrowDate': b.borrow_date.strftime('%Y-%m-%d'),
            'returnDate': b.return_date.strftime('%Y-%m-%d')
        }
        print book
        if b.return_date == b.borrow_date + timedelta((2 - b.renew_number) * 15):  # 等于,说明还没还
            borrow_table_data.append(book)
        else:
            #if len(history_table_data) < 10:  # 只返回前十本
            history_table_data.append(book)
    return borrow_table_data, history_table_data

def borrow(user, bookISBN):

    book = Book.objects.get(ISBN=bookISBN)
    if book == None:
        print 'no Such book has ISBN: '+bookISBN
        return None
    newBorrow = Borrow.objects.create(user = user[0], book = book)
    book.left_number -= 1
    book.save()
    newBorrow.save()
    return True

def returnBook(user, bookISBN):
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

#should return
    # {
    #     'ISBN': 111,
    #     'bookName': 'borrow1',
    #     'borrowDate': '22',
    #     'returnDate': '2017-10-11'
    # }