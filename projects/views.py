from django.shortcuts import redirect, render
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
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'projects/project_form.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    context = {'form': form}
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {'object': project}
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete_template.html', context)
