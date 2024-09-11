from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from my_web.models import Contatct
def index_view(request):
    return render(request,'my_web/index.html')

def about_view(request):
    return render(request,'my_web/about.html')

def contact_view(request):
    return render(request,'my_web/contact.html')


def test_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = Contatct()
        c.name = name
        c.email = email
        c.subject = subject
        c.message = message
        c.save()
        print(name, email, subject, message)
    return render(request,'my_web/test.html')

