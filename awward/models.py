from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

  @classmethod
  def all_projects(cls):
    projects = cls.objects.all()
    return projects

  @classmethod
  def search_by_title(cls,search_term):
    projects = cls.objects.filter(title__icontains=search_term)
    return projects

  @classmethod
  def get_profile_projects(cls,profile):
    return cls.objects.filter(profile = profile)

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

  @receiver(post_save, sender = User)
  def create_profile(sender, instance,created, **kwargs):
    if created:
      Profile.objects.create(user = instance)

  @receiver(post_save,sender = User)
  def save_profile( sender, instance, **kwargs):
    instance.profile.save()