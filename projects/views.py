from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Here is our projects')

def project(request, pk):
    return HttpResponse('Here is our projects ' + pk)
