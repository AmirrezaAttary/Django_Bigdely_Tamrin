
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('' ,blog_view,name='blog'),
    path('<int:post_id>/' ,blog_single,name='single'),
    ]
