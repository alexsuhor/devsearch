from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectList = [
    {
        'id': '1',
        'title': 'Ecommerse website',
        'description': 'Fully functional ecommerse website'
    },
    {
        'id': '2',
        'title': 'Portfolio website',
        'description': 'This was a project where I built out my portfolio'
    },
    {
        'id': '3',
        'title': 'Social network',
        'description': 'Awesome open source project I am still working'
    },
]

def projects(request):
    proj = Project.objects.all()
    params = {'projects': proj}
    return render(request, 'projects/projects.html', params)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})
