from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project,Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    projects = Project.all_projects()
    return render(request, 'home.html', {'projects':projects} )

def search_projects(request):
  if 'awward' in request.GET and request.GET["awward"]:
    search_term = request.GET.get("awward")
    search_project = Project.search_by_title(search_term)
    message = f"{search_term}"

    return render(request, 'search.html', {"message":message, "awward":search_project})

  else:
    message = "You haven't searched for any term"
    return render(request, 'search.html', {"message":message} )