from django import forms
from my_web.models import Contatct,Newsletter

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    
    
class ContatctForm(forms.ModelForm):

    class Meta:
        model = Contatct
        fields = ['message','email'] 

        
        
class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = '__all__'