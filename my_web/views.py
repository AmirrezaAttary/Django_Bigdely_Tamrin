from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from my_web.models import Contatct
from my_web.forms import NameForm ,ContatctForm
def index_view(request):
    return render(request,'my_web/index.html')

def about_view(request):
    return render(request,'my_web/about.html')

def contact_view(request):
    return render(request,'my_web/contact.html')


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

