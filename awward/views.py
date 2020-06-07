from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import NewProjectForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProjectsSerializer

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    projects = Project.all_projects()
    return render(request, 'home.html', {"projects":projects} )

def search_projects(request):
  if 'awward' in request.GET and request.GET["awward"]:
    search_term = request.GET.get("awward")
    search_project = Project.search_by_title(search_term)
    message = f"{search_term}"

    return render(request, 'search.html', {"message":message, "awward":search_project})

  else:
    message = "You haven't searched for any term"
    return render(request, 'search.html', {"message":message} )

@login_required(login_url='/accounts/login/')
def new_project(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewProjectForm(request.POST, request.FILES)
    if form.is_valid():
      project = form.save(commit=False)
      project.profile = current_user
      project.save()
    return redirect('home')
  else:
    form = NewProjectForm()
  return render(request, 'new_project.html', {"form":form} )

class ProjectsList(APIView):
  def get(self, request, format=None):
    all_projects = Project.objects.all()
    serializers = ProjectsSerializer(all_projects, many=True)
    return Response(serializers.data)

def profile(request):
    title = "Profile"
    current_user = request.user
    profile = Profile.objects.get(user =current_user)
    projects = Project.get_profile_projects(current_user)
    posts = projects.count()
    return render(request, 'profile.html', {"profile" : profile, 'projects':projects, "posts":posts } )