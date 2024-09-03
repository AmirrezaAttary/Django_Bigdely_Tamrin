from django import template
from blog.models import Post,Category

register = template.Library()

@register.simple_tag(name="totalpost")
def func():
    posts = Post.objects.filter(status = 1).count()
    return posts

@register.simple_tag(name="posts")
def func():
    posts = Post.objects.filter(status = 1)
    return posts

@register.filter
def snippet(value,arg = 20):
    return value[:arg] + '...'

@register.inclusion_tag("blog/blog-popular-post.html")
def latestpost(arg=3):
    posts = Post.objects.filter(status = 1).order_by('published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag("blog/blog-post-catgories.html")
def postcategory():
    posts = Post.objects.filter(status = 1)
    categoryies = Category.objects.all()
    cat_dict = {}
    for name in categoryies:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categoryies':cat_dict}
        