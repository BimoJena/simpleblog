from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from datetime import datetime

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts, 'current_year': datetime.now().year})

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return redirect('home')