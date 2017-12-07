# -*- coding: utf-8 -*-
from backend.models import Book

def query_by_id(book_ISBN):
    query_result = []
    book = Book.objects.get(ISBN=book_ISBN)
    if book is None:
        return query_result
    query_result.append(book)
    return query_result

def query_by_author(book_author):
    query_result = []
    book = Book.objects.get(author=book_author)
    if book is None:
        return query_result
    query_result.append(book)
    return query_result

def query_by_publisher(book_publisher):
    query_result = []
    book = Book.objects.get(publisher=book_publisher)
    if book is None:
        return query_result
    query_result.append(book)
    return query_result

def query_by_name(book_name):
    query_result = []
    book = Book.objects.get(title=book_name)
    if book is None:
        return query_result
    query_result.append(book)
    return query_result

def query_all():
    query_result = []
    count = Book.objects.count()
    index = 10 if count >10 else count  # index = 10 or count
    print index
    book = Book.objects.order_by('?')[:index]  # 随机挑选 index 条记录返回
    for i in range(book.count()):
        query_result.append(book[i])
    return query_result