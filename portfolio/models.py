from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pofile_pic = models.ImageField(upload_to='portfolio/images/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def get_full_name(self):
        full_name = f"{self.user.first_name} {self.user.last_name}"
        return full_name.strip() or self.user.username
        

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='portfolio/images/', null=True, blank=True)

    def __str__(self):
        return self.title

class PersonalInformation(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField()
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return self.name