from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(published_date__lte =timezone.now(),status = 1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pk):
    
    post = get_object_or_404(Post, pk=pk)
    post.contend_view += 1
    post.save()

    context = {'post': post}
    return render(request,'blog/blog-single.html', context)

def test(request,pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post,}
    return render(request,'blog/test.html', context)

