from rest_framework import serializers
from .models import Project,Profile

class ProjectsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('id','title','image','description','link')

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('id','profile_pic','user','bio')