from django.db import models

# Create your models here.
class Contatct(models.Model):
    name = models.CharField(max_length=2555)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)