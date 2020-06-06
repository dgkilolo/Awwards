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

class Profile(models.Model):
  profile_pic = models.ImageField(upload_to='awward/')
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  bio = models.TextField()

  def __str__(self):
    return self.user.username 