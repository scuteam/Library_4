# views.py
from django.http import HttpResponse


def add(request):
    print "Hello django"
    return HttpResponse("Hello django")