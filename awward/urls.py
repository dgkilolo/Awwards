from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('', views.home, name='home'),
  path('search/', views.search_projects, name='search_projects'),
  path('new/project', views.new_project, name='new-project' ),
  path('api/projects', views.ProjectsList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)