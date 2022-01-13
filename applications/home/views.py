from django.views.generic import TemplateView
from applications.entry.models import Entry


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_cover'] = Entry.objects.get_home_cover()
        context['home_entries'] = Entry.objects.get_home_entries()
        context['recent_entries'] = Entry.objects.get_recent_entries()
        return context
