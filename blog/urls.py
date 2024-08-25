
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('' ,blog_view,name='blog'),
    path('<int:pk>' ,blog_single,name='single'),
    # path('post-<str:pid>',test,name='test'),
    ]
