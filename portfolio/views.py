from django.shortcuts import get_object_or_404, render

from .models import Project, UserProfile
from blog.models import Post

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    personal_info = UserProfile.objects.first()
    posts = Post.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects, 'personal_info': personal_info, 'posts': posts})


def show_all_projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'portfolio/show_all_projects.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {
        'project': project
    }
    return render(request, 'portfolio/project_detail.html', context)