from unicodedata import name
from django.urls import path
from .views import blogs, all_blogs, blog_detail

app_name = 'blog'

urlpatterns = [
    path('', blogs, name='blogs'),
    path('all_blogs/', all_blogs, name='all_blogs'),
    path('blogs/<int:post_id>', blog_detail, name='blog_detail')
]
