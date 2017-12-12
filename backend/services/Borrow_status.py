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

#should return
    # {
    #     'ISBN': 111,
    #     'bookName': 'borrow1',
    #     'borrowDate': '22',
    #     'returnDate': '2017-10-11'
    # }