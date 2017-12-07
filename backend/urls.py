from django.conf.urls import url
# from django.contrib import admin
# from django.conf.urls import include
from controllers.Login import verify_account
from controllers.Borrow_status import get_borrow_status, get_borrow_status_by_userInfo,borrow_book ,return_book
from views import query_book
from views import logout
from controllers.Query_all_tags import query_all_tags
from controllers.Book_manage import create_book, delete_book
from controllers.Book_manage import upload_book_surface
from controllers.Renew import renew

from controllers.Inner_operator import get_all_operator, create_operator, delete_operator, update_operator
from controllers.User_manage import get_all_user, create_user, delete_user, update_user
urlpatterns = [
    url(r'^verify_account/', verify_account),
    url(r'^logout/',logout),
    url(r'^get_borrow_status/', get_borrow_status),
    url(r'^get_borrow_status_by_userInfo/', get_borrow_status_by_userInfo),
    url(r'^borrow_book/', borrow_book),
    url(r'^return_book/', return_book),
    url(r'^query_book/', query_book),
    url(r'^query_all_tags/', query_all_tags),
    url(r'^create_book/', create_book),
    url(r'^delete_book/', delete_book),
    url(r'^upload_book_surface', upload_book_surface),
    url(r'^renew/', renew),
    url(r'^get_all_operator', get_all_operator),
    url(r'^create_operator', create_operator),
    url(r'^delete_operator', delete_operator),
    url(r'^update_operator', update_operator),
    url(r'^get_all_user', get_all_user),
    url(r'^create_user', create_user),
    url(r'^delete_user', delete_user),
    url(r'^update_user', update_user),
    url(r'^upload_book_surface', upload_book_surface),
    url(r'^renew/', renew),
]