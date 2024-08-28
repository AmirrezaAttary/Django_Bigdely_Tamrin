from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(published_date__lte =timezone.now(),status = 1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,post_id):
    posts = Post.objects.filter(published_date__lte =timezone.now(),status = 1)
    post = get_object_or_404(posts, pk=post_id)
    post.contend_view += 1
    post.save()
    
    current_index = None
    for index, p in enumerate(posts):
        if p.id == post.id:
            current_index = index
            break

    # Get previous and next posts
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

def test(request,pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post,}
    return render(request,'blog/test.html', context)




def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # Get all posts in the database
    all_posts = Post.objects.all()

    # Find the index of the current post
    current_index = None
    for index, p in enumerate(all_posts):
        if p.id == post.id:
            current_index = index
            break

    # Get previous and next posts
    previous_post = None
    next_post = None
    if current_index is not None:
        if current_index > 0:
            previous_post = all_posts[current_index - 1]
        if current_index < len(all_posts) - 1:
            next_post = all_posts[current_index + 1]

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    return render(request, 'post_detail.html', context)
