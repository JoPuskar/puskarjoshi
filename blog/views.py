from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.


def blogs(request):
    posts = Post.objects.all()
    context = { 'posts': posts }
    return render(request, 'blog/blog.html', context)


def all_blogs(request):
    posts = Post.objects.all()
    context = { 'posts': posts }
    return render(request, 'blog/all_posts.html', context)


def blog_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)