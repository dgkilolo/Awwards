from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
  '''
  class that defines project objects
  '''
  title = models.CharField(max_length=30)
  image = models.ImageField(upload_to='awward/')
  description = models.TextField()
  link = models.URLField()
  profile = models.ForeignKey(User, on_delete=models.CASCADE)

  def save_project(self):
    self.save()
  def delete_project(self):
    Project.objects.filter(pk=self.id).delete()

class Profile(models.Model):
  profile_pic = models.ImageField(upload_to='awward/')
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  bio = models.TextField(blank=True)

  def save_profile(self):
    self.save()
  def delete_profile(self):
    Profile.objects.filter(pk=self.id).delete()

  def __str__(self):
    return self.user.username 