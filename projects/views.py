from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArchivedProjects, Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

# Projects
@login_required(login_url="login")
def projects(request):
    projects = Project.objects.all().order_by('priority', '-created')
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    context = {'projects':projects, 'form':form}

    return render(request, 'projects/projects.html', context)

# Update Project
login_required(login_url="login")
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    projects = Project.objects.all().order_by('priority', '-created')
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form, 'projects': projects, 'selectedProject': project}
    return render(request, "projects/update_project.html", context)

# Archived Projects
@login_required(login_url="login")
def archivedProjects(request):
    projects = ArchivedProjects.objects.all().order_by('-created')
        
    context = {'archivedProjects':projects}

    return render(request, 'projects/archived_projects.html', context)

# Delete Then archive Project
login_required(login_url="login")
def archiveProject(request, pk):
    project = Project.objects.get(id=pk)
    archiveProject = ArchivedProjects.objects.create(project=project.title, priority=project.priority, notes=project.notes)
    project.delete()
    return redirect('projects')

# Restore archived Project
login_required(login_url="login")
def restoreArchivedProject(request, pk):
    archivedProject = ArchivedProjects.objects.get(id=pk)
    restoreProject = Project.objects.create(title=archivedProject.project, priority=archivedProject.priority, notes=archivedProject.notes)
    archivedProject.delete()
    return redirect('archived-projects')
