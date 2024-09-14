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
        fields = ['message','email','subject'] 
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.name = 'anonymous'  # Set name to anonymous
        if commit:
                instance.save()
        return instance

        
        
class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = '__all__'