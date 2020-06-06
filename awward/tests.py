from django.test import TestCase
from .models import Profile,Project

# Create your tests here.
class ProjectsTestClass(TestCase):
  # Set up method
  def setUp(self):
    self.project = Project(title='akan project', description="Know your akan name", link="gitub.com")
  # Testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.project,Project))
  # Testing Save method
  def test_save_method(self):
    self.project.save_project()
    projects = Project.objects.all()
    self.assertTrue(len(projects)>0)
  # Testing Delete method
  def test_delete_method(self):
    self.project.delete_project()
    projects = Project.objects.all()
    self.assertTrue(len(projects)<1)
  # Clearing database after each test
  def test_teardown(self):
    Project.objects.all().delete()
    

class ProfileTestClass(TestCase):
  # Set up method
  def setUp(self):
    self.profile = Profile(bio='developer in training')
  # Testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.profile,Profile))
  # Testing Save method
  # def test_save_method(self):
  #   self.profile.save_profile()                         ### work on save test.
  #   profiles = Profile.objects.all()
  #   self.assertTrue(len(profiles)>0)
  # Testing Delete method
  def test_delete_method(self):
    self.profile.delete_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles)<1)
  # Clearing database after each test
  def test_teardown(self):
    Profile.objects.all().delete()