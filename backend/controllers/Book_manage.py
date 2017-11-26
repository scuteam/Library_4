# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
from backend.services import Book_manage


def create_book(request):
    book = request.GET.get('newBook')
    book = json.loads(book)
    print type(book)
    print book['ISBN']
    print book['author']
    print book['publisher']
    print book['total_number']
    print book['left_number']
    print book['intro']
    print book['title']
    print book['surface']
    print book['tag']
    # TODO: check tag if in tags table, if not, create one
    is_success = Book_manage.create(new_ISBN=book['ISBN'],
                       new_author=book['author'],
                       new_intro=book['intro'],
                       new_left_number=book['left_number'],
                       new_publisher=book['publisher'],
                       new_surface=book['surface'],
                       new_total_number=book['total_number'],
                       new_title=book['title'])
    if is_success:
        return HttpResponse(json.dumps({'createStatus': 200}))
    else:
        return HttpResponse(json.dumps({'createStatus': 500}))


def get_book_all():
    pass


def update_book():
    pass


def delete_book(request):
    book_list = request.GET.get('delete_book_list')
    book_list = json.loads(book_list)
    print type(book_list)

    # delete from database
    for book in book_list:
        print book  # {'bookAuthor': u'author', u'bookName': u'test_book', u'ISBN': u'1234567890123'}
        is_success = Book_manage.delete(book['ISBN'])
        if not is_success:
            response = HttpResponse(json.dumps({'deleteStatus': 500}))
            response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
            response['Access-Control-Allow-Credentials'] = 'true'
            return response
    response = HttpResponse(json.dumps({'deleteStatus': 200}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response


def get_book():
    pass

