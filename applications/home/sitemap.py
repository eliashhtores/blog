from datetime import date
from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy
from datetime import datetime
from applications.entry.models import Entry


class EntrySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Entry.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.created


class Sitemap(Sitemap):
    protocol = 'https'

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'monthly'

    def lastmod(self, obj):
        return datetime.now()

    def location(self, item):
        return reverse_lazy(item)
