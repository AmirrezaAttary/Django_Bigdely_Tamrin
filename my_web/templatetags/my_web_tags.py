from django import template
from django.utils import timezone
from blog.models import Post,Category


register = template.Library()


@register.inclusion_tag("my_web/Latest_blog.html")
def latestpost(arg=6):
    posts = Post.objects.filter(published_date__lte =timezone.now(),status = 1).order_by('-published_date')[:arg]
    return {'posts': posts}