from django import forms
from .models import Project,Profile

class NewProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    exclude = ['profile']

class EditProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']