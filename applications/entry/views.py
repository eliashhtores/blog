from django.views.generic import ListView
from .models import Entry


class EntryListView(ListView):
    model = Entry
    template_name = 'entry/list.html'
    context_object_name = 'entries'
    paginate_by = 5

    def get_queryset(self):
        return Entry.objects.order_by('-created')
