
from django.urls import path
from my_web.views import *

app_name = 'my_web'

urlpatterns = [
    path('' ,index_view,name='index'),
    path('about',about_view,name='about'),
    path('contact',contact_view,name='contact'),
    path('test',test_view,name='test'),
    path('newsletter',newsletter_view,name='newsletter'),
    ]