from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='portfolio/images/', default='images/MyProject.png')

    def __str__(self):
        return self.title

class PersonalInformation(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name