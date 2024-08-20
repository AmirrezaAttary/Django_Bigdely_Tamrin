from django.contrib import admin
from my_web.models import Contatct
# Register your models here.

class ContatctAdmin(admin.ModelAdmin):
    date_hierarchy ='created_date'
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ('name','message')
    
admin.site.register(Contatct,ContatctAdmin)
