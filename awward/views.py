from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project,Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    projects = Project.all_projects()
    return render(request, 'home.html', {'projects':projects} )