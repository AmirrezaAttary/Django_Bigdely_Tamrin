from django.contrib import admin
from blog.models import Post,Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# @admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy ='created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author','contend_view','status','published_date','created_date',)
    list_filter = ('status','author')
    # ordering = ['-created_date']
    search_fields = ('title','contend')
    summernote_fields = ('contend',)
    
    
admin.site.register(Category)
admin.site.register(Post,PostAdmin)

