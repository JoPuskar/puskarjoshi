from django.shortcuts import render

from .models import Project, PersonalInformation

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    personal_info = PersonalInformation.objects.first()
    return render(request, 'portfolio/portfolio.html', {'projects': projects, 'personal_info': personal_info})


