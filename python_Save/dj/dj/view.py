from django.http import HttpResponse , Http404
from django.shortcuts import render
import datetime


def hello(request):
    context = {}
    return render(request, 'gos2.html', context)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    return render(request,'as.html',{'date':dt})