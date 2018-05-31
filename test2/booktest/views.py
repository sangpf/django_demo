#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max,Min,F,Q
from models import *
from datetime import *

def index(request):
    # list = BookInfo.books1.all()
    # list = BookInfo.books1.filter(heroinfo__hcontent__contains='六')
    # list = BookInfo.books1.filter(pk__gte=3)
    Max1 = BookInfo.books1.aggregate(Max('bpub_date'))
    Min1 = BookInfo.books1.aggregate(Min('bpub_date'))
    list = BookInfo.books1.filter(bread__gt=F('bcommet'))
    # list = BookInfo.books1.filter(pk__lt=4,btitle__contains='1')
    # list = BookInfo.books1.filter(pk__lt=4).filter(btitle__contains='1')
    # list = BookInfo.books1.filter(Q(pk__lt=4)|Q(btitle__contains='1'))
    context = {'list1':list ,'Max1':Max1 , 'Min1':Min1}
    return render(request,'booktest/index.html', context)

def add(request):
    # 使用类方法新增
    # book = BookInfo.create("python开发指南", datetime(1980, 10, 11))
    # book.save()

    # 使用管理器新增
    book2 = BookInfo.books2.create("走你呵呵呵", datetime(2001, 10, 11))
    book2.save()

    return HttpResponse('ok')




