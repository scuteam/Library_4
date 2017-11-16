# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def login(request):
    print request.GET.get('account')
    # account = request.GET.get('account')
    # password = request.GET.get('password')
    # role = request.GET.get('role')
    # print account + password + role
    return HttpResponse('Hello world')
