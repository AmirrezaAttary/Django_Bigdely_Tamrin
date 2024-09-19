from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns=[
    path('login',login_view,name='login'),
    # login
    # path('logout',logout_view,name='logout'),
    # logout
    path('signup',signup_view,name='signup'),
    # registration / signup
]