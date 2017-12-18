# -*- coding: utf-8 -*-
import sys, os, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 把manage.py所在目录添加到系统目录
django.setup()
from datetime import datetime
from datetime import timedelta
from backend.models import User
from backend.models import Role
from backend.models import Book
from backend.models import Tag
from backend.models import Has_tag
from backend.models import Borrow

# user = Role.objects.create(appellation='user')
# bookManager = Role.objects.create(appellation='bookManager')
user = Role.objects.get(appellation='user')
bookManager = Role.objects.get(appellation='bookManager')
admin = Role.objects.get(appellation='admin')
reception = Role.objects.get(appellation='reception')

user1 = User.objects.create_user(username='023456789012345678',password='user',borrower_available=15,name='user1',role=user)
user2 = User.objects.create_user(username='023456789012345679',password='bookManager',borrower_available=15,name='user2',role=bookManager)
user3 = User.objects.create_user(username='023456789012345680',password='admin',borrower_available=15,name='user3',role=admin)
user4 = User.objects.create_user(username='023456789012345681',password='reception',borrower_available=15,name='user4',role=reception)

book = Book.objects.create(ISBN='0111111111111',publisher='aaa',total_number=20,left_number=20,intro='this is a book',title='book1',surface='/static/11111111111.jpg',author='author1')

tag1 = Tag.objects.create(tag_name='tag3')
tag2 = Tag.objects.create(tag_name='tag4')

Has_tag.objects.create(book=book,tag=tag1)
Has_tag.objects.create(book=book,tag=tag2)

Borrow.objects.create(user=user1,book=book)
Borrow.objects.create(user=user2,book=book)
Borrow.objects.create(user=user3,book=book)
Borrow.objects.create(user=user4,book=book)

Borrow.objects.create(user=user1,book=book,return_date=datetime.now()+timedelta(5),number=2,renew_number=0)