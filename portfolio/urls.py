from urllib.parse import urlparse
from django.urls import path
from .views import portfolio, show_all_projects, project_detail

app_name = 'portfolio'

urlpatterns = [
    path('', portfolio, name='portfolio'),
    path('projects/', show_all_projects, name='show_all_projects'),
    path('projects/<int:project_id>', project_detail, name='project_detail')
]