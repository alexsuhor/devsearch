from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    proj = Project.objects.all()
    params = {'projects': proj}
    return render(request, 'projects/projects.html', params)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {'project': projectObj}
    return render(request, 'projects/single-project.html', context)
    
def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/create-project.html', context)
