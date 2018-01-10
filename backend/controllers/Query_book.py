# -*- coding: utf-8 -*-
from backend.services import Query_book

def query_book(query_type, query_keyword):
    book_list = []
    if query_keyword.isspace():
        print 'is space'
        book_list = Query_book.query_all()
        return book_list
    print 'not space'
    if query_type == 'bookISBN':
        book_list = Query_book.query_by_ISBN(query_keyword)
    elif query_type == 'bookName':
        book_list = Query_book.query_by_name(query_keyword)
    elif query_type == 'bookPublisher':
        book_list = Query_book.query_by_publisher(query_keyword)
    elif query_type == 'bookAuthor':
        book_list = Query_book.query_by_author(query_keyword)
    return book_list

