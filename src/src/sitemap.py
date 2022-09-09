from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['/',
                '/about',
                '/contact_us'
                
        ]

    def location(self, item) :
        return item
    