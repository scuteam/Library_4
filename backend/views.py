# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.http import HttpResponse
import json
from backend.controllers import Query_book
def query_book(request):
    query_type = request.GET.get('query_type')
    query_keyword = request.GET.get('query_keyword')
    print query_type, query_keyword
    if query_keyword == '':  # user didn't input any keyword, use space to replace
        query_keyword = ' '
    query_result = Query_book.query_book(query_type,query_keyword)
    print query_result
    book_list = []
    for book in query_result:
        tmp_book = {
            'ISBN': book.ISBN,
            'author': book.author,
            'publisher': book.publisher,
            'total_number': book.total_number,
            'left_number': book.left_number,
            'intro': book.intro,
            'title': book.title,
            'surface': book.surface,
            'tags': book.tags
        }
        book_list.append(tmp_book)
    # mock data
    # book_list = [{
    #     'ISBN': 'isbn',
    #     'author': 'author',
    #     'publisher': 'publisher',
    #     'total_number': 20,
    #     'left_number': 13,
    #     'intro': 'this is a string of introduction',
    #     'title': 'book title',
    #     'surface': 'http://XXX/xxx.jpg'
    # },{
    #     'ISBN': 'isbn',
    #     'author': 'author',
    #     'publisher': 'publisher',
    #     'total_number': 20,
    #     'left_number': 13,
    #     'intro': 'this is a string of introduction',
    #     'title': 'book title',
    #     'surface': 'http://XXX/xxx.jpg'
    # }]
    response = HttpResponse(json.dumps({'book_list': book_list}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response


def logout(request):
    auth.logout(request)
    response = HttpResponse(json.dumps({'logoutStatus': 200}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response