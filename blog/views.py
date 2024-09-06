from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from blog.models import Post

# Create your views here.
def blog_view(request,**kwargs):
    posts = Post.objects.filter(published_date__lte =timezone.now(),status = 1)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,**kwargs):
    posts = Post.objects.filter(published_date__lte =timezone.now(),status = 1)
    post = get_object_or_404(posts, pk=kwargs.get('post_id'))
    post.contend_view += 1
    post.save()
    
    current_index = None
    for index, p in enumerate(posts):
        if p.id == post.id:
            current_index = index
            break

    previous_post = None
    next_post = None
    if current_index is not None:
        if current_index > 0:
            previous_post = posts[current_index - 1]
        if current_index < len(posts) - 1:
            next_post = posts[current_index + 1]

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    return render(request,'blog/blog-single.html', context)

def test(request):

    return render(request,'blog/test.html')
