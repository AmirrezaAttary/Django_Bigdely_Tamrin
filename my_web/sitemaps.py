from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['my_web:index', 'my_web:about', 'my_web:contact']

    def location(self, item):
        return reverse(item)
    
