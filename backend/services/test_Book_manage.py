# -*- coding: utf-8 -*-
from Book_manage import create

def test_create():
    new_ISBN = '1234567890123'
    new_author = 'author'
    new_publisher = 'publisher'
    new_total_number = 20
    new_left_number = 20
    new_intro = """this is a long message"""
    new_title = 'test_book'
    new_surface = 'http://XXX.yy.com/aa.jpg'
    create(new_ISBN,new_author,new_publisher,
           new_total_number,new_left_number,
           new_intro,new_title,new_surface)

if '__name__' == '__main__':
    test_create()