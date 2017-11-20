from django.conf.urls import url
# from django.contrib import admin
# from django.conf.urls import include
from views import verify_account
from views import get_borrow_status
urlpatterns = [
    url(r'^verify_account/', verify_account),
    url(r'^get_borrow_status/', get_borrow_status)
]