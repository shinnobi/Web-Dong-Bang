# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse ("Hello, world you are at polls index")

def detail(request, question_id):
    return HttpResponse("you are looking at question %s." % question_id)
def result(request, question_id):
    respone = "you're looking at the result of question %s."
    return  HttpResponse(respone % question_id)

def vote (request, question_id):
    return HttpResponse("you're voting on question %s."%question_id)

# Create your views here.
