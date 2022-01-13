from django.contrib import admin
from .models import Entry, Category, Tag


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published', 'in_home']
    list_filter = ['category', 'published', 'created']
    search_fields = ['title', 'summary', 'content']


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category)
admin.site.register(Tag)
