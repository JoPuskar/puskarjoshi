from django.contrib import admin

from portfolio.models import PersonalInformation, Project

# Register your models here.
admin.site.register(PersonalInformation)
admin.site.register(Project)
