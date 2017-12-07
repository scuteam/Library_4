# -*- coding: utf-8 -*-
from backend.models import Book
from backend.models import Has_tag

def query_by_ISBN(book_ISBN):
    query_result = []
    books = Book.objects.filter(ISBN=book_ISBN)
    for book in books:
        tags = Has_tag.objects.filter(book = book)
        book.tags = []
        for tag in tags:
            book.tags.append(tag.tag.tag_name)
        query_result.append(book)
    return query_result

def query_by_author(book_author):
    query_result = []
    books = Book.objects.filter(author=book_author)
    for book in books:
        tags = Has_tag.objects.filter(book = book)
        book.tags = []
        for tag in tags:
            book.tags.append(tag.tag.tag_name)
        query_result.append(book)
    return query_result

def query_by_publisher(book_publisher):
    query_result = []
    books = Book.objects.filter(publisher=book_publisher)
    for book in books:
        tags = Has_tag.objects.filter(book=book)
        book.tags = []
        for tag in tags:
            book.tags.append(tag.tag.tag_name)
        query_result.append(book)
    return query_result

def query_by_name(book_name):
    query_result = []
    books = Book.objects.filter(title=book_name)
    for book in books:
        tags = Has_tag.objects.filter(book=book)
        book.tags = []
        for tag in tags:
            book.tags.append(tag.tag.tag_name)
        query_result.append(book)
    return query_result

def query_all():
    query_result = []
    count = Book.objects.count()
    #index = 10 if count >10 else count  # index = 10 or count
    #print index
    books = Book.objects.order_by('?')[:count]  # 随机挑选 index 条记录返回
    for book in books:
        tags = Has_tag.objects.filter(book=book)
        book.tags = []
        for tag in tags:
            book.tags.append(tag.tag.tag_name)
        query_result.append(book)
    return query_result