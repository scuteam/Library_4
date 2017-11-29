from django.conf.urls import url
# from django.contrib import admin
# from django.conf.urls import include
from controllers.Login import verify_account
from controllers.Borrow_status import get_borrow_status
from views import query_book
from views import logout
from controllers.Query_all_tags import query_all_tags
from controllers.Book_manage import create_book
from controllers.Book_manage import delete_book
from controllers.Book_manage import upload_book_surface
from controllers.Renew import renew
urlpatterns = [
    url(r'^verify_account/', verify_account),
    url(r'^logout/',logout),
    url(r'^get_borrow_status/', get_borrow_status),
    url(r'^query_book/', query_book),
    url(r'^query_all_tags/', query_all_tags),
    url(r'^create_book/', create_book),
    url(r'^delete_book/', delete_book),
    url(r'^upload_book_surface', upload_book_surface),
    url(r'^renew/', renew),
]