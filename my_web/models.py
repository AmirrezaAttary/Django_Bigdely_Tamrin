from django.db import models

# Create your models here.
class Contatct(models.Model):
    name = models.CharField(max_length=255, default='anonymous')
    email = models.EmailField()
    subject = models.CharField(max_length=255, default='')
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    def __str__(self) :
        return f"{self.name}: {self.subject}"
    
class Newsletter(models.Model):
    email = models.EmailField()
    
    
    def __str__(self) :
        return self.email