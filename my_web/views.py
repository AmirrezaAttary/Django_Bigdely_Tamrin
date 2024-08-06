from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return render(request,'my_web/index.html')

def about_view(request):
    return render(request,'my_web/about.html')

def contact_view(request):
    return render(request,'my_web/contact.html')

