from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def index(request):
    return render(request,'blog/blogindex.html')
def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'blog/single.html', {'post': post })