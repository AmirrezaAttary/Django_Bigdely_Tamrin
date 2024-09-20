from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def blog_view(request,**kwargs):
    posts = Post.objects.filter(published_date__lte =timezone.now(),status = 1)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts,3)
    try:   
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts,
    }
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your Comment Submited Successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Your Comment Didnt Submited')
        
    posts = Post.objects.filter(published_date__lte =timezone.now(),status = 1)
    post = get_object_or_404(posts, pk=pid)
    if not post.login_require: 
        comments = Comment.objects.filter(post=post.id,approved=True)
        form = CommentForm()
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
            'comments': comments,
            'form' : form,
        }
        return render(request,'blog/blog-single.html', context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def test(request):

    return render(request,'blog/test.html')


def blog_search(request):
    posts = Post.objects.filter(published_date__lte =timezone.now(),status = 1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(contend__contains = s)
    
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)