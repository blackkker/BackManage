# encoding: utf-8
__author__ = 'black'
__date__ = '2018/7/30 17:10'
from  django.shortcuts import render


def index(request):
    return render(request, 'index.html')