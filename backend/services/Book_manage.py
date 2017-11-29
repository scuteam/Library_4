# -*- coding: utf-8 -*-
from backend.models import Book

def create(new_ISBN,new_author,new_publisher,
           new_total_number,new_left_number,
           new_intro,new_title,new_surface):
    # TODO: check type
    book = Book.objects.create(ISBN=new_ISBN,
                               author=new_author,
                               publisher=new_publisher,
                               total_number=new_total_number,
                               left_number=new_left_number,
                               intro=new_intro,
                               title=new_title,
                               surface=new_surface)
    book.save()
    # TODO: add tag
    return True

def get_all():
    pass

def update():
    pass

def delete(ISBN):
    book = Book.objects.get(ISBN=ISBN)
    if book is None:
        print 'no such book'
        return False
    print book
    # book.delete()
    return True

def get():
    pass