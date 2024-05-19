from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='portfolio/images/', null=True, blank=True)
    job_title = models.CharField(max_length=100, default='')
    email = models.EmailField(default='puskarjoshi22@gmail.com')
    website = models.URLField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
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