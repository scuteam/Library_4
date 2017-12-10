# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os
import os.path
import json
from backend.models import Tag
from backend.models import Has_tag
from backend.services import Book_manage
from backend.services import Query_all_tags

@login_required
def create_book(request):
    ISBN = request.POST.get('ISBN')
    author = request.POST.get('author')
    publisher = request.POST.get('publisher')
    total_number = request.POST.get('total_number')
    left_number = request.POST.get('left_number')
    intro = request.POST.get('intro')
    title = request.POST.get('title')
    tags = request.POST.get('tag')
    surface = ''
    print ISBN,author,publisher,total_number,left_number,intro,title
    # for surface img
    dir = 'static/image/'
    # print os.listdir()
    list = os.listdir(dir)
    # print list
    # create path
    for line in list:
        file_path = os.path.join(dir,line)
        if os.path.isfile(file_path):
            if line.startswith(ISBN):
                surface = '/static/image/'+line
    if surface == '':
        surface = '/static/image/default.jpg'
    # create book
    book = Book_manage.create(new_ISBN=ISBN,
                              new_author=author,
                              new_intro=intro,
                              new_left_number=left_number,
                              new_publisher=publisher,
                              new_surface=surface,
                              new_total_number=total_number,
                              new_title=title)
    if book is None:
        response = HttpResponse(json.dumps({'createStatus': 500}))
        response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response

    # create tag
    print tags
    print type(tags)
    tags = json.loads(tags)
    total_tags = Query_all_tags.query_all_tags()
    for tag in tags:
        if tag not in total_tags:
            t = Tag.objects.create(tag_name=tag)
        else:
            t = Tag.objects.get(tag_name=tag)
        Has_tag.objects.create(book=book,tag=t)

    response = HttpResponse(json.dumps({'createStatus': 200}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response

@login_required
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


def upload_book_surface(request):
    print 'call this function'
    file = request.FILES.get('file')
    print file
    with open("static/image/%s" % file.name, 'wb+') as f:
        # 分块写入文件
        for chunk in file.chunks():
            f.write(chunk)
    print 'write over'
    response = HttpResponse(json.dumps({'uploadStatus': 200}))
    response['access-Control-Allow-Origin'] = '127.0.0.1:8080'
    response['Access-Control-Allow-Credentials'] = 'true'
    return response
    #return HttpResponse("upload over!")