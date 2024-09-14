from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from my_web.models import Contatct
from my_web.forms import NameForm ,ContatctForm,NewsletterForm
from django.contrib import messages
def index_view(request):
    return render(request,'my_web/index.html')

def about_view(request):
    return render(request,'my_web/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContatctForm(request.POST) 
        if form.is_valid():
            form.save()  
            messages.add_message(request, messages.SUCCESS, 'Your Ticket Submited Successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Your Ticket Didnt Submited')
        
    form = ContatctForm()
    return render(request,'my_web/contact.html')

def newsletter_view(request):
    if request.method == 'POST':
        form =NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
            

def test_view(request):
    if request.method == 'POST':
        form = ContatctForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('error')
        
        
    form = ContatctForm()
    return render(request,'my_web/test.html',{'form':form})

