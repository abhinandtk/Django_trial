from django.shortcuts import render

from django.http import HttpResponse

def projects(request):
    return HttpResponse('Hello Welcome')

def project(request,pk):
    return HttpResponse('Hello'+''+str(pk))