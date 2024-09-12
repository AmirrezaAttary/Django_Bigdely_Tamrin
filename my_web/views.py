from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from my_web.models import Contatct
from my_web.forms import NameForm
def index_view(request):
    return render(request,'my_web/index.html')

def about_view(request):
    return render(request,'my_web/about.html')

def contact_view(request):
    return render(request,'my_web/contact.html')


def test_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name,subject, email, message)
            return HttpResponse('done')
        else:
            return HttpResponse('error')
        
        
    form = NameForm()
    return render(request,'my_web/test.html',{'form':form})

