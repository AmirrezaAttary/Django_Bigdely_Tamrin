from django.shortcuts import render
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    return render(request,'blog/blog-single.html')

def blog_single(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'blog/test.html', context)