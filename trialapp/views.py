from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return render(request,'projects/Main_project.html')

def project_two(request):
    return render(request,'projects/project.html')

def project(request,pk):
    return HttpResponse('Hello'+''+str(pk))