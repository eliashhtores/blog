from unicodedata import category
from django.views.generic import ListView, DetailView
from .models import Entry, Category


class EntryListView(ListView):
    model = Entry
    template_name = 'entry/list.html'
    context_object_name = 'entries'
    paginate_by = 5

    def get_queryset(self):
        title = self.request.GET.get('title', '')
        category = self.request.GET.get('category', '')
        return Entry.objects.search_entries(title, category)

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('name')
        return context


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entry/detail.html'

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('name')
        return context
